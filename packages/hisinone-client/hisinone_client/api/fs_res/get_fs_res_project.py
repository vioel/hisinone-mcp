from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_project_project_obj import FsResProjectProjectObj
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    l: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["l"] = l

    params["from"] = from_

    params["until"] = until

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/project",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[FsResProjectProjectObj] | None:
    if response.status_code == 200:
        response_200: list[FsResProjectProjectObj] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsResProjectProjectObj.from_dict(response_200_item_data)

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
) -> Response[Any | list[FsResProjectProjectObj]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    l: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | list[FsResProjectProjectObj]]:
    """This method conducts a search of projects based on the provided parameters.

    **Parameters:**

    * `searchText:` The text to search for.
    * `limit:` The maximum number of projects to return. Default value is 100.
    * `from:` The start date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "1970-01-01T00:00:00". *Example:*
    Start date: „2023-08-04T16:00:00“ will return projects that have been last saved since or on the
    start date.
    * `until:` The end date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "2100-01-01T00:00:00". *Example:*
    Until date: „2023-08-04T16:00:00“ will return projects that have been last saved before or on the
    end date.
    * `offset:` The offset for returning changed projects. The default value is 0. Please note: *Offset*
    cannot be used without *until*.

    *Please note:* If no parameters are provided, the method will return the first 100 projects by
    default due to the default limit.

    **Return**

    * The return A ResponseEntity with a list of ProjectDto objects and HTTP status OK.

    **Error Handling**

    In case of an error occurrence (for example, if *until* is provided but *offset* is missing), a
    Service Exception with a message will be thrown.




    #### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str | Unset):
        l (int | Unset):
        from_ (str | Unset):
        until (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResProjectProjectObj]]
    """

    kwargs = _get_kwargs(
        q=q,
        l=l,
        from_=from_,
        until=until,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    l: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | list[FsResProjectProjectObj] | None:
    """This method conducts a search of projects based on the provided parameters.

    **Parameters:**

    * `searchText:` The text to search for.
    * `limit:` The maximum number of projects to return. Default value is 100.
    * `from:` The start date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "1970-01-01T00:00:00". *Example:*
    Start date: „2023-08-04T16:00:00“ will return projects that have been last saved since or on the
    start date.
    * `until:` The end date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "2100-01-01T00:00:00". *Example:*
    Until date: „2023-08-04T16:00:00“ will return projects that have been last saved before or on the
    end date.
    * `offset:` The offset for returning changed projects. The default value is 0. Please note: *Offset*
    cannot be used without *until*.

    *Please note:* If no parameters are provided, the method will return the first 100 projects by
    default due to the default limit.

    **Return**

    * The return A ResponseEntity with a list of ProjectDto objects and HTTP status OK.

    **Error Handling**

    In case of an error occurrence (for example, if *until* is provided but *offset* is missing), a
    Service Exception with a message will be thrown.




    #### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str | Unset):
        l (int | Unset):
        from_ (str | Unset):
        until (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResProjectProjectObj]
    """

    return sync_detailed(
        client=client,
        q=q,
        l=l,
        from_=from_,
        until=until,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    l: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | list[FsResProjectProjectObj]]:
    """This method conducts a search of projects based on the provided parameters.

    **Parameters:**

    * `searchText:` The text to search for.
    * `limit:` The maximum number of projects to return. Default value is 100.
    * `from:` The start date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "1970-01-01T00:00:00". *Example:*
    Start date: „2023-08-04T16:00:00“ will return projects that have been last saved since or on the
    start date.
    * `until:` The end date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "2100-01-01T00:00:00". *Example:*
    Until date: „2023-08-04T16:00:00“ will return projects that have been last saved before or on the
    end date.
    * `offset:` The offset for returning changed projects. The default value is 0. Please note: *Offset*
    cannot be used without *until*.

    *Please note:* If no parameters are provided, the method will return the first 100 projects by
    default due to the default limit.

    **Return**

    * The return A ResponseEntity with a list of ProjectDto objects and HTTP status OK.

    **Error Handling**

    In case of an error occurrence (for example, if *until* is provided but *offset* is missing), a
    Service Exception with a message will be thrown.




    #### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str | Unset):
        l (int | Unset):
        from_ (str | Unset):
        until (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResProjectProjectObj]]
    """

    kwargs = _get_kwargs(
        q=q,
        l=l,
        from_=from_,
        until=until,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    l: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    until: str | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | list[FsResProjectProjectObj] | None:
    """This method conducts a search of projects based on the provided parameters.

    **Parameters:**

    * `searchText:` The text to search for.
    * `limit:` The maximum number of projects to return. Default value is 100.
    * `from:` The start date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "1970-01-01T00:00:00". *Example:*
    Start date: „2023-08-04T16:00:00“ will return projects that have been last saved since or on the
    start date.
    * `until:` The end date for searching changed projects in ISO 8601 format (e.g.,
    "2023-08-04T16:00:00"). The default value is a predefined date "2100-01-01T00:00:00". *Example:*
    Until date: „2023-08-04T16:00:00“ will return projects that have been last saved before or on the
    end date.
    * `offset:` The offset for returning changed projects. The default value is 0. Please note: *Offset*
    cannot be used without *until*.

    *Please note:* If no parameters are provided, the method will return the first 100 projects by
    default due to the default limit.

    **Return**

    * The return A ResponseEntity with a list of ProjectDto objects and HTTP status OK.

    **Error Handling**

    In case of an error occurrence (for example, if *until* is provided but *offset* is missing), a
    Service Exception with a message will be thrown.




    #### At least one of these rights:
    * RIGHT_FS_RES_PROJECT_VIEW_PROJECT,RIGHT_FS_RES_PROJECT_VIEW_PROJECT_OWN,RIGHT_FS_RES_PROJECT_VIEW_
    PROJECT_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        q (str | Unset):
        l (int | Unset):
        from_ (str | Unset):
        until (str | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResProjectProjectObj]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            l=l,
            from_=from_,
            until=until,
            offset=offset,
        )
    ).parsed
