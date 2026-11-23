from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.communication_log_rest import CommunicationLogRest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    owner_id: int,
    *,
    older_than: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["olderThan"] = older_than

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/communicationlog/{owner_id}".format(
            owner_id=quote(str(owner_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CommunicationLogRest | None:
    if response.status_code == 200:
        response_200 = CommunicationLogRest.from_dict(response.json())

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
) -> Response[Any | CommunicationLogRest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    owner_id: int,
    *,
    client: AuthenticatedClient,
    older_than: str | Unset = UNSET,
) -> Response[Any | CommunicationLogRest]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_APPLOG_VIEW_COMMUNICATION_LOG
    * RIGHT_CS_SYS_SELF_APPLOG_VIEW_COMMUNICATION_LOG


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        owner_id (int):
        older_than (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CommunicationLogRest]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        older_than=older_than,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    owner_id: int,
    *,
    client: AuthenticatedClient,
    older_than: str | Unset = UNSET,
) -> Any | CommunicationLogRest | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_APPLOG_VIEW_COMMUNICATION_LOG
    * RIGHT_CS_SYS_SELF_APPLOG_VIEW_COMMUNICATION_LOG


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        owner_id (int):
        older_than (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CommunicationLogRest
    """

    return sync_detailed(
        owner_id=owner_id,
        client=client,
        older_than=older_than,
    ).parsed


async def asyncio_detailed(
    owner_id: int,
    *,
    client: AuthenticatedClient,
    older_than: str | Unset = UNSET,
) -> Response[Any | CommunicationLogRest]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_APPLOG_VIEW_COMMUNICATION_LOG
    * RIGHT_CS_SYS_SELF_APPLOG_VIEW_COMMUNICATION_LOG


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        owner_id (int):
        older_than (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CommunicationLogRest]
    """

    kwargs = _get_kwargs(
        owner_id=owner_id,
        older_than=older_than,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    owner_id: int,
    *,
    client: AuthenticatedClient,
    older_than: str | Unset = UNSET,
) -> Any | CommunicationLogRest | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_APPLOG_VIEW_COMMUNICATION_LOG
    * RIGHT_CS_SYS_SELF_APPLOG_VIEW_COMMUNICATION_LOG


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        owner_id (int):
        older_than (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CommunicationLogRest
    """

    return (
        await asyncio_detailed(
            owner_id=owner_id,
            client=client,
            older_than=older_than,
        )
    ).parsed
