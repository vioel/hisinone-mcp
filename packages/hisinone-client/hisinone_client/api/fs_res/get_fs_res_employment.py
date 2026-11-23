from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_psv_employment_employment import CsPsvEmploymentEmployment
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/employment",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[CsPsvEmploymentEmployment] | None:
    if response.status_code == 200:
        response_200: list[CsPsvEmploymentEmployment] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsPsvEmploymentEmployment.from_dict(response_200_item_data)

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
) -> Response[Any | list[CsPsvEmploymentEmployment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsPsvEmploymentEmployment]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsPsvEmploymentEmployment]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | list[CsPsvEmploymentEmployment] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsPsvEmploymentEmployment]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[CsPsvEmploymentEmployment]]:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsPsvEmploymentEmployment]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | list[CsPsvEmploymentEmployment] | None:
    """#### At least one of these rights:
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_EXTERNAL_EMPLOYMENT
    * RIGHT_CS_PSV_EMPLOYMENT_VIEW_INTERNAL_EMPLOYMENT


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsPsvEmploymentEmployment]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
