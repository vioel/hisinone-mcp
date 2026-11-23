from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_conference_to_import import (
        FsResPublicationUniversalImportConferenceToImport,
    )
    from ..models.fs_res_publication_universal_import_creator_to_import import (
        FsResPublicationUniversalImportCreatorToImport,
    )
    from ..models.fs_res_publication_universal_import_journal_to_import import (
        FsResPublicationUniversalImportJournalToImport,
    )
    from ..models.fs_res_publication_universal_import_key_word_value import FsResPublicationUniversalImportKeyWordValue
    from ..models.fs_res_publication_universal_import_project_reference import (
        FsResPublicationUniversalImportProjectReference,
    )
    from ..models.fs_res_publication_universal_import_publication_to_import_foreigntext import (
        FsResPublicationUniversalImportPublicationToImportForeigntext,
    )
    from ..models.fs_res_publication_universal_import_publisher_to_import import (
        FsResPublicationUniversalImportPublisherToImport,
    )
    from ..models.fs_res_publication_universal_import_simple_generic_value import (
        FsResPublicationUniversalImportSimpleGenericValue,
    )
    from ..models.fs_res_publication_universal_import_simple_global_identifier import (
        FsResPublicationUniversalImportSimpleGlobalIdentifier,
    )
    from ..models.impl_cs_sys_dynamic_import_items_dynamic_object_item import (
        ImplCsSysDynamicImportItemsDynamicObjectItem,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportPublicationToImport")


@_attrs_define
class FsResPublicationUniversalImportPublicationToImport:
    """
    Attributes:
        field_foreigntext (FsResPublicationUniversalImportPublicationToImportForeigntext | Unset):
        access (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        article_number (str | Unset):
        blog_name (str | Unset):
        commentary (str | Unset):
        conference (FsResPublicationUniversalImportConferenceToImport | Unset):
        creators (list[FsResPublicationUniversalImportCreatorToImport] | Unset):
        document_type (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        dynamic_objects (list[ImplCsSysDynamicImportItemsDynamicObjectItem] | Unset):
        edition (str | Unset):
        global_identifiers (list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset):
        id (int | Unset):
        issue (str | Unset):
        journal (FsResPublicationUniversalImportJournalToImport | Unset):
        key_words (list[FsResPublicationUniversalImportKeyWordValue] | Unset):
        languages (list[FsResPublicationUniversalImportSimpleGenericValue] | Unset):
        number_in_series (str | Unset):
        number_of_pages (int | Unset):
        obj_guid (str | Unset):
        page_range_from (str | Unset):
        page_range_to (str | Unset):
        parent (FsResPublicationUniversalImportPublicationToImport | Unset):
        peer_reviewed_process (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        projects (list[FsResPublicationUniversalImportProjectReference] | Unset):
        publication_creator_type (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        publication_resource (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        publication_resource_type (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        publication_type (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        publisher (FsResPublicationUniversalImportPublisherToImport | Unset):
        qualification_thesis (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        release_year (int | Unset):
        research_areas (list[FsResPublicationUniversalImportSimpleGenericValue] | Unset):
        research_areas_kdsf (list[FsResPublicationUniversalImportSimpleGenericValue] | Unset):
        series (str | Unset):
        status (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        subject_areas (list[FsResPublicationUniversalImportSimpleGenericValue] | Unset):
        subtitle (str | Unset):
        text_abstract (str | Unset):
        title (str | Unset):
        visibility_value (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        volume (str | Unset):
    """

    field_foreigntext: FsResPublicationUniversalImportPublicationToImportForeigntext | Unset = UNSET
    access: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    article_number: str | Unset = UNSET
    blog_name: str | Unset = UNSET
    commentary: str | Unset = UNSET
    conference: FsResPublicationUniversalImportConferenceToImport | Unset = UNSET
    creators: list[FsResPublicationUniversalImportCreatorToImport] | Unset = UNSET
    document_type: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    dynamic_objects: list[ImplCsSysDynamicImportItemsDynamicObjectItem] | Unset = UNSET
    edition: str | Unset = UNSET
    global_identifiers: list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset = UNSET
    id: int | Unset = UNSET
    issue: str | Unset = UNSET
    journal: FsResPublicationUniversalImportJournalToImport | Unset = UNSET
    key_words: list[FsResPublicationUniversalImportKeyWordValue] | Unset = UNSET
    languages: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
    number_in_series: str | Unset = UNSET
    number_of_pages: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    page_range_from: str | Unset = UNSET
    page_range_to: str | Unset = UNSET
    parent: FsResPublicationUniversalImportPublicationToImport | Unset = UNSET
    peer_reviewed_process: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    projects: list[FsResPublicationUniversalImportProjectReference] | Unset = UNSET
    publication_creator_type: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    publication_resource: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    publication_resource_type: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    publication_type: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    publisher: FsResPublicationUniversalImportPublisherToImport | Unset = UNSET
    qualification_thesis: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    release_year: int | Unset = UNSET
    research_areas: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
    research_areas_kdsf: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
    series: str | Unset = UNSET
    status: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    subject_areas: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
    subtitle: str | Unset = UNSET
    text_abstract: str | Unset = UNSET
    title: str | Unset = UNSET
    visibility_value: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    volume: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        article_number = self.article_number

        blog_name = self.blog_name

        commentary = self.commentary

        conference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference, Unset):
            conference = self.conference.to_dict()

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        document_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_type, Unset):
            document_type = self.document_type.to_dict()

        dynamic_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dynamic_objects, Unset):
            dynamic_objects = []
            for dynamic_objects_item_data in self.dynamic_objects:
                dynamic_objects_item = dynamic_objects_item_data.to_dict()
                dynamic_objects.append(dynamic_objects_item)

        edition = self.edition

        global_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_identifiers, Unset):
            global_identifiers = []
            for global_identifiers_item_data in self.global_identifiers:
                global_identifiers_item = global_identifiers_item_data.to_dict()
                global_identifiers.append(global_identifiers_item)

        id = self.id

        issue = self.issue

        journal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.journal, Unset):
            journal = self.journal.to_dict()

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

        number_in_series = self.number_in_series

        number_of_pages = self.number_of_pages

        obj_guid = self.obj_guid

        page_range_from = self.page_range_from

        page_range_to = self.page_range_to

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

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

        subtitle = self.subtitle

        text_abstract = self.text_abstract

        title = self.title

        visibility_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_value, Unset):
            visibility_value = self.visibility_value.to_dict()

        volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if access is not UNSET:
            field_dict["access"] = access
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if blog_name is not UNSET:
            field_dict["blogName"] = blog_name
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if conference is not UNSET:
            field_dict["conference"] = conference
        if creators is not UNSET:
            field_dict["creators"] = creators
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if dynamic_objects is not UNSET:
            field_dict["dynamicObjects"] = dynamic_objects
        if edition is not UNSET:
            field_dict["edition"] = edition
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
        if number_in_series is not UNSET:
            field_dict["numberInSeries"] = number_in_series
        if number_of_pages is not UNSET:
            field_dict["numberOfPages"] = number_of_pages
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if page_range_from is not UNSET:
            field_dict["pageRangeFrom"] = page_range_from
        if page_range_to is not UNSET:
            field_dict["pageRangeTo"] = page_range_to
        if parent is not UNSET:
            field_dict["parent"] = parent
        if peer_reviewed_process is not UNSET:
            field_dict["peerReviewedProcess"] = peer_reviewed_process
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publication_creator_type is not UNSET:
            field_dict["publicationCreatorType"] = publication_creator_type
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
        from ..models.fs_res_publication_universal_import_conference_to_import import (
            FsResPublicationUniversalImportConferenceToImport,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_creator_to_import import (
            FsResPublicationUniversalImportCreatorToImport,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_journal_to_import import (
            FsResPublicationUniversalImportJournalToImport,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_key_word_value import (
            FsResPublicationUniversalImportKeyWordValue,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_project_reference import (
            FsResPublicationUniversalImportProjectReference,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_publication_to_import_foreigntext import (
            FsResPublicationUniversalImportPublicationToImportForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_publisher_to_import import (
            FsResPublicationUniversalImportPublisherToImport,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_simple_generic_value import (
            FsResPublicationUniversalImportSimpleGenericValue,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_simple_global_identifier import (
            FsResPublicationUniversalImportSimpleGlobalIdentifier,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_import_items_dynamic_object_item import (
            ImplCsSysDynamicImportItemsDynamicObjectItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationUniversalImportPublicationToImportForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationUniversalImportPublicationToImportForeigntext.from_dict(
                _field_foreigntext
            )

        _access = d.pop("access", UNSET)
        access: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_access)

        article_number = d.pop("articleNumber", UNSET)

        blog_name = d.pop("blogName", UNSET)

        commentary = d.pop("commentary", UNSET)

        _conference = d.pop("conference", UNSET)
        conference: FsResPublicationUniversalImportConferenceToImport | Unset
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = FsResPublicationUniversalImportConferenceToImport.from_dict(_conference)

        _creators = d.pop("creators", UNSET)
        creators: list[FsResPublicationUniversalImportCreatorToImport] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = FsResPublicationUniversalImportCreatorToImport.from_dict(creators_item_data)

                creators.append(creators_item)

        _document_type = d.pop("documentType", UNSET)
        document_type: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_document_type, Unset):
            document_type = UNSET
        else:
            document_type = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_document_type)

        _dynamic_objects = d.pop("dynamicObjects", UNSET)
        dynamic_objects: list[ImplCsSysDynamicImportItemsDynamicObjectItem] | Unset = UNSET
        if _dynamic_objects is not UNSET:
            dynamic_objects = []
            for dynamic_objects_item_data in _dynamic_objects:
                dynamic_objects_item = ImplCsSysDynamicImportItemsDynamicObjectItem.from_dict(dynamic_objects_item_data)

                dynamic_objects.append(dynamic_objects_item)

        edition = d.pop("edition", UNSET)

        _global_identifiers = d.pop("globalIdentifiers", UNSET)
        global_identifiers: list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset = UNSET
        if _global_identifiers is not UNSET:
            global_identifiers = []
            for global_identifiers_item_data in _global_identifiers:
                global_identifiers_item = FsResPublicationUniversalImportSimpleGlobalIdentifier.from_dict(
                    global_identifiers_item_data
                )

                global_identifiers.append(global_identifiers_item)

        id = d.pop("id", UNSET)

        issue = d.pop("issue", UNSET)

        _journal = d.pop("journal", UNSET)
        journal: FsResPublicationUniversalImportJournalToImport | Unset
        if isinstance(_journal, Unset):
            journal = UNSET
        else:
            journal = FsResPublicationUniversalImportJournalToImport.from_dict(_journal)

        _key_words = d.pop("keyWords", UNSET)
        key_words: list[FsResPublicationUniversalImportKeyWordValue] | Unset = UNSET
        if _key_words is not UNSET:
            key_words = []
            for key_words_item_data in _key_words:
                key_words_item = FsResPublicationUniversalImportKeyWordValue.from_dict(key_words_item_data)

                key_words.append(key_words_item)

        _languages = d.pop("languages", UNSET)
        languages: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
        if _languages is not UNSET:
            languages = []
            for languages_item_data in _languages:
                languages_item = FsResPublicationUniversalImportSimpleGenericValue.from_dict(languages_item_data)

                languages.append(languages_item)

        number_in_series = d.pop("numberInSeries", UNSET)

        number_of_pages = d.pop("numberOfPages", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        page_range_from = d.pop("pageRangeFrom", UNSET)

        page_range_to = d.pop("pageRangeTo", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: FsResPublicationUniversalImportPublicationToImport | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FsResPublicationUniversalImportPublicationToImport.from_dict(_parent)

        _peer_reviewed_process = d.pop("peerReviewedProcess", UNSET)
        peer_reviewed_process: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_peer_reviewed_process, Unset):
            peer_reviewed_process = UNSET
        else:
            peer_reviewed_process = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_peer_reviewed_process)

        _projects = d.pop("projects", UNSET)
        projects: list[FsResPublicationUniversalImportProjectReference] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = FsResPublicationUniversalImportProjectReference.from_dict(projects_item_data)

                projects.append(projects_item)

        _publication_creator_type = d.pop("publicationCreatorType", UNSET)
        publication_creator_type: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_publication_creator_type, Unset):
            publication_creator_type = UNSET
        else:
            publication_creator_type = FsResPublicationUniversalImportSimpleGenericValue.from_dict(
                _publication_creator_type
            )

        _publication_resource = d.pop("publicationResource", UNSET)
        publication_resource: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_publication_resource, Unset):
            publication_resource = UNSET
        else:
            publication_resource = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_publication_resource)

        _publication_resource_type = d.pop("publicationResourceType", UNSET)
        publication_resource_type: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_publication_resource_type, Unset):
            publication_resource_type = UNSET
        else:
            publication_resource_type = FsResPublicationUniversalImportSimpleGenericValue.from_dict(
                _publication_resource_type
            )

        _publication_type = d.pop("publicationType", UNSET)
        publication_type: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_publication_type, Unset):
            publication_type = UNSET
        else:
            publication_type = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_publication_type)

        _publisher = d.pop("publisher", UNSET)
        publisher: FsResPublicationUniversalImportPublisherToImport | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = FsResPublicationUniversalImportPublisherToImport.from_dict(_publisher)

        _qualification_thesis = d.pop("qualificationThesis", UNSET)
        qualification_thesis: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_qualification_thesis, Unset):
            qualification_thesis = UNSET
        else:
            qualification_thesis = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_qualification_thesis)

        release_year = d.pop("releaseYear", UNSET)

        _research_areas = d.pop("researchAreas", UNSET)
        research_areas: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
        if _research_areas is not UNSET:
            research_areas = []
            for research_areas_item_data in _research_areas:
                research_areas_item = FsResPublicationUniversalImportSimpleGenericValue.from_dict(
                    research_areas_item_data
                )

                research_areas.append(research_areas_item)

        _research_areas_kdsf = d.pop("researchAreasKdsf", UNSET)
        research_areas_kdsf: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
        if _research_areas_kdsf is not UNSET:
            research_areas_kdsf = []
            for research_areas_kdsf_item_data in _research_areas_kdsf:
                research_areas_kdsf_item = FsResPublicationUniversalImportSimpleGenericValue.from_dict(
                    research_areas_kdsf_item_data
                )

                research_areas_kdsf.append(research_areas_kdsf_item)

        series = d.pop("series", UNSET)

        _status = d.pop("status", UNSET)
        status: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_status)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[FsResPublicationUniversalImportSimpleGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = FsResPublicationUniversalImportSimpleGenericValue.from_dict(
                    subject_areas_item_data
                )

                subject_areas.append(subject_areas_item)

        subtitle = d.pop("subtitle", UNSET)

        text_abstract = d.pop("textAbstract", UNSET)

        title = d.pop("title", UNSET)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_visibility_value)

        volume = d.pop("volume", UNSET)

        fs_res_publication_universal_import_publication_to_import = cls(
            field_foreigntext=field_foreigntext,
            access=access,
            article_number=article_number,
            blog_name=blog_name,
            commentary=commentary,
            conference=conference,
            creators=creators,
            document_type=document_type,
            dynamic_objects=dynamic_objects,
            edition=edition,
            global_identifiers=global_identifiers,
            id=id,
            issue=issue,
            journal=journal,
            key_words=key_words,
            languages=languages,
            number_in_series=number_in_series,
            number_of_pages=number_of_pages,
            obj_guid=obj_guid,
            page_range_from=page_range_from,
            page_range_to=page_range_to,
            parent=parent,
            peer_reviewed_process=peer_reviewed_process,
            projects=projects,
            publication_creator_type=publication_creator_type,
            publication_resource=publication_resource,
            publication_resource_type=publication_resource_type,
            publication_type=publication_type,
            publisher=publisher,
            qualification_thesis=qualification_thesis,
            release_year=release_year,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            series=series,
            status=status,
            subject_areas=subject_areas,
            subtitle=subtitle,
            text_abstract=text_abstract,
            title=title,
            visibility_value=visibility_value,
            volume=volume,
        )

        fs_res_publication_universal_import_publication_to_import.additional_properties = d
        return fs_res_publication_universal_import_publication_to_import

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
