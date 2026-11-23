from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_project_project_obj import FsResProjectProjectObj
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/project/{id}/details".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | FsResProjectProjectObj | None:
    if response.status_code == 200:
        response_200 = FsResProjectProjectObj.from_dict(response.json())

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
) -> Response[Any | FsResProjectProjectObj]:
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
) -> Response[Any | FsResProjectProjectObj]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FsResProjectProjectObj]
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
) -> Any | FsResProjectProjectObj | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FsResProjectProjectObj
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FsResProjectProjectObj]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FsResProjectProjectObj]
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
) -> Any | FsResProjectProjectObj | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FsResProjectProjectObj
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
