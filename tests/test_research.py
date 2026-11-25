from pathlib import Path

import httpx2
import pytest

from hisinone_mcp import models, research
from hisinone_mcp.research import Project, ProjectError, read_project

from .api_client import mock_api_client


async def lookup(response: httpx2.Response) -> Project:
    def respond(request: httpx2.Request) -> httpx2.Response:
        assert request.url.path == "/api/v1/fs/res/project/100002"
        assert request.headers["Authorization"] == "Bearer caller"
        return response

    async with mock_api_client(respond, base_url="https://his.test/api/v1") as client:
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


async def test_research_collections_bound_their_results() -> None:
    def respond(request: httpx2.Request) -> httpx2.Response:
        assert request.method == "GET"
        assert request.headers["Authorization"] == "Bearer caller"
        path = request.url.path
        if path == "/fs/res/patent":
            assert not request.url.params
        else:
            assert path in {
                "/fs/res/project",
                "/fs/res/publication/simple",
                "/fs/res/researchInfrastructure/simple",
            }
            assert dict(request.url.params) == {"q": "Example", "l": "2"}
        rows = [
            {
                "id": 1,
                "title": "First",
                "defaulttext": "Private",
                "isPseudonymized": {"id": 1},
            },
            {
                "id": 2,
                "title": "Second",
                "defaulttext": "Private",
                "pseudonymizedTitle": "Visible",
            },
            {"id": 3},
        ]
        return httpx2.Response(200, json=rows)

    async with mock_api_client(respond) as client:
        projects = await research.search_projects(client, " Example ", 2)
        assert [p.title for p in projects] == [None, "Visible"]
        papers = await research.find_publications(client, " Example ", 2)
        facilities = await research.search_research_infrastructures(
            client, " Example ", 2
        )
        patents = await research.list_patents(client, 2)
        assert [p.id for p in papers] == [1, 2]
        assert [f.id for f in facilities] == [1, 2]
        assert [p.id for p in patents] == [1, 2]
        with pytest.raises(research.ResearchError, match="limit"):
            await research.list_patents(client, 21)
        with pytest.raises(research.ResearchError, match="search term"):
            await research.search_research_infrastructures(client, " ", 2)


async def test_new_lookups_validate_id_and_allow_missing_fields() -> None:
    async with mock_api_client(
        lambda _: httpx2.Response(200, json={"id": 8})
    ) as client:
        for read in (
            read_project,
            research.read_publication,
            research.read_patent,
            research.read_research_infrastructure,
        ):
            with pytest.raises(research.ResearchError, match="unexpected"):
                await read(client, 7)
            record = await read(client, 8)
            assert record.model_dump(exclude_none=True) == {"id": 8}


async def test_rich_lookups_decode_captured_hisinone_responses() -> None:
    fixtures = Path(__file__).parent / "fixtures"
    paths = {
        "/fs/res/project/100002": "project-lookup.json",
        "/fs/res/publication/7": "publication-lookup.json",
        "/fs/res/patent/7": "patent-lookup.json",
        "/fs/res/researchInfrastructure/7": "research-infrastructure-lookup.json",
    }

    def respond(request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(
            200, content=(fixtures / paths[request.url.path]).read_bytes()
        )

    async with mock_api_client(respond) as client:
        project = await read_project(client, 100002)
        assert (project.status, project.project_type, project.objective) == (
            "Example",
            None,
            "Example",
        )
        assert project.subject_areas == ["Example"]
        paper = await research.read_publication(client, 7)
        assert paper.creators == ["Example Example Example Example"]
        assert paper.publication_type == paper.publisher == "Example"
        assert paper.identifiers == [
            models.PublicationIdentifier(type="Example", value="Example")
        ]
        patent = await research.read_patent(client, 7)
        assert patent.country is None
        assert patent.registration_type == "Example"
        assert patent.inventors == ["Example Example"]
        facility = await research.read_research_infrastructure(client, 7)
        assert facility.access_modes == ["Example"]
        assert facility.organizations == [
            models.InfrastructureOrganization(name="Example", is_coordinator=False)
        ]


async def test_present_empty_lists_stay_empty() -> None:
    async with mock_api_client(
        lambda _: httpx2.Response(
            200, json={"id": 7, "creators": [], "globalIdentifiers": []}
        )
    ) as client:
        paper = await research.read_publication(client, 7)
    assert paper.creators == paper.identifiers == []


async def test_publication_validates_id_and_bibtex_payload() -> None:
    async with mock_api_client(
        lambda _: httpx2.Response(200, json={"id": 8, "secret": "private-diagnostic"})
    ) as client:
        with pytest.raises(research.ResearchError, match="unexpected publication"):
            await research.read_publication(client, 7)
        with pytest.raises(research.ResearchError, match="unreadable citation") as exc:
            await research.read_bibtex(client, 7)
        assert "private-diagnostic" not in str(exc.value)


async def test_plain_text_citation_preserves_comments_and_rejects_diagnostics() -> None:
    citation = "% Exported by HISinOne\n@book(example, title={Example})\n"
    replies = iter((citation, "private-diagnostic"))
    async with mock_api_client(
        lambda _: httpx2.Response(200, text=next(replies))
    ) as client:
        assert (await research.read_bibtex(client, 7)).bibtex == citation
        with pytest.raises(research.ResearchError, match="unreadable citation") as exc:
            await research.read_bibtex(client, 7)
        assert "private-diagnostic" not in str(exc.value)


async def test_empty_search_result_must_be_a_json_array() -> None:
    replies = iter((b"{}", b"[]"))
    async with mock_api_client(
        lambda _: httpx2.Response(200, content=next(replies))
    ) as client:
        with pytest.raises(research.ResearchError, match="unexpected publication"):
            await research.find_publications(client, "example", 10)
        assert await research.find_publications(client, "example", 10) == []
