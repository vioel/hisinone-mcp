import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from http.cookiejar import CookieJar, DefaultCookiePolicy

import httpx2
from cryptography.fernet import Fernet
from fastmcp import FastMCP
from fastmcp import settings as fastmcp_settings
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from starlette.types import ASGIApp

from hisinone_mcp.auth.provider import HisinoneOAuthProxy
from hisinone_mcp.auth.verifier import HisinoneTokenVerifier
from hisinone_mcp.settings import Settings, load_settings
from hisinone_mcp.tools import register_research_tools


@dataclass
class BorrowedTransport(httpx2.AsyncBaseTransport):
    """Keep the server's pool open when FastMCP closes a tool's HTTP client."""

    pool: httpx2.AsyncBaseTransport

    async def handle_async_request(self, request: httpx2.Request) -> httpx2.Response:
        return await self.pool.handle_async_request(request)


def create_server(settings: Settings) -> FastMCP:
    logging.basicConfig(level=fastmcp_settings.log_level)

    cookie_policy = DefaultCookiePolicy(allowed_domains=())
    cookies = CookieJar(policy=cookie_policy)
    pool = httpx2.AsyncHTTPTransport(trust_env=False)
    http = httpx2.AsyncClient(transport=pool, trust_env=False, cookies=cookies)

    redis = RedisStore(url=settings.redis_dsn.encoded_string())
    fernet = Fernet(settings.oauth_encryption_key.get_secret_value())
    store = FernetEncryptionWrapper(redis, fernet=fernet)

    verifier = HisinoneTokenVerifier(
        http=http,
        userinfo_endpoint=str(settings.upstream_userinfo_endpoint),
        client_id=settings.upstream_client_id,
        required_scopes=sorted(settings.oauth_required_scopes),
    )
    auth = HisinoneOAuthProxy(
        base_url=settings.server_base_url,
        upstream_authorization_endpoint=str(settings.upstream_authorization_endpoint),
        upstream_token_endpoint=str(settings.upstream_token_endpoint),
        upstream_client_id=settings.upstream_client_id,
        upstream_client_secret=settings.upstream_client_secret.get_secret_value(),
        forward_resource=False,
        token_verifier=verifier,
        valid_scopes=sorted(settings.oauth_available_scopes),
        client_storage=store,
        jwt_signing_key=settings.oauth_signing_key.get_secret_value(),
        fallback_access_token_expiry_seconds=(
            settings.oauth_fallback_access_token_expiry_seconds
        ),
        fastmcp_access_token_expiry_seconds=settings.oauth_mcp_access_token_expiry_seconds,
        allowed_client_redirect_uris=settings.oauth_allowed_client_redirect_uris,
    )

    @asynccontextmanager
    async def lifespan(_: FastMCP) -> AsyncGenerator[None]:
        async with redis, http:
            yield

    server = FastMCP(settings.server_name, auth=auth, lifespan=lifespan)
    register_research_tools(
        server,
        api_base_url=str(settings.upstream_api_base_url),
        timezone=settings.upstream_timezone,
        transport=BorrowedTransport(pool),
    )
    return server


def create_app() -> ASGIApp:
    settings = load_settings()
    server = create_server(settings)
    return server.http_app()


def main() -> None:
    settings = load_settings()
    server = create_server(settings)
    server.run(
        transport="http",
        host=str(settings.server_host),
        port=settings.server_port,
    )
