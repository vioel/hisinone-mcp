from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_project_change_request_project_change_request import FsResProjectChangeRequestProjectChangeRequest
from ...types import Response


def _get_kwargs(
    project_lid: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/projectChangeRequest/list/project/{project_lid}".format(
            project_lid=quote(str(project_lid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[FsResProjectChangeRequestProjectChangeRequest] | None:
    if response.status_code == 200:
        response_200: list[FsResProjectChangeRequestProjectChangeRequest] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsResProjectChangeRequestProjectChangeRequest.from_dict(response_200_item_data)

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
) -> Response[Any | list[FsResProjectChangeRequestProjectChangeRequest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_lid: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[FsResProjectChangeRequestProjectChangeRequest]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        project_lid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResProjectChangeRequestProjectChangeRequest]]
    """

    kwargs = _get_kwargs(
        project_lid=project_lid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_lid: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[FsResProjectChangeRequestProjectChangeRequest] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        project_lid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResProjectChangeRequestProjectChangeRequest]
    """

    return sync_detailed(
        project_lid=project_lid,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_lid: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[FsResProjectChangeRequestProjectChangeRequest]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        project_lid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResProjectChangeRequestProjectChangeRequest]]
    """

    kwargs = _get_kwargs(
        project_lid=project_lid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_lid: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[FsResProjectChangeRequestProjectChangeRequest] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        project_lid (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResProjectChangeRequestProjectChangeRequest]
    """

    return (
        await asyncio_detailed(
            project_lid=project_lid,
            client=client,
        )
    ).parsed
