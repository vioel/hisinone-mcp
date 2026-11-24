import json
import re
from collections.abc import AsyncGenerator, Awaitable, Callable
from contextlib import asynccontextmanager
from datetime import datetime
from zoneinfo import ZoneInfo

import httpx2
from hisinone_client import AuthenticatedClient
from hisinone_client.api.fs_res import (
    get_fs_res_project,
    get_fs_res_project_id,
    get_fs_res_publication_id,
    get_fs_res_publication_id_bibtex,
    get_fs_res_publication_simple,
)
from hisinone_client.models import (
    CsSysValueGenericValue,
    FsResProjectProjectObj,
    FsResPublicationGlobalIdentifier,
    FsResPublicationPublicationCreator,
    FsResPublicationPublicationTypeValue,
)
from hisinone_client.types import Response, Unset
from pydantic import AwareDatetime, BaseModel

from hisinone_mcp.bearer import oauth_error
from hisinone_mcp.models import PublicationIdentifier
from hisinone_mcp.settings import DEFAULT_UPSTREAM_TIMEZONE

MAX_RESULTS = 20


class ProjectSummary(BaseModel):
    id: int
    title: str | None
    status: str | None


class Project(ProjectSummary):
    description: str | None
    project_type: str | None
    objective: str | None
    subject_areas: list[str] | None
    start_date: AwareDatetime | None
    end_date: AwareDatetime | None


class PublicationSummary(BaseModel):
    id: int
    title: str | None


class Publication(PublicationSummary):
    release_year: int | None
    journal: str | None
    abstract: str | None
    creators: list[str] | None
    publication_type: str | None
    identifiers: list[PublicationIdentifier] | None
    publisher: str | None


class PublicationBibtex(BaseModel):
    publication_id: int
    bibtex: str


class ResearchError(Exception):
    """A research API error safe to show to the caller."""


ProjectError = ResearchError


@asynccontextmanager
async def _read[T](call: Awaitable[Response[T]], resource: str) -> AsyncGenerator[T]:
    try:
        response = await call
        status = response.status_code
        if status in (400, 401, 403):
            code = oauth_error(
                response.headers.get("WWW-Authenticate", ""), response.content
            )
            if code == "invalid_token":
                raise ResearchError(
                    "Your HISinOne authorization is no longer valid. Sign in again."
                )
            if status in (401, 403) or code == "insufficient_scope":
                raise ResearchError(
                    f"You do not have permission to read this {resource}."
                )
            raise ResearchError(f"HISinOne rejected the {resource} request.")
        if status == 404:
            raise ResearchError(f"{resource.capitalize()} not found.")
        if status == 429:
            raise ResearchError("HISinOne is rate limiting requests. Try again later.")
        if status >= 500:
            raise ResearchError("HISinOne is temporarily unavailable.")
        result = response.parsed
        # The generated list decoder also iterates an empty JSON object as zero rows.
        if (
            status != 200
            or result is None
            or (result == [] and json.loads(response.content) != [])
        ):
            raise ResearchError(f"HISinOne returned an unexpected {resource} response.")
        yield result
    except httpx2.RequestError:
        raise ResearchError("HISinOne is temporarily unavailable.") from None
    except (TypeError, ValueError, KeyError, AttributeError):
        raise ResearchError(f"HISinOne returned an unreadable {resource}.") from None


def _record_id(value: int | Unset, resource: str, expected: int | None = None) -> int:
    if type(value) is not int or (expected is not None and value != expected):
        raise ResearchError(f"HISinOne returned an unexpected {resource} response.")
    return value


def _limit(value: int) -> int:
    if not 1 <= value <= MAX_RESULTS:
        raise ResearchError(f"Choose a limit between 1 and {MAX_RESULTS}.")
    return value


def _query(value: str) -> str:
    if not (query := value.strip()):
        raise ResearchError("Enter a search term.")
    return query


def _label(
    value: CsSysValueGenericValue | FsResPublicationPublicationTypeValue | None | Unset,
) -> str | None:
    return (value.text or value.defaulttext or None) if value else None


def _values[T, V](
    items: list[T] | Unset, display: Callable[[T], V | None]
) -> list[V] | None:
    if isinstance(items, Unset):
        return None
    return [value for item in items if (value := display(item)) is not None]


def _from_epoch_milliseconds(
    value: int | None | Unset, timezone: ZoneInfo
) -> datetime | None:
    if value is None or isinstance(value, Unset):
        return None
    if type(value) is not int:
        raise ValueError("Expected integer epoch milliseconds")
    seconds, milliseconds = divmod(value, 1000)
    try:
        return datetime.fromtimestamp(seconds, tz=timezone).replace(
            microsecond=milliseconds * 1000
        )
    except (OSError, OverflowError) as exc:
        raise ValueError("Timestamp is out of range") from exc


