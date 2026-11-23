from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rm_erp_absencemanagement_calendar_absence_calendar import RmErpAbsencemanagementCalendarAbsenceCalendar
from ...types import UNSET, Response


def _get_kwargs(
    *,
    unnamed1: str,
    unnamed2: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["unnamed1"] = unnamed1

    params["unnamed2"] = unnamed2

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rm/erp/absencemanagement/calendar",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RmErpAbsencemanagementCalendarAbsenceCalendar | None:
    if response.status_code == 200:
        response_200 = RmErpAbsencemanagementCalendarAbsenceCalendar.from_dict(response.json())

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
) -> Response[Any | RmErpAbsencemanagementCalendarAbsenceCalendar]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    unnamed1: str,
    unnamed2: str,
) -> Response[Any | RmErpAbsencemanagementCalendarAbsenceCalendar]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_ABSENCEMANAGEMENT_ABSENCECALENDAR_VIEW_ABSENCECALENDAR_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        unnamed1 (str):
        unnamed2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RmErpAbsencemanagementCalendarAbsenceCalendar]
    """

    kwargs = _get_kwargs(
        unnamed1=unnamed1,
        unnamed2=unnamed2,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    unnamed1: str,
    unnamed2: str,
) -> Any | RmErpAbsencemanagementCalendarAbsenceCalendar | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_ABSENCEMANAGEMENT_ABSENCECALENDAR_VIEW_ABSENCECALENDAR_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        unnamed1 (str):
        unnamed2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RmErpAbsencemanagementCalendarAbsenceCalendar
    """

    return sync_detailed(
        client=client,
        unnamed1=unnamed1,
        unnamed2=unnamed2,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    unnamed1: str,
    unnamed2: str,
) -> Response[Any | RmErpAbsencemanagementCalendarAbsenceCalendar]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_ABSENCEMANAGEMENT_ABSENCECALENDAR_VIEW_ABSENCECALENDAR_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        unnamed1 (str):
        unnamed2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RmErpAbsencemanagementCalendarAbsenceCalendar]
    """

    kwargs = _get_kwargs(
        unnamed1=unnamed1,
        unnamed2=unnamed2,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    unnamed1: str,
    unnamed2: str,
) -> Any | RmErpAbsencemanagementCalendarAbsenceCalendar | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_ABSENCEMANAGEMENT_ABSENCECALENDAR_VIEW_ABSENCECALENDAR_OWN


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        unnamed1 (str):
        unnamed2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RmErpAbsencemanagementCalendarAbsenceCalendar
    """

    return (
        await asyncio_detailed(
            client=client,
            unnamed1=unnamed1,
            unnamed2=unnamed2,
        )
    ).parsed
