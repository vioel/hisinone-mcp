from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rm_erp_travelmanagement_shared_bahncard import RmErpTravelmanagementSharedBahncard
from ...types import Response


def _get_kwargs(
    pgd_join_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rm/erp/travelmanagement/bahncard/{pgd_join_id}".format(
            pgd_join_id=quote(str(pgd_join_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RmErpTravelmanagementSharedBahncard | None:
    if response.status_code == 200:
        response_200 = RmErpTravelmanagementSharedBahncard.from_dict(response.json())

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
) -> Response[Any | RmErpTravelmanagementSharedBahncard]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pgd_join_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RmErpTravelmanagementSharedBahncard]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION_PROCESSOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        pgd_join_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RmErpTravelmanagementSharedBahncard]
    """

    kwargs = _get_kwargs(
        pgd_join_id=pgd_join_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pgd_join_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RmErpTravelmanagementSharedBahncard | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION_PROCESSOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        pgd_join_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RmErpTravelmanagementSharedBahncard
    """

    return sync_detailed(
        pgd_join_id=pgd_join_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    pgd_join_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RmErpTravelmanagementSharedBahncard]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION_PROCESSOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        pgd_join_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RmErpTravelmanagementSharedBahncard]
    """

    kwargs = _get_kwargs(
        pgd_join_id=pgd_join_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pgd_join_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RmErpTravelmanagementSharedBahncard | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_CREATE_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_EDIT_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION
    * RIGHT_RM_ERP_TRAVELMANAGEMENT_BUSINESSTRIPAPPLICATION_VIEW_BUSINESSTRIPAPPLICATION_PROCESSOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        pgd_join_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RmErpTravelmanagementSharedBahncard
    """

    return (
        await asyncio_detailed(
            pgd_join_id=pgd_join_id,
            client=client,
        )
    ).parsed
