from collections.abc import Awaitable
from typing import Annotated
from zoneinfo import ZoneInfo

import httpx2
from fastmcp import FastMCP
from fastmcp.dependencies import CurrentAccessToken, Depends
from fastmcp.exceptions import ToolError
from fastmcp.server.auth import AccessToken
from hisinone_client import AuthenticatedClient
from pydantic import Field, StringConstraints

from hisinone_mcp import models, research

Query = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
Limit = Annotated[int, Field(ge=1, le=research.MAX_RESULTS)]


async def _result[T](call: Awaitable[T]) -> T:
    try:
        return await call
    except research.ResearchError as exc:
        raise ToolError(str(exc)) from None


def register_research_tools(
    server: FastMCP,
    *,
    api_base_url: str,
    timezone: ZoneInfo,
    transport: httpx2.AsyncBaseTransport,
) -> None:
    def upstream_client(
        grant: Annotated[AccessToken, CurrentAccessToken()],
    ) -> AuthenticatedClient:
        return AuthenticatedClient(
            base_url=api_base_url,
            token=grant.token,
            httpx_args={"transport": transport, "trust_env": False},
        )

    caller_client = Depends(upstream_client)
    read_tool = server.tool(
        annotations={"readOnlyHint": True, "destructiveHint": False}
    )

    @read_tool
    async def get_project(
        project_id: int, client: AuthenticatedClient = caller_client
    ) -> models.Project:
        """Get a project's visible description, status, classification and dates.

        Dates include the HISinOne time zone's offset. Midnight on end_date begins
        the recorded end day.
        """
        project = await _result(
            research.read_project(client, project_id, timezone=timezone)
        )
        return models.Project.model_validate(project)

    @read_tool
    async def find_projects(
        query: Query, limit: Limit = 10, client: AuthenticatedClient = caller_client
    ) -> list[models.ProjectSummary]:
        """Find projects by text and return their IDs, visible titles and statuses."""
        projects = await _result(research.search_projects(client, query, limit))
        return [models.ProjectSummary.model_validate(project) for project in projects]

    @read_tool
    async def find_publications(
        query: Query, limit: Limit = 10, client: AuthenticatedClient = caller_client
    ) -> list[models.PublicationSummary]:
        """Find publications by text and return their IDs and titles."""
        publications = await _result(research.find_publications(client, query, limit))
        return [
            models.PublicationSummary.model_validate(publication)
            for publication in publications
        ]

    @read_tool
    async def get_publication(
        publication_id: int, client: AuthenticatedClient = caller_client
    ) -> models.Publication:
        """Get bibliographic details, credited creators, identifiers and abstract."""
        publication = await _result(research.read_publication(client, publication_id))
        return models.Publication.model_validate(publication)

    @read_tool
    async def get_publication_bibtex(
        publication_id: int, client: AuthenticatedClient = caller_client
    ) -> research.PublicationBibtex:
        """Get the BibTeX citation supplied by HISinOne for one publication."""
        return await _result(research.read_bibtex(client, publication_id))

    @read_tool
    async def list_patents(
        limit: Limit = 10, client: AuthenticatedClient = caller_client
    ) -> list[models.PatentSummary]:
        """List patents with their numbers, titles, statuses and countries."""
        patents = await _result(research.list_patents(client, limit))
        return [models.PatentSummary.model_validate(patent) for patent in patents]

    @read_tool
    async def get_patent(
        patent_id: int, client: AuthenticatedClient = caller_client
    ) -> models.Patent:
        """Get patent numbers, inventors, registration details and grant date.

        Registration and grant dates mark calendar days in the HISinOne time zone.
        """
        patent = await _result(
            research.read_patent(client, patent_id, timezone=timezone)
        )
        return models.Patent.model_validate(patent)

    @read_tool
    async def find_research_infrastructures(
        query: Query, limit: Limit = 10, client: AuthenticatedClient = caller_client
    ) -> list[models.ResearchInfrastructureSummary]:
        """Find research infrastructures by text and return their IDs and titles."""
        facilities = await _result(
            research.search_research_infrastructures(client, query, limit)
        )
        return [
            models.ResearchInfrastructureSummary.model_validate(facility)
            for facility in facilities
        ]

    @read_tool
    async def get_research_infrastructure(
        research_infrastructure_id: int, client: AuthenticatedClient = caller_client
    ) -> models.ResearchInfrastructure:
        """Get a facility's description, type, access modes and organizations."""
        facility = await _result(
            research.read_research_infrastructure(client, research_infrastructure_id)
        )
        return models.ResearchInfrastructure.model_validate(facility)
