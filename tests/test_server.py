import logging
from unittest.mock import patch

import pytest
import uvicorn
from fastmcp import settings as fastmcp_settings
from starlette.testclient import TestClient

from hisinone_mcp.app import create_app, create_server, main
from hisinone_mcp.settings import Settings


@pytest.mark.parametrize("path", ["/mcp", "/research/mcp"])
def test_mcp_requires_oauth_and_advertises_discovery(
    settings: Settings,
    caplog: pytest.LogCaptureFixture,
    monkeypatch: pytest.MonkeyPatch,
    path: str,
) -> None:
    scopes = frozenset({"openid", "campus.projects:read"})
    settings = settings.model_copy(update={"oauth_available_scopes": scopes})
    monkeypatch.setattr(fastmcp_settings, "streamable_http_path", path)
    caplog.set_level(logging.INFO, logger="httpx2")
    with (
        patch("hisinone_mcp.app.load_settings", return_value=settings),
        TestClient(create_app(), base_url=str(settings.server_base_url)) as c,
    ):
        response = c.post(path)
        assert response.status_code == 401
        challenge = response.headers["WWW-Authenticate"]
        assert "invalid_token" not in challenge
        assert 'scope="openid"' in challenge
        metadata_url = challenge.split('resource_metadata="')[1].split('"')[0]
        resource = c.get(metadata_url).json()
        assert resource["resource"] == f"http://127.0.0.1{path}"
        assert resource["authorization_servers"] == ["http://127.0.0.1/"]
        assert set(resource["scopes_supported"]) == scopes
        discovery = "/.well-known/oauth-authorization-server?probe=discovery"
        metadata = c.get(discovery).json()
        assert discovery in caplog.text
        assert metadata["registration_endpoint"].endswith("/register")
        assert "S256" in metadata["code_challenge_methods_supported"]
        assert set(metadata["scopes_supported"]) == scopes
        invalid = c.post(path, headers={"Authorization": "Bearer not-a-grant"})
        assert invalid.status_code == 401
        assert 'error="invalid_token"' in invalid.headers["WWW-Authenticate"]


def test_registration_rejects_unavailable_scope(settings: Settings) -> None:
    with TestClient(create_server(settings).http_app()) as client:
        response = client.post(
            "/register",
            json={
                "redirect_uris": ["http://127.0.0.1/callback"],
                "scope": "openid fs.res.projects:read",
            },
        )
        assert response.status_code == 400
        assert response.json()["error"] == "invalid_client_metadata"


def test_console_uses_streamable_http_path(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(fastmcp_settings, "streamable_http_path", "/research/mcp")
    with (
        patch("hisinone_mcp.app.load_settings", return_value=settings),
        patch.object(uvicorn.Server, "serve", autospec=True) as serve,
    ):
        main()
    assert serve.call_args.args[0].config.app.state.path == "/research/mcp"
