from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_jobs_job_status import CsSysJobsJobStatus
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/jobExecution/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysJobsJobStatus | None:
    if response.status_code == 200:
        response_200 = CsSysJobsJobStatus.from_dict(response.json())

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
) -> Response[Any | CsSysJobsJobStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysJobsJobStatus]:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User

    <br>

    The Service returns the `HisJobStatus` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysJobsJobStatus]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysJobsJobStatus | None:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User

    <br>

    The Service returns the `HisJobStatus` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysJobsJobStatus
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysJobsJobStatus]:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User

    <br>

    The Service returns the `HisJobStatus` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysJobsJobStatus]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysJobsJobStatus | None:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User

    <br>

    The Service returns the `HisJobStatus` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysJobsJobStatus
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
