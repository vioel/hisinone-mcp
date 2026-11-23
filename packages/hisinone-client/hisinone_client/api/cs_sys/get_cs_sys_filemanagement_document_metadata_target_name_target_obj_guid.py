from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_documents_document_metadata import CsSysRestDocumentsDocumentMetadata
from ...types import Response


def _get_kwargs(
    target_name: str,
    target_obj_guid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/filemanagement/documentMetadata/{target_name}/{target_obj_guid}".format(
            target_name=quote(str(target_name), safe=""),
            target_obj_guid=quote(str(target_obj_guid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[CsSysRestDocumentsDocumentMetadata] | None:
    if response.status_code == 200:
        response_200: list[CsSysRestDocumentsDocumentMetadata] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsSysRestDocumentsDocumentMetadata.from_dict(response_200_item_data)

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
) -> Response[Any | list[CsSysRestDocumentsDocumentMetadata]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_name: str,
    target_obj_guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsSysRestDocumentsDocumentMetadata]]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_obj_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysRestDocumentsDocumentMetadata]]
    """

    kwargs = _get_kwargs(
        target_name=target_name,
        target_obj_guid=target_obj_guid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_name: str,
    target_obj_guid: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[CsSysRestDocumentsDocumentMetadata] | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_obj_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysRestDocumentsDocumentMetadata]
    """

    return sync_detailed(
        target_name=target_name,
        target_obj_guid=target_obj_guid,
        client=client,
    ).parsed


async def asyncio_detailed(
    target_name: str,
    target_obj_guid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsSysRestDocumentsDocumentMetadata]]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_obj_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysRestDocumentsDocumentMetadata]]
    """

    kwargs = _get_kwargs(
        target_name=target_name,
        target_obj_guid=target_obj_guid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_name: str,
    target_obj_guid: str,
    *,
    client: AuthenticatedClient,
) -> Any | list[CsSysRestDocumentsDocumentMetadata] | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_obj_guid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysRestDocumentsDocumentMetadata]
    """

    return (
        await asyncio_detailed(
            target_name=target_name,
            target_obj_guid=target_obj_guid,
            client=client,
        )
    ).parsed
