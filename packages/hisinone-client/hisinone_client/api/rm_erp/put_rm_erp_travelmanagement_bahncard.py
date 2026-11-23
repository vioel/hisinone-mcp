from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.rm_erp_travelmanagement_shared_bahncard import RmErpTravelmanagementSharedBahncard
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RmErpTravelmanagementSharedBahncard | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rm/erp/travelmanagement/bahncard",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard | None:
    if response.status_code == 200:
        response_200 = RmErpTravelmanagementSharedBahncard.from_dict(response.json())

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
) -> Response[Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RmErpTravelmanagementSharedBahncard | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (RmErpTravelmanagementSharedBahncard | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RmErpTravelmanagementSharedBahncard | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (RmErpTravelmanagementSharedBahncard | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RmErpTravelmanagementSharedBahncard | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (RmErpTravelmanagementSharedBahncard | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RmErpTravelmanagementSharedBahncard | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (RmErpTravelmanagementSharedBahncard | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | RmErpTravelmanagementSharedBahncard
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
