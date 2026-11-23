from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_psv_person_profile_person_profile import CsPsvPersonProfilePersonProfile
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: int,
    *,
    body: CsPsvPersonProfilePersonProfile | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/psv/personProfile/entries/update/{person_id}".format(
            person_id=quote(str(person_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = CsPsvPersonProfilePersonProfile.from_dict(response.json())

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
) -> Response[Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient,
    body: CsPsvPersonProfilePersonProfile | Unset = UNSET,
) -> Response[Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PROFILE_EDIT_PROFILE,RIGHT_CS_PSV_PROFILE_EDIT_PROFILE_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):
        body (CsPsvPersonProfilePersonProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient,
    body: CsPsvPersonProfilePersonProfile | Unset = UNSET,
) -> Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PROFILE_EDIT_PROFILE,RIGHT_CS_PSV_PROFILE_EDIT_PROFILE_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):
        body (CsPsvPersonProfilePersonProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient,
    body: CsPsvPersonProfilePersonProfile | Unset = UNSET,
) -> Response[Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PROFILE_EDIT_PROFILE,RIGHT_CS_PSV_PROFILE_EDIT_PROFILE_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):
        body (CsPsvPersonProfilePersonProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient,
    body: CsPsvPersonProfilePersonProfile | Unset = UNSET,
) -> Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PROFILE_EDIT_PROFILE,RIGHT_CS_PSV_PROFILE_EDIT_PROFILE_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):
        body (CsPsvPersonProfilePersonProfile | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsPsvPersonProfilePersonProfile | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
        )
    ).parsed
