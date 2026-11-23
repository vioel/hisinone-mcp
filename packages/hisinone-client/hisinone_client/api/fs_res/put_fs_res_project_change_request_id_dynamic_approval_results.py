from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.impl_cs_sys_dynamic_dynamic_approval_result import ImplCsSysDynamicDynamicApprovalResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: list[ImplCsSysDynamicDynamicApprovalResult] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/fs/res/projectChangeRequest/{id}/dynamicApprovalResults".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _body_json: list[dict[str, Any]] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _body_json.append(body_item)
        _kwargs["json"] = _body_json

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult] | None:
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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = CsSysRestGenericExceptionResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]]:
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
    body: list[ImplCsSysDynamicDynamicApprovalResult] | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_A
    PPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ImplCsSysDynamicDynamicApprovalResult] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[ImplCsSysDynamicDynamicApprovalResult] | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_A
    PPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ImplCsSysDynamicDynamicApprovalResult] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[ImplCsSysDynamicDynamicApprovalResult] | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_A
    PPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ImplCsSysDynamicDynamicApprovalResult] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: list[ImplCsSysDynamicDynamicApprovalResult] | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_APPROVE_FUNDING_NOTIFICATION,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_A
    PPROVALS,RIGHT_FS_RES_PROJECT_EDIT_FUNDING_NOTIFICATION_RESULT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ImplCsSysDynamicDynamicApprovalResult] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[ImplCsSysDynamicDynamicApprovalResult]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
