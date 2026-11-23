from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.impl_grading_type_impl import ImplGradingTypeImpl
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cm/exa/gradingType/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ImplGradingTypeImpl | None:
    if response.status_code == 200:
        response_200 = ImplGradingTypeImpl.from_dict(response.json())

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
) -> Response[Any | ImplGradingTypeImpl]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplGradingTypeImpl]:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_VIEW_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_EDIT_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_DELETE_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_CREATE_GRADING_TYPE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplGradingTypeImpl]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Any | ImplGradingTypeImpl | None:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_VIEW_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_EDIT_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_DELETE_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_CREATE_GRADING_TYPE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplGradingTypeImpl
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ImplGradingTypeImpl]:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_VIEW_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_EDIT_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_DELETE_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_CREATE_GRADING_TYPE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ImplGradingTypeImpl]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Any | ImplGradingTypeImpl | None:
    """#### At least one of these rights:
    * RIGHT_CM_EXA_CURRICULA_VIEW_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_EDIT_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_DELETE_GRADING_TYPE
    * RIGHT_CM_EXA_CURRICULA_CREATE_GRADING_TYPE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ImplGradingTypeImpl
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
