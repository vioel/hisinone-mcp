from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.impl_cs_sys_dynamic_dynamic_approval_result import ImplCsSysDynamicDynamicApprovalResult
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/projectChangeRequest/{id}/dynamicApprovalResults".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[ImplCsSysDynamicDynamicApprovalResult] | None:
    if response.status_code == 200:
        response_200: list[ImplCsSysDynamicDynamicApprovalResult] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ImplCsSysDynamicDynamicApprovalResult.from_dict(response_200_item_data)

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
) -> Response[Any | list[ImplCsSysDynamicDynamicApprovalResult]]:
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
) -> Response[Any | list[ImplCsSysDynamicDynamicApprovalResult]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATION_RESULT,RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATI
    ON_RESULT_OWN,RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NO
    TIFICATION_APPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ImplCsSysDynamicDynamicApprovalResult]]
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
) -> Any | list[ImplCsSysDynamicDynamicApprovalResult] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATION_RESULT,RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATI
    ON_RESULT_OWN,RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NO
    TIFICATION_APPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ImplCsSysDynamicDynamicApprovalResult]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[ImplCsSysDynamicDynamicApprovalResult]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATION_RESULT,RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATI
    ON_RESULT_OWN,RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NO
    TIFICATION_APPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ImplCsSysDynamicDynamicApprovalResult]]
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
) -> Any | list[ImplCsSysDynamicDynamicApprovalResult] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATION_RESULT,RIGHT_FS_RES_PROJECT_VIEW_FUNDING_NOTIFICATI
    ON_RESULT_OWN,RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NO
    TIFICATION_APPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ImplCsSysDynamicDynamicApprovalResult]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
