from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.org_springframework_web_servlet_view_redirect_view import OrgSpringframeworkWebServletViewRedirectView
from ...models.post_cs_psv_emrex_unnamed_1 import PostCsPsvEmrexUnnamed1
from ...types import UNSET, Response


def _get_kwargs(
    *,
    session_id: str,
    return_url: str,
    unnamed1: PostCsPsvEmrexUnnamed1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sessionId"] = session_id

    params["returnUrl"] = return_url

    json_unnamed1 = unnamed1.to_dict()
    params.update(json_unnamed1)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/psv/emrex",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView | None:
    if response.status_code == 200:
        response_200 = OrgSpringframeworkWebServletViewRedirectView.from_dict(response.json())

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
) -> Response[Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str,
    return_url: str,
    unnamed1: PostCsPsvEmrexUnnamed1,
) -> Response[Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        session_id (str):
        return_url (str):
        unnamed1 (PostCsPsvEmrexUnnamed1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        return_url=return_url,
        unnamed1=unnamed1,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    session_id: str,
    return_url: str,
    unnamed1: PostCsPsvEmrexUnnamed1,
) -> Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        session_id (str):
        return_url (str):
        unnamed1 (PostCsPsvEmrexUnnamed1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView
    """

    return sync_detailed(
        client=client,
        session_id=session_id,
        return_url=return_url,
        unnamed1=unnamed1,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    session_id: str,
    return_url: str,
    unnamed1: PostCsPsvEmrexUnnamed1,
) -> Response[Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        session_id (str):
        return_url (str):
        unnamed1 (PostCsPsvEmrexUnnamed1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView]
    """

    kwargs = _get_kwargs(
        session_id=session_id,
        return_url=return_url,
        unnamed1=unnamed1,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    session_id: str,
    return_url: str,
    unnamed1: PostCsPsvEmrexUnnamed1,
) -> Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        session_id (str):
        return_url (str):
        unnamed1 (PostCsPsvEmrexUnnamed1):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | OrgSpringframeworkWebServletViewRedirectView
    """

    return (
        await asyncio_detailed(
            client=client,
            session_id=session_id,
            return_url=return_url,
            unnamed1=unnamed1,
        )
    ).parsed
