from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level import (
    ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cm/app/admission/allocationScheme/quotaLevel/{id}".format(
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
) -> (
    Any
    | CsSysRestGenericExceptionResponse
    | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
    | None
):
    if response.status_code == 200:
        response_200: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel.from_dict(
                response_200_item_data
            )

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
) -> Response[
    Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
]:
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
    body: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET,
) -> Response[
    Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
]:
    """#### At least one of these rights:
    * RIGHT_CM_APP_ADMISSION_EDIT_ALLOCATION_SCHEME


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]]
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
    body: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET,
) -> (
    Any
    | CsSysRestGenericExceptionResponse
    | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
    | None
):
    """#### At least one of these rights:
    * RIGHT_CM_APP_ADMISSION_EDIT_ALLOCATION_SCHEME


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
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
    body: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET,
) -> Response[
    Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
]:
    """#### At least one of these rights:
    * RIGHT_CM_APP_ADMISSION_EDIT_ALLOCATION_SCHEME


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]]
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
    body: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET,
) -> (
    Any
    | CsSysRestGenericExceptionResponse
    | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
    | None
):
    """#### At least one of these rights:
    * RIGHT_CM_APP_ADMISSION_EDIT_ALLOCATION_SCHEME


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
