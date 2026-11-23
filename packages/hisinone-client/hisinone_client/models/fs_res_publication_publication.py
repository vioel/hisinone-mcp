from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract
    from ..models.fs_res_project_project_obj import FsResProjectProjectObj
    from ..models.fs_res_publication_change_request_publication_change_request import (
        FsResPublicationChangeRequestPublicationChangeRequest,
    )
    from ..models.fs_res_publication_conference import FsResPublicationConference
    from ..models.fs_res_publication_global_identifier import FsResPublicationGlobalIdentifier
    from ..models.fs_res_publication_journal import FsResPublicationJournal
    from ..models.fs_res_publication_publication_creator import FsResPublicationPublicationCreator
    from ..models.fs_res_publication_publication_document_metadata import FsResPublicationPublicationDocumentMetadata
    from ..models.fs_res_publication_publication_foreigntext_type_0 import FsResPublicationPublicationForeigntextType0
    from ..models.fs_res_publication_publication_listviews_type_0 import FsResPublicationPublicationListviewsType0
    from ..models.fs_res_publication_publication_type_value import FsResPublicationPublicationTypeValue
    from ..models.fs_res_publication_publisher import FsResPublicationPublisher
    from ..models.fs_res_research_infrastructure_research_infrastructure import (
        FsResResearchInfrastructureResearchInfrastructure,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResPublicationPublication")


@_attrs_define
class FsResPublicationPublication:
    """
    Example:
        {'pageRange': '17-24', 'parent': None, 'access': {'id': 1}, 'projects': [{'id': 14}], 'documentType': {'id': 2},
            'creators': [{'id': 135, 'creatorname': 'Krüger', 'firstname': 'Gudrun', 'sortorder': 1}], 'researchAreas':
            [{'id': 9}], 'edition': None, 'title': 'Eine neue Test-Publikation', 'visibilityValue': {'id': 1}, 'journal':
            {'id': 5}, 'peerReviewed': {'id': 1}, 'publicationResource': {'id': 1}, 'id': None, 'subjectAreas': [{'id':
            206}], 'releaseYear': 2017, 'textAbstract': 'In der Geschichte der Finanzkrisen lassen sich Hinweise auf
            bestimmte Konstellationen finden, die die Entstehung von Krisen an den Finanzmärkten begünstigen. Im
            vorliegenden Buch werden Vorbedingungen, Auslöser und Faktoren beschrieben, für die ein signifikanter Einfluss
            nachgewiesen werden konnte. Aus den Ergebnissen lassen sich Indikatoren für bevorstehende Krisen ableiten, so
            dass eine frühzeitiges Eingreifen möglich wird.', 'conferenceName': None, 'issue': None, 'languages': [{'id':
            12}], 'publicationCreatorType': {'id': 1}, 'publicationType': {'id': 5}, 'volume': None, 'researchAreasKdsf':
            [{'id': 60}], 'series': None, 'subtitle': 'Vorbedingungen, Auslöser, Einflussfaktoren', 'publisher': {'id': 1},
            'qualificationThesis': {'id': 3}, 'commentary': None, 'numberInSeries': None, 'globalIdentifiers': [{'id': 3,
            'lockVersion': 0, 'identifier': '10.1145/2556624.2556639', 'tablename': 'publication', 'tabpk': 2,
            'globalIdentifierType': {'id': 2}}], 'status': {'id': 15069}}

    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResPublicationPublicationForeigntextType0 | None | Unset):
        access (CsSysValueGenericValue | Unset):
        access_after_embargo_date (CsSysValueGenericValue | None | Unset):
        article_number (None | str | Unset):
        blog_name (None | str | Unset):
        change_request (FsResPublicationChangeRequestPublicationChangeRequest | None | Unset):
        citations (list[list[str]] | Unset):
        commentary (None | str | Unset):
        conference (FsResPublicationConference | None | Unset):
        conference_name (None | str | Unset):
        creators (list[FsResPublicationPublicationCreator] | Unset):
        defaulttext (str | Unset):
        document_type (CsSysValueGenericValue | Unset):
        edition (None | str | Unset):
        embargo_date (int | None | Unset):
        funding_programs (list[FsResFinanceResearchContract] | Unset):
        global_identifiers (list[FsResPublicationGlobalIdentifier] | Unset):
        id (int | Unset):
        issue (None | str | Unset):
        journal (FsResPublicationJournal | None | Unset):
        key_words (list[CsSysValueGenericValue] | Unset):
        languages (list[ImplFsResLanguageValue] | Unset):
        license_ (CsSysValueGenericValue | None | Unset):
        listviews (FsResPublicationPublicationListviewsType0 | None | Unset):
        lock_version (int | Unset):
        number_in_series (None | str | Unset):
        number_of_pages (int | None | Unset):
        obj_guid (str | Unset):
        page_range (None | str | Unset):
        page_range_from (None | str | Unset):
        page_range_to (None | str | Unset):
        parent (FsResPublicationPublication | None | Unset):
        parents (list[FsResPublicationPublication] | Unset):
        peer_reviewed (CsSysValueGenericValue | Unset):
        peer_reviewed_process (CsSysValueGenericValue | Unset):
        projects (list[FsResProjectProjectObj] | Unset):
        publication_creator_type (CsSysValueGenericValue | Unset):
        publication_documents (list[FsResPublicationPublicationDocumentMetadata] | Unset):
        publication_resource (CsSysValueGenericValue | Unset):
        publication_resource_type (CsSysValueGenericValue | Unset):
        publication_type (FsResPublicationPublicationTypeValue | Unset):
        publisher (FsResPublicationPublisher | Unset):
        qualification_thesis (CsSysValueGenericValue | Unset):
        release_year (int | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        research_infrastructures (list[FsResResearchInfrastructureResearchInfrastructure] | Unset):
        series (None | str | Unset):
        status (CsSysValueGenericValue | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        subtitle (None | str | Unset):
        text_abstract (None | str | Unset):
        title (str | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
        volume (None | str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResPublicationPublicationForeigntextType0 | None | Unset = UNSET
    access: CsSysValueGenericValue | Unset = UNSET
    access_after_embargo_date: CsSysValueGenericValue | None | Unset = UNSET
    article_number: None | str | Unset = UNSET
    blog_name: None | str | Unset = UNSET
    change_request: FsResPublicationChangeRequestPublicationChangeRequest | None | Unset = UNSET
    citations: list[list[str]] | Unset = UNSET
    commentary: None | str | Unset = UNSET
    conference: FsResPublicationConference | None | Unset = UNSET
    conference_name: None | str | Unset = UNSET
    creators: list[FsResPublicationPublicationCreator] | Unset = UNSET
    defaulttext: str | Unset = UNSET
    document_type: CsSysValueGenericValue | Unset = UNSET
    edition: None | str | Unset = UNSET
    embargo_date: int | None | Unset = UNSET
    funding_programs: list[FsResFinanceResearchContract] | Unset = UNSET
    global_identifiers: list[FsResPublicationGlobalIdentifier] | Unset = UNSET
    id: int | Unset = UNSET
    issue: None | str | Unset = UNSET
    journal: FsResPublicationJournal | None | Unset = UNSET
    key_words: list[CsSysValueGenericValue] | Unset = UNSET
    languages: list[ImplFsResLanguageValue] | Unset = UNSET
    license_: CsSysValueGenericValue | None | Unset = UNSET
    listviews: FsResPublicationPublicationListviewsType0 | None | Unset = UNSET
    lock_version: int | Unset = UNSET
    number_in_series: None | str | Unset = UNSET
    number_of_pages: int | None | Unset = UNSET
    obj_guid: str | Unset = UNSET
    page_range: None | str | Unset = UNSET
    page_range_from: None | str | Unset = UNSET
    page_range_to: None | str | Unset = UNSET
    parent: FsResPublicationPublication | None | Unset = UNSET
    parents: list[FsResPublicationPublication] | Unset = UNSET
    peer_reviewed: CsSysValueGenericValue | Unset = UNSET
    peer_reviewed_process: CsSysValueGenericValue | Unset = UNSET
    projects: list[FsResProjectProjectObj] | Unset = UNSET
    publication_creator_type: CsSysValueGenericValue | Unset = UNSET
    publication_documents: list[FsResPublicationPublicationDocumentMetadata] | Unset = UNSET
    publication_resource: CsSysValueGenericValue | Unset = UNSET
    publication_resource_type: CsSysValueGenericValue | Unset = UNSET
    publication_type: FsResPublicationPublicationTypeValue | Unset = UNSET
    publisher: FsResPublicationPublisher | Unset = UNSET
    qualification_thesis: CsSysValueGenericValue | Unset = UNSET
    release_year: int | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    research_infrastructures: list[FsResResearchInfrastructureResearchInfrastructure] | Unset = UNSET
    series: None | str | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    subtitle: None | str | Unset = UNSET
    text_abstract: None | str | Unset = UNSET
    title: str | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    volume: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_change_request_publication_change_request import (
            FsResPublicationChangeRequestPublicationChangeRequest,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_conference import FsResPublicationConference  # noqa: PLC0415
        from ..models.fs_res_publication_journal import FsResPublicationJournal  # noqa: PLC0415
        from ..models.fs_res_publication_publication_foreigntext_type_0 import (
            FsResPublicationPublicationForeigntextType0,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_publication_listviews_type_0 import FsResPublicationPublicationListviewsType0  # noqa: PLC0415

        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResPublicationPublicationForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        access_after_embargo_date: dict[str, Any] | None | Unset
        if isinstance(self.access_after_embargo_date, Unset):
            access_after_embargo_date = UNSET
        elif isinstance(self.access_after_embargo_date, CsSysValueGenericValue):
            access_after_embargo_date = self.access_after_embargo_date.to_dict()
        else:
            access_after_embargo_date = self.access_after_embargo_date

        article_number: None | str | Unset
        if isinstance(self.article_number, Unset):
            article_number = UNSET
        else:
            article_number = self.article_number

        blog_name: None | str | Unset
        if isinstance(self.blog_name, Unset):
            blog_name = UNSET
        else:
            blog_name = self.blog_name

        change_request: dict[str, Any] | None | Unset
        if isinstance(self.change_request, Unset):
            change_request = UNSET
        elif isinstance(self.change_request, FsResPublicationChangeRequestPublicationChangeRequest):
            change_request = self.change_request.to_dict()
        else:
            change_request = self.change_request

        citations: list[list[str]] | Unset = UNSET
        if not isinstance(self.citations, Unset):
            citations = []
            for citations_item_data in self.citations:
                citations_item = citations_item_data

                citations.append(citations_item)

        commentary: None | str | Unset
        if isinstance(self.commentary, Unset):
            commentary = UNSET
        else:
            commentary = self.commentary

        conference: dict[str, Any] | None | Unset
        if isinstance(self.conference, Unset):
            conference = UNSET
        elif isinstance(self.conference, FsResPublicationConference):
            conference = self.conference.to_dict()
        else:
            conference = self.conference

        conference_name: None | str | Unset
        if isinstance(self.conference_name, Unset):
            conference_name = UNSET
        else:
            conference_name = self.conference_name

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        defaulttext = self.defaulttext

        document_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.to_dict()

        edition: None | str | Unset
        if isinstance(self.edition, Unset):
            edition = UNSET
        else:
            edition = self.edition

        embargo_date: int | None | Unset
        if isinstance(self.embargo_date, Unset):
            embargo_date = UNSET
        else:
            embargo_date = self.embargo_date

        funding_programs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.funding_programs, Unset):
            funding_programs = []
            for funding_programs_item_data in self.funding_programs:
                funding_programs_item = funding_programs_item_data.to_dict()
                funding_programs.append(funding_programs_item)

        global_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_identifiers, Unset):
            global_identifiers = []
            for global_identifiers_item_data in self.global_identifiers:
                global_identifiers_item = global_identifiers_item_data.to_dict()
                global_identifiers.append(global_identifiers_item)

        id = self.id

        issue: None | str | Unset
        if isinstance(self.issue, Unset):
            issue = UNSET
        else:
            issue = self.issue

        journal: dict[str, Any] | None | Unset
        if isinstance(self.journal, Unset):
            journal = UNSET
        elif isinstance(self.journal, FsResPublicationJournal):
            journal = self.journal.to_dict()
        else:
            journal = self.journal

        key_words: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_words, Unset):
            key_words = []
            for key_words_item_data in self.key_words:
                key_words_item = key_words_item_data.to_dict()
                key_words.append(key_words_item)

        languages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()
                languages.append(languages_item)

        license_: dict[str, Any] | None | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        elif isinstance(self.license_, CsSysValueGenericValue):
            license_ = self.license_.to_dict()
        else:
            license_ = self.license_

        listviews: dict[str, Any] | None | Unset
        if isinstance(self.listviews, Unset):
            listviews = UNSET
        elif isinstance(self.listviews, FsResPublicationPublicationListviewsType0):
            listviews = self.listviews.to_dict()
        else:
            listviews = self.listviews

        lock_version = self.lock_version

        number_in_series: None | str | Unset
        if isinstance(self.number_in_series, Unset):
            number_in_series = UNSET
        else:
            number_in_series = self.number_in_series

        number_of_pages: int | None | Unset
        if isinstance(self.number_of_pages, Unset):
            number_of_pages = UNSET
        else:
            number_of_pages = self.number_of_pages

        obj_guid = self.obj_guid

        page_range: None | str | Unset
        if isinstance(self.page_range, Unset):
            page_range = UNSET
        else:
            page_range = self.page_range

        page_range_from: None | str | Unset
        if isinstance(self.page_range_from, Unset):
            page_range_from = UNSET
        else:
            page_range_from = self.page_range_from

        page_range_to: None | str | Unset
        if isinstance(self.page_range_to, Unset):
            page_range_to = UNSET
        else:
            page_range_to = self.page_range_to

        parent: dict[str, Any] | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, FsResPublicationPublication):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        parents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()
                parents.append(parents_item)

        peer_reviewed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.peer_reviewed, Unset):
            peer_reviewed = self.peer_reviewed.to_dict()

        peer_reviewed_process: dict[str, Any] | Unset = UNSET
        if not isinstance(self.peer_reviewed_process, Unset):
            peer_reviewed_process = self.peer_reviewed_process.to_dict()

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        publication_creator_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publication_creator_type, Unset):
            publication_creator_type = self.publication_creator_type.to_dict()

        publication_documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publication_documents, Unset):
            publication_documents = []
            for publication_documents_item_data in self.publication_documents:
                publication_documents_item = publication_documents_item_data.to_dict()
                publication_documents.append(publication_documents_item)

        publication_resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publication_resource, Unset):
            publication_resource = self.publication_resource.to_dict()

        publication_resource_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publication_resource_type, Unset):
            publication_resource_type = self.publication_resource_type.to_dict()

        publication_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publication_type, Unset):
            publication_type = self.publication_type.to_dict()

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        qualification_thesis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qualification_thesis, Unset):
            qualification_thesis = self.qualification_thesis.to_dict()

        release_year = self.release_year

        research_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_areas, Unset):
            research_areas = []
            for research_areas_item_data in self.research_areas:
                research_areas_item = research_areas_item_data.to_dict()
                research_areas.append(research_areas_item)

        research_areas_kdsf: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_areas_kdsf, Unset):
            research_areas_kdsf = []
            for research_areas_kdsf_item_data in self.research_areas_kdsf:
                research_areas_kdsf_item = research_areas_kdsf_item_data.to_dict()
                research_areas_kdsf.append(research_areas_kdsf_item)

        research_infrastructures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_infrastructures, Unset):
            research_infrastructures = []
            for research_infrastructures_item_data in self.research_infrastructures:
                research_infrastructures_item = research_infrastructures_item_data.to_dict()
                research_infrastructures.append(research_infrastructures_item)

        series: None | str | Unset
        if isinstance(self.series, Unset):
            series = UNSET
        else:
            series = self.series

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        subtitle: None | str | Unset
        if isinstance(self.subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = self.subtitle

        text_abstract: None | str | Unset
        if isinstance(self.text_abstract, Unset):
            text_abstract = UNSET
        else:
            text_abstract = self.text_abstract

        title = self.title

        visibility_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_value, Unset):
            visibility_value = self.visibility_value.to_dict()

        volume: None | str | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if access is not UNSET:
            field_dict["access"] = access
        if access_after_embargo_date is not UNSET:
            field_dict["accessAfterEmbargoDate"] = access_after_embargo_date
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if blog_name is not UNSET:
            field_dict["blogName"] = blog_name
        if change_request is not UNSET:
            field_dict["changeRequest"] = change_request
        if citations is not UNSET:
            field_dict["citations"] = citations
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if conference is not UNSET:
            field_dict["conference"] = conference
        if conference_name is not UNSET:
            field_dict["conferenceName"] = conference_name
        if creators is not UNSET:
            field_dict["creators"] = creators
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if edition is not UNSET:
            field_dict["edition"] = edition
        if embargo_date is not UNSET:
            field_dict["embargoDate"] = embargo_date
        if funding_programs is not UNSET:
            field_dict["fundingPrograms"] = funding_programs
        if global_identifiers is not UNSET:
            field_dict["globalIdentifiers"] = global_identifiers
        if id is not UNSET:
            field_dict["id"] = id
        if issue is not UNSET:
            field_dict["issue"] = issue
        if journal is not UNSET:
            field_dict["journal"] = journal
        if key_words is not UNSET:
            field_dict["keyWords"] = key_words
        if languages is not UNSET:
            field_dict["languages"] = languages
        if license_ is not UNSET:
            field_dict["license"] = license_
        if listviews is not UNSET:
            field_dict["listviews"] = listviews
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if number_in_series is not UNSET:
            field_dict["numberInSeries"] = number_in_series
        if number_of_pages is not UNSET:
            field_dict["numberOfPages"] = number_of_pages
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if page_range is not UNSET:
            field_dict["pageRange"] = page_range
        if page_range_from is not UNSET:
            field_dict["pageRangeFrom"] = page_range_from
        if page_range_to is not UNSET:
            field_dict["pageRangeTo"] = page_range_to
        if parent is not UNSET:
            field_dict["parent"] = parent
        if parents is not UNSET:
            field_dict["parents"] = parents
        if peer_reviewed is not UNSET:
            field_dict["peerReviewed"] = peer_reviewed
        if peer_reviewed_process is not UNSET:
            field_dict["peerReviewedProcess"] = peer_reviewed_process
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publication_creator_type is not UNSET:
            field_dict["publicationCreatorType"] = publication_creator_type
        if publication_documents is not UNSET:
            field_dict["publicationDocuments"] = publication_documents
        if publication_resource is not UNSET:
            field_dict["publicationResource"] = publication_resource
        if publication_resource_type is not UNSET:
            field_dict["publicationResourceType"] = publication_resource_type
        if publication_type is not UNSET:
            field_dict["publicationType"] = publication_type
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if qualification_thesis is not UNSET:
            field_dict["qualificationThesis"] = qualification_thesis
        if release_year is not UNSET:
            field_dict["releaseYear"] = release_year
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if research_infrastructures is not UNSET:
            field_dict["researchInfrastructures"] = research_infrastructures
        if series is not UNSET:
            field_dict["series"] = series
        if status is not UNSET:
            field_dict["status"] = status
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if text_abstract is not UNSET:
            field_dict["textAbstract"] = text_abstract
        if title is not UNSET:
            field_dict["title"] = title
        if visibility_value is not UNSET:
            field_dict["visibilityValue"] = visibility_value
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract  # noqa: PLC0415
        from ..models.fs_res_project_project_obj import FsResProjectProjectObj  # noqa: PLC0415
        from ..models.fs_res_publication_change_request_publication_change_request import (
            FsResPublicationChangeRequestPublicationChangeRequest,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_conference import FsResPublicationConference  # noqa: PLC0415
        from ..models.fs_res_publication_global_identifier import FsResPublicationGlobalIdentifier  # noqa: PLC0415
        from ..models.fs_res_publication_journal import FsResPublicationJournal  # noqa: PLC0415
        from ..models.fs_res_publication_publication_creator import FsResPublicationPublicationCreator  # noqa: PLC0415
        from ..models.fs_res_publication_publication_document_metadata import (
            FsResPublicationPublicationDocumentMetadata,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_publication_foreigntext_type_0 import (
            FsResPublicationPublicationForeigntextType0,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_publication_listviews_type_0 import FsResPublicationPublicationListviewsType0  # noqa: PLC0415
        from ..models.fs_res_publication_publication_type_value import FsResPublicationPublicationTypeValue  # noqa: PLC0415
        from ..models.fs_res_publication_publisher import FsResPublicationPublisher  # noqa: PLC0415
        from ..models.fs_res_research_infrastructure_research_infrastructure import (
            FsResResearchInfrastructureResearchInfrastructure,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        def _parse_field_foreigntext(data: object) -> FsResPublicationPublicationForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResPublicationPublicationForeigntextType0.from_dict(cast(dict[str, Any], data))

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        _access = d.pop("access", UNSET)
        access: CsSysValueGenericValue | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = CsSysValueGenericValue.from_dict(_access)

        def _parse_access_after_embargo_date(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            access_after_embargo_date_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return access_after_embargo_date_type_0

        access_after_embargo_date = _parse_access_after_embargo_date(d.pop("accessAfterEmbargoDate", UNSET))

        def _parse_article_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        article_number = _parse_article_number(d.pop("articleNumber", UNSET))

        def _parse_blog_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blog_name = _parse_blog_name(d.pop("blogName", UNSET))

        def _parse_change_request(data: object) -> FsResPublicationChangeRequestPublicationChangeRequest | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            change_request_type_0 = FsResPublicationChangeRequestPublicationChangeRequest.from_dict(
                cast(dict[str, Any], data)
            )

            return change_request_type_0

        change_request = _parse_change_request(d.pop("changeRequest", UNSET))

        _citations = d.pop("citations", UNSET)
        citations: list[list[str]] | Unset = UNSET
        if _citations is not UNSET:
            citations = []
            for citations_item_data in _citations:
                citations_item = cast(list[str], citations_item_data)

                citations.append(citations_item)

        def _parse_commentary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commentary = _parse_commentary(d.pop("commentary", UNSET))

        def _parse_conference(data: object) -> FsResPublicationConference | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            conference_type_0 = FsResPublicationConference.from_dict(cast(dict[str, Any], data))

            return conference_type_0

        conference = _parse_conference(d.pop("conference", UNSET))

        def _parse_conference_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conference_name = _parse_conference_name(d.pop("conferenceName", UNSET))

        _creators = d.pop("creators", UNSET)
        creators: list[FsResPublicationPublicationCreator] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = FsResPublicationPublicationCreator.from_dict(creators_item_data)

                creators.append(creators_item)

        defaulttext = d.pop("defaulttext", UNSET)

        _document_type = d.pop("documentType", UNSET)
        document_type: CsSysValueGenericValue | Unset
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = CsSysValueGenericValue.from_dict(_document_type)

        def _parse_edition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edition = _parse_edition(d.pop("edition", UNSET))

        def _parse_embargo_date(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        embargo_date = _parse_embargo_date(d.pop("embargoDate", UNSET))

        _funding_programs = d.pop("fundingPrograms", UNSET)
        funding_programs: list[FsResFinanceResearchContract] | Unset = UNSET
        if _funding_programs is not UNSET:
            funding_programs = []
            for funding_programs_item_data in _funding_programs:
                funding_programs_item = FsResFinanceResearchContract.from_dict(funding_programs_item_data)

                funding_programs.append(funding_programs_item)

        _global_identifiers = d.pop("globalIdentifiers", UNSET)
        global_identifiers: list[FsResPublicationGlobalIdentifier] | Unset = UNSET
        if _global_identifiers is not UNSET:
            global_identifiers = []
            for global_identifiers_item_data in _global_identifiers:
                global_identifiers_item = FsResPublicationGlobalIdentifier.from_dict(global_identifiers_item_data)

                global_identifiers.append(global_identifiers_item)

        id = d.pop("id", UNSET)

        def _parse_issue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issue = _parse_issue(d.pop("issue", UNSET))

        def _parse_journal(data: object) -> FsResPublicationJournal | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            journal_type_0 = FsResPublicationJournal.from_dict(cast(dict[str, Any], data))

            return journal_type_0

        journal = _parse_journal(d.pop("journal", UNSET))

        _key_words = d.pop("keyWords", UNSET)
        key_words: list[CsSysValueGenericValue] | Unset = UNSET
        if _key_words is not UNSET:
            key_words = []
            for key_words_item_data in _key_words:
                key_words_item = CsSysValueGenericValue.from_dict(key_words_item_data)

                key_words.append(key_words_item)

        _languages = d.pop("languages", UNSET)
        languages: list[ImplFsResLanguageValue] | Unset = UNSET
        if _languages is not UNSET:
            languages = []
            for languages_item_data in _languages:
                languages_item = ImplFsResLanguageValue.from_dict(languages_item_data)

                languages.append(languages_item)

        def _parse_license_(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            license_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return license_type_0

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_listviews(data: object) -> FsResPublicationPublicationListviewsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            listviews_type_0 = FsResPublicationPublicationListviewsType0.from_dict(cast(dict[str, Any], data))

            return listviews_type_0

        listviews = _parse_listviews(d.pop("listviews", UNSET))

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_number_in_series(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_in_series = _parse_number_in_series(d.pop("numberInSeries", UNSET))

        def _parse_number_of_pages(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_pages = _parse_number_of_pages(d.pop("numberOfPages", UNSET))

        obj_guid = d.pop("objGuid", UNSET)

        def _parse_page_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_range = _parse_page_range(d.pop("pageRange", UNSET))

        def _parse_page_range_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_range_from = _parse_page_range_from(d.pop("pageRangeFrom", UNSET))

        def _parse_page_range_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_range_to = _parse_page_range_to(d.pop("pageRangeTo", UNSET))

        def _parse_parent(data: object) -> FsResPublicationPublication | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            parent_type_0 = FsResPublicationPublication.from_dict(cast(dict[str, Any], data))

            return parent_type_0

        parent = _parse_parent(d.pop("parent", UNSET))

        _parents = d.pop("parents", UNSET)
        parents: list[FsResPublicationPublication] | Unset = UNSET
        if _parents is not UNSET:
            parents = []
            for parents_item_data in _parents:
                parents_item = FsResPublicationPublication.from_dict(parents_item_data)

                parents.append(parents_item)

        _peer_reviewed = d.pop("peerReviewed", UNSET)
        peer_reviewed: CsSysValueGenericValue | Unset
        if isinstance(_peer_reviewed, Unset):
            peer_reviewed = UNSET
        else:
            peer_reviewed = CsSysValueGenericValue.from_dict(_peer_reviewed)

        _peer_reviewed_process = d.pop("peerReviewedProcess", UNSET)
        peer_reviewed_process: CsSysValueGenericValue | Unset
        if isinstance(_peer_reviewed_process, Unset):
            peer_reviewed_process = UNSET
        else:
            peer_reviewed_process = CsSysValueGenericValue.from_dict(_peer_reviewed_process)

        _projects = d.pop("projects", UNSET)
        projects: list[FsResProjectProjectObj] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = FsResProjectProjectObj.from_dict(projects_item_data)

                projects.append(projects_item)

        _publication_creator_type = d.pop("publicationCreatorType", UNSET)
        publication_creator_type: CsSysValueGenericValue | Unset
        if isinstance(_publication_creator_type, Unset):
            publication_creator_type = UNSET
        else:
            publication_creator_type = CsSysValueGenericValue.from_dict(_publication_creator_type)

        _publication_documents = d.pop("publicationDocuments", UNSET)
        publication_documents: list[FsResPublicationPublicationDocumentMetadata] | Unset = UNSET
        if _publication_documents is not UNSET:
            publication_documents = []
            for publication_documents_item_data in _publication_documents:
                publication_documents_item = FsResPublicationPublicationDocumentMetadata.from_dict(
                    publication_documents_item_data
                )

                publication_documents.append(publication_documents_item)

        _publication_resource = d.pop("publicationResource", UNSET)
        publication_resource: CsSysValueGenericValue | Unset
        if isinstance(_publication_resource, Unset):
            publication_resource = UNSET
        else:
            publication_resource = CsSysValueGenericValue.from_dict(_publication_resource)

        _publication_resource_type = d.pop("publicationResourceType", UNSET)
        publication_resource_type: CsSysValueGenericValue | Unset
        if isinstance(_publication_resource_type, Unset):
            publication_resource_type = UNSET
        else:
            publication_resource_type = CsSysValueGenericValue.from_dict(_publication_resource_type)

        _publication_type = d.pop("publicationType", UNSET)
        publication_type: FsResPublicationPublicationTypeValue | Unset
        if isinstance(_publication_type, Unset):
            publication_type = UNSET
        else:
            publication_type = FsResPublicationPublicationTypeValue.from_dict(_publication_type)

        _publisher = d.pop("publisher", UNSET)
        publisher: FsResPublicationPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = FsResPublicationPublisher.from_dict(_publisher)

        _qualification_thesis = d.pop("qualificationThesis", UNSET)
        qualification_thesis: CsSysValueGenericValue | Unset
        if isinstance(_qualification_thesis, Unset):
            qualification_thesis = UNSET
        else:
            qualification_thesis = CsSysValueGenericValue.from_dict(_qualification_thesis)

        release_year = d.pop("releaseYear", UNSET)

        _research_areas = d.pop("researchAreas", UNSET)
        research_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _research_areas is not UNSET:
            research_areas = []
            for research_areas_item_data in _research_areas:
                research_areas_item = CsSysValueGenericValue.from_dict(research_areas_item_data)

                research_areas.append(research_areas_item)

        _research_areas_kdsf = d.pop("researchAreasKdsf", UNSET)
        research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
        if _research_areas_kdsf is not UNSET:
            research_areas_kdsf = []
            for research_areas_kdsf_item_data in _research_areas_kdsf:
                research_areas_kdsf_item = CsSysValueGenericValue.from_dict(research_areas_kdsf_item_data)

                research_areas_kdsf.append(research_areas_kdsf_item)

        _research_infrastructures = d.pop("researchInfrastructures", UNSET)
        research_infrastructures: list[FsResResearchInfrastructureResearchInfrastructure] | Unset = UNSET
        if _research_infrastructures is not UNSET:
            research_infrastructures = []
            for research_infrastructures_item_data in _research_infrastructures:
                research_infrastructures_item = FsResResearchInfrastructureResearchInfrastructure.from_dict(
                    research_infrastructures_item_data
                )

                research_infrastructures.append(research_infrastructures_item)

        def _parse_series(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        series = _parse_series(d.pop("series", UNSET))

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        def _parse_subtitle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subtitle = _parse_subtitle(d.pop("subtitle", UNSET))

        def _parse_text_abstract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text_abstract = _parse_text_abstract(d.pop("textAbstract", UNSET))

        title = d.pop("title", UNSET)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        def _parse_volume(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        fs_res_publication_publication = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            access=access,
            access_after_embargo_date=access_after_embargo_date,
            article_number=article_number,
            blog_name=blog_name,
            change_request=change_request,
            citations=citations,
            commentary=commentary,
            conference=conference,
            conference_name=conference_name,
            creators=creators,
            defaulttext=defaulttext,
            document_type=document_type,
            edition=edition,
            embargo_date=embargo_date,
            funding_programs=funding_programs,
            global_identifiers=global_identifiers,
            id=id,
            issue=issue,
            journal=journal,
            key_words=key_words,
            languages=languages,
            license_=license_,
            listviews=listviews,
            lock_version=lock_version,
            number_in_series=number_in_series,
            number_of_pages=number_of_pages,
            obj_guid=obj_guid,
            page_range=page_range,
            page_range_from=page_range_from,
            page_range_to=page_range_to,
            parent=parent,
            parents=parents,
            peer_reviewed=peer_reviewed,
            peer_reviewed_process=peer_reviewed_process,
            projects=projects,
            publication_creator_type=publication_creator_type,
            publication_documents=publication_documents,
            publication_resource=publication_resource,
            publication_resource_type=publication_resource_type,
            publication_type=publication_type,
            publisher=publisher,
            qualification_thesis=qualification_thesis,
            release_year=release_year,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            research_infrastructures=research_infrastructures,
            series=series,
            status=status,
            subject_areas=subject_areas,
            subtitle=subtitle,
            text_abstract=text_abstract,
            title=title,
            visibility_value=visibility_value,
            volume=volume,
        )

        fs_res_publication_publication.additional_properties = d
        return fs_res_publication_publication

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
