from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_prize_nomination_nomination import FsResPrizeNominationNomination
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/nomination/pub/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[FsResPrizeNominationNomination] | None:
    if response.status_code == 200:
        response_200: list[FsResPrizeNominationNomination] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsResPrizeNominationNomination.from_dict(response_200_item_data)

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
) -> Response[Any | list[FsResPrizeNominationNomination]]:
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
) -> Response[Any | list[FsResPrizeNominationNomination]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PRIZE_VIEW_NOMINATION,RIGHT_FS_RES_PRIZE_VIEW_NOMINATION_OWN,RIGHT_FS_RES_PRIZE_VIEW_
    NOMINATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResPrizeNominationNomination]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[FsResPrizeNominationNomination] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PRIZE_VIEW_NOMINATION,RIGHT_FS_RES_PRIZE_VIEW_NOMINATION_OWN,RIGHT_FS_RES_PRIZE_VIEW_
    NOMINATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResPrizeNominationNomination]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[FsResPrizeNominationNomination]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PRIZE_VIEW_NOMINATION,RIGHT_FS_RES_PRIZE_VIEW_NOMINATION_OWN,RIGHT_FS_RES_PRIZE_VIEW_
    NOMINATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResPrizeNominationNomination]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[FsResPrizeNominationNomination] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PRIZE_VIEW_NOMINATION,RIGHT_FS_RES_PRIZE_VIEW_NOMINATION_OWN,RIGHT_FS_RES_PRIZE_VIEW_
    NOMINATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResPrizeNominationNomination]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
