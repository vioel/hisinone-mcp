from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fs_res_research_infrastructure_research_infrastructure import (
    FsResResearchInfrastructureResearchInfrastructure,
)
from ...types import Response


def _get_kwargs(
    ids: list[int],
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fs/res/researchInfrastructures/{ids}".format(
            ids=quote(str(ids), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[FsResResearchInfrastructureResearchInfrastructure] | None:
    if response.status_code == 200:
        response_200: list[FsResResearchInfrastructureResearchInfrastructure] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsResResearchInfrastructureResearchInfrastructure.from_dict(response_200_item_data)

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
) -> Response[Any | list[FsResResearchInfrastructureResearchInfrastructure]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[FsResResearchInfrastructureResearchInfrastructure]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_VIEW_RESEARCH_INFRASTRUCTURE,RIGHT_FS_RES_RESEARCHINFRASTRUCTU
    RE_VIEW_RESEARCH_INFRASTRUCTURE_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResResearchInfrastructureResearchInfrastructure]]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Any | list[FsResResearchInfrastructureResearchInfrastructure] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_VIEW_RESEARCH_INFRASTRUCTURE,RIGHT_FS_RES_RESEARCHINFRASTRUCTU
    RE_VIEW_RESEARCH_INFRASTRUCTURE_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResResearchInfrastructureResearchInfrastructure]
    """

    return sync_detailed(
        ids=ids,
        client=client,
    ).parsed


async def asyncio_detailed(
    ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[FsResResearchInfrastructureResearchInfrastructure]]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_VIEW_RESEARCH_INFRASTRUCTURE,RIGHT_FS_RES_RESEARCHINFRASTRUCTU
    RE_VIEW_RESEARCH_INFRASTRUCTURE_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FsResResearchInfrastructureResearchInfrastructure]]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ids: list[int],
    *,
    client: AuthenticatedClient,
) -> Any | list[FsResResearchInfrastructureResearchInfrastructure] | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_RESEARCHINFRASTRUCTURE_VIEW_RESEARCH_INFRASTRUCTURE,RIGHT_FS_RES_RESEARCHINFRASTRUCTU
    RE_VIEW_RESEARCH_INFRASTRUCTURE_VISIBLE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FsResResearchInfrastructureResearchInfrastructure]
    """

    return (
        await asyncio_detailed(
            ids=ids,
            client=client,
        )
    ).parsed
