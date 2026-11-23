from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.de_mathplan_moses_edci_europass_credential_type import DeMathplanMosesEdciEuropassCredentialType
from ...types import Response


def _get_kwargs(
    cos_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cm/exa/edci/{cos_id}".format(
            cos_id=quote(str(cos_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | DeMathplanMosesEdciEuropassCredentialType | None:
    if response.status_code == 200:
        response_200 = DeMathplanMosesEdciEuropassCredentialType.from_dict(response.json())

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
) -> Response[Any | DeMathplanMosesEdciEuropassCredentialType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cos_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DeMathplanMosesEdciEuropassCredentialType]:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_EDIT_CURRICULA_ELEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        cos_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeMathplanMosesEdciEuropassCredentialType]
    """

    kwargs = _get_kwargs(
        cos_id=cos_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cos_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | DeMathplanMosesEdciEuropassCredentialType | None:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_EDIT_CURRICULA_ELEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        cos_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeMathplanMosesEdciEuropassCredentialType
    """

    return sync_detailed(
        cos_id=cos_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cos_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DeMathplanMosesEdciEuropassCredentialType]:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_EDIT_CURRICULA_ELEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        cos_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeMathplanMosesEdciEuropassCredentialType]
    """

    kwargs = _get_kwargs(
        cos_id=cos_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cos_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | DeMathplanMosesEdciEuropassCredentialType | None:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_EDIT_CURRICULA_ELEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        cos_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeMathplanMosesEdciEuropassCredentialType
    """

    return (
        await asyncio_detailed(
            cos_id=cos_id,
            client=client,
        )
    ).parsed
