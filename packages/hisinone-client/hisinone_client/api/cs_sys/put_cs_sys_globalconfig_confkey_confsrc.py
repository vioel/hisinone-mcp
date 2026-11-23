from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    confkey: str,
    confsrc: str,
    *,
    body: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/cs/sys/globalconfig/{confkey}/{confsrc}".format(
            confkey=quote(str(confkey), safe=""),
            confsrc=quote(str(confsrc), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = CsSysRestGenericExceptionResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CsSysRestGenericExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    confkey: str,
    confsrc: str,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CONFIGURATION_USE_GLOBALCONFIGURATIONEDITOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        confkey (str):
        confsrc (str):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        confkey=confkey,
        confsrc=confsrc,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    confkey: str,
    confsrc: str,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CONFIGURATION_USE_GLOBALCONFIGURATIONEDITOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        confkey (str):
        confsrc (str):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        confkey=confkey,
        confsrc=confsrc,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    confkey: str,
    confsrc: str,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CONFIGURATION_USE_GLOBALCONFIGURATIONEDITOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        confkey (str):
        confsrc (str):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        confkey=confkey,
        confsrc=confsrc,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    confkey: str,
    confsrc: str,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CONFIGURATION_USE_GLOBALCONFIGURATIONEDITOR


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        confkey (str):
        confsrc (str):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            confkey=confkey,
            confsrc=confsrc,
            client=client,
            body=body,
        )
    ).parsed
