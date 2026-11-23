from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_psv_person_identifier_info_rest import CsPsvPersonIdentifierInfoRest
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    identifier_value: str,
    type_uniquename: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["identifierValue"] = identifier_value

    params["typeUniquename"] = type_uniquename

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/psv/person/identifier",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = CsPsvPersonIdentifierInfoRest.from_dict(response.json())

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
) -> Response[Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    identifier_value: str,
    type_uniquename: str,
) -> Response[Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_VIEW_PERSON_IDENTIFIER


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier_value (str):
        type_uniquename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        identifier_value=identifier_value,
        type_uniquename=type_uniquename,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    identifier_value: str,
    type_uniquename: str,
) -> Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_VIEW_PERSON_IDENTIFIER


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier_value (str):
        type_uniquename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        client=client,
        identifier_value=identifier_value,
        type_uniquename=type_uniquename,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    identifier_value: str,
    type_uniquename: str,
) -> Response[Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_VIEW_PERSON_IDENTIFIER


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier_value (str):
        type_uniquename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        identifier_value=identifier_value,
        type_uniquename=type_uniquename,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    identifier_value: str,
    type_uniquename: str,
) -> Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_VIEW_PERSON_IDENTIFIER


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        identifier_value (str):
        type_uniquename (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsPsvPersonIdentifierInfoRest | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            identifier_value=identifier_value,
            type_uniquename=type_uniquename,
        )
    ).parsed
