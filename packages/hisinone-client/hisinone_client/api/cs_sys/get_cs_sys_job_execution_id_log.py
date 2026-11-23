from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_jobs_job_protocol_chunk import CsSysJobsJobProtocolChunk
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    start_pos: int | Unset = UNSET,
    max_lines: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startPos"] = start_pos

    params["maxLines"] = max_lines

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/jobExecution/{id}/log".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysJobsJobProtocolChunk | None:
    if response.status_code == 200:
        response_200 = CsSysJobsJobProtocolChunk.from_dict(response.json())

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
) -> Response[Any | CsSysJobsJobProtocolChunk]:
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
    start_pos: int | Unset = UNSET,
    max_lines: int | Unset = UNSET,
) -> Response[Any | CsSysJobsJobProtocolChunk]:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User
    * The parameter 'startPos' contains the index of the first Protocol line to transfer
    * The parameter 'maxLines' contains the maximum number of Protocol lines to transfer. If not set or
    negative, no maximum is used

    <br>

    The Service returns a `HisJobProtocolChunk` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):
        start_pos (int | Unset):
        max_lines (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysJobsJobProtocolChunk]
    """

    kwargs = _get_kwargs(
        id=id,
        start_pos=start_pos,
        max_lines=max_lines,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    start_pos: int | Unset = UNSET,
    max_lines: int | Unset = UNSET,
) -> Any | CsSysJobsJobProtocolChunk | None:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User
    * The parameter 'startPos' contains the index of the first Protocol line to transfer
    * The parameter 'maxLines' contains the maximum number of Protocol lines to transfer. If not set or
    negative, no maximum is used

    <br>

    The Service returns a `HisJobProtocolChunk` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):
        start_pos (int | Unset):
        max_lines (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysJobsJobProtocolChunk
    """

    return sync_detailed(
        id=id,
        client=client,
        start_pos=start_pos,
        max_lines=max_lines,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    start_pos: int | Unset = UNSET,
    max_lines: int | Unset = UNSET,
) -> Response[Any | CsSysJobsJobProtocolChunk]:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User
    * The parameter 'startPos' contains the index of the first Protocol line to transfer
    * The parameter 'maxLines' contains the maximum number of Protocol lines to transfer. If not set or
    negative, no maximum is used

    <br>

    The Service returns a `HisJobProtocolChunk` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):
        start_pos (int | Unset):
        max_lines (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysJobsJobProtocolChunk]
    """

    kwargs = _get_kwargs(
        id=id,
        start_pos=start_pos,
        max_lines=max_lines,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    start_pos: int | Unset = UNSET,
    max_lines: int | Unset = UNSET,
) -> Any | CsSysJobsJobProtocolChunk | None:
    """This service expects the following argument:
    * The path segment `id` contains the JobExecutionContext ID of a Job formerly started by the current
    User
    * The parameter 'startPos' contains the index of the first Protocol line to transfer
    * The parameter 'maxLines' contains the maximum number of Protocol lines to transfer. If not set or
    negative, no maximum is used

    <br>

    The Service returns a `HisJobProtocolChunk` for the given JobExecutionContext ID

     <!--SKIP_RIGHTS--><br>

    **Rights:**

    Minimum Requirement is `RIGHT_CS_SYS_JOBS_RIGHT_EXECUTE_JOB`.

    The current User may only request the Status of Jobs started by himself.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (str):
        start_pos (int | Unset):
        max_lines (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysJobsJobProtocolChunk
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start_pos=start_pos,
            max_lines=max_lines,
        )
    ).parsed
