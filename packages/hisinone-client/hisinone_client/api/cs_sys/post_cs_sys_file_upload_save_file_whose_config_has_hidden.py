from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.cs_sys_upload_configuration_demo_his_file_upload_demo_response import (
    CsSysUploadConfigurationDemoHisFileUploadDemoResponse,
)
from ...models.cs_sys_upload_configuration_demo_his_my_demo_data import CsSysUploadConfigurationDemoHisMyDemoData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysUploadConfigurationDemoHisMyDemoData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/fileUpload/saveFileWhoseConfigHasHidden",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse | None:
    if response.status_code == 200:
        response_200 = CsSysUploadConfigurationDemoHisFileUploadDemoResponse.from_dict(response.json())

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
) -> Response[Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysUploadConfigurationDemoHisMyDemoData | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_TUTORIAL_VIEW_TUTORIALS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationDemoHisMyDemoData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse]
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
    body: CsSysUploadConfigurationDemoHisMyDemoData | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_TUTORIAL_VIEW_TUTORIALS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationDemoHisMyDemoData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysUploadConfigurationDemoHisMyDemoData | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_TUTORIAL_VIEW_TUTORIALS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationDemoHisMyDemoData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CsSysUploadConfigurationDemoHisMyDemoData | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_TUTORIAL_VIEW_TUTORIALS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationDemoHisMyDemoData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | CsSysUploadConfigurationDemoHisFileUploadDemoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
