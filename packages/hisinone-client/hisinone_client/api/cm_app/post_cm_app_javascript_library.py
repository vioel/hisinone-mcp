from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.model_cm_app_backend_javascript_library_java_script_library_entry import (
    ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cm/app/javascript/library/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | None:
    if response.status_code == 200:
        response_200 = ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 422:
        response_422 = CsSysRestGenericExceptionResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_PROGRAM_CODE
    * RIGHT_CM_APP_JSLIBRARY_EDIT_JSLIBRARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_PROGRAM_CODE
    * RIGHT_CM_APP_JSLIBRARY_EDIT_JSLIBRARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry]:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_PROGRAM_CODE
    * RIGHT_CM_APP_JSLIBRARY_EDIT_JSLIBRARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | None:
    """#### At least one of these rights:
    * RIGHT_CS_SYS_CORE_EDIT_PROGRAM_CODE
    * RIGHT_CM_APP_JSLIBRARY_EDIT_JSLIBRARY


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
