from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/researchInfrastructure/dynamicContent/generate",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ImplCsSysDynamicDynamicComponent | None:
    if response.status_code == 200:
        response_200 = ImplCsSysDynamicDynamicComponent.from_dict(response.json())

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
) -> Response[Any | ImplCsSysDynamicDynamicComponent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplCsSysDynamicDynamicComponent]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_CREATE_RESEARCH_INFRASTRUCTURE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplCsSysDynamicDynamicComponent]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | ImplCsSysDynamicDynamicComponent | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_CREATE_RESEARCH_INFRASTRUCTURE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplCsSysDynamicDynamicComponent
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplCsSysDynamicDynamicComponent]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_CREATE_RESEARCH_INFRASTRUCTURE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplCsSysDynamicDynamicComponent]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | ImplCsSysDynamicDynamicComponent | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_CREATE_RESEARCH_INFRASTRUCTURE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplCsSysDynamicDynamicComponent
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
