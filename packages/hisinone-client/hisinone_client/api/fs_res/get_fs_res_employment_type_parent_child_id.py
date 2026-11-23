from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_value_generic_value import CsSysValueGenericValue
from ...types import Response


def _get_kwargs(
    child_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/employmentType/parent/{child_id}".format(
            child_id=quote(str(child_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysValueGenericValue | None:
    if response.status_code == 200:
        response_200 = CsSysValueGenericValue.from_dict(response.json())

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
) -> Response[Any | CsSysValueGenericValue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    child_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysValueGenericValue]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        child_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysValueGenericValue]
    """

    kwargs = _get_kwargs(
        child_id=child_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    child_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysValueGenericValue | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        child_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysValueGenericValue
    """

    return sync_detailed(
        child_id=child_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    child_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysValueGenericValue]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        child_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysValueGenericValue]
    """

    kwargs = _get_kwargs(
        child_id=child_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    child_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysValueGenericValue | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        child_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysValueGenericValue
    """

    return (
        await asyncio_detailed(
            child_id=child_id,
            client=client,
        )
    ).parsed
