from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.model_cm_app_backend_entrance_examination_entrance_exam_appointment import (
    ModelCmAppBackendEntranceExaminationEntranceExamAppointment,
)
from ...models.model_cm_app_backend_entrance_examination_entrance_exam_appointment_assignment import (
    ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cm/app/entrance/examination/cancelApplicant",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] | None:
    if response.status_code == 200:
        response_200: list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelCmAppBackendEntranceExaminationEntranceExamAppointment.from_dict(
                response_200_item_data
            )

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
) -> Response[
    Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset = UNSET,
) -> Response[
    Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]
]:
    """#### At least one of these rights:
    * RIGHT_CM_APP_ENTRANCE_EXAMINATION_PLAN_EXAMINATION
    * RIGHT_CM_EXA_EXAMASSESSMENT_DELETE_EXAMPLANS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]]
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
    body: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] | None:
    """#### At least one of these rights:
    * RIGHT_CM_APP_ENTRANCE_EXAMINATION_PLAN_EXAMINATION
    * RIGHT_CM_EXA_EXAMASSESSMENT_DELETE_EXAMPLANS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset = UNSET,
) -> Response[
    Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]
]:
    """#### At least one of these rights:
    * RIGHT_CM_APP_ENTRANCE_EXAMINATION_PLAN_EXAMINATION
    * RIGHT_CM_EXA_EXAMASSESSMENT_DELETE_EXAMPLANS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] | None:
    """#### At least one of these rights:
    * RIGHT_CM_APP_ENTRANCE_EXAMINATION_PLAN_EXAMINATION
    * RIGHT_CM_EXA_EXAMASSESSMENT_DELETE_EXAMPLANS


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
