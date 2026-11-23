from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.java_lang_void import JavaLangVoid
from ...types import Response


def _get_kwargs(
    interface_name: str,
    key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/psv/configuration/externalsystem/configs/{interface_name}/{key}".format(
            interface_name=quote(str(interface_name), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[JavaLangVoid] | None:
    if response.status_code == 200:
        response_200: list[JavaLangVoid] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = JavaLangVoid.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[JavaLangVoid]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    interface_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[JavaLangVoid]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[JavaLangVoid]]
    """

    kwargs = _get_kwargs(
        interface_name=interface_name,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    interface_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[JavaLangVoid] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[JavaLangVoid]
    """

    return sync_detailed(
        interface_name=interface_name,
        key=key,
        client=client,
    ).parsed


async def asyncio_detailed(
    interface_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[JavaLangVoid]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[JavaLangVoid]]
    """

    kwargs = _get_kwargs(
        interface_name=interface_name,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    interface_name: str,
    key: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[JavaLangVoid] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[JavaLangVoid]
    """

    return (
        await asyncio_detailed(
            interface_name=interface_name,
            key=key,
            client=client,
        )
    ).parsed
