from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_adminutils_dynamic_dynamic_class_delete_rest_result import (
    CsSysAdminutilsDynamicDynamicClassDeleteRestResult,
)
from ...types import Response


def _get_kwargs(
    dynamic_class_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/cs/sys/adminutils/deleteDynamicClass/{dynamic_class_id}".format(
            dynamic_class_id=quote(str(dynamic_class_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult | None:
    if response.status_code == 200:
        response_200 = CsSysAdminutilsDynamicDynamicClassDeleteRestResult.from_dict(response.json())

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
) -> Response[Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dynamic_class_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_DYNAMIC_MANAGE_ATTRIBUTE
    * RIGHT_CS_SYS_CORE_EDIT_UITEXT
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        dynamic_class_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult]
    """

    kwargs = _get_kwargs(
        dynamic_class_id=dynamic_class_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dynamic_class_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_DYNAMIC_MANAGE_ATTRIBUTE
    * RIGHT_CS_SYS_CORE_EDIT_UITEXT
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        dynamic_class_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult
    """

    return sync_detailed(
        dynamic_class_id=dynamic_class_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dynamic_class_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_DYNAMIC_MANAGE_ATTRIBUTE
    * RIGHT_CS_SYS_CORE_EDIT_UITEXT
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        dynamic_class_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult]
    """

    kwargs = _get_kwargs(
        dynamic_class_id=dynamic_class_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dynamic_class_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_DYNAMIC_MANAGE_ATTRIBUTE
    * RIGHT_CS_SYS_CORE_EDIT_UITEXT
    * RIGHT_CS_SYS_CORE_EDIT_DATADICTIONARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        dynamic_class_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysAdminutilsDynamicDynamicClassDeleteRestResult
    """

    return (
        await asyncio_detailed(
            dynamic_class_id=dynamic_class_id,
            client=client,
        )
    ).parsed
