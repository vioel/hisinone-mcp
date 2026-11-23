from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cs_sys_rest_generic_exception_response import CsSysRestGenericExceptionResponse
from ...models.fs_res_publication_publication import FsResPublicationPublication
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: FsResPublicationPublication | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/fs/res/publication/{id}/changerequest".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication | None:
    if response.status_code == 200:
        response_200 = FsResPublicationPublication.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = CsSysRestGenericExceptionResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: FsResPublicationPublication | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION_OWN
    * RIGHT_FS_RES_PUBLICATION_CHANGE_PUBLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (FsResPublicationPublication | Unset):  Example: {'pageRange': '17-24', 'parent':
            None, 'access': {'id': 1}, 'projects': [{'id': 14}], 'documentType': {'id': 2},
            'creators': [{'id': 135, 'creatorname': 'Krüger', 'firstname': 'Gudrun', 'sortorder': 1}],
            'researchAreas': [{'id': 9}], 'edition': None, 'title': 'Eine neue Test-Publikation',
            'visibilityValue': {'id': 1}, 'journal': {'id': 5}, 'peerReviewed': {'id': 1},
            'publicationResource': {'id': 1}, 'id': None, 'subjectAreas': [{'id': 206}],
            'releaseYear': 2017, 'textAbstract': 'In der Geschichte der Finanzkrisen lassen sich
            Hinweise auf bestimmte Konstellationen finden, die die Entstehung von Krisen an den
            Finanzmärkten begünstigen. Im vorliegenden Buch werden Vorbedingungen, Auslöser und
            Faktoren beschrieben, für die ein signifikanter Einfluss nachgewiesen werden konnte. Aus
            den Ergebnissen lassen sich Indikatoren für bevorstehende Krisen ableiten, so dass eine
            frühzeitiges Eingreifen möglich wird.', 'conferenceName': None, 'issue': None,
            'languages': [{'id': 12}], 'publicationCreatorType': {'id': 1}, 'publicationType': {'id':
            5}, 'volume': None, 'researchAreasKdsf': [{'id': 60}], 'series': None, 'subtitle':
            'Vorbedingungen, Auslöser, Einflussfaktoren', 'publisher': {'id': 1},
            'qualificationThesis': {'id': 3}, 'commentary': None, 'numberInSeries': None,
            'globalIdentifiers': [{'id': 3, 'lockVersion': 0, 'identifier': '10.1145/2556624.2556639',
            'tablename': 'publication', 'tabpk': 2, 'globalIdentifierType': {'id': 2}}], 'status':
            {'id': 15069}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: FsResPublicationPublication | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION_OWN
    * RIGHT_FS_RES_PUBLICATION_CHANGE_PUBLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (FsResPublicationPublication | Unset):  Example: {'pageRange': '17-24', 'parent':
            None, 'access': {'id': 1}, 'projects': [{'id': 14}], 'documentType': {'id': 2},
            'creators': [{'id': 135, 'creatorname': 'Krüger', 'firstname': 'Gudrun', 'sortorder': 1}],
            'researchAreas': [{'id': 9}], 'edition': None, 'title': 'Eine neue Test-Publikation',
            'visibilityValue': {'id': 1}, 'journal': {'id': 5}, 'peerReviewed': {'id': 1},
            'publicationResource': {'id': 1}, 'id': None, 'subjectAreas': [{'id': 206}],
            'releaseYear': 2017, 'textAbstract': 'In der Geschichte der Finanzkrisen lassen sich
            Hinweise auf bestimmte Konstellationen finden, die die Entstehung von Krisen an den
            Finanzmärkten begünstigen. Im vorliegenden Buch werden Vorbedingungen, Auslöser und
            Faktoren beschrieben, für die ein signifikanter Einfluss nachgewiesen werden konnte. Aus
            den Ergebnissen lassen sich Indikatoren für bevorstehende Krisen ableiten, so dass eine
            frühzeitiges Eingreifen möglich wird.', 'conferenceName': None, 'issue': None,
            'languages': [{'id': 12}], 'publicationCreatorType': {'id': 1}, 'publicationType': {'id':
            5}, 'volume': None, 'researchAreasKdsf': [{'id': 60}], 'series': None, 'subtitle':
            'Vorbedingungen, Auslöser, Einflussfaktoren', 'publisher': {'id': 1},
            'qualificationThesis': {'id': 3}, 'commentary': None, 'numberInSeries': None,
            'globalIdentifiers': [{'id': 3, 'lockVersion': 0, 'identifier': '10.1145/2556624.2556639',
            'tablename': 'publication', 'tabpk': 2, 'globalIdentifierType': {'id': 2}}], 'status':
            {'id': 15069}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: FsResPublicationPublication | Unset = UNSET,
) -> Response[Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication]:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION_OWN
    * RIGHT_FS_RES_PUBLICATION_CHANGE_PUBLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (FsResPublicationPublication | Unset):  Example: {'pageRange': '17-24', 'parent':
            None, 'access': {'id': 1}, 'projects': [{'id': 14}], 'documentType': {'id': 2},
            'creators': [{'id': 135, 'creatorname': 'Krüger', 'firstname': 'Gudrun', 'sortorder': 1}],
            'researchAreas': [{'id': 9}], 'edition': None, 'title': 'Eine neue Test-Publikation',
            'visibilityValue': {'id': 1}, 'journal': {'id': 5}, 'peerReviewed': {'id': 1},
            'publicationResource': {'id': 1}, 'id': None, 'subjectAreas': [{'id': 206}],
            'releaseYear': 2017, 'textAbstract': 'In der Geschichte der Finanzkrisen lassen sich
            Hinweise auf bestimmte Konstellationen finden, die die Entstehung von Krisen an den
            Finanzmärkten begünstigen. Im vorliegenden Buch werden Vorbedingungen, Auslöser und
            Faktoren beschrieben, für die ein signifikanter Einfluss nachgewiesen werden konnte. Aus
            den Ergebnissen lassen sich Indikatoren für bevorstehende Krisen ableiten, so dass eine
            frühzeitiges Eingreifen möglich wird.', 'conferenceName': None, 'issue': None,
            'languages': [{'id': 12}], 'publicationCreatorType': {'id': 1}, 'publicationType': {'id':
            5}, 'volume': None, 'researchAreasKdsf': [{'id': 60}], 'series': None, 'subtitle':
            'Vorbedingungen, Auslöser, Einflussfaktoren', 'publisher': {'id': 1},
            'qualificationThesis': {'id': 3}, 'commentary': None, 'numberInSeries': None,
            'globalIdentifiers': [{'id': 3, 'lockVersion': 0, 'identifier': '10.1145/2556624.2556639',
            'tablename': 'publication', 'tabpk': 2, 'globalIdentifierType': {'id': 2}}], 'status':
            {'id': 15069}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: FsResPublicationPublication | Unset = UNSET,
) -> Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication | None:
    """#### At least one of these rights:
    * RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION,RIGHT_FS_RES_PUBLICATION_EDIT_PUBLICATION_OWN
    * RIGHT_FS_RES_PUBLICATION_CHANGE_PUBLICATION


    **Dieser Service ist nicht freigegeben und kann sich ohne Ankündigung ändern.**

    Args:
        id (int):
        body (FsResPublicationPublication | Unset):  Example: {'pageRange': '17-24', 'parent':
            None, 'access': {'id': 1}, 'projects': [{'id': 14}], 'documentType': {'id': 2},
            'creators': [{'id': 135, 'creatorname': 'Krüger', 'firstname': 'Gudrun', 'sortorder': 1}],
            'researchAreas': [{'id': 9}], 'edition': None, 'title': 'Eine neue Test-Publikation',
            'visibilityValue': {'id': 1}, 'journal': {'id': 5}, 'peerReviewed': {'id': 1},
            'publicationResource': {'id': 1}, 'id': None, 'subjectAreas': [{'id': 206}],
            'releaseYear': 2017, 'textAbstract': 'In der Geschichte der Finanzkrisen lassen sich
            Hinweise auf bestimmte Konstellationen finden, die die Entstehung von Krisen an den
            Finanzmärkten begünstigen. Im vorliegenden Buch werden Vorbedingungen, Auslöser und
            Faktoren beschrieben, für die ein signifikanter Einfluss nachgewiesen werden konnte. Aus
            den Ergebnissen lassen sich Indikatoren für bevorstehende Krisen ableiten, so dass eine
            frühzeitiges Eingreifen möglich wird.', 'conferenceName': None, 'issue': None,
            'languages': [{'id': 12}], 'publicationCreatorType': {'id': 1}, 'publicationType': {'id':
            5}, 'volume': None, 'researchAreasKdsf': [{'id': 60}], 'series': None, 'subtitle':
            'Vorbedingungen, Auslöser, Einflussfaktoren', 'publisher': {'id': 1},
            'qualificationThesis': {'id': 3}, 'commentary': None, 'numberInSeries': None,
            'globalIdentifiers': [{'id': 3, 'lockVersion': 0, 'identifier': '10.1145/2556624.2556639',
            'tablename': 'publication', 'tabpk': 2, 'globalIdentifierType': {'id': 2}}], 'status':
            {'id': 15069}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CsSysRestGenericExceptionResponse | FsResPublicationPublication
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
