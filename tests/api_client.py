from collections.abc import Callable

import httpx2
from hisinone_client import AuthenticatedClient


def mock_api_client(
    respond: Callable[[httpx2.Request], httpx2.Response],
    *,
    base_url: str = "https://his.test",
) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=base_url,
        token="caller",
        httpx_args={"transport": httpx2.MockTransport(respond)},
    )
