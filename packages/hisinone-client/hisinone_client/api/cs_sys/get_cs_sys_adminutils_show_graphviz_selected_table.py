from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    selected_table: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/adminutils/showGraphviz/{selected_table}".format(
            selected_table=quote(str(selected_table), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | list[int] | None:
    if response.status_code == 200:
        response_200 = cast(list[int], response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | list[int]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    selected_table: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[int]]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        selected_table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[int]]
    """

    kwargs = _get_kwargs(
        selected_table=selected_table,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    selected_table: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[int] | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        selected_table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[int]
    """

    return sync_detailed(
        selected_table=selected_table,
        client=client,
    ).parsed


async def asyncio_detailed(
    selected_table: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[int]]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        selected_table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[int]]
    """

    kwargs = _get_kwargs(
        selected_table=selected_table,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    selected_table: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[int] | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_MANAGEMENT_VIEW_SYSTEM_FILES,RIGHT_CS_SYS_DATABASE_EXECUTE_QL


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        selected_table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[int]
    """

    return (
        await asyncio_detailed(
            selected_table=selected_table,
            client=client,
        )
    ).parsed
