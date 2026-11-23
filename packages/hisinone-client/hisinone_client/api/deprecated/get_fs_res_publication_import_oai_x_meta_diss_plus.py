from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identifier: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_until: str | Unset = UNSET,
    sets: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identifier"] = identifier

    params["dateFrom"] = date_from

    params["dateUntil"] = date_until

    params["sets"] = sets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/publication/import/oaiXMetaDissPlus",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    identifier: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_until: str | Unset = UNSET,
    sets: str | Unset = UNSET,
) -> Response[Any | str]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier (str | Unset):
        date_from (str | Unset):
        date_until (str | Unset):
        sets (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        date_from=date_from,
        date_until=date_until,
        sets=sets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    identifier: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_until: str | Unset = UNSET,
    sets: str | Unset = UNSET,
) -> Any | str | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier (str | Unset):
        date_from (str | Unset):
        date_until (str | Unset):
        sets (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        client=client,
        identifier=identifier,
        date_from=date_from,
        date_until=date_until,
        sets=sets,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    identifier: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_until: str | Unset = UNSET,
    sets: str | Unset = UNSET,
) -> Response[Any | str]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier (str | Unset):
        date_from (str | Unset):
        date_until (str | Unset):
        sets (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        date_from=date_from,
        date_until=date_until,
        sets=sets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    identifier: str | Unset = UNSET,
    date_from: str | Unset = UNSET,
    date_until: str | Unset = UNSET,
    sets: str | Unset = UNSET,
) -> Any | str | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier (str | Unset):
        date_from (str | Unset):
        date_until (str | Unset):
        sets (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            client=client,
            identifier=identifier,
            date_from=date_from,
            date_until=date_until,
            sets=sets,
        )
    ).parsed
