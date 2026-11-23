from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.post_fs_res_publication_import_interface_name_body import PostFsResPublicationImportInterfaceNameBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    interface_name: str,
    *,
    body: PostFsResPublicationImportInterfaceNameBody | Unset = UNSET,
    run_import_job_synchronous: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["runImportJobSynchronous"] = run_import_job_synchronous

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/fs/res/publication/import/{interface_name}".format(
            interface_name=quote(str(interface_name), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | CsSysRestGenericExceptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    interface_name: str,
    *,
    client: AuthenticatedClient,
    body: PostFsResPublicationImportInterfaceNameBody | Unset = UNSET,
    run_import_job_synchronous: bool | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        run_import_job_synchronous (bool | Unset):
        body (PostFsResPublicationImportInterfaceNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        interface_name=interface_name,
        body=body,
        run_import_job_synchronous=run_import_job_synchronous,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    interface_name: str,
    *,
    client: AuthenticatedClient,
    body: PostFsResPublicationImportInterfaceNameBody | Unset = UNSET,
    run_import_job_synchronous: bool | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        run_import_job_synchronous (bool | Unset):
        body (PostFsResPublicationImportInterfaceNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        interface_name=interface_name,
        client=client,
        body=body,
        run_import_job_synchronous=run_import_job_synchronous,
    ).parsed


async def asyncio_detailed(
    interface_name: str,
    *,
    client: AuthenticatedClient,
    body: PostFsResPublicationImportInterfaceNameBody | Unset = UNSET,
    run_import_job_synchronous: bool | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        run_import_job_synchronous (bool | Unset):
        body (PostFsResPublicationImportInterfaceNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse]
    """

    kwargs = _get_kwargs(
        interface_name=interface_name,
        body=body,
        run_import_job_synchronous=run_import_job_synchronous,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    interface_name: str,
    *,
    client: AuthenticatedClient,
    body: PostFsResPublicationImportInterfaceNameBody | Unset = UNSET,
    run_import_job_synchronous: bool | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_IMPORT_PUBLICATION_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        interface_name (str):
        run_import_job_synchronous (bool | Unset):
        body (PostFsResPublicationImportInterfaceNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            interface_name=interface_name,
            client=client,
            body=body,
            run_import_job_synchronous=run_import_job_synchronous,
        )
    ).parsed
