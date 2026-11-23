from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_dto_base_impl import CsSysRestDtoBaseImpl
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.rm_erp_common_account_account import RmErpCommonAccountAccount
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity_name: str,
    *,
    body: RmErpCommonAccountAccount | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rm/erp/common/account/list/{entity_name}".format(
            entity_name=quote(str(entity_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl] | None:
    if response.status_code == 200:
        response_200: list[CsSysRestDtoBaseImpl] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsSysRestDtoBaseImpl.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_name: str,
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]]
    """

    kwargs = _get_kwargs(
        entity_name=entity_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_name: str,
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl] | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]
    """

    return sync_detailed(
        entity_name=entity_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entity_name: str,
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]]
    """

    kwargs = _get_kwargs(
        entity_name=entity_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_name: str,
    *,
    client: AuthenticatedClient,
    body: RmErpCommonAccountAccount | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl] | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        entity_name (str):
        body (RmErpCommonAccountAccount | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[CsSysRestDtoBaseImpl]
    """

    return (
        await asyncio_detailed(
            entity_name=entity_name,
            client=client,
            body=body,
        )
    ).parsed
