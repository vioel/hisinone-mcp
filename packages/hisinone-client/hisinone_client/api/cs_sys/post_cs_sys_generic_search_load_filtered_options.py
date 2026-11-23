from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_generic_search_search_configuration_filtered_options_request import (
    CsSysGenericSearchSearchConfigurationFilteredOptionsRequest,
)
from ...models.cs_sys_generic_search_search_configuration_his_option import (
    CsSysGenericSearchSearchConfigurationHisOption,
)
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/genericSearch/loadFilteredOptions",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption] | None:
    if response.status_code == 200:
        response_200: list[CsSysGenericSearchSearchConfigurationHisOption] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsSysGenericSearchSearchConfigurationHisOption.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]]:
    """This service provides a filtered list of values that may be selected in a drop-down-menu. It expects
    an object of type `FilteredOptionsRequest` as its argument:
    * The field `configFile` holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned list of options is of type `HisOption[]`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]]
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
    body: CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption] | None:
    """This service provides a filtered list of values that may be selected in a drop-down-menu. It expects
    an object of type `FilteredOptionsRequest` as its argument:
    * The field `configFile` holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned list of options is of type `HisOption[]`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]]:
    """This service provides a filtered list of values that may be selected in a drop-down-menu. It expects
    an object of type `FilteredOptionsRequest` as its argument:
    * The field `configFile` holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned list of options is of type `HisOption[]`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption] | None:
    """This service provides a filtered list of values that may be selected in a drop-down-menu. It expects
    an object of type `FilteredOptionsRequest` as its argument:
    * The field `configFile` holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned list of options is of type `HisOption[]`.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysGenericSearchSearchConfigurationFilteredOptionsRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[CsSysGenericSearchSearchConfigurationHisOption]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
