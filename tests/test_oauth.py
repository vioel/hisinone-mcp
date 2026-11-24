import asyncio
import base64
import hashlib
import re
import secrets
import time
from collections.abc import AsyncGenerator
from dataclasses import dataclass, field
from unittest.mock import patch
from urllib.parse import parse_qs, urlencode, urlsplit
from zoneinfo import ZoneInfo

import httpx2
import pytest
from fastmcp import Client, FastMCP
from fastmcp.server.dependencies import get_access_token
from fastmcp.utilities.tests import ASGIServer, asgi_server, run_server_async
from key_value.aio.stores.redis import RedisStore
from pydantic import AnyUrl
from redis.exceptions import RedisError
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse

from hisinone_mcp.app import create_server
from hisinone_mcp.auth.provider import HisinoneOAuthProxy
from hisinone_mcp.auth.verifier import HisinoneTokenVerifier
from hisinone_mcp.settings import Settings

CALLBACK = "http://127.0.0.1:9191/return"
UPSTREAM_CALLBACK = "http://127.0.0.1/auth/callback"
PROJECT_SCOPE = "campus.projects:read"
PATENT_SCOPE = "campus.patents:read"
INFRASTRUCTURE_SCOPE = "campus.infrastructure:read"
AVAILABLE_SCOPES = frozenset(
    {"openid", PROJECT_SCOPE, PATENT_SCOPE, INFRASTRUCTURE_SCOPE}
)
TOOL_CONTRACT = {
    "find_projects": (["query", "limit"], "project_id"),
    "get_project": (["project_id"], "project_id"),
    "find_publications": (["query", "limit"], "publication_id"),
    "get_publication": (["publication_id"], "publication_id"),
    "get_publication_bibtex": (["publication_id"], "publication_id"),
    "list_patents": (["limit"], "patent_id"),
    "get_patent": (["patent_id"], "patent_id"),
    "find_research_infrastructures": (["query", "limit"], "research_infrastructure_id"),
    "get_research_infrastructure": (
        ["research_infrastructure_id"],
        "research_infrastructure_id",
    ),
}


def challenge(verifier: str) -> str:
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()


