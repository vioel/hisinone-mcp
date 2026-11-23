from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_psv_group_object_group_entry_rest import CsPsvGroupObjectGroupEntryRest
from ...types import Response


def _get_kwargs(
    object_group_id: int,
    person_ids: list[int],
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/psv/group/objectgroup/{object_group_id}/getNewObjectGroupEntries/{person_ids}".format(
            object_group_id=quote(str(object_group_id), safe=""),
            person_ids=quote(str(person_ids), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[CsPsvGroupObjectGroupEntryRest] | None:
    if response.status_code == 200:
        response_200: list[CsPsvGroupObjectGroupEntryRest] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsPsvGroupObjectGroupEntryRest.from_dict(response_200_item_data)

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
) -> Response[Any | list[CsPsvGroupObjectGroupEntryRest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_group_id: int,
    person_ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsPsvGroupObjectGroupEntryRest]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_EDIT_PERSON_GROUPS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        object_group_id (int):
        person_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsPsvGroupObjectGroupEntryRest]]
    """

    kwargs = _get_kwargs(
        object_group_id=object_group_id,
        person_ids=person_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_group_id: int,
    person_ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Any | list[CsPsvGroupObjectGroupEntryRest] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_EDIT_PERSON_GROUPS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        object_group_id (int):
        person_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsPsvGroupObjectGroupEntryRest]
    """

    return sync_detailed(
        object_group_id=object_group_id,
        person_ids=person_ids,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_group_id: int,
    person_ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsPsvGroupObjectGroupEntryRest]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_EDIT_PERSON_GROUPS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        object_group_id (int):
        person_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsPsvGroupObjectGroupEntryRest]]
    """

    kwargs = _get_kwargs(
        object_group_id=object_group_id,
        person_ids=person_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_group_id: int,
    person_ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Any | list[CsPsvGroupObjectGroupEntryRest] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_PERSON_EDIT_PERSON_GROUPS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        object_group_id (int):
        person_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsPsvGroupObjectGroupEntryRest]
    """

    return (
        await asyncio_detailed(
            object_group_id=object_group_id,
            person_ids=person_ids,
            client=client,
        )
    ).parsed
