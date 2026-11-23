from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_jobs_job_request import CsSysJobsJobRequest
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fs/res/publication/import/jobExecution/oaiXMetaDissPlus",
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
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | bool]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysJobsJobRequest | Unset):  Example: {'searchRequest': {'configFile':
            'sucheRollen.xml', 'searchFields': [{'key': 'OrgroleValue.uniquename', 'searchString':
            'alumni', 'selectList': None}], 'offset': 0, 'limit': -1}, 'executionType':
            'JobManagement', 'jobKey': 'csvExport', 'selectedRowData': [{'OrgroleValue.id': 100069}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | bool]
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
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | bool | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysJobsJobRequest | Unset):  Example: {'searchRequest': {'configFile':
            'sucheRollen.xml', 'searchFields': [{'key': 'OrgroleValue.uniquename', 'searchString':
            'alumni', 'selectList': None}], 'offset': 0, 'limit': -1}, 'executionType':
            'JobManagement', 'jobKey': 'csvExport', 'selectedRowData': [{'OrgroleValue.id': 100069}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | bool
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | bool]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysJobsJobRequest | Unset):  Example: {'searchRequest': {'configFile':
            'sucheRollen.xml', 'searchFields': [{'key': 'OrgroleValue.uniquename', 'searchString':
            'alumni', 'selectList': None}], 'offset': 0, 'limit': -1}, 'executionType':
            'JobManagement', 'jobKey': 'csvExport', 'selectedRowData': [{'OrgroleValue.id': 100069}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | bool]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | bool | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EXPORT_PUBLICATION_REPOSITORIES


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysJobsJobRequest | Unset):  Example: {'searchRequest': {'configFile':
            'sucheRollen.xml', 'searchFields': [{'key': 'OrgroleValue.uniquename', 'searchString':
            'alumni', 'selectList': None}], 'offset': 0, 'limit': -1}, 'executionType':
            'JobManagement', 'jobKey': 'csvExport', 'selectedRowData': [{'OrgroleValue.id': 100069}]}.

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
        )
    ).parsed
