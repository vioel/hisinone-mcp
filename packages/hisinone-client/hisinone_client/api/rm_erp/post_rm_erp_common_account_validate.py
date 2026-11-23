from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.rm_erp_common_account_account import RmErpCommonAccountAccount
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RmErpCommonAccountAccount | Unset = UNSET,
    withdetails: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["withdetails"] = withdetails

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rm/erp/common/account/validate",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 422:
        response_422 = CsSysRestGenericExceptionResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CsSysRestGenericExceptionResponse | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
    withdetails: bool | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | bool]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        withdetails (bool | Unset):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | bool]
    """

    kwargs = _get_kwargs(
        body=body,
        withdetails=withdetails,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
    withdetails: bool | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | bool | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        withdetails (bool | Unset):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | bool
    """

    return sync_detailed(
        client=client,
        body=body,
        withdetails=withdetails,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
    withdetails: bool | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | bool]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        withdetails (bool | Unset):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | bool]
    """

    kwargs = _get_kwargs(
        body=body,
        withdetails=withdetails,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
    withdetails: bool | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | bool | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        withdetails (bool | Unset):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | bool
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            withdetails=withdetails,
        )
    ).parsed
