from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.context_and_config_rest import ContextAndConfigRest
from ...types import Response


def _get_kwargs(
    context_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/adminutils/conditionalContext/findContext/{context_id}".format(
            context_id=quote(str(context_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ContextAndConfigRest | None:
    if response.status_code == 200:
        response_200 = ContextAndConfigRest.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ContextAndConfigRest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    context_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ContextAndConfigRest]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        context_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContextAndConfigRest]
    """

    kwargs = _get_kwargs(
        context_id=context_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    context_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | ContextAndConfigRest | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        context_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContextAndConfigRest
    """

    return sync_detailed(
        context_id=context_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    context_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ContextAndConfigRest]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        context_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContextAndConfigRest]
    """

    kwargs = _get_kwargs(
        context_id=context_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    context_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | ContextAndConfigRest | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        context_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContextAndConfigRest
    """

    return (
        await asyncio_detailed(
            context_id=context_id,
            client=client,
        )
    ).parsed
