from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_jobs_job_request import CsSysJobsJobRequest
from ...models.cs_sys_jobs_job_status import CsSysJobsJobStatus
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/jobExecution",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = CsSysJobsJobStatus.from_dict(response.json())

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
) -> Response[Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse]:
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
) -> Response[Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse]:
    """This service expects an object of type `HisJobRequest` as its argument:
    * The field `jobKey` identifies the Job to be started by its key (usually uniquename).
    * The field `executionType` is meant to potentially select different job starting mechanisms in
    HISinOne (not evaluated yet)
    * The field `searchRequest` contains a generic search request meant to select the data processed by
    the job
    * The field `selectedRowData` holds selected Lines to further limit the search result. If nothing is
    selected, the whole search result is processed.

    <br>

    **Example 1: Start job 'CSV-Export' on one selected row of a Role Search (restricted to Alumni-
    Roles)**

    ~~~~
    {
        "jobKey": "csvExport",
        "executionType": "JobManagement",
        "searchRequest": {
                "configFile": "sucheRollen.xml",
                "searchFields": [
                        {
                                "key": "OrgroleValue.uniquename",
                                "searchString": "alumni",
                                "selectList": null
                        }
                ],
                "offset": 0,
                "limit": -1
        },
        "selectedRowData": [
                {
                        "OrgroleValue.id": 100069
                }
        ]
    }
    ~~~~
    <br>

    The response body is of type `HisJobStatus`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    If a generic search is used, the additionally required permissions are defined in each search
    configuration file. Search configuration files without a dedicated &lt;authorities&gt; element are
    not accessible via REST.

    The particular Job may check for additional Rights as precondition for being started.




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
        Response[Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse]
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
) -> Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse | None:
    """This service expects an object of type `HisJobRequest` as its argument:
    * The field `jobKey` identifies the Job to be started by its key (usually uniquename).
    * The field `executionType` is meant to potentially select different job starting mechanisms in
    HISinOne (not evaluated yet)
    * The field `searchRequest` contains a generic search request meant to select the data processed by
    the job
    * The field `selectedRowData` holds selected Lines to further limit the search result. If nothing is
    selected, the whole search result is processed.

    <br>

    **Example 1: Start job 'CSV-Export' on one selected row of a Role Search (restricted to Alumni-
    Roles)**

    ~~~~
    {
        "jobKey": "csvExport",
        "executionType": "JobManagement",
        "searchRequest": {
                "configFile": "sucheRollen.xml",
                "searchFields": [
                        {
                                "key": "OrgroleValue.uniquename",
                                "searchString": "alumni",
                                "selectList": null
                        }
                ],
                "offset": 0,
                "limit": -1
        },
        "selectedRowData": [
                {
                        "OrgroleValue.id": 100069
                }
        ]
    }
    ~~~~
    <br>

    The response body is of type `HisJobStatus`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    If a generic search is used, the additionally required permissions are defined in each search
    configuration file. Search configuration files without a dedicated &lt;authorities&gt; element are
    not accessible via REST.

    The particular Job may check for additional Rights as precondition for being started.




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
        Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysJobsJobRequest | Unset = UNSET,
) -> Response[Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse]:
    """This service expects an object of type `HisJobRequest` as its argument:
    * The field `jobKey` identifies the Job to be started by its key (usually uniquename).
    * The field `executionType` is meant to potentially select different job starting mechanisms in
    HISinOne (not evaluated yet)
    * The field `searchRequest` contains a generic search request meant to select the data processed by
    the job
    * The field `selectedRowData` holds selected Lines to further limit the search result. If nothing is
    selected, the whole search result is processed.

    <br>

    **Example 1: Start job 'CSV-Export' on one selected row of a Role Search (restricted to Alumni-
    Roles)**

    ~~~~
    {
        "jobKey": "csvExport",
        "executionType": "JobManagement",
        "searchRequest": {
                "configFile": "sucheRollen.xml",
                "searchFields": [
                        {
                                "key": "OrgroleValue.uniquename",
                                "searchString": "alumni",
                                "selectList": null
                        }
                ],
                "offset": 0,
                "limit": -1
        },
        "selectedRowData": [
                {
                        "OrgroleValue.id": 100069
                }
        ]
    }
    ~~~~
    <br>

    The response body is of type `HisJobStatus`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    If a generic search is used, the additionally required permissions are defined in each search
    configuration file. Search configuration files without a dedicated &lt;authorities&gt; element are
    not accessible via REST.

    The particular Job may check for additional Rights as precondition for being started.




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
        Response[Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse]
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
) -> Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse | None:
    """This service expects an object of type `HisJobRequest` as its argument:
    * The field `jobKey` identifies the Job to be started by its key (usually uniquename).
    * The field `executionType` is meant to potentially select different job starting mechanisms in
    HISinOne (not evaluated yet)
    * The field `searchRequest` contains a generic search request meant to select the data processed by
    the job
    * The field `selectedRowData` holds selected Lines to further limit the search result. If nothing is
    selected, the whole search result is processed.

    <br>

    **Example 1: Start job 'CSV-Export' on one selected row of a Role Search (restricted to Alumni-
    Roles)**

    ~~~~
    {
        "jobKey": "csvExport",
        "executionType": "JobManagement",
        "searchRequest": {
                "configFile": "sucheRollen.xml",
                "searchFields": [
                        {
                                "key": "OrgroleValue.uniquename",
                                "searchString": "alumni",
                                "selectList": null
                        }
                ],
                "offset": 0,
                "limit": -1
        },
        "selectedRowData": [
                {
                        "OrgroleValue.id": 100069
                }
        ]
    }
    ~~~~
    <br>

    The response body is of type `HisJobStatus`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    If a generic search is used, the additionally required permissions are defined in each search
    configuration file. Search configuration files without a dedicated &lt;authorities&gt; element are
    not accessible via REST.

    The particular Job may check for additional Rights as precondition for being started.




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
        Any | CsSysJobsJobStatus | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
