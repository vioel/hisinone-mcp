from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_documents_document_metadata import CsSysRestDocumentsDocumentMetadata
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import Response


def _get_kwargs(
    target_name: str,
    target_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/filemanagement/uploadFile/{target_name}/{target_id}".format(
            target_name=quote(str(target_name), safe=""),
            target_id=quote(str(target_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = CsSysRestDocumentsDocumentMetadata.from_dict(response.json())

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
) -> Response[Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_name: str,
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse]:
    """
    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions for accessing a document depend on the associated entity.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        target_name=target_name,
        target_id=target_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_name: str,
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse | None:
    """
    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions for accessing a document depend on the associated entity.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        target_name=target_name,
        target_id=target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    target_name: str,
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse]:
    """
    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions for accessing a document depend on the associated entity.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        target_name=target_name,
        target_id=target_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_name: str,
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse | None:
    """
    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions for accessing a document depend on the associated entity.




    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        target_name (str):
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestDocumentsDocumentMetadata | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            target_name=target_name,
            target_id=target_id,
            client=client,
        )
    ).parsed
