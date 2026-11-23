from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_generic_search_search_result_his_search_request import (
    CsSysGenericSearchSearchResultHisSearchRequest,
)
from ...models.cs_sys_generic_search_search_result_rest_search_result import (
    CsSysGenericSearchSearchResultRestSearchResult,
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
        "url": "/cs/sys/genericSearch/loadSearchResult",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse | None:
    if response.status_code == 200:
        response_200 = CsSysGenericSearchSearchResultRestSearchResult.from_dict(response.json())

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
) -> Response[Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse]:
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
) -> Response[Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse]:
    """This service expects an object of type `HisSearchRequest` as its argument:
    * The fields `limit` and `offset` allow to request only a partial list of search results. This
    functionality may be used to display paged search results quickly without retrieving the whole list
    of search results.
    * The field `search` contains
    ** a field `configFile` that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`, and
    ** a nested structure of `groups` and `criteria` for keys and user-provided search criteria.
    The keys are derived from the search configuration file as provided by the loadSearchConfig service.
    The key may seem like it has an internal structure, but it is used verbatim. Each search criterion
    `value` may be a single value or a comma-separated list of id's of selected options, in case of
    single- or multiple-select fields, respectively.


    <br>

    **Example 1: Search for publication titles with the word "database"**

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.title","value":"database"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>

    **Example 2: Search for journal articles**

    To search for monographs (publication type 1) and journal articles (publication type 5) use the
    following example

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.publicationType.id","value":"1,5"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>


    The returned search result is of type `RestSearchResult`. It has the following fields:
    * `name` the name of the search entity class

    * `offset` the index of the first result row to return, starting at 0
    * `maxResultRows` a hard limit on the number of result rows to return at once imposed by search
    configuration
    * `limit` the actual number of returned result rows
    * `totalCount` the total number of search results
    * `columns` contains metadata for each column of the returned data
    * `data` contains the actual data that has been found


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
        Response[Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse]
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
) -> Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse | None:
    """This service expects an object of type `HisSearchRequest` as its argument:
    * The fields `limit` and `offset` allow to request only a partial list of search results. This
    functionality may be used to display paged search results quickly without retrieving the whole list
    of search results.
    * The field `search` contains
    ** a field `configFile` that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`, and
    ** a nested structure of `groups` and `criteria` for keys and user-provided search criteria.
    The keys are derived from the search configuration file as provided by the loadSearchConfig service.
    The key may seem like it has an internal structure, but it is used verbatim. Each search criterion
    `value` may be a single value or a comma-separated list of id's of selected options, in case of
    single- or multiple-select fields, respectively.


    <br>

    **Example 1: Search for publication titles with the word "database"**

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.title","value":"database"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>

    **Example 2: Search for journal articles**

    To search for monographs (publication type 1) and journal articles (publication type 5) use the
    following example

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.publicationType.id","value":"1,5"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>


    The returned search result is of type `RestSearchResult`. It has the following fields:
    * `name` the name of the search entity class

    * `offset` the index of the first result row to return, starting at 0
    * `maxResultRows` a hard limit on the number of result rows to return at once imposed by search
    configuration
    * `limit` the actual number of returned result rows
    * `totalCount` the total number of search results
    * `columns` contains metadata for each column of the returned data
    * `data` contains the actual data that has been found


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
        Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET,
) -> Response[Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse]:
    """This service expects an object of type `HisSearchRequest` as its argument:
    * The fields `limit` and `offset` allow to request only a partial list of search results. This
    functionality may be used to display paged search results quickly without retrieving the whole list
    of search results.
    * The field `search` contains
    ** a field `configFile` that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`, and
    ** a nested structure of `groups` and `criteria` for keys and user-provided search criteria.
    The keys are derived from the search configuration file as provided by the loadSearchConfig service.
    The key may seem like it has an internal structure, but it is used verbatim. Each search criterion
    `value` may be a single value or a comma-separated list of id's of selected options, in case of
    single- or multiple-select fields, respectively.


    <br>

    **Example 1: Search for publication titles with the word "database"**

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.title","value":"database"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>

    **Example 2: Search for journal articles**

    To search for monographs (publication type 1) and journal articles (publication type 5) use the
    following example

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.publicationType.id","value":"1,5"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>


    The returned search result is of type `RestSearchResult`. It has the following fields:
    * `name` the name of the search entity class

    * `offset` the index of the first result row to return, starting at 0
    * `maxResultRows` a hard limit on the number of result rows to return at once imposed by search
    configuration
    * `limit` the actual number of returned result rows
    * `totalCount` the total number of search results
    * `columns` contains metadata for each column of the returned data
    * `data` contains the actual data that has been found


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
        Response[Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse]
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
) -> Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse | None:
    """This service expects an object of type `HisSearchRequest` as its argument:
    * The fields `limit` and `offset` allow to request only a partial list of search results. This
    functionality may be used to display paged search results quickly without retrieving the whole list
    of search results.
    * The field `search` contains
    ** a field `configFile` that holds the path to the search configuration file, e.g.
    `psv/facility/searchRoomDemo.xml`, and
    ** a nested structure of `groups` and `criteria` for keys and user-provided search criteria.
    The keys are derived from the search configuration file as provided by the loadSearchConfig service.
    The key may seem like it has an internal structure, but it is used verbatim. Each search criterion
    `value` may be a single value or a comma-separated list of id's of selected options, in case of
    single- or multiple-select fields, respectively.


    <br>

    **Example 1: Search for publication titles with the word "database"**

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.title","value":"database"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>

    **Example 2: Search for journal articles**

    To search for monographs (publication type 1) and journal articles (publication type 5) use the
    following example

    ~~~~
    {
        "search": {
                "groups": [
                        {
                                "criteria":[{"field":"Publication.publicationType.id","value":"1,5"}],
                                "criteriaGroups":[],
                                "groupLabel":"fs.res.common.basicData"
                        }
                ],
                "configFile":"fs/res/searchPublication.xml"
        },
        "offset":0,
        "limit":10
    }

    ~~~~
    <br>


    The returned search result is of type `RestSearchResult`. It has the following fields:
    * `name` the name of the search entity class

    * `offset` the index of the first result row to return, starting at 0
    * `maxResultRows` a hard limit on the number of result rows to return at once imposed by search
    configuration
    * `limit` the actual number of returned result rows
    * `totalCount` the total number of search results
    * `columns` contains metadata for each column of the returned data
    * `data` contains the actual data that has been found


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
        Any | CsSysGenericSearchSearchResultRestSearchResult | CsSysRestGenericExceptionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
