from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.cs_sys_upload_configuration_upload_field_validation_rest_controller_batch_feedback_request_rest import (
    CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest,
)
from ...models.post_cs_sys_fileupload_validation_batch_provide_feedback_response_200 import (
    PostCsSysFileuploadValidationBatchProvideFeedbackResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cs/sys/fileupload/validation/batchProvideFeedback",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200 | None:
    if response.status_code == 200:
        response_200 = PostCsSysFileuploadValidationBatchProvideFeedbackResponse200.from_dict(response.json())

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
) -> Response[Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest
            | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200]
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
    body: CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200 | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest
            | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200]:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest
            | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200 | None:
    """#### At least one of these rights:
    * RIGHT_EVERYONE


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        body (CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest
            | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | PostCsSysFileuploadValidationBatchProvideFeedbackResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
