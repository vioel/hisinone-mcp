from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    accountconfigname: str,
    departmment: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["accountconfigname"] = accountconfigname

    params["departmment"] = departmment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rm/erp/common/account/institutes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RmErpCommonInstituteErpInstitute] | None:
    if response.status_code == 200:
        response_200: list[RmErpCommonInstituteErpInstitute] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RmErpCommonInstituteErpInstitute.from_dict(response_200_item_data)

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
) -> Response[Any | list[RmErpCommonInstituteErpInstitute]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    accountconfigname: str,
    departmment: str | Unset = UNSET,
) -> Response[Any | list[RmErpCommonInstituteErpInstitute]]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        accountconfigname (str):
        departmment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RmErpCommonInstituteErpInstitute]]
    """

    kwargs = _get_kwargs(
        accountconfigname=accountconfigname,
        departmment=departmment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    accountconfigname: str,
    departmment: str | Unset = UNSET,
) -> Any | list[RmErpCommonInstituteErpInstitute] | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        accountconfigname (str):
        departmment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RmErpCommonInstituteErpInstitute]
    """

    return sync_detailed(
        client=client,
        accountconfigname=accountconfigname,
        departmment=departmment,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    accountconfigname: str,
    departmment: str | Unset = UNSET,
) -> Response[Any | list[RmErpCommonInstituteErpInstitute]]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        accountconfigname (str):
        departmment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RmErpCommonInstituteErpInstitute]]
    """

    kwargs = _get_kwargs(
        accountconfigname=accountconfigname,
        departmment=departmment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    accountconfigname: str,
    departmment: str | Unset = UNSET,
) -> Any | list[RmErpCommonInstituteErpInstitute] | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_PROCUREMENT_REQUISITION_EDIT_REQUISITION,RIGHT_RM_ERP_PROCUREMENT_REQUISITION_CREATE_
    REQUISITION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        accountconfigname (str):
        departmment (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RmErpCommonInstituteErpInstitute]
    """

    return (
        await asyncio_detailed(
            client=client,
            accountconfigname=accountconfigname,
            departmment=departmment,
        )
    ).parsed