@dataclass
class Issuer:
    client_secret: str = field(repr=False)
    codes: dict[str, tuple[str, str]] = field(
        default_factory=dict[str, tuple[str, str]]
    )
    tokens: dict[str, str] = field(default_factory=dict[str, str])
    granted_scopes: dict[str, set[str]] = field(default_factory=dict[str, set[str]])
    userinfo_tokens: list[str] = field(default_factory=list[str])
    project_tokens: list[str] = field(default_factory=list[str])
    denied_readers: set[str] = field(default_factory=set[str])
    userinfo_ports: set[int] = field(default_factory=set[int])
    project_ports: set[int] = field(default_factory=set[int])
    scopes: str = f"openid {PROJECT_SCOPE} ROLE_scientist"
    lifetime: int | None = 120
    include_refresh_token: bool = False
    userinfo_status: int = 200
    error_in_body: bool = False

    async def authorize(self, request: Request) -> RedirectResponse:
        params = request.query_params
        assert params["client_id"] == "his-client"
        assert params["response_type"] == "code"
        assert params["redirect_uri"] == UPSTREAM_CALLBACK
        assert params["code_challenge_method"] == "S256"
        assert set(params["scope"].split()) <= AVAILABLE_SCOPES
        assert "resource" not in params
        code = secrets.token_urlsafe()
        self.codes[code] = (request.headers["X-Test-User"], params["code_challenge"])
        query = urlencode({"code": code, "state": params["state"]})
        return RedirectResponse(f"{UPSTREAM_CALLBACK}?{query}", 302)

    async def token(self, request: Request) -> JSONResponse:
        basic = base64.b64encode(f"his-client:{self.client_secret}".encode()).decode()
        assert request.headers["Authorization"] == f"Basic {basic}"
        form = await request.form()
        assert "client_secret" not in form
        assert form["redirect_uri"] == UPSTREAM_CALLBACK
        assert form["grant_type"] == "authorization_code"
        authorization = self.codes.pop(str(form["code"]), None)
        if authorization is None:
            return JSONResponse({"error": "invalid_grant"}, 400)
        subject, expected = authorization
        assert challenge(str(form["code_verifier"])) == expected
        token = f"opaque-{secrets.token_urlsafe()}"
        self.tokens[token] = subject
        self.granted_scopes[token] = set(self.scopes.split())
        body = {
            "access_token": token,
            "scope": self.scopes,
            "token_type": "bearer",
            "id_token": "unsigned-id-token-must-be-ignored",
        }
        if self.include_refresh_token:
            body["refresh_token"] = secrets.token_urlsafe()
        return JSONResponse(
            body if self.lifetime is None else {**body, "expires_in": self.lifetime}
        )

    async def userinfo(self, request: Request) -> JSONResponse:
        assert "cookie" not in request.headers
        assert request.client is not None
        self.userinfo_ports.add(request.client.port)
        token = request.headers["Authorization"].removeprefix("Bearer ")
        self.userinfo_tokens.append(token)
        if token not in self.tokens:
            return JSONResponse(
                {}, 401, {"WWW-Authenticate": 'Bearer error="invalid_token"'}
            )
        if self.userinfo_status != 200:
            if self.error_in_body:
                return JSONResponse(
                    {"error": "insufficient_scope"}, self.userinfo_status
                )
            return JSONResponse(
                {"error_description": "private-diagnostic"},
                self.userinfo_status,
                {"WWW-Authenticate": 'Bearer error="insufficient_scope"'},
            )
        response = JSONResponse(
            {"sub": self.tokens[token], "name": "private-display-name"}
        )
        response.set_cookie("session", self.tokens[token])
        return response

    async def research(self, request: Request) -> JSONResponse:
        assert "cookie" not in request.headers
        assert request.method == "GET"
        assert request.client is not None
        self.project_ports.add(request.client.port)
        token = request.headers["Authorization"].removeprefix("Bearer ")
        self.project_tokens.append(token)
        subject = self.tokens[token]
        path = request.path_params["path"]
        scope = {
            "patent": PATENT_SCOPE,
            "researchInfrastructure": INFRASTRUCTURE_SCOPE,
        }.get(path.partition("/")[0])
        if subject in self.denied_readers or (
            scope is not None and scope not in self.granted_scopes[token]
        ):
            return JSONResponse({"message": "private-diagnostic"}, 401)
        project = {
            "id": 100002,
            "defaulttext": "Ein super Projekt",
            "pseudonymizedTitle": "Visible project" if subject == "bob" else None,
            "longtext": "Original project description",
            "canViewOriginalData": {
                "uniquename": "false" if subject == "bob" else "true"
            },
            "startdate": 1745186400000,
            "enddate": 1745964000000,
            "projectStatus": {"text": "Prepared"},
            "projectType": {"text": "Research"},
            "projectObjective": {"defaulttext": "Basic research"},
            "subjectAreas": [{"text": "Physics"}],
            "members": [{"id": 3, "projectPeriodStatus": None}],
            "publications": None,
        }
        paper = {"id": 7, "title": "Example paper"}
        patent = {
            "id": 9,
            "title": "Example patent",
            "patentNumber": "DE-123",
            "publicationNumber": "DE-456",
            "status": {"text": "Granted"},
            "country": {"defaulttext": "Germany"},
            "registrationType": {"text": "National"},
            "registrationDate": 1781042400000,
            "grantDate": 1793746800000,
            "inventors": [{"person": {"firstname": "Eva", "surname": "Lang"}}],
        }
        infrastructure = {"id": 8, "title": "Example facility"}
        if path in {"project", "publication/simple", "researchInfrastructure/simple"}:
            assert dict(request.query_params) == {"q": "Example", "l": "10"}
        else:
            assert not request.query_params
        bodies = {
            "project": [project],
            "project/100002": project,
            "publication/simple": [{**paper, "_foreigntext": None}],
            "publication/7": {
                **paper,
                "_foreigntext": None,
                "creators": [
                    {"sortorder": 2, "creatorname": "Chen", "firstname": "Lin"},
                    {
                        "sortorder": 1,
                        "creatorname": "Meier",
                        "firstname": "Eva",
                        "person": {"surname": "Private name", "academicdegree": None},
                    },
                    {"person": {"surname": "Uncredited private name"}},
                    {"creatorname": "Research group"},
                ],
                "globalIdentifiers": [
                    {"identifier": "untyped"},
                    {
                        "globalIdentifierType": {"text": "DOI"},
                        "identifier": "10.1234/example",
                    },
                ],
                "publicationType": {"defaulttext": "Article"},
                "publisher": {"label": "Example Press"},
                "releaseYear": 2024,
                "textAbstract": "Summary",
                "journal": {"defaulttext": "Example journal"},
            },
            "publication/7/bibtex": "@article{example, title={Example paper}}",
            "patent": [patent],
            "patent/9": patent,
            "researchInfrastructure/simple": [infrastructure],
            "researchInfrastructure/8": {
                **infrastructure,
                "description": "Example description",
                "researchInfrastructureKind": {"text": "Laboratory"},
                "researchInfrastructureType": {"defaulttext": "Facility"},
                "researchInfrastructureAccessKinds": [{"text": "By appointment"}],
                "researchInfrastructureOrganisations": [
                    {"orgunit": {"text": "Physics"}, "isCoordinator": True},
                    {"researchPartner": {"defaulttext": "Partner laboratory"}},
                ],
            },
        }
        response = JSONResponse(bodies[path])
        response.set_cookie("session", subject)
        return response


