import secrets
import shutil
import socket
import subprocess
import time
from collections.abc import Iterator
from pathlib import Path

import pytest
from cryptography.fernet import Fernet

from hisinone_mcp.settings import Settings


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--hisinone-openapi",
        type=Path,
        metavar="PATH",
        help="Check the generated client against an original HISinOne OpenAPI export.",
    )


@pytest.fixture(scope="session")
def hisinone_openapi(pytestconfig: pytest.Config) -> Path:
    source: Path | None = pytestconfig.getoption("hisinone_openapi")
    if source is None:
        pytest.skip("Supply --hisinone-openapi=PATH for full-export checks")
    path = pytestconfig.invocation_params.dir / source
    if not path.is_file():
        pytest.fail(f"Expected an OpenAPI export file at {path}")
    return path


@pytest.fixture
def settings(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Settings:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("SERVER_NAME", "Research MCP")
    monkeypatch.setenv("SERVER_HOST", "127.0.0.1")
    monkeypatch.setenv("SERVER_PORT", "8000")
    monkeypatch.setenv("SERVER_BASE_URL", "http://127.0.0.1")
    monkeypatch.setenv("UPSTREAM_BASE_URL", "https://his.test/qisserver")
    monkeypatch.delenv("UPSTREAM_TIMEZONE", raising=False)
    monkeypatch.setenv("UPSTREAM_CLIENT_ID", "his-client")
    monkeypatch.setenv("UPSTREAM_CLIENT_SECRET", secrets.token_hex(32))
    for route in ("API_BASE", "AUTHORIZATION", "TOKEN", "USERINFO"):
        monkeypatch.delenv(f"UPSTREAM_{route}_PATH", raising=False)
    monkeypatch.setenv("OAUTH_SIGNING_KEY", "test-signing-key-" * 3)
    monkeypatch.setenv("OAUTH_ENCRYPTION_KEY", Fernet.generate_key().decode())
    for key in (
        "OAUTH_ALLOWED_CLIENT_REDIRECT_URIS",
        "OAUTH_AVAILABLE_SCOPES",
        "OAUTH_FALLBACK_ACCESS_TOKEN_EXPIRY_SECONDS",
        "OAUTH_MCP_ACCESS_TOKEN_EXPIRY_SECONDS",
        "OAUTH_REQUIRED_SCOPES",
        "REDIS_DB",
        "REDIS_PASSWORD",
        "REDIS_SCHEME",
        "REDIS_USERNAME",
    ):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("REDIS_HOST", "127.0.0.1")
    monkeypatch.setenv("REDIS_PORT", "1")
    return Settings.model_validate({})


@pytest.fixture(scope="module")
def redis_port(tmp_path_factory: pytest.TempPathFactory) -> Iterator[int]:
    executable = shutil.which("redis-server")
    if not executable:
        pytest.skip("The OAuth integration tests require redis-server on PATH")
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    directory = tmp_path_factory.mktemp("oauth-redis")
    with subprocess.Popen(
        [
            executable,
            "--bind",
            "127.0.0.1",
            "--port",
            str(port),
            "--save",
            "",
            "--appendonly",
            "no",
            "--dir",
            str(directory),
        ],
        stdout=subprocess.DEVNULL,
    ) as process:
        try:
            deadline = time.monotonic() + 5
            while process.poll() is None and time.monotonic() < deadline:
                try:
                    with socket.create_connection(("127.0.0.1", port), timeout=0.1):
                        break
                except OSError:
                    time.sleep(0.02)
            else:
                pytest.fail("The private test Redis failed to start")
            yield port
        finally:
            process.terminate()
