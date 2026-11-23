from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_value_generic_value import CsSysValueGenericValue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    search_text: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["searchText"] = search_text

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/psv/person/{id}/organizations".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
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
    id: int,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
) -> Response[Any | list[CsSysValueGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_ORGTREE_VIEW_AFFILIATION
    * RIGHT_CS_PSV_ORGTREE_SEARCH_AFFILIATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        search_text (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysValueGenericValue]]
    """

    kwargs = _get_kwargs(
        id=id,
        search_text=search_text,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
) -> Any | list[CsSysValueGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_ORGTREE_VIEW_AFFILIATION
    * RIGHT_CS_PSV_ORGTREE_SEARCH_AFFILIATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        search_text (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysValueGenericValue]
    """

    return sync_detailed(
        id=id,
        client=client,
        search_text=search_text,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
) -> Response[Any | list[CsSysValueGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_ORGTREE_VIEW_AFFILIATION
    * RIGHT_CS_PSV_ORGTREE_SEARCH_AFFILIATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        search_text (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysValueGenericValue]]
    """

    kwargs = _get_kwargs(
        id=id,
        search_text=search_text,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    search_text: str | Unset = UNSET,
) -> Any | list[CsSysValueGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_ORGTREE_VIEW_AFFILIATION
    * RIGHT_CS_PSV_ORGTREE_SEARCH_AFFILIATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        search_text (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysValueGenericValue]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            search_text=search_text,
        )
    ).parsed