@pytest.fixture
async def deployment(
    settings: Settings, redis_port: int
) -> AsyncGenerator[tuple[Settings, Issuer]]:
    issuer = Issuer(settings.upstream_client_secret.get_secret_value())
    mock = FastMCP("Mock HISinOne")
    mock.custom_route("/qisserver/pages/oauth.faces", methods=["GET"])(issuer.authorize)
    mock.custom_route("/qisserver/api/v1/cs/psv/oauth/token", methods=["POST"])(
        issuer.token
    )
    mock.custom_route("/qisserver/api/v1/cs/psv/oauth/userinfo", methods=["GET"])(
        issuer.userinfo
    )
    mock.custom_route("/qisserver/api/v1/fs/res/{path:path}", methods=["GET"])(
        issuer.research
    )
    async with run_server_async(mock) as url:
        base = url.removesuffix("/mcp")
        configured = settings.model_copy(
            update={
                "upstream_base_url": f"{base}/qisserver",
                "oauth_available_scopes": AVAILABLE_SCOPES,
                "redis_port": redis_port,
            }
        )
        yield configured, issuer


@dataclass
class Flow:
    client_id: str
    verifier: str
    state: str
    callback: str

    async def redeem(
        self, browser: httpx2.AsyncClient, code: str, **changes: str
    ) -> httpx2.Response:
        form = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "code": code,
            "code_verifier": self.verifier,
            "redirect_uri": CALLBACK,
        }
        return await browser.post("/token", data={**form, **changes})


async def register(browser: httpx2.AsyncClient) -> str:
    registration = await browser.post(
        "/register",
        json={
            "client_name": "OAuth test",
            "redirect_uris": [CALLBACK],
            "token_endpoint_auth_method": "none",
        },
    )
    assert registration.status_code == 201
    return registration.json()["client_id"]


async def begin(
    browser: httpx2.AsyncClient,
    user: str,
    client_id: str | None = None,
    *,
    scope: str = f"openid {PROJECT_SCOPE}",
) -> Flow:
    client_id = client_id or await register(browser)
    verifier, state = secrets.token_urlsafe(48), secrets.token_urlsafe()
    start = await browser.get(
        "/authorize",
        params={
            "client_id": client_id,
            "redirect_uri": CALLBACK,
            "response_type": "code",
            "scope": scope,
            "state": state,
            "resource": "http://127.0.0.1/mcp",
            "code_challenge": challenge(verifier),
            "code_challenge_method": "S256",
        },
    )
    page = await browser.get(start.headers["location"])
    form = dict(re.findall(r'name="(txn_id|csrf_token)" value="([^"]+)"', page.text))
    assert set(form) == {"txn_id", "csrf_token"}
    consent = await browser.post("/consent", data={**form, "action": "approve"})
    upstream = consent.headers["location"]
    upstream_query = parse_qs(urlsplit(upstream).query)
    assert upstream_query["code_challenge"] != [challenge(verifier)]
    assert set(upstream_query["scope"][0].split()) == set(scope.split())
    async with httpx2.AsyncClient(trust_env=False) as wire:
        response = await wire.get(upstream, headers={"X-Test-User": user})
    return Flow(client_id, verifier, state, response.headers["location"])


async def finish(browser: httpx2.AsyncClient, flow: Flow) -> str:
    response = await browser.get(flow.callback)
    assert response.status_code == 302
    redirect = response.headers["location"]
    assert redirect.split("?")[0] == CALLBACK
    query = parse_qs(urlsplit(redirect).query)
    assert query["state"] == [flow.state]
    return query["code"][0]


async def authorize(
    server: ASGIServer,
    user: str,
    client_id: str,
    *,
    scope: str = f"openid {PROJECT_SCOPE}",
) -> str:
    async with server.http_client() as browser:
        flow = await begin(browser, user, client_id, scope=scope)
        code = await finish(browser, flow)
        response = await flow.redeem(browser, code)
        assert response.status_code == 200
        body = response.json()
        assert "refresh_token" not in body
        assert set(body["scope"].split()) == {*scope.split(), "ROLE_scientist"}
        assert "opaque-" not in response.text
        return body["access_token"]


