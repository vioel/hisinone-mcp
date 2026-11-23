from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_value_generic_value import CsSysValueGenericValue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    clazz_name: str,
    *,
    q: str | Unset = UNSET,
    fkc: str | Unset = UNSET,
    fkid: int | Unset = UNSET,
    dynamic_table_id: int | Unset = UNSET,
    dynamic_table_ouid: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    his_key_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["fkc"] = fkc

    params["fkid"] = fkid

    params["dynamicTableId"] = dynamic_table_id

    params["dynamicTableOuid"] = dynamic_table_ouid

    params["sortBy"] = sort_by

    json_ids: list[int] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = ids

    params["ids"] = json_ids

    json_his_key_ids: list[int] | Unset = UNSET
    if not isinstance(his_key_ids, Unset):
        json_his_key_ids = his_key_ids

    params["hisKeyIds"] = json_his_key_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cs/sys/values/{clazz_name}".format(
            clazz_name=quote(str(clazz_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[CsSysValueGenericValue] | None:
    if response.status_code == 200:
        response_200: list[CsSysValueGenericValue] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CsSysValueGenericValue.from_dict(response_200_item_data)

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
) -> Response[Any | list[CsSysValueGenericValue]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    fkc: str | Unset = UNSET,
    fkid: int | Unset = UNSET,
    dynamic_table_id: int | Unset = UNSET,
    dynamic_table_ouid: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    his_key_ids: list[int] | Unset = UNSET,
) -> Response[Any | list[CsSysValueGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_IS_LOGGED_IN

    Args:
        clazz_name (str):
        q (str | Unset):
        fkc (str | Unset):
        fkid (int | Unset):
        dynamic_table_id (int | Unset):
        dynamic_table_ouid (str | Unset):
        sort_by (str | Unset):
        ids (list[int] | Unset):
        his_key_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysValueGenericValue]]
    """

    kwargs = _get_kwargs(
        clazz_name=clazz_name,
        q=q,
        fkc=fkc,
        fkid=fkid,
        dynamic_table_id=dynamic_table_id,
        dynamic_table_ouid=dynamic_table_ouid,
        sort_by=sort_by,
        ids=ids,
        his_key_ids=his_key_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    fkc: str | Unset = UNSET,
    fkid: int | Unset = UNSET,
    dynamic_table_id: int | Unset = UNSET,
    dynamic_table_ouid: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    his_key_ids: list[int] | Unset = UNSET,
) -> Any | list[CsSysValueGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_IS_LOGGED_IN

    Args:
        clazz_name (str):
        q (str | Unset):
        fkc (str | Unset):
        fkid (int | Unset):
        dynamic_table_id (int | Unset):
        dynamic_table_ouid (str | Unset):
        sort_by (str | Unset):
        ids (list[int] | Unset):
        his_key_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysValueGenericValue]
    """

    return sync_detailed(
        clazz_name=clazz_name,
        client=client,
        q=q,
        fkc=fkc,
        fkid=fkid,
        dynamic_table_id=dynamic_table_id,
        dynamic_table_ouid=dynamic_table_ouid,
        sort_by=sort_by,
        ids=ids,
        his_key_ids=his_key_ids,
    ).parsed


async def asyncio_detailed(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    fkc: str | Unset = UNSET,
    fkid: int | Unset = UNSET,
    dynamic_table_id: int | Unset = UNSET,
    dynamic_table_ouid: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    his_key_ids: list[int] | Unset = UNSET,
) -> Response[Any | list[CsSysValueGenericValue]]:
    """#### At least one of these rights:
    * RIGHT_IS_LOGGED_IN

    Args:
        clazz_name (str):
        q (str | Unset):
        fkc (str | Unset):
        fkid (int | Unset):
        dynamic_table_id (int | Unset):
        dynamic_table_ouid (str | Unset):
        sort_by (str | Unset):
        ids (list[int] | Unset):
        his_key_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[CsSysValueGenericValue]]
    """

    kwargs = _get_kwargs(
        clazz_name=clazz_name,
        q=q,
        fkc=fkc,
        fkid=fkid,
        dynamic_table_id=dynamic_table_id,
        dynamic_table_ouid=dynamic_table_ouid,
        sort_by=sort_by,
        ids=ids,
        his_key_ids=his_key_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    clazz_name: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    fkc: str | Unset = UNSET,
    fkid: int | Unset = UNSET,
    dynamic_table_id: int | Unset = UNSET,
    dynamic_table_ouid: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    ids: list[int] | Unset = UNSET,
    his_key_ids: list[int] | Unset = UNSET,
) -> Any | list[CsSysValueGenericValue] | None:
    """#### At least one of these rights:
    * RIGHT_IS_LOGGED_IN

    Args:
        clazz_name (str):
        q (str | Unset):
        fkc (str | Unset):
        fkid (int | Unset):
        dynamic_table_id (int | Unset):
        dynamic_table_ouid (str | Unset):
        sort_by (str | Unset):
        ids (list[int] | Unset):
        his_key_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[CsSysValueGenericValue]
    """

    return (
        await asyncio_detailed(
            clazz_name=clazz_name,
            client=client,
            q=q,
            fkc=fkc,
            fkid=fkid,
            dynamic_table_id=dynamic_table_id,
            dynamic_table_ouid=dynamic_table_ouid,
            sort_by=sort_by,
            ids=ids,
            his_key_ids=his_key_ids,
        )
    ).parsed
