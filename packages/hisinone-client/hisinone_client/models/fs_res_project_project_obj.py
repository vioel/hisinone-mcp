from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract
    from ..models.fs_res_prize_nomination_nomination import FsResPrizeNominationNomination
    from ..models.fs_res_project_project_member_position import FsResProjectProjectMemberPosition
    from ..models.fs_res_project_project_obj_foreigntext_type_0 import FsResProjectProjectObjForeigntextType0
    from ..models.fs_res_project_project_obj_listviews_type_0 import FsResProjectProjectObjListviewsType0
    from ..models.fs_res_project_project_orgunit import FsResProjectProjectOrgunit
    from ..models.fs_res_publication_publication import FsResPublicationPublication
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResProjectProjectObj")


@_attrs_define
class FsResProjectProjectObj:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | None | Unset):
        field_foreigntext (FsResProjectProjectObjForeigntextType0 | None | Unset):
        can_view_original_data (CsSysValueGenericValue | Unset):
        commentary (None | str | Unset):
        cv_id (int | Unset):
        cv_lock_version (int | Unset):
        defaulttext (str | Unset):
        documents (list[CsSysUploadConfigurationHisUploadFile] | None | Unset):
        enddate (int | Unset):
        funding_programs (list[FsResFinanceResearchContract] | None | Unset):
        id (int | Unset):
        is_economical (CsSysValueGenericValue | None | Unset):
        is_pseudonymized (CsSysValueGenericValue | None | Unset):
        kdsf_category (CsSysValueGenericValue | None | Unset):
        kdsf_category_details (bool | Unset):
        key_words (list[CsSysValueGenericValue] | Unset):
        language (ImplFsResLanguageValue | Unset):
        listviews (FsResProjectProjectObjListviewsType0 | None | Unset):
        lock_version (int | Unset):
        longtext (None | str | Unset):
        members (list[FsResProjectProjectMemberPosition] | Unset):
        nominations (list[FsResPrizeNominationNomination] | None | Unset):
        obj_guid (str | Unset):
        organizations (list[FsResProjectProjectOrgunit] | Unset):
        parent (FsResProjectProjectObj | None | Unset):
        predecessor (FsResProjectProjectObj | None | Unset):
        project_objective (CsSysValueGenericValue | Unset):
        project_status (CsSysValueGenericValue | Unset):
        project_type (CsSysValueGenericValue | None | Unset):
        pseudonymized_research_partner (None | str | Unset):
        pseudonymized_title (None | str | Unset):
        publications (list[FsResPublicationPublication] | None | Unset):
        reference_number (None | str | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        shorttext (None | str | Unset):
        startdate (int | Unset):
        still_available_details (bool | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        uniquename (None | str | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | None | Unset = UNSET
    field_foreigntext: FsResProjectProjectObjForeigntextType0 | None | Unset = UNSET
    can_view_original_data: CsSysValueGenericValue | Unset = UNSET
    commentary: None | str | Unset = UNSET
    cv_id: int | Unset = UNSET
    cv_lock_version: int | Unset = UNSET
    defaulttext: str | Unset = UNSET
    documents: list[CsSysUploadConfigurationHisUploadFile] | None | Unset = UNSET
    enddate: int | Unset = UNSET
    funding_programs: list[FsResFinanceResearchContract] | None | Unset = UNSET
    id: int | Unset = UNSET
    is_economical: CsSysValueGenericValue | None | Unset = UNSET
    is_pseudonymized: CsSysValueGenericValue | None | Unset = UNSET
    kdsf_category: CsSysValueGenericValue | None | Unset = UNSET
    kdsf_category_details: bool | Unset = UNSET
    key_words: list[CsSysValueGenericValue] | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    listviews: FsResProjectProjectObjListviewsType0 | None | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: None | str | Unset = UNSET
    members: list[FsResProjectProjectMemberPosition] | Unset = UNSET
    nominations: list[FsResPrizeNominationNomination] | None | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organizations: list[FsResProjectProjectOrgunit] | Unset = UNSET
    parent: FsResProjectProjectObj | None | Unset = UNSET
    predecessor: FsResProjectProjectObj | None | Unset = UNSET
    project_objective: CsSysValueGenericValue | Unset = UNSET
    project_status: CsSysValueGenericValue | Unset = UNSET
    project_type: CsSysValueGenericValue | None | Unset = UNSET
    pseudonymized_research_partner: None | str | Unset = UNSET
    pseudonymized_title: None | str | Unset = UNSET
    publications: list[FsResPublicationPublication] | None | Unset = UNSET
    reference_number: None | str | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    shorttext: None | str | Unset = UNSET
    startdate: int | Unset = UNSET
    still_available_details: bool | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    uniquename: None | str | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_project_project_obj_foreigntext_type_0 import FsResProjectProjectObjForeigntextType0  # noqa: PLC0415
        from ..models.fs_res_project_project_obj_listviews_type_0 import FsResProjectProjectObjListviewsType0  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        field_dynamic_component: dict[str, Any] | None | Unset
        if isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        elif isinstance(self.field_dynamic_component, ImplCsSysDynamicDynamicComponent):
            field_dynamic_component = self.field_dynamic_component.to_dict()
        else:
            field_dynamic_component = self.field_dynamic_component

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResProjectProjectObjForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        can_view_original_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.can_view_original_data, Unset):
            can_view_original_data = self.can_view_original_data.to_dict()

        commentary: None | str | Unset
        if isinstance(self.commentary, Unset):
            commentary = UNSET
        else:
            commentary = self.commentary

        cv_id = self.cv_id

        cv_lock_version = self.cv_lock_version

        defaulttext = self.defaulttext

        documents: list[dict[str, Any]] | None | Unset
        if isinstance(self.documents, Unset):
            documents = UNSET
        elif isinstance(self.documents, list):
            documents = []
            for documents_type_0_item_data in self.documents:
                documents_type_0_item = documents_type_0_item_data.to_dict()
                documents.append(documents_type_0_item)

        else:
            documents = self.documents

        enddate = self.enddate

        funding_programs: list[dict[str, Any]] | None | Unset
        if isinstance(self.funding_programs, Unset):
            funding_programs = UNSET
        elif isinstance(self.funding_programs, list):
            funding_programs = []
            for funding_programs_type_0_item_data in self.funding_programs:
                funding_programs_type_0_item = funding_programs_type_0_item_data.to_dict()
                funding_programs.append(funding_programs_type_0_item)

        else:
            funding_programs = self.funding_programs

        id = self.id

        is_economical: dict[str, Any] | None | Unset
        if isinstance(self.is_economical, Unset):
            is_economical = UNSET
        elif isinstance(self.is_economical, CsSysValueGenericValue):
            is_economical = self.is_economical.to_dict()
        else:
            is_economical = self.is_economical

        is_pseudonymized: dict[str, Any] | None | Unset
        if isinstance(self.is_pseudonymized, Unset):
            is_pseudonymized = UNSET
        elif isinstance(self.is_pseudonymized, CsSysValueGenericValue):
            is_pseudonymized = self.is_pseudonymized.to_dict()
        else:
            is_pseudonymized = self.is_pseudonymized

        kdsf_category: dict[str, Any] | None | Unset
        if isinstance(self.kdsf_category, Unset):
            kdsf_category = UNSET
        elif isinstance(self.kdsf_category, CsSysValueGenericValue):
            kdsf_category = self.kdsf_category.to_dict()
        else:
            kdsf_category = self.kdsf_category

        kdsf_category_details = self.kdsf_category_details

        key_words: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_words, Unset):
            key_words = []
            for key_words_item_data in self.key_words:
                key_words_item = key_words_item_data.to_dict()
                key_words.append(key_words_item)

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        listviews: dict[str, Any] | None | Unset
        if isinstance(self.listviews, Unset):
            listviews = UNSET
        elif isinstance(self.listviews, FsResProjectProjectObjListviewsType0):
            listviews = self.listviews.to_dict()
        else:
            listviews = self.listviews

        lock_version = self.lock_version

        longtext: None | str | Unset
        if isinstance(self.longtext, Unset):
            longtext = UNSET
        else:
            longtext = self.longtext

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        nominations: list[dict[str, Any]] | None | Unset
        if isinstance(self.nominations, Unset):
            nominations = UNSET
        elif isinstance(self.nominations, list):
            nominations = []
            for nominations_type_0_item_data in self.nominations:
                nominations_type_0_item = nominations_type_0_item_data.to_dict()
                nominations.append(nominations_type_0_item)

        else:
            nominations = self.nominations

        obj_guid = self.obj_guid

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        parent: dict[str, Any] | None | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, FsResProjectProjectObj):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        predecessor: dict[str, Any] | None | Unset
        if isinstance(self.predecessor, Unset):
            predecessor = UNSET
        elif isinstance(self.predecessor, FsResProjectProjectObj):
            predecessor = self.predecessor.to_dict()
        else:
            predecessor = self.predecessor

        project_objective: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_objective, Unset):
            project_objective = self.project_objective.to_dict()

        project_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_status, Unset):
            project_status = self.project_status.to_dict()

        project_type: dict[str, Any] | None | Unset
        if isinstance(self.project_type, Unset):
            project_type = UNSET
        elif isinstance(self.project_type, CsSysValueGenericValue):
            project_type = self.project_type.to_dict()
        else:
            project_type = self.project_type

        pseudonymized_research_partner: None | str | Unset
        if isinstance(self.pseudonymized_research_partner, Unset):
            pseudonymized_research_partner = UNSET
        else:
            pseudonymized_research_partner = self.pseudonymized_research_partner

        pseudonymized_title: None | str | Unset
        if isinstance(self.pseudonymized_title, Unset):
            pseudonymized_title = UNSET
        else:
            pseudonymized_title = self.pseudonymized_title

        publications: list[dict[str, Any]] | None | Unset
        if isinstance(self.publications, Unset):
            publications = UNSET
        elif isinstance(self.publications, list):
            publications = []
            for publications_type_0_item_data in self.publications:
                publications_type_0_item = publications_type_0_item_data.to_dict()
                publications.append(publications_type_0_item)

        else:
            publications = self.publications

        reference_number: None | str | Unset
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

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

        shorttext: None | str | Unset
        if isinstance(self.shorttext, Unset):
            shorttext = UNSET
        else:
            shorttext = self.shorttext

        startdate = self.startdate

        still_available_details = self.still_available_details

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        uniquename: None | str | Unset
        if isinstance(self.uniquename, Unset):
            uniquename = UNSET
        else:
            uniquename = self.uniquename

        visibility_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_value, Unset):
            visibility_value = self.visibility_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if can_view_original_data is not UNSET:
            field_dict["canViewOriginalData"] = can_view_original_data
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if cv_id is not UNSET:
            field_dict["cvId"] = cv_id
        if cv_lock_version is not UNSET:
            field_dict["cvLockVersion"] = cv_lock_version
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if documents is not UNSET:
            field_dict["documents"] = documents
        if enddate is not UNSET:
            field_dict["enddate"] = enddate
        if funding_programs is not UNSET:
            field_dict["fundingPrograms"] = funding_programs
        if id is not UNSET:
            field_dict["id"] = id
        if is_economical is not UNSET:
            field_dict["isEconomical"] = is_economical
        if is_pseudonymized is not UNSET:
            field_dict["isPseudonymized"] = is_pseudonymized
        if kdsf_category is not UNSET:
            field_dict["kdsfCategory"] = kdsf_category
        if kdsf_category_details is not UNSET:
            field_dict["kdsfCategoryDetails"] = kdsf_category_details
        if key_words is not UNSET:
            field_dict["keyWords"] = key_words
        if language is not UNSET:
            field_dict["language"] = language
        if listviews is not UNSET:
            field_dict["listviews"] = listviews
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if members is not UNSET:
            field_dict["members"] = members
        if nominations is not UNSET:
            field_dict["nominations"] = nominations
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if parent is not UNSET:
            field_dict["parent"] = parent
        if predecessor is not UNSET:
            field_dict["predecessor"] = predecessor
        if project_objective is not UNSET:
            field_dict["projectObjective"] = project_objective
        if project_status is not UNSET:
            field_dict["projectStatus"] = project_status
        if project_type is not UNSET:
            field_dict["projectType"] = project_type
        if pseudonymized_research_partner is not UNSET:
            field_dict["pseudonymizedResearchPartner"] = pseudonymized_research_partner
        if pseudonymized_title is not UNSET:
            field_dict["pseudonymizedTitle"] = pseudonymized_title
        if publications is not UNSET:
            field_dict["publications"] = publications
        if reference_number is not UNSET:
            field_dict["referenceNumber"] = reference_number
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if still_available_details is not UNSET:
            field_dict["stillAvailableDetails"] = still_available_details
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if visibility_value is not UNSET:
            field_dict["visibilityValue"] = visibility_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_nomination import FsResPrizeNominationNomination  # noqa: PLC0415
        from ..models.fs_res_project_project_member_position import FsResProjectProjectMemberPosition  # noqa: PLC0415
        from ..models.fs_res_project_project_obj_foreigntext_type_0 import FsResProjectProjectObjForeigntextType0  # noqa: PLC0415
        from ..models.fs_res_project_project_obj_listviews_type_0 import FsResProjectProjectObjListviewsType0  # noqa: PLC0415
        from ..models.fs_res_project_project_orgunit import FsResProjectProjectOrgunit  # noqa: PLC0415
        from ..models.fs_res_publication_publication import FsResPublicationPublication  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_field_dynamic_component(data: object) -> ImplCsSysDynamicDynamicComponent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_dynamic_component_type_0 = ImplCsSysDynamicDynamicComponent.from_dict(cast(dict[str, Any], data))

            return field_dynamic_component_type_0

        field_dynamic_component = _parse_field_dynamic_component(d.pop("_dynamicComponent", UNSET))

        def _parse_field_foreigntext(data: object) -> FsResProjectProjectObjForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResProjectProjectObjForeigntextType0.from_dict(cast(dict[str, Any], data))

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        _can_view_original_data = d.pop("canViewOriginalData", UNSET)
        can_view_original_data: CsSysValueGenericValue | Unset
        if isinstance(_can_view_original_data, Unset):
            can_view_original_data = UNSET
        else:
            can_view_original_data = CsSysValueGenericValue.from_dict(_can_view_original_data)

        def _parse_commentary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commentary = _parse_commentary(d.pop("commentary", UNSET))

        cv_id = d.pop("cvId", UNSET)

        cv_lock_version = d.pop("cvLockVersion", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        def _parse_documents(data: object) -> list[CsSysUploadConfigurationHisUploadFile] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            documents_type_0: list[CsSysUploadConfigurationHisUploadFile] = []
            _documents_type_0 = cast(list[dict[str, Any]], data)
            for documents_type_0_item_data in _documents_type_0:
                documents_type_0_item = CsSysUploadConfigurationHisUploadFile.from_dict(documents_type_0_item_data)

                documents_type_0.append(documents_type_0_item)

            return documents_type_0

        documents = _parse_documents(d.pop("documents", UNSET))

        enddate = d.pop("enddate", UNSET)

        def _parse_funding_programs(data: object) -> list[FsResFinanceResearchContract] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            funding_programs_type_0: list[FsResFinanceResearchContract] = []
            _funding_programs_type_0 = cast(list[dict[str, Any]], data)
            for funding_programs_type_0_item_data in _funding_programs_type_0:
                funding_programs_type_0_item = FsResFinanceResearchContract.from_dict(funding_programs_type_0_item_data)

                funding_programs_type_0.append(funding_programs_type_0_item)

            return funding_programs_type_0

        funding_programs = _parse_funding_programs(d.pop("fundingPrograms", UNSET))

        id = d.pop("id", UNSET)

        def _parse_is_economical(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            is_economical_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return is_economical_type_0

        is_economical = _parse_is_economical(d.pop("isEconomical", UNSET))

        def _parse_is_pseudonymized(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            is_pseudonymized_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return is_pseudonymized_type_0

        is_pseudonymized = _parse_is_pseudonymized(d.pop("isPseudonymized", UNSET))

        def _parse_kdsf_category(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            kdsf_category_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return kdsf_category_type_0

        kdsf_category = _parse_kdsf_category(d.pop("kdsfCategory", UNSET))

        kdsf_category_details = d.pop("kdsfCategoryDetails", UNSET)

        _key_words = d.pop("keyWords", UNSET)
        key_words: list[CsSysValueGenericValue] | Unset = UNSET
        if _key_words is not UNSET:
            key_words = []
            for key_words_item_data in _key_words:
                key_words_item = CsSysValueGenericValue.from_dict(key_words_item_data)

                key_words.append(key_words_item)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        def _parse_listviews(data: object) -> FsResProjectProjectObjListviewsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            listviews_type_0 = FsResProjectProjectObjListviewsType0.from_dict(cast(dict[str, Any], data))

            return listviews_type_0

        listviews = _parse_listviews(d.pop("listviews", UNSET))

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_longtext(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longtext = _parse_longtext(d.pop("longtext", UNSET))

        _members = d.pop("members", UNSET)
        members: list[FsResProjectProjectMemberPosition] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = FsResProjectProjectMemberPosition.from_dict(members_item_data)

                members.append(members_item)

        def _parse_nominations(data: object) -> list[FsResPrizeNominationNomination] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            nominations_type_0: list[FsResPrizeNominationNomination] = []
            _nominations_type_0 = cast(list[dict[str, Any]], data)
            for nominations_type_0_item_data in _nominations_type_0:
                nominations_type_0_item = FsResPrizeNominationNomination.from_dict(nominations_type_0_item_data)

                nominations_type_0.append(nominations_type_0_item)

            return nominations_type_0

        nominations = _parse_nominations(d.pop("nominations", UNSET))

        obj_guid = d.pop("objGuid", UNSET)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[FsResProjectProjectOrgunit] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = FsResProjectProjectOrgunit.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        def _parse_parent(data: object) -> FsResProjectProjectObj | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            parent_type_0 = FsResProjectProjectObj.from_dict(cast(dict[str, Any], data))

            return parent_type_0

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_predecessor(data: object) -> FsResProjectProjectObj | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            predecessor_type_0 = FsResProjectProjectObj.from_dict(cast(dict[str, Any], data))

            return predecessor_type_0

        predecessor = _parse_predecessor(d.pop("predecessor", UNSET))

        _project_objective = d.pop("projectObjective", UNSET)
        project_objective: CsSysValueGenericValue | Unset
        if isinstance(_project_objective, Unset):
            project_objective = UNSET
        else:
            project_objective = CsSysValueGenericValue.from_dict(_project_objective)

        _project_status = d.pop("projectStatus", UNSET)
        project_status: CsSysValueGenericValue | Unset
        if isinstance(_project_status, Unset):
            project_status = UNSET
        else:
            project_status = CsSysValueGenericValue.from_dict(_project_status)

        def _parse_project_type(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            project_type_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return project_type_type_0

        project_type = _parse_project_type(d.pop("projectType", UNSET))

        def _parse_pseudonymized_research_partner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pseudonymized_research_partner = _parse_pseudonymized_research_partner(
            d.pop("pseudonymizedResearchPartner", UNSET)
        )

        def _parse_pseudonymized_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pseudonymized_title = _parse_pseudonymized_title(d.pop("pseudonymizedTitle", UNSET))

        def _parse_publications(data: object) -> list[FsResPublicationPublication] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            publications_type_0: list[FsResPublicationPublication] = []
            _publications_type_0 = cast(list[dict[str, Any]], data)
            for publications_type_0_item_data in _publications_type_0:
                publications_type_0_item = FsResPublicationPublication.from_dict(publications_type_0_item_data)

                publications_type_0.append(publications_type_0_item)

            return publications_type_0

        publications = _parse_publications(d.pop("publications", UNSET))

        def _parse_reference_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_number = _parse_reference_number(d.pop("referenceNumber", UNSET))

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

        def _parse_shorttext(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shorttext = _parse_shorttext(d.pop("shorttext", UNSET))

        startdate = d.pop("startdate", UNSET)

        still_available_details = d.pop("stillAvailableDetails", UNSET)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        def _parse_uniquename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uniquename = _parse_uniquename(d.pop("uniquename", UNSET))

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        fs_res_project_project_obj = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            can_view_original_data=can_view_original_data,
            commentary=commentary,
            cv_id=cv_id,
            cv_lock_version=cv_lock_version,
            defaulttext=defaulttext,
            documents=documents,
            enddate=enddate,
            funding_programs=funding_programs,
            id=id,
            is_economical=is_economical,
            is_pseudonymized=is_pseudonymized,
            kdsf_category=kdsf_category,
            kdsf_category_details=kdsf_category_details,
            key_words=key_words,
            language=language,
            listviews=listviews,
            lock_version=lock_version,
            longtext=longtext,
            members=members,
            nominations=nominations,
            obj_guid=obj_guid,
            organizations=organizations,
            parent=parent,
            predecessor=predecessor,
            project_objective=project_objective,
            project_status=project_status,
            project_type=project_type,
            pseudonymized_research_partner=pseudonymized_research_partner,
            pseudonymized_title=pseudonymized_title,
            publications=publications,
            reference_number=reference_number,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            shorttext=shorttext,
            startdate=startdate,
            still_available_details=still_available_details,
            subject_areas=subject_areas,
            uniquename=uniquename,
            visibility_value=visibility_value,
        )

        fs_res_project_project_obj.additional_properties = d
        return fs_res_project_project_obj

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
