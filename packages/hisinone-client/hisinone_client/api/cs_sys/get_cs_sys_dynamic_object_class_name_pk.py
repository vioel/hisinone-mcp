from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.impl_cs_sys_dynamic_dynamic_object import ImplCsSysDynamicDynamicObject
from ...types import Response


def _get_kwargs(
    class_name: str,
    pk: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/dynamicObject/{class_name}/{pk}".format(
            class_name=quote(str(class_name), safe=""),
            pk=quote(str(pk), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ImplCsSysDynamicDynamicObject | None:
    if response.status_code == 200:
        response_200 = ImplCsSysDynamicDynamicObject.from_dict(response.json())

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
) -> Response[Any | ImplCsSysDynamicDynamicObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    class_name: str,
    pk: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplCsSysDynamicDynamicObject]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_WS_ADMIN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        class_name (str):
        pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplCsSysDynamicDynamicObject]
    """

    kwargs = _get_kwargs(
        class_name=class_name,
        pk=pk,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    class_name: str,
    pk: int,
    *,
    client: AuthenticatedClient,
) -> Any | ImplCsSysDynamicDynamicObject | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_WS_ADMIN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        class_name (str):
        pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplCsSysDynamicDynamicObject
    """

    return sync_detailed(
        class_name=class_name,
        pk=pk,
        client=client,
    ).parsed


async def asyncio_detailed(
    class_name: str,
    pk: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplCsSysDynamicDynamicObject]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_WS_ADMIN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        class_name (str):
        pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplCsSysDynamicDynamicObject]
    """

    kwargs = _get_kwargs(
        class_name=class_name,
        pk=pk,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    class_name: str,
    pk: int,
    *,
    client: AuthenticatedClient,
) -> Any | ImplCsSysDynamicDynamicObject | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_WS_ADMIN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        class_name (str):
        pk (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplCsSysDynamicDynamicObject
    """

    return (
        await asyncio_detailed(
            class_name=class_name,
            pk=pk,
            client=client,
        )
    ).parsed
