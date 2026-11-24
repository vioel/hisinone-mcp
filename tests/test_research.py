import httpx2
import pytest
from hisinone_client import AuthenticatedClient

from hisinone_mcp import research
from hisinone_mcp.research import Project, ProjectError, read_project


async def lookup(response: httpx2.Response) -> Project:
    def respond(request: httpx2.Request) -> httpx2.Response:
        assert request.url.path == "/api/v1/fs/res/project/100002"
        assert request.headers["Authorization"] == "Bearer caller"
        return response

    async with AuthenticatedClient(
        base_url="https://his.test/api/v1",
        token="caller",
        httpx_args={"transport": httpx2.MockTransport(respond)},
    ) as client:
        return await read_project(client, 100002)


@pytest.mark.parametrize(
    ("response", "message"),
    [
        (httpx2.Response(401), "permission"),
        (
            httpx2.Response(
                401, headers={"WWW-Authenticate": 'Bearer error="invalid_token"'}
            ),
            "Sign in again",
        ),
        (httpx2.Response(401, json={"error": "insufficient_scope"}), "permission"),
        (httpx2.Response(403), "permission"),
        (httpx2.Response(400), "rejected"),
        (httpx2.Response(404), "not found"),
        (httpx2.Response(429), "rate limiting"),
        (httpx2.Response(503, text="private-diagnostic"), "temporarily unavailable"),
        (httpx2.Response(200, text="private-diagnostic"), "unreadable"),
        (httpx2.Response(200, json={"id": 7}), "unexpected project"),
    ],
)
async def test_project_errors(response: httpx2.Response, message: str) -> None:
    with pytest.raises(ProjectError, match=message) as exc:
        await lookup(response)
    assert "private-diagnostic" not in str(exc.value)


async def test_pseudonymized_project_without_display_title() -> None:
    project = await lookup(
        httpx2.Response(
            200,
            json={
                "id": 100002,
                "defaulttext": "Private title",
                "isPseudonymized": {"id": 1},
            },
        )
    )
    assert project.title is None
    assert project.model_dump(exclude_none=True) == {"id": 100002}


@pytest.mark.parametrize(
    ("fields", "title", "description"),
    [
        ({}, "Original", None),
        ({"canViewOriginalData": {"text": "yes"}}, "Original", None),
        ({"canViewOriginalData": {"uniquename": "false"}}, None, None),
        (
            {"canViewOriginalData": {"uniquename": "true"}},
            "Original",
            "Original description",
        ),
        (
            {
                "canViewOriginalData": {"uniquename": "true"},
                "isPseudonymized": {"uniquename": "true"},
            },
            None,
            None,
        ),
        (
            {
                "canViewOriginalData": {"uniquename": "true"},
                "pseudonymizedTitle": "Alias",
            },
            "Alias",
            None,
        ),
    ],
)
async def test_project_description_requires_original_view(
    fields: dict[str, object], title: str | None, description: str | None
) -> None:
    project = await lookup(
        httpx2.Response(
            200,
            json={
                "id": 100002,
                "defaulttext": "Original",
                "longtext": "Original description",
                **fields,
            },
        )
    )
    assert (project.title, project.description) == (title, description)


@pytest.mark.parametrize("invalid", [True, "2025-04-21", 10**24])
async def test_invalid_project_date_is_a_domain_error(invalid: object) -> None:
    with pytest.raises(ProjectError, match="unreadable project"):
        await lookup(httpx2.Response(200, json={"id": 100002, "startdate": invalid}))


async def test_project_dates_preserve_epoch_milliseconds() -> None:
    project = await lookup(
        httpx2.Response(200, json={"id": 100002, "startdate": -1, "enddate": 0})
    )
    assert project.start_date and project.end_date
    assert project.start_date.isoformat() == "1970-01-01T00:59:59.999000+01:00"
    assert project.end_date.isoformat() == "1970-01-01T01:00:00+01:00"


async def test_present_empty_lists_stay_empty() -> None:
    async with AuthenticatedClient(
        base_url="https://his.test",
        token="caller",
        httpx_args={
            "transport": httpx2.MockTransport(
                lambda _: httpx2.Response(
                    200, json={"id": 7, "creators": [], "globalIdentifiers": []}
                )
            )
        },
    ) as client:
        paper = await research.read_publication(client, 7)
    assert paper.creators == paper.identifiers == []


async def test_publication_validates_id_and_bibtex_payload() -> None:
    async with AuthenticatedClient(
        base_url="https://his.test",
        token="caller",
        httpx_args={
            "transport": httpx2.MockTransport(
                lambda _: httpx2.Response(
                    200, json={"id": 8, "secret": "private-diagnostic"}
                )
            )
        },
    ) as client:
        with pytest.raises(research.ResearchError, match="unexpected publication"):
            await research.read_publication(client, 7)
        with pytest.raises(research.ResearchError, match="unreadable citation") as exc:
            await research.read_bibtex(client, 7)
        assert "private-diagnostic" not in str(exc.value)


async def test_plain_text_citation_preserves_comments_and_rejects_diagnostics() -> None:
    citation = "% Exported by HISinOne\n@book(example, title={Example})\n"
    replies = iter((citation, "private-diagnostic"))
    async with AuthenticatedClient(
        base_url="https://his.test",
        token="caller",
        httpx_args={
            "transport": httpx2.MockTransport(
                lambda _: httpx2.Response(200, text=next(replies))
            )
        },
    ) as client:
        assert (await research.read_bibtex(client, 7)).bibtex == citation
        with pytest.raises(research.ResearchError, match="unreadable citation") as exc:
            await research.read_bibtex(client, 7)
        assert "private-diagnostic" not in str(exc.value)


async def test_empty_search_result_must_be_a_json_array() -> None:
    replies = iter((b"{}", b"[]"))
    async with AuthenticatedClient(
        base_url="https://his.test",
        token="caller",
        httpx_args={
            "transport": httpx2.MockTransport(
                lambda _: httpx2.Response(200, content=next(replies))
            )
        },
    ) as client:
        with pytest.raises(research.ResearchError, match="unexpected publication"):
            await research.find_publications(client, "example", 10)
        assert await research.find_publications(client, "example", 10) == []
