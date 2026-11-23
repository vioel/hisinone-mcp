from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    metadata_guid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cm/stu/smv/updateSmvFileAcknowledged/{metadata_guid}".format(
            metadata_guid=quote(str(metadata_guid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    metadata_guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | str]:
    """#### At least one of these rights:
    * RIGHT_CM_STU_SMV_USE_REST_API+RIGHT_CM_STU_SMV_EXPORT_NOTIFICATIONS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        metadata_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        metadata_guid=metadata_guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    metadata_guid: str,
    *,
    client: AuthenticatedClient,
) -> Any | str | None:
    """#### At least one of these rights:
    * RIGHT_CM_STU_SMV_USE_REST_API+RIGHT_CM_STU_SMV_EXPORT_NOTIFICATIONS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        metadata_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return sync_detailed(
        metadata_guid=metadata_guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    metadata_guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | str]:
    """#### At least one of these rights:
    * RIGHT_CM_STU_SMV_USE_REST_API+RIGHT_CM_STU_SMV_EXPORT_NOTIFICATIONS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        metadata_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | str]
    """

    kwargs = _get_kwargs(
        metadata_guid=metadata_guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    metadata_guid: str,
    *,
    client: AuthenticatedClient,
) -> Any | str | None:
    """#### At least one of these rights:
    * RIGHT_CM_STU_SMV_USE_REST_API+RIGHT_CM_STU_SMV_EXPORT_NOTIFICATIONS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        metadata_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | str
    """

    return (
        await asyncio_detailed(
            metadata_guid=metadata_guid,
            client=client,
        )
    ).parsed
