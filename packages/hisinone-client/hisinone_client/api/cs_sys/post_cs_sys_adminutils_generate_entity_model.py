from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_model import (
    ImplCsSysAdminutilsEntityexplorerEntityExplorerModel,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/adminutils/generateEntityModel",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel | None:
    if response.status_code == 200:
        response_200 = ImplCsSysAdminutilsEntityexplorerEntityExplorerModel.from_dict(response.json())

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
) -> Response[Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | ImplCsSysAdminutilsEntityexplorerEntityExplorerModel
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
