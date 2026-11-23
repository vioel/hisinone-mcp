from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rm_erp_common_workflow_erp_workflow_operation import RmErpCommonWorkflowErpWorkflowOperation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_type: str,
    use_case_ident: str,
    *,
    user_id: str,
    process_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["userId"] = user_id

    params["processId"] = process_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rm/erp/workflow/onbehalf/{process_type}/{use_case_ident}".format(
            process_type=quote(str(process_type), safe=""),
            use_case_ident=quote(str(use_case_ident), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RmErpCommonWorkflowErpWorkflowOperation | None:
    if response.status_code == 200:
        response_200 = RmErpCommonWorkflowErpWorkflowOperation.from_dict(response.json())

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
) -> Response[Any | RmErpCommonWorkflowErpWorkflowOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_type: str,
    use_case_ident: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    process_id: int | Unset = UNSET,
) -> Response[Any | RmErpCommonWorkflowErpWorkflowOperation]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_COMMON_WORKFLOW_USE_ERP_WORKFLOW


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        process_type (str):
        use_case_ident (str):
        user_id (str):
        process_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RmErpCommonWorkflowErpWorkflowOperation]
    """

    kwargs = _get_kwargs(
        process_type=process_type,
        use_case_ident=use_case_ident,
        user_id=user_id,
        process_id=process_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_type: str,
    use_case_ident: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    process_id: int | Unset = UNSET,
) -> Any | RmErpCommonWorkflowErpWorkflowOperation | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_COMMON_WORKFLOW_USE_ERP_WORKFLOW


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        process_type (str):
        use_case_ident (str):
        user_id (str):
        process_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RmErpCommonWorkflowErpWorkflowOperation
    """

    return sync_detailed(
        process_type=process_type,
        use_case_ident=use_case_ident,
        client=client,
        user_id=user_id,
        process_id=process_id,
    ).parsed


async def asyncio_detailed(
    process_type: str,
    use_case_ident: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    process_id: int | Unset = UNSET,
) -> Response[Any | RmErpCommonWorkflowErpWorkflowOperation]:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_COMMON_WORKFLOW_USE_ERP_WORKFLOW


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        process_type (str):
        use_case_ident (str):
        user_id (str):
        process_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RmErpCommonWorkflowErpWorkflowOperation]
    """

    kwargs = _get_kwargs(
        process_type=process_type,
        use_case_ident=use_case_ident,
        user_id=user_id,
        process_id=process_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_type: str,
    use_case_ident: str,
    *,
    client: AuthenticatedClient,
    user_id: str,
    process_id: int | Unset = UNSET,
) -> Any | RmErpCommonWorkflowErpWorkflowOperation | None:
    """#### At least one of these rights:
    * RIGHT_RM_ERP_COMMON_WORKFLOW_USE_ERP_WORKFLOW


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        process_type (str):
        use_case_ident (str):
        user_id (str):
        process_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RmErpCommonWorkflowErpWorkflowOperation
    """

    return (
        await asyncio_detailed(
            process_type=process_type,
            use_case_ident=use_case_ident,
            client=client,
            user_id=user_id,
            process_id=process_id,
        )
    ).parsed
