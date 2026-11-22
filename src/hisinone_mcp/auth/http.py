import logging
from uuid import uuid4

from fastmcp.server.auth import TokenVerificationError
from key_value.aio.errors import BaseKeyValueError
from redis.exceptions import RedisError
from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from hisinone_mcp.auth.verifier import InsufficientScope

logger = logging.getLogger(__name__)


def auth_errors(app: ASGIApp) -> ASGIApp:
    async def handle(scope: Scope, receive: Receive, send: Send) -> None:
        try:
            await app(scope, receive, send)
            return
        except InsufficientScope:
            status, error = 403, "insufficient_scope"
        except (TokenVerificationError, RedisError, BaseKeyValueError):
            status, error = 503, "temporarily_unavailable"

        request_id = uuid4().hex
        logger.warning(
            "OAuth request failed (%s, request %s)",
            error,
            request_id,
            extra={"request_id": request_id, "status": status},
        )

        headers = {"X-Request-ID": request_id, "Cache-Control": "no-store"}
        if status == 403:
            headers["WWW-Authenticate"] = 'Bearer error="insufficient_scope"'

        response = JSONResponse({"error": error}, status, headers)
        await response(scope, receive, send)

    return handle