async def test_read_only_publication_tools(deployment: tuple[Settings, Issuer]) -> None:
    settings, issuer = deployment
    async with asgi_server(create_server(settings)) as server:
        async with server.http_client() as browser:
            client_id = await register(browser)
        bearer = await authorize(server, "scientist", client_id)
        transport = server.transport(headers={"Authorization": f"Bearer {bearer}"})
        async with Client(transport) as client:
            query = {"query": " Example "}
            search = await client.call_tool("find_publications", query)
            paper = {"publication_id": 7, "title": "Example paper"}
            body = search.structured_content
            assert body is not None and body == {"result": [paper]}
            lookup = {"publication_id": body["result"][0]["publication_id"]}
            expected_results = {
                "get_publication": {
                    **paper,
                    "release_year": 2024,
                    "journal": "Example journal",
                    "abstract": "Summary",
                    "creators": ["Eva Meier", "Lin Chen", "Research group"],
                    "publication_type": "Article",
                    "identifiers": [{"type": "DOI", "value": "10.1234/example"}],
                    "publisher": "Example Press",
                },
                "get_publication_bibtex": {
                    "publication_id": 7,
                    "bibtex": "@article{example, title={Example paper}}",
                },
            }
            for name, expected in expected_results.items():
                result = await client.call_tool(name, lookup)
                assert result.structured_content == expected
            assert len(issuer.project_tokens) == 3
            assert all(
                issuer.tokens[token] == "scientist" for token in issuer.project_tokens
            )

            for args in ({"query": " "}, {"query": "Example", "limit": 21}):
                invalid = await client.call_tool(
                    "find_publications", args, raise_on_error=False
                )
                assert invalid.is_error
            assert len(issuer.project_tokens) == 3
            issuer.denied_readers.add("scientist")
            for name, args in (
                ("find_publications", query),
                ("get_publication", lookup),
                ("get_publication_bibtex", lookup),
            ):
                denied = await client.call_tool(name, args, raise_on_error=False)
                assert denied.is_error and "permission" in str(denied.content)
                assert "private-diagnostic" not in str(denied.content)


@pytest.mark.parametrize(
    ("scope", "collection", "args", "lookup", "id_param", "summary", "fields"),
    [
        (
            PATENT_SCOPE,
            "list_patents",
            {},
            "get_patent",
            "patent_id",
            {
                "patent_id": 9,
                "title": "Example patent",
                "patent_number": "DE-123",
                "status": "Granted",
                "country": "Germany",
            },
            {
                "publication_number": "DE-456",
                "registration_type": "National",
                "inventors": ["Eva Lang"],
                "registration_date": "2026-06-10T00:00:00+02:00",
                "grant_date": "2026-11-04T00:00:00+01:00",
            },
        ),
        (
            INFRASTRUCTURE_SCOPE,
            "find_research_infrastructures",
            {"query": " Example "},
            "get_research_infrastructure",
            "research_infrastructure_id",
            {"research_infrastructure_id": 8, "title": "Example facility"},
            {
                "description": "Example description",
                "kind": "Laboratory",
                "type": "Facility",
                "access_modes": ["By appointment"],
                "organizations": [
                    {"name": "Physics", "is_coordinator": True},
                    {"name": "Partner laboratory", "is_coordinator": None},
                ],
            },
        ),
    ],
)
async def test_resource_scope_allows_collection_and_lookup(
    deployment: tuple[Settings, Issuer],
    scope: str,
    collection: str,
    args: dict[str, str],
    lookup: str,
    id_param: str,
    summary: dict[str, object],
    fields: dict[str, object],
) -> None:
    settings, issuer = deployment
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as browser,
    ):
        client_id = await register(browser)
        issuer.scopes = "openid ROLE_scientist"
        original = await authorize(server, "scientist", client_id, scope="openid")
        issuer.scopes = f"openid {scope} ROLE_scientist"
        granted = await authorize(
            server, "scientist", client_id, scope=f"openid {scope}"
        )
        async with Client(
            server.transport(headers={"Authorization": f"Bearer {granted}"})
        ) as client:
            result = await client.call_tool(collection, args)
            body = result.structured_content
            assert body is not None and body == {"result": [summary]}
            record_id = body["result"][0][id_param]
            assert isinstance(record_id, int)
            record = await client.call_tool(lookup, {id_param: record_id})
            assert record.structured_content == {**summary, **fields}
        async with Client(
            server.transport(headers={"Authorization": f"Bearer {original}"})
        ) as client:
            for name, inputs in ((collection, args), (lookup, {id_param: record_id})):
                denied = await client.call_tool(name, inputs, raise_on_error=False)
                assert denied.is_error and "permission" in str(denied.content)
                assert "private-diagnostic" not in str(denied.content)
            assert {tool.name for tool in await client.list_tools()} == set(
                TOOL_CONTRACT
            )


