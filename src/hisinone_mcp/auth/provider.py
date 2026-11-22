from typing import Protocol, cast

from fastmcp.server.auth import OAuthProxy
from fastmcp.server.auth.oauth_proxy.models import ProxyDCRClient
from joserfc.errors import JoseError
from mcp.server.auth.provider import AccessToken
from mcp.shared.auth import OAuthClientInformationFull
from starlette.middleware import Middleware

from hisinone_mcp.auth.http import auth_errors


class _MiddlewareProvider(Protocol):
    def get_middleware(self) -> list[Middleware]: ...


class HisinoneOAuthProxy(OAuthProxy):
    async def get_client(self, client_id: str) -> OAuthClientInformationFull | None:
        if client_id == self._upstream_client_id:
            return None

        client_information = await super().get_client(client_id)
        if isinstance(client_information, ProxyDCRClient):
            client_information.allowed_redirect_uri_patterns = (
                self._allowed_client_redirect_uris
            )

        return client_information

    async def load_access_token(self, token: str) -> AccessToken | None:
        upstream = await super().load_access_token(token)
        if upstream is None:
            return None

        try:
            claims = self.jwt_issuer.verify_token(token)
        except (JoseError, ValueError):
            return None

        access_token = upstream.model_copy(
            update={
                "client_id": claims["client_id"],
                "scopes": claims["scope"].split(),
                "expires_at": claims["exp"],
            }
        )

        return access_token

    def get_middleware(self) -> list[Middleware]:
        auth_errors_middleware = Middleware(auth_errors)

        parent = cast(_MiddlewareProvider, super())
        middleware = [auth_errors_middleware, *parent.get_middleware()]

        return middleware
