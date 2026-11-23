from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.context_config_rest import ContextConfigRest
from ...types import Response


def _get_kwargs(
    config_id: int,
    confsrc_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/adminutils/conditionalContext/findConfigs/{config_id}/{confsrc_id}".format(
            config_id=quote(str(config_id), safe=""),
            confsrc_id=quote(str(confsrc_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[ContextConfigRest] | None:
    if response.status_code == 200:
        response_200: list[ContextConfigRest] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ContextConfigRest.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[ContextConfigRest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    config_id: int,
    confsrc_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[ContextConfigRest]]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_id (int):
        confsrc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ContextConfigRest]]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
        confsrc_id=confsrc_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    config_id: int,
    confsrc_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[ContextConfigRest] | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_id (int):
        confsrc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ContextConfigRest]
    """

    return sync_detailed(
        config_id=config_id,
        confsrc_id=confsrc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    config_id: int,
    confsrc_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[ContextConfigRest]]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_id (int):
        confsrc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ContextConfigRest]]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
        confsrc_id=confsrc_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    config_id: int,
    confsrc_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[ContextConfigRest] | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_id (int):
        confsrc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ContextConfigRest]
    """

    return (
        await asyncio_detailed(
            config_id=config_id,
            confsrc_id=confsrc_id,
            client=client,
        )
    ).parsed