async def test_userinfo_and_project_calls_reuse_connections_across_callers(
    deployment: tuple[Settings, Issuer],
) -> None:
    settings, issuer = deployment
    with patch(
        "hisinone_mcp.app.HisinoneOAuthProxy", wraps=HisinoneOAuthProxy
    ) as create_proxy:
        server = create_server(settings)
    verifier = create_proxy.call_args.kwargs["token_verifier"]
    assert isinstance(verifier, HisinoneTokenVerifier)
    async with asgi_server(server) as running:
        async with running.http_client() as browser:
            client_id = await register(browser)
        for user, title in (("alice", "Ein super Projekt"), ("bob", "Visible project")):
            token = await authorize(running, user, client_id)
            headers = {"Authorization": f"Bearer {token}"}
            async with Client(running.transport(headers=headers)) as client:
                result = await client.call_tool("get_project", {"project_id": 100002})
                assert result.structured_content is not None
                assert result.structured_content["title"] == title
        assert len(issuer.project_ports) == 1
        assert issuer.project_ports <= issuer.userinfo_ports
    assert verifier.http.is_closed


@pytest.mark.parametrize("lifetime", [120, None])
async def test_callers_and_restart(
    deployment: tuple[Settings, Issuer],
    caplog: pytest.LogCaptureFixture,
    lifetime: int | None,
) -> None:
    settings, issuer = deployment
    issuer.lifetime = lifetime
    collection = "mcp-upstream-tokens"
    async with (
        asgi_server(create_server(settings)) as server,
        RedisStore(url=settings.redis_dsn.encoded_string()) as raw,
    ):
        existing_keys = set(await raw.keys(collection=collection))
        async with server.http_client() as c:
            client_id = await register(c)
        alice, bob = await asyncio.gather(
            authorize(server, "alice", client_id), authorize(server, "bob", client_id)
        )

    seen: dict[str, str] = {}
    restarted = create_server(settings)

    @restarted.tool
    def identity() -> str:
        grant = get_access_token()
        assert grant and grant.subject and grant.expires_at
        seen[grant.subject] = grant.token
        return f"{grant.subject}/{grant.client_id}"

    async with asgi_server(restarted) as server:

        async def call(token: str) -> str:
            transport = server.transport(headers={"Authorization": f"Bearer {token}"})
            async with Client(transport) as client:
                assert client.server_info and client.server_info.name == "Research MCP"
                identity = (await client.call_tool("identity")).data
                tools = {tool.name: tool for tool in await client.list_tools()}
                assert set(tools) == {"identity", *TOOL_CONTRACT}
                for name, (inputs, id_field) in TOOL_CONTRACT.items():
                    tool = tools[name]
                    properties = tool.input_schema["properties"]
                    assert list(properties) == inputs
                    schema = tool.output_schema
                    assert schema
                    if "limit" in inputs:
                        limit = properties["limit"]
                        assert (
                            limit["minimum"],
                            limit["default"],
                            limit["maximum"],
                        ) == (1, 10, 20)
                        schema = schema["properties"]["result"]["items"]
                    assert schema["properties"][id_field]["type"] == "integer"
                    assert id_field in schema["required"]
                    assert "id" not in schema["properties"]
                    assert tool.annotations and tool.annotations.read_only_hint
                    assert tool.annotations.destructive_hint is False
                for name, fields in (
                    ("get_project", ("start_date", "end_date")),
                    ("get_patent", ("registration_date", "grant_date")),
                ):
                    schema = tools[name].output_schema
                    assert schema
                    for field in fields:
                        variants = schema["properties"][field]["anyOf"]
                        assert {"type": "string", "format": "date-time"} in variants
                        assert {"type": "null"} in variants
                expected = (
                    "Visible project"
                    if identity.startswith("bob/")
                    else "Ein super Projekt"
                )
                search = await client.call_tool("find_projects", {"query": "Example"})
                body = search.structured_content
                row = {"project_id": 100002, "title": expected, "status": "Prepared"}
                assert body is not None and body == {"result": [row]}
                project = await client.call_tool(
                    "get_project", {"project_id": body["result"][0]["project_id"]}
                )
                assert project.structured_content == {
                    **row,
                    "description": None
                    if identity.startswith("bob/")
                    else "Original project description",
                    "project_type": "Research",
                    "objective": "Basic research",
                    "subject_areas": ["Physics"],
                    "start_date": "2025-04-21T00:00:00+02:00",
                    "end_date": "2025-04-30T00:00:00+02:00",
                }
                return identity

        assert await asyncio.gather(call(alice), call(bob)) == [
            f"alice/{client_id}",
            f"bob/{client_id}",
        ]
        assert seen["alice"] != seen["bob"]
        assert issuer.tokens[seen["alice"]] == "alice"
        assert issuer.tokens[seen["bob"]] == "bob"
        assert set(issuer.userinfo_tokens) == set(seen.values())
        assert set(issuer.project_tokens) == set(seen.values())
        headers = {"Authorization": f"Bearer {alice}"}
        async with server.http_client() as c:
            with patch.object(RedisStore, "get", side_effect=RedisError("offline")):
                unavailable = await c.post("/mcp", headers=headers)
                assert unavailable.status_code == 401
            attempts = len(issuer.userinfo_tokens)
            raw = await c.post(
                "/mcp", headers={"Authorization": f"Bearer {seen['alice']}"}
            )
            assert raw.status_code == 401
            assert len(issuer.userinfo_tokens) == attempts
            for upstream, expected in [(401, 403), (403, 403), (429, 503), (503, 503)]:
                issuer.userinfo_status = upstream
                response = await c.post("/mcp", headers=headers)
                assert response.status_code == expected
                assert "invalid_token" not in response.headers.get(
                    "WWW-Authenticate", ""
                )
                assert "private-diagnostic" not in response.text
            issuer.error_in_body, issuer.userinfo_status = True, 401
            assert (await c.post("/mcp", headers=headers)).status_code == 403
            issuer.userinfo_status = 200
            assert await call(alice) == f"alice/{client_id}"
            del issuer.tokens[seen["alice"]]
            revoked = await c.post("/mcp", headers=headers)
            assert revoked.status_code == 401
            assert 'error="invalid_token"' in revoked.headers["WWW-Authenticate"]
            attempts = len(issuer.userinfo_tokens)
            assert (await c.post("/mcp", headers=headers)).status_code == 401
            assert len(issuer.userinfo_tokens) == attempts + 1
            assert await call(bob) == f"bob/{client_id}"

    async with RedisStore(url=settings.redis_dsn.encoded_string()) as raw:
        new_keys = set(await raw.keys(collection=collection)) - existing_keys
        assert len(new_keys) == 2
        for key in new_keys:
            encrypted, ttl = await raw.ttl(key, collection=collection)
            assert encrypted and "__encrypted_data__" in encrypted
            assert ttl and 0 < ttl <= (lifetime or 365 * 24 * 60 * 60)
            assert "opaque-" not in str(encrypted)
    for secret in [*seen.values(), alice, bob, issuer.client_secret]:
        assert secret not in caplog.text