def _original_project_view(row: FsResProjectProjectObj) -> bool | None:
    if row.pseudonymized_title or row.is_pseudonymized:
        return False
    permission = row.can_view_original_data
    if permission and permission.uniquename in ("true", "false"):
        return permission.uniquename == "true"
    return None


def _project_summary(
    row: FsResProjectProjectObj, expected: int | None = None
) -> ProjectSummary:
    title = (
        row.pseudonymized_title
        if _original_project_view(row) is False
        else row.defaulttext
    )
    return ProjectSummary(
        id=_record_id(row.id, "project", expected),
        title=title or None,
        status=_label(row.project_status),
    )


async def read_project(
    client: AuthenticatedClient,
    id: int,
    *,
    timezone: ZoneInfo = DEFAULT_UPSTREAM_TIMEZONE,
) -> Project:
    call = get_fs_res_project_id.asyncio_detailed(id, client=client)
    async with _read(call, "project") as row:
        description = row.longtext if _original_project_view(row) is True else None
        return Project(
            **_project_summary(row, id).model_dump(),
            description=description or None,
            project_type=_label(row.project_type),
            objective=_label(row.project_objective),
            subject_areas=_values(row.subject_areas, _label),
            start_date=_from_epoch_milliseconds(row.startdate, timezone),
            end_date=_from_epoch_milliseconds(row.enddate, timezone),
        )


async def search_projects(
    client: AuthenticatedClient, query: str, limit: int
) -> list[ProjectSummary]:
    call = get_fs_res_project.asyncio_detailed(
        client=client, q=_query(query), l=_limit(limit)
    )
    async with _read(call, "project") as rows:
        return [_project_summary(row) for row in rows[:limit]]


async def find_publications(
    client: AuthenticatedClient, query: str, limit: int
) -> list[PublicationSummary]:
    call = get_fs_res_publication_simple.asyncio_detailed(
        client=client, q=_query(query), l=_limit(limit)
    )
    async with _read(call, "publication") as rows:
        return [
            PublicationSummary(
                id=_record_id(row.id, "publication"), title=row.title or None
            )
            for row in rows[:limit]
        ]


def _name(*parts: str | None | Unset) -> str | None:
    return " ".join(part.strip() for part in parts if part and part.strip()) or None


def _creators(
    items: list[FsResPublicationPublicationCreator] | Unset,
) -> list[str] | None:
    if isinstance(items, Unset):
        return None
    ordered = sorted(
        items,
        key=lambda item: (
            item.sortorder if isinstance(item.sortorder, int) else float("inf")
        ),
    )
    return [
        name
        for item in ordered
        if (
            name := _name(
                item.firstname, item.nameprefix, item.creatorname, item.namesuffix
            )
        )
    ]


def _identifier(item: FsResPublicationGlobalIdentifier) -> PublicationIdentifier | None:
    kind = _label(item.global_identifier_type)
    if kind and item.identifier:
        return PublicationIdentifier(type=kind, value=item.identifier)
    return None


async def read_publication(
    client: AuthenticatedClient, publication_id: int
) -> Publication:
    call = get_fs_res_publication_id.asyncio_detailed(publication_id, client=client)
    async with _read(call, "publication") as row:
        year = row.release_year
        return Publication(
            id=_record_id(row.id, "publication", publication_id),
            title=row.title or None,
            release_year=None if isinstance(year, Unset) else year,
            journal=(row.journal.defaulttext or None) if row.journal else None,
            abstract=row.text_abstract or None,
            creators=_creators(row.creators),
            publication_type=_label(row.publication_type),
            identifiers=_values(row.global_identifiers, _identifier),
            publisher=(row.publisher.label or row.publisher.defaulttext or None)
            if row.publisher
            else None,
        )


async def read_bibtex(
    client: AuthenticatedClient, publication_id: int
) -> PublicationBibtex:
    call = get_fs_res_publication_id_bibtex.asyncio_detailed(
        publication_id, client=client
    )
    async with _read(call, "citation") as bibtex:
        if not re.match(r"\s*(?:%[^\n]*\n\s*)*@[a-zA-Z][\w-]*\s*[{(]", bibtex):
            raise ResearchError("HISinOne returned an unreadable citation.")
        return PublicationBibtex(publication_id=publication_id, bibtex=bibtex)
