from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_publication_publication import FsResPublicationPublication
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    cite_format: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["citeFormat"] = cite_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/publication/{id}/details".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | FsResPublicationPublication | None:
    if response.status_code == 200:
        response_200 = FsResPublicationPublication.from_dict(response.json())

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
) -> Response[Any | FsResPublicationPublication]:
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
    cite_format: str | Unset = UNSET,
) -> Response[Any | FsResPublicationPublication]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        cite_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FsResPublicationPublication]
    """

    kwargs = _get_kwargs(
        id=id,
        cite_format=cite_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    cite_format: str | Unset = UNSET,
) -> Any | FsResPublicationPublication | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        cite_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FsResPublicationPublication
    """

    return sync_detailed(
        id=id,
        client=client,
        cite_format=cite_format,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    cite_format: str | Unset = UNSET,
) -> Response[Any | FsResPublicationPublication]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        cite_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FsResPublicationPublication]
    """

    kwargs = _get_kwargs(
        id=id,
        cite_format=cite_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    cite_format: str | Unset = UNSET,
) -> Any | FsResPublicationPublication | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        cite_format (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FsResPublicationPublication
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cite_format=cite_format,
        )
    ).parsed
