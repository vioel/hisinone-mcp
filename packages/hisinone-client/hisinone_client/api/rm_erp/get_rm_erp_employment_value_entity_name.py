from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
from ...types import Response


def _get_kwargs(
    entity_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rm/erp/employment/value/{entity_name}".format(
            entity_name=quote(str(entity_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RmErpCommonErpGenericValue] | None:
    if response.status_code == 200:
        response_200: list[RmErpCommonErpGenericValue] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RmErpCommonErpGenericValue.from_dict(response_200_item_data)

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
) -> Response[Any | list[RmErpCommonErpGenericValue]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[RmErpCommonErpGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RmErpCommonErpGenericValue]]
    """

    kwargs = _get_kwargs(
        entity_name=entity_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[RmErpCommonErpGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RmErpCommonErpGenericValue]
    """

    return sync_detailed(
        entity_name=entity_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[RmErpCommonErpGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RmErpCommonErpGenericValue]]
    """

    kwargs = _get_kwargs(
        entity_name=entity_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[RmErpCommonErpGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RmErpCommonErpGenericValue]
    """

    return (
        await asyncio_detailed(
            entity_name=entity_name,
            client=client,
        )
    ).parsed