async def test_project_permission_denial_keeps_the_session(
    deployment: tuple[Settings, Issuer],
) -> None:
    settings, issuer = deployment
    settings = settings.model_copy(
        update={
            "oauth_required_scopes": frozenset({"openid", PROJECT_SCOPE}),
            "upstream_timezone": ZoneInfo("UTC"),
        }
    )
    async with asgi_server(create_server(settings)) as server:
        async with server.http_client() as browser:
            client_id = await register(browser)
        bearer = await authorize(server, "scientist", client_id)
        transport = server.transport(headers={"Authorization": f"Bearer {bearer}"})
        async with Client(transport) as client:
            issuer.denied_readers.add("scientist")
            denied = await client.call_tool(
                "get_project", {"project_id": 100002}, raise_on_error=False
            )
            assert denied.is_error
            assert "permission" in str(denied.content)
            assert "private-diagnostic" not in str(denied.content)
            issuer.denied_readers.clear()
            allowed = await client.call_tool("get_project", {"project_id": 100002})
            assert allowed.structured_content is not None
            assert allowed.structured_content["project_id"] == 100002
            assert allowed.structured_content["start_date"] == "2025-04-20T22:00:00Z"
        assert len(issuer.project_tokens) == 2
        assert len(set(issuer.project_tokens)) == 1


async def test_code_binding_and_expiry(deployment: tuple[Settings, Issuer]) -> None:
    settings, issuer = deployment
    issuer.lifetime = 5
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as c,
    ):
        flow = await begin(c, "alice")
        async with server.http_client() as other_browser:
            assert (await other_browser.get(flow.callback)).status_code == 403
        parsed_callback = httpx2.URL(flow.callback)
        bad_state = parsed_callback.copy_set_param("state", "unknown-state")
        assert (await c.get(bad_state)).status_code == 400
        code = await finish(c, flow)
        other = await begin(c, "bob")
        for incorrect, expected in [
            ({"client_id": other.client_id}, "invalid_grant"),
            ({"code_verifier": "z" * 64}, "invalid_grant"),
            ({"redirect_uri": "http://127.0.0.1:9191/wrong"}, "invalid_request"),
        ]:
            denied = await flow.redeem(c, code, **incorrect)
            assert denied.status_code in (400, 401)
            assert denied.json()["error"] == expected
        response = await flow.redeem(c, code)
        assert response.status_code == 200
        result = response.json()
        assert result["expires_in"] == issuer.lifetime
        assert (await flow.redeem(c, code)).json()["error"] == "invalid_grant"
        with patch("fastmcp.server.auth.jwt_issuer.time") as clock:
            clock.time.return_value = time.time() + issuer.lifetime + 1
            expired = await c.post(
                "/mcp", headers={"Authorization": f"Bearer {result['access_token']}"}
            )
        assert expired.status_code == 401
        assert not issuer.userinfo_tokens


