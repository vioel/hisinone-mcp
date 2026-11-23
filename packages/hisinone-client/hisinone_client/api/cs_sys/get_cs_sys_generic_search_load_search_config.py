from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_generic_search_search_configuration_his_search_configuration import (
    CsSysGenericSearchSearchConfigurationHisSearchConfiguration,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    config_file: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["configFile"] = config_file

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/genericSearch/loadSearchConfig",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration | None:
    if response.status_code == 200:
        response_200 = CsSysGenericSearchSearchConfigurationHisSearchConfiguration.from_dict(response.json())

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
) -> Response[Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    config_file: str,
) -> Response[Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration]:
    """This service provides a search form that corresponds to a search configuration file of HISinOne. It
    expects a string value that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned search configuration is of type `HisSearchConfiguration`. Its field `searchEntity`
    provides the entity to search for, fields `pageTitle` and `tableTitle` hold headings as defined in
    the search config file, and the field `searchCriteria` of type `HisSearchCriteria` provides the list
    of field sets that constitute the search form.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration]
    """

    kwargs = _get_kwargs(
        config_file=config_file,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    config_file: str,
) -> Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration | None:
    """This service provides a search form that corresponds to a search configuration file of HISinOne. It
    expects a string value that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned search configuration is of type `HisSearchConfiguration`. Its field `searchEntity`
    provides the entity to search for, fields `pageTitle` and `tableTitle` hold headings as defined in
    the search config file, and the field `searchCriteria` of type `HisSearchCriteria` provides the list
    of field sets that constitute the search form.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration
    """

    return sync_detailed(
        client=client,
        config_file=config_file,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    config_file: str,
) -> Response[Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration]:
    """This service provides a search form that corresponds to a search configuration file of HISinOne. It
    expects a string value that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned search configuration is of type `HisSearchConfiguration`. Its field `searchEntity`
    provides the entity to search for, fields `pageTitle` and `tableTitle` hold headings as defined in
    the search config file, and the field `searchCriteria` of type `HisSearchCriteria` provides the list
    of field sets that constitute the search form.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration]
    """

    kwargs = _get_kwargs(
        config_file=config_file,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    config_file: str,
) -> Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration | None:
    """This service provides a search form that corresponds to a search configuration file of HISinOne. It
    expects a string value that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`. This configuration file is a standard generic search
    configuration, except that it must contain an additional tag 'authorities' that provides a list of
    rights.

    The returned search configuration is of type `HisSearchConfiguration`. Its field `searchEntity`
    provides the entity to search for, fields `pageTitle` and `tableTitle` hold headings as defined in
    the search config file, and the field `searchCriteria` of type `HisSearchCriteria` provides the list
    of field sets that constitute the search form.

    <!--SKIP_RIGHTS--><br>

    **Rights:**

    The required permissions are defined in each search configuration file. Search configuration files
    without a dedicated &lt;authorities&gt; element are not accessible via REST.





    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        config_file (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysGenericSearchSearchConfigurationHisSearchConfiguration
    """

    return (
        await asyncio_detailed(
            client=client,
            config_file=config_file,
        )
    ).parsed
