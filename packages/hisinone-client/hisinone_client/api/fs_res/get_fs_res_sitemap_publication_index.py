from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_site_map_url_dto_list import CsSysRestSiteMapUrlDtoList
from ...types import Response


def _get_kwargs(
    index: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/sitemap/publication/{index}".format(
            index=quote(str(index), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestSiteMapUrlDtoList | None:
    if response.status_code == 200:
        response_200 = CsSysRestSiteMapUrlDtoList.from_dict(response.json())

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
) -> Response[Any | CsSysRestSiteMapUrlDtoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    index: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysRestSiteMapUrlDtoList]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestSiteMapUrlDtoList]
    """

    kwargs = _get_kwargs(
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    index: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysRestSiteMapUrlDtoList | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestSiteMapUrlDtoList
    """

    return sync_detailed(
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    index: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysRestSiteMapUrlDtoList]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestSiteMapUrlDtoList]
    """

    kwargs = _get_kwargs(
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    index: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysRestSiteMapUrlDtoList | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_OWN,RIGHT_FS_R
    ES_PUBLICATION_VIEW_PUBLICATION_BY_TYPE,RIGHT_FS_RES_PUBLICATION_VIEW_PUBLICATION_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestSiteMapUrlDtoList
    """

    return (
        await asyncio_detailed(
            index=index,
            client=client,
        )
    ).parsed