@pytest.mark.parametrize("lifetime", [0, -1])
async def test_nonpositive_lifetime_at_redemption(
    deployment: tuple[Settings, Issuer], lifetime: int
) -> None:
    settings, issuer = deployment
    issuer.lifetime = lifetime
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as browser,
    ):
        flow = await begin(browser, "alice")
        code = await finish(browser, flow)
        response = await flow.redeem(browser, code)
        assert response.is_client_error
        body = response.json()
        assert body["error"] == "invalid_grant"
        assert "access_token" not in body


@pytest.mark.parametrize("requested", ["openid", f"openid {PROJECT_SCOPE}"])
async def test_openid_grant_can_list_tools_after_a_denied_project_read(
    deployment: tuple[Settings, Issuer], requested: str
) -> None:
    settings, issuer = deployment
    issuer.scopes = "openid"
    issuer.denied_readers.add("alice")
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as browser,
    ):
        flow = await begin(browser, "alice", scope=requested)
        code = await finish(browser, flow)
        response = await flow.redeem(browser, code)
        assert response.status_code == 200
        body = response.json()
        assert body["scope"] == "openid"
        transport = server.transport(
            headers={"Authorization": f"Bearer {body['access_token']}"}
        )
        async with Client(transport) as client:
            denied = await client.call_tool(
                "get_project", {"project_id": 100002}, raise_on_error=False
            )
            assert denied.is_error and "permission" in str(denied.content)
            assert {tool.name for tool in await client.list_tools()} == set(
                TOOL_CONTRACT
            )
        assert len(issuer.project_tokens) == 1


@pytest.mark.parametrize(
    ("required", "granted"),
    [
        (frozenset({"openid"}), PROJECT_SCOPE),
        (frozenset({"openid", PROJECT_SCOPE}), "openid"),
    ],
)
async def test_grant_missing_a_required_scope_is_rejected(
    deployment: tuple[Settings, Issuer], required: frozenset[str], granted: str
) -> None:
    settings, issuer = deployment
    settings = settings.model_copy(update={"oauth_required_scopes": required})
    issuer.scopes = granted
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as c,
    ):
        challenge = await c.post("/mcp")
        assert challenge.status_code == 401
        challenge_scope = " ".join(sorted(required))
        assert f'scope="{challenge_scope}"' in challenge.headers["WWW-Authenticate"]
        flow = await begin(c, "alice")
        code = await finish(c, flow)
        response = await flow.redeem(c, code)
        assert response.status_code == 200
        body = response.json()
        assert body["scope"] == granted
        denied = await c.post(
            "/mcp", headers={"Authorization": f"Bearer {body['access_token']}"}
        )
        assert denied.status_code == 403
        assert 'error="insufficient_scope"' in denied.headers["WWW-Authenticate"]


async def test_pending_code_uses_upstream_scopes_across_restart(
    deployment: tuple[Settings, Issuer],
) -> None:
    settings, issuer = deployment
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as browser,
    ):
        flow = await begin(browser, "alice", scope=PROJECT_SCOPE)
        code = await finish(browser, flow)

    async with (
        asgi_server(create_server(settings)) as restarted,
        restarted.http_client() as browser,
    ):
        response = await flow.redeem(browser, code)
        assert response.status_code == 200
        assert response.json()["scope"] == issuer.scopes


