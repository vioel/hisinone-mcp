from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_value_generic_value import CsSysValueGenericValue
from ...types import Response


def _get_kwargs(
    clazz_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/{clazz_name}/globalIdentifierType".format(
            clazz_name=quote(str(clazz_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[CsSysValueGenericValue] | None:
    if response.status_code == 200:
        response_200: list[CsSysValueGenericValue] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsSysValueGenericValue.from_dict(response_200_item_data)

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
) -> Response[Any | list[CsSysValueGenericValue]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsSysValueGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        clazz_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysValueGenericValue]]
    """

    kwargs = _get_kwargs(
        clazz_name=clazz_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[CsSysValueGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        clazz_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysValueGenericValue]
    """

    return sync_detailed(
        clazz_name=clazz_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsSysValueGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        clazz_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysValueGenericValue]]
    """

    kwargs = _get_kwargs(
        clazz_name=clazz_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[CsSysValueGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        clazz_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysValueGenericValue]
    """

    return (
        await asyncio_detailed(
            clazz_name=clazz_name,
            client=client,
        )
    ).parsed
