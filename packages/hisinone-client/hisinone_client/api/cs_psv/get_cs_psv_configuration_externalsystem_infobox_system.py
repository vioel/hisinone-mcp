from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.interfaceconfiguration_interface_configuration_info_box import (
    InterfaceconfigurationInterfaceConfigurationInfoBox,
)
from ...types import Response


def _get_kwargs(
    system: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/psv/configuration/externalsystem/infobox/{system}".format(
            system=quote(str(system), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | InterfaceconfigurationInterfaceConfigurationInfoBox | None:
    if response.status_code == 200:
        response_200 = InterfaceconfigurationInterfaceConfigurationInfoBox.from_dict(response.json())

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
) -> Response[Any | InterfaceconfigurationInterfaceConfigurationInfoBox]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | InterfaceconfigurationInterfaceConfigurationInfoBox]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        system (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InterfaceconfigurationInterfaceConfigurationInfoBox]
    """

    kwargs = _get_kwargs(
        system=system,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    system: str,
    *,
    client: AuthenticatedClient,
) -> Any | InterfaceconfigurationInterfaceConfigurationInfoBox | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        system (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InterfaceconfigurationInterfaceConfigurationInfoBox
    """

    return sync_detailed(
        system=system,
        client=client,
    ).parsed


async def asyncio_detailed(
    system: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | InterfaceconfigurationInterfaceConfigurationInfoBox]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        system (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InterfaceconfigurationInterfaceConfigurationInfoBox]
    """

    kwargs = _get_kwargs(
        system=system,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    system: str,
    *,
    client: AuthenticatedClient,
) -> Any | InterfaceconfigurationInterfaceConfigurationInfoBox | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_INTERFACE_MANAGE_INTERFACE_CONFIGURATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        system (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InterfaceconfigurationInterfaceConfigurationInfoBox
    """

    return (
        await asyncio_detailed(
            system=system,
            client=client,
        )
    ).parsed
