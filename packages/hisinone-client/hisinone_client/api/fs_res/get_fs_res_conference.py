from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_publication_conference import FsResPublicationConference
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    l: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["l"] = l

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/conference",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[FsResPublicationConference] | None:
    if response.status_code == 200:
        response_200: list[FsResPublicationConference] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsResPublicationConference.from_dict(response_200_item_data)

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
) -> Response[Any | list[FsResPublicationConference]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    l: int | Unset = UNSET,
) -> Response[Any | list[FsResPublicationConference]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_CONFERENCE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str):
        l (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResPublicationConference]]
    """

    kwargs = _get_kwargs(
        q=q,
        l=l,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    l: int | Unset = UNSET,
) -> Any | list[FsResPublicationConference] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_CONFERENCE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str):
        l (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResPublicationConference]
    """

    return sync_detailed(
        client=client,
        q=q,
        l=l,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    l: int | Unset = UNSET,
) -> Response[Any | list[FsResPublicationConference]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_CONFERENCE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str):
        l (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResPublicationConference]]
    """

    kwargs = _get_kwargs(
        q=q,
        l=l,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    l: int | Unset = UNSET,
) -> Any | list[FsResPublicationConference] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_CONFERENCE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str):
        l (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResPublicationConference]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            l=l,
        )
    ).parsed
