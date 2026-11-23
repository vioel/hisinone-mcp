from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_generic_search_search_result_his_search_request import (
    CsSysGenericSearchSearchResultHisSearchRequest,
)
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/genericSearch/validateInputs",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | int | None:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
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
) -> Response[Any | CsSysRestGenericExceptionResponse | int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | int]:
    """This service may be used to run the backend validation of user inputs.
    This helps to prevent the redirect from a search form to the search result form, in case that one
    wants to display the validation error on the search form.

    It takes the same inputs as the loadSearchResult service.

    It's result is a validation error, or one of the following integer result codes:
    * 0: empty search result
    * 1: non-empty search result, grouping failed
    * 2: non-empty search result, grouping worked


    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchResultHisSearchRequest | Unset):  Example: {'offset': 0,
            'configFile': 'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key':
            'Publication.publicationType.id', 'selectList': [5]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | int]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | int | None:
    """This service may be used to run the backend validation of user inputs.
    This helps to prevent the redirect from a search form to the search result form, in case that one
    wants to display the validation error on the search form.

    It takes the same inputs as the loadSearchResult service.

    It's result is a validation error, or one of the following integer result codes:
    * 0: empty search result
    * 1: non-empty search result, grouping failed
    * 2: non-empty search result, grouping worked


    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchResultHisSearchRequest | Unset):  Example: {'offset': 0,
            'configFile': 'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key':
            'Publication.publicationType.id', 'selectList': [5]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | int
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | int]:
    """This service may be used to run the backend validation of user inputs.
    This helps to prevent the redirect from a search form to the search result form, in case that one
    wants to display the validation error on the search form.

    It takes the same inputs as the loadSearchResult service.

    It's result is a validation error, or one of the following integer result codes:
    * 0: empty search result
    * 1: non-empty search result, grouping failed
    * 2: non-empty search result, grouping worked


    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchResultHisSearchRequest | Unset):  Example: {'offset': 0,
            'configFile': 'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key':
            'Publication.publicationType.id', 'selectList': [5]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | int]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | int | None:
    """This service may be used to run the backend validation of user inputs.
    This helps to prevent the redirect from a search form to the search result form, in case that one
    wants to display the validation error on the search form.

    It takes the same inputs as the loadSearchResult service.

    It's result is a validation error, or one of the following integer result codes:
    * 0: empty search result
    * 1: non-empty search result, grouping failed
    * 2: non-empty search result, grouping worked


    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchResultHisSearchRequest | Unset):  Example: {'offset': 0,
            'configFile': 'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key':
            'Publication.publicationType.id', 'selectList': [5]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | int
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
