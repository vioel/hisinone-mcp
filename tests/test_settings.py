from pathlib import Path
from unittest.mock import patch

import pytest
from fastmcp import FastMCP
from pydantic import AnyHttpUrl, ValidationError

from hisinone_mcp.app import main
from hisinone_mcp.settings import Settings, load_settings


def test_settings_from_dotenv_and_environment(
    settings: Settings, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert settings.oauth_available_scopes == {"openid"}
    assert settings.oauth_required_scopes == {"openid"}
    assert settings.upstream_timezone.key == "Europe/Berlin"
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text(
        "SERVER_HOST=127.0.0.2\nSERVER_PORT=8100\nUPSTREAM_TIMEZONE=Etc/UTC\n"
        "REDIS_PASSWORD=test-password\n"
        'OAUTH_ALLOWED_CLIENT_REDIRECT_URIS=["https://client.test/callback"]\n'
        'OAUTH_AVAILABLE_SCOPES=["openid","campus.projects:read"]\n'
        'OAUTH_REQUIRED_SCOPES=["openid","campus.projects:read"]\n'
        "OAUTH_MCP_ACCESS_TOKEN_EXPIRY_SECONDS=300\n",
        encoding="utf-8",
    )
    monkeypatch.delenv("SERVER_HOST", raising=False)
    monkeypatch.setenv("SERVER_PORT", "8101")
    monkeypatch.setenv("OAUTH_FALLBACK_ACCESS_TOKEN_EXPIRY_SECONDS", "900")
    load_settings.cache_clear()
    try:
        loaded = load_settings()
        assert load_settings() is loaded
        assert loaded.upstream_timezone.key == "Etc/UTC"
        assert loaded.redis_dsn.password == "test-password"
        assert loaded.oauth_fallback_access_token_expiry_seconds == 900
        assert loaded.oauth_mcp_access_token_expiry_seconds == 300
        assert loaded.oauth_available_scopes == {"openid", "campus.projects:read"}
        assert loaded.oauth_required_scopes == {"openid", "campus.projects:read"}
        assert loaded.oauth_allowed_client_redirect_uris == [
            "https://client.test/callback"
        ]
        for secret in (
            "test-password",
            settings.upstream_client_secret.get_secret_value(),
            settings.oauth_signing_key.get_secret_value(),
            settings.oauth_encryption_key.get_secret_value(),
        ):
            assert secret not in repr(loaded)
            assert secret not in loaded.model_dump_json()
        with patch.object(FastMCP, "run") as run:
            main()
        run.assert_called_once_with(transport="http", host="127.0.0.2", port=8101)
    finally:
        load_settings.cache_clear()


@pytest.mark.parametrize("scopes", ["[]", '["campus.projects:read"]'])
@pytest.mark.parametrize("key", ["OAUTH_REQUIRED_SCOPES", "OAUTH_AVAILABLE_SCOPES"])
def test_oauth_scopes_must_include_openid(
    settings: Settings, monkeypatch: pytest.MonkeyPatch, scopes: str, key: str
) -> None:
    monkeypatch.setenv("OAUTH_AVAILABLE_SCOPES", '["openid","campus.projects:read"]')
    monkeypatch.setenv(key, scopes)
    with pytest.raises(ValidationError, match=f"{key} must include openid"):
        Settings.model_validate({})


def test_required_scopes_must_be_available(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("OAUTH_REQUIRED_SCOPES", '["openid","campus.access"]')
    with pytest.raises(ValidationError, match=r"campus\.access"):
        Settings.model_validate({})


@pytest.mark.parametrize("key", ["SERVER_HOST", "REDIS_HOST"])
@pytest.mark.parametrize("host", ["localhost", "::1", "127.0.0.1/32"])
def test_hosts_require_ipv4_addresses(
    settings: Settings, monkeypatch: pytest.MonkeyPatch, key: str, host: str
) -> None:
    monkeypatch.setenv(key, host)
    with pytest.raises(ValidationError, match=key.lower()):
        Settings.model_validate({})


@pytest.mark.parametrize(
    "root", ["https://other.test", "https://other.test/campus/qisserver"]
)
def test_upstream_urls_follow_the_installation_root(
    settings: Settings, root: str
) -> None:
    assert settings.upstream_token_endpoint.host == "his.test"
    moved = settings.model_copy(update={"upstream_base_url": root})
    assert moved.upstream_api_base_url == AnyHttpUrl(f"{root}/api/v1")
    assert moved.upstream_authorization_endpoint == AnyHttpUrl(
        f"{root}/pages/oauth.faces"
    )
    assert moved.upstream_token_endpoint == AnyHttpUrl(
        f"{root}/api/v1/cs/psv/oauth/token"
    )
    assert moved.upstream_userinfo_endpoint == AnyHttpUrl(
        f"{root}/api/v1/cs/psv/oauth/userinfo"
    )


def test_upstream_path_overrides(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("UPSTREAM_API_BASE_PATH", "rest")
    monkeypatch.setenv("UPSTREAM_AUTHORIZATION_PATH", "auth/authorize")
    monkeypatch.setenv("UPSTREAM_TOKEN_PATH", "auth/token")
    monkeypatch.setenv("UPSTREAM_USERINFO_PATH", "auth/userinfo")
    loaded = Settings.model_validate({})
    root = settings.upstream_base_url
    assert loaded.upstream_api_base_url == AnyHttpUrl(f"{root}/rest")
    assert loaded.upstream_authorization_endpoint == AnyHttpUrl(
        f"{root}/auth/authorize"
    )
    assert loaded.upstream_token_endpoint == AnyHttpUrl(f"{root}/auth/token")
    assert loaded.upstream_userinfo_endpoint == AnyHttpUrl(f"{root}/auth/userinfo")


def test_redis_dsn_encodes_credentials(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("REDIS_HOST", "192.0.2.1")
    monkeypatch.setenv("REDIS_PORT", "6380")
    monkeypatch.setenv("REDIS_DB", "3")
    monkeypatch.setenv("REDIS_SCHEME", "rediss")
    monkeypatch.setenv("REDIS_USERNAME", "team@lab/%2F")
    monkeypatch.setenv("REDIS_PASSWORD", "p/a:%2F#?")
    loaded = Settings.model_validate({})
    assert loaded.redis_username == "team@lab/%2F"
    assert loaded.redis_dsn.encoded_string() == (
        "rediss://team%40lab%2F%252F:p%2Fa%3A%252F%23%3F@192.0.2.1:6380/3"
    )


def test_redis_defaults(settings: Settings, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("REDIS_HOST")
    monkeypatch.delenv("REDIS_PORT")
    assert (
        Settings.model_validate({}).redis_dsn.encoded_string()
        == "redis://127.0.0.1:6379/0"
    )


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("REDIS_SCHEME", "http"),
        ("REDIS_PORT", "0"),
        ("REDIS_PORT", "65536"),
        ("REDIS_DB", "-1"),
    ],
)
def test_invalid_redis_settings_hide_credentials(
    settings: Settings, monkeypatch: pytest.MonkeyPatch, key: str, value: str
) -> None:
    monkeypatch.setenv("REDIS_PASSWORD", "test-password")
    monkeypatch.setenv(key, value)
    with pytest.raises(ValidationError, match=key.lower()) as error:
        Settings.model_validate({})
    assert "test-password" not in str(error.value)


def test_upstream_client_secret_minimum(
    settings: Settings, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("UPSTREAM_CLIENT_SECRET", "x" * 63)
    with pytest.raises(ValidationError, match="upstream_client_secret"):
        Settings.model_validate({})
    monkeypatch.setenv("UPSTREAM_CLIENT_SECRET", "x" * 64)
    assert (
        Settings.model_validate({}).upstream_client_secret.get_secret_value()
        == "x" * 64
    )


@pytest.mark.parametrize(
    "key",
    [
        "A" * 44,
        "A" * 42 + "==",
        "A" * 43,
        "!" * 44,
        "/" * 42 + "8=",
        "A" * 42 + "B=",
    ],
)
def test_encryption_key_requires_32_bytes_in_canonical_base64url(
    settings: Settings, monkeypatch: pytest.MonkeyPatch, key: str
) -> None:
    monkeypatch.setenv("OAUTH_ENCRYPTION_KEY", key)
    with pytest.raises(ValidationError, match="oauth_encryption_key") as error:
        Settings.model_validate({})
    assert key not in str(error.value)


@pytest.mark.parametrize(
    "key",
    [
        "OAUTH_FALLBACK_ACCESS_TOKEN_EXPIRY_SECONDS",
        "OAUTH_MCP_ACCESS_TOKEN_EXPIRY_SECONDS",
    ],
)
@pytest.mark.parametrize("value", ["0", "-1"])
def test_oauth_expiry_must_be_positive(
    settings: Settings, monkeypatch: pytest.MonkeyPatch, key: str, value: str
) -> None:
    monkeypatch.setenv(key, value)
    with pytest.raises(ValidationError, match=key.lower()):
        Settings.model_validate({})


@pytest.mark.parametrize(("raw", "expected"), [("", None), ("[]", [])])
def test_optional_oauth_environment_values(
    settings: Settings,
    monkeypatch: pytest.MonkeyPatch,
    raw: str,
    expected: list[str] | None,
) -> None:
    monkeypatch.setenv("OAUTH_ALLOWED_CLIENT_REDIRECT_URIS", raw)
    monkeypatch.setenv("OAUTH_MCP_ACCESS_TOKEN_EXPIRY_SECONDS", "")
    monkeypatch.setenv("OAUTH_FALLBACK_ACCESS_TOKEN_EXPIRY_SECONDS", "")
    loaded = Settings.model_validate({})
    assert loaded.oauth_allowed_client_redirect_uris == expected
    assert loaded.oauth_mcp_access_token_expiry_seconds is None
    assert loaded.oauth_fallback_access_token_expiry_seconds is None


@pytest.mark.parametrize(
    "key",
    [
        "SERVER_HOST",
        "SERVER_PORT",
        "SERVER_BASE_URL",
        "UPSTREAM_BASE_URL",
        "UPSTREAM_CLIENT_ID",
        "UPSTREAM_CLIENT_SECRET",
        "OAUTH_SIGNING_KEY",
        "OAUTH_ENCRYPTION_KEY",
    ],
)
def test_required_settings(
    settings: Settings, monkeypatch: pytest.MonkeyPatch, key: str
) -> None:
    monkeypatch.delenv(key)
    with pytest.raises(ValidationError, match=key.lower()):
        Settings.model_validate({})
