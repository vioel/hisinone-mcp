from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_psv_agreement_personal_agreement_simple import CsPsvAgreementPersonalAgreementSimple
from ...types import Response


def _get_kwargs(
    person_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/psv/personalagreement/byPerson/{person_id}".format(
            person_id=quote(str(person_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[CsPsvAgreementPersonalAgreementSimple] | None:
    if response.status_code == 200:
        response_200: list[CsPsvAgreementPersonalAgreementSimple] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsPsvAgreementPersonalAgreementSimple.from_dict(response_200_item_data)

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
) -> Response[Any | list[CsPsvAgreementPersonalAgreementSimple]]:
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
) -> Response[Any | list[CsPsvAgreementPersonalAgreementSimple]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_LIST_PERSONAL_AGREEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsPsvAgreementPersonalAgreementSimple]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[CsPsvAgreementPersonalAgreementSimple] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_LIST_PERSONAL_AGREEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsPsvAgreementPersonalAgreementSimple]
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    person_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsPsvAgreementPersonalAgreementSimple]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_LIST_PERSONAL_AGREEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsPsvAgreementPersonalAgreementSimple]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[CsPsvAgreementPersonalAgreementSimple] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_LIST_PERSONAL_AGREEMENTS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        person_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsPsvAgreementPersonalAgreementSimple]
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
        )
    ).parsed
