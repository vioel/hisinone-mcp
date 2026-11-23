from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_adminutils_entityexplorer_sys_entity_explorer_db_query_result import (
    CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult,
)
from ...models.cs_sys_adminutils_entityexplorer_sys_entity_explorer_simulation_request import (
    CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest,
)
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/adminutils/getDbQueryExpressions",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult.from_dict(response.json())

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
) -> Response[Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset = UNSET,
) -> Response[Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse]
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
    body: CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset = UNSET,
) -> Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset = UNSET,
) -> Response[Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset = UNSET,
) -> Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysAdminutilsEntityexplorerSysEntityExplorerDbQueryResult | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
