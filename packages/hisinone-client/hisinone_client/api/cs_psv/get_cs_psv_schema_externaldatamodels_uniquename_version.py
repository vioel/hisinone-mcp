from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.impl_psv_schema_external_data_model_rest import ImplPsvSchemaExternalDataModelRest
from ...types import Response


def _get_kwargs(
    uniquename: str,
    version: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/psv/schema/externaldatamodels/{uniquename}/{version}".format(
            uniquename=quote(str(uniquename), safe=""),
            version=quote(str(version), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ImplPsvSchemaExternalDataModelRest | None:
    if response.status_code == 200:
        response_200 = ImplPsvSchemaExternalDataModelRest.from_dict(response.json())

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
) -> Response[Any | ImplPsvSchemaExternalDataModelRest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uniquename: str,
    version: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplPsvSchemaExternalDataModelRest]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_SCHEMA_MANAGE_EXTERNAL_DATA_MODELS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        uniquename (str):
        version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplPsvSchemaExternalDataModelRest]
    """

    kwargs = _get_kwargs(
        uniquename=uniquename,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uniquename: str,
    version: str,
    *,
    client: AuthenticatedClient,
) -> Any | ImplPsvSchemaExternalDataModelRest | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_SCHEMA_MANAGE_EXTERNAL_DATA_MODELS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        uniquename (str):
        version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplPsvSchemaExternalDataModelRest
    """

    return sync_detailed(
        uniquename=uniquename,
        version=version,
        client=client,
    ).parsed


async def asyncio_detailed(
    uniquename: str,
    version: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplPsvSchemaExternalDataModelRest]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_SCHEMA_MANAGE_EXTERNAL_DATA_MODELS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        uniquename (str):
        version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplPsvSchemaExternalDataModelRest]
    """

    kwargs = _get_kwargs(
        uniquename=uniquename,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uniquename: str,
    version: str,
    *,
    client: AuthenticatedClient,
) -> Any | ImplPsvSchemaExternalDataModelRest | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_SCHEMA_MANAGE_EXTERNAL_DATA_MODELS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        uniquename (str):
        version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplPsvSchemaExternalDataModelRest
    """

    return (
        await asyncio_detailed(
            uniquename=uniquename,
            version=version,
            client=client,
        )
    ).parsed