@pytest.mark.parametrize(
    ("lifetime", "fallback", "mcp_lifetime", "refresh", "expected"),
    [
        (None, None, None, False, 365 * 24 * 60 * 60),
        (None, None, None, True, 3600),
        (None, 900, None, False, 900),
        (None, 900, None, True, 900),
        (172800, 900, None, False, 172800),
        (172800, 900, 300, False, 300),
        (120, 900, 300, False, 120),
        (None, 120, 300, False, 120),
        (120, None, 300, True, 300),
    ],
)
async def test_access_token_lifetime(
    deployment: tuple[Settings, Issuer],
    lifetime: int | None,
    fallback: int | None,
    mcp_lifetime: int | None,
    refresh: bool,
    expected: int,
) -> None:
    settings, issuer = deployment
    issuer.lifetime = lifetime
    issuer.include_refresh_token = refresh
    settings = settings.model_copy(
        update={
            "oauth_fallback_access_token_expiry_seconds": fallback,
            "oauth_mcp_access_token_expiry_seconds": mcp_lifetime,
        }
    )
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as browser,
    ):
        flow = await begin(browser, "alice")
        code = await finish(browser, flow)
        response = await flow.redeem(browser, code)
        assert response.status_code == 200
        body = response.json()
        assert body["expires_in"] == expected
        with patch("fastmcp.server.auth.jwt_issuer.time") as clock:
            clock.time.return_value = time.time() + expected + 1
            expired = await browser.post(
                "/mcp", headers={"Authorization": f"Bearer {body['access_token']}"}
            )
        assert expired.status_code == 401


async def test_failed_exchange_returns_no_authorization_code(
    deployment: tuple[Settings, Issuer],
    caplog: pytest.LogCaptureFixture,
) -> None:
    settings, issuer = deployment
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as c,
    ):
        flow = await begin(c, "alice")
        issuer.codes.clear()
        error = await c.get(flow.callback)
        assert error.is_error
        assert "location" not in error.headers
        secret = settings.upstream_client_secret.get_secret_value()
        assert secret not in error.text
        assert secret not in caplog.text


@pytest.mark.parametrize("allowed", [[CALLBACK], []])
async def test_downstream_redirect_allowlist(
    deployment: tuple[Settings, Issuer], allowed: list[str]
) -> None:
    settings, _ = deployment
    configured = settings.model_copy(
        update={"oauth_allowed_client_redirect_uris": allowed}
    )
    async with (
        asgi_server(create_server(configured)) as server,
        server.http_client() as browser,
    ):
        rejected = await browser.post(
            "/register", json={"redirect_uris": ["https://other.test/callback"]}
        )
        assert rejected.status_code == 400
        assert rejected.json()["error"] == "invalid_redirect_uri"
        if allowed:
            flow = await begin(browser, "alice")
            assert await finish(browser, flow)
        else:
            rejected = await browser.post(
                "/register", json={"redirect_uris": [CALLBACK]}
            )
            assert rejected.status_code == 400
            assert rejected.json()["error"] == "invalid_redirect_uri"


async def test_clearing_redirect_allowlist_restores_registered_loopback_ports(
    deployment: tuple[Settings, Issuer],
) -> None:
    settings, _ = deployment
    fixed_port = settings.model_copy(
        update={"oauth_allowed_client_redirect_uris": [CALLBACK]}
    )
    async with (
        asgi_server(create_server(fixed_port)) as server,
        server.http_client() as browser,
    ):
        client_id = await register(browser)

    restarted = create_server(settings)
    async with asgi_server(restarted):
        assert isinstance(restarted.auth, HisinoneOAuthProxy)
        client = await restarted.auth.get_client(client_id)
        assert client is not None
        new_port = AnyUrl("http://127.0.0.1:9292/return")
        assert client.validate_redirect_uri(new_port) == new_port


async def test_consent_denial_and_redirect_registration(
    deployment: tuple[Settings, Issuer],
) -> None:
    settings, _ = deployment
    async with (
        asgi_server(create_server(settings)) as server,
        server.http_client() as c,
    ):
        flow = await begin(c, "alice")
        upstream_query = parse_qs(urlsplit(flow.callback).query)
        denied = await c.get(
            "/auth/callback",
            params={
                "state": upstream_query["state"][0],
                "error": "access_denied",
            },
        )
        redirect = denied.headers["location"]
        assert redirect.startswith(CALLBACK + "?")
        query = parse_qs(urlsplit(redirect).query)
        assert query["error"] == ["access_denied"]
        assert query["state"] == [flow.state]
        assert "code" not in query
        for client_id in (flow.client_id, settings.upstream_client_id):
            invalid = await c.get(
                "/authorize",
                params={
                    "client_id": client_id,
                    "redirect_uri": CALLBACK + "/unregistered",
                    "response_type": "code",
                    "code_challenge": challenge(flow.verifier),
                    "code_challenge_method": "S256",
                },
            )
            assert invalid.status_code == 400
            assert "location" not in invalid.headers
        flow = await begin(c, "bob")
        code = await finish(c, flow)
        exchanges = await asyncio.gather(flow.redeem(c, code), flow.redeem(c, code))
        assert sorted(r.status_code for r in exchanges) == [200, 401]
