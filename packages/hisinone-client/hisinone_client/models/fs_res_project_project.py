from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract
    from ..models.fs_res_project_project_foreigntext import FsResProjectProjectForeigntext
    from ..models.fs_res_project_project_member_position import FsResProjectProjectMemberPosition
    from ..models.fs_res_project_project_orgunit import FsResProjectProjectOrgunit
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResProjectProject")


@_attrs_define
class FsResProjectProject:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResProjectProjectForeigntext | Unset):
        can_view_original_data (CsSysValueGenericValue | Unset):
        commentary (str | Unset):
        defaulttext (str | Unset):
        enddate (int | Unset):
        funding_programs (list[FsResFinanceResearchContract] | Unset):
        id (int | Unset):
        is_economical (CsSysValueGenericValue | Unset):
        is_pseudonymized (CsSysValueGenericValue | Unset):
        kdsf_category (CsSysValueGenericValue | Unset):
        kdsf_category_details (bool | Unset):
        key_words (list[CsSysValueGenericValue] | Unset):
        language (ImplFsResLanguageValue | Unset):
        lid (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        members (list[FsResProjectProjectMemberPosition] | Unset):
        obj_guid (str | Unset):
        organizations (list[FsResProjectProjectOrgunit] | Unset):
        project_objective (CsSysValueGenericValue | Unset):
        project_status (CsSysValueGenericValue | Unset):
        project_type (CsSysValueGenericValue | Unset):
        pseudonymized_research_partner (str | Unset):
        pseudonymized_title (str | Unset):
        reference_number (str | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        shorttext (str | Unset):
        startdate (int | Unset):
        still_available_details (bool | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        uniquename (str | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResProjectProjectForeigntext | Unset = UNSET
    can_view_original_data: CsSysValueGenericValue | Unset = UNSET
    commentary: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    enddate: int | Unset = UNSET
    funding_programs: list[FsResFinanceResearchContract] | Unset = UNSET
    id: int | Unset = UNSET
    is_economical: CsSysValueGenericValue | Unset = UNSET
    is_pseudonymized: CsSysValueGenericValue | Unset = UNSET
    kdsf_category: CsSysValueGenericValue | Unset = UNSET
    kdsf_category_details: bool | Unset = UNSET
    key_words: list[CsSysValueGenericValue] | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lid: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    members: list[FsResProjectProjectMemberPosition] | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organizations: list[FsResProjectProjectOrgunit] | Unset = UNSET
    project_objective: CsSysValueGenericValue | Unset = UNSET
    project_status: CsSysValueGenericValue | Unset = UNSET
    project_type: CsSysValueGenericValue | Unset = UNSET
    pseudonymized_research_partner: str | Unset = UNSET
    pseudonymized_title: str | Unset = UNSET
    reference_number: str | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    shorttext: str | Unset = UNSET
    startdate: int | Unset = UNSET
    still_available_details: bool | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    uniquename: str | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        can_view_original_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.can_view_original_data, Unset):
            can_view_original_data = self.can_view_original_data.to_dict()

        commentary = self.commentary

        defaulttext = self.defaulttext

        enddate = self.enddate

        funding_programs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.funding_programs, Unset):
            funding_programs = []
            for funding_programs_item_data in self.funding_programs:
                funding_programs_item = funding_programs_item_data.to_dict()
                funding_programs.append(funding_programs_item)

        id = self.id

        is_economical: dict[str, Any] | Unset = UNSET
        if not isinstance(self.is_economical, Unset):
            is_economical = self.is_economical.to_dict()

        is_pseudonymized: dict[str, Any] | Unset = UNSET
        if not isinstance(self.is_pseudonymized, Unset):
            is_pseudonymized = self.is_pseudonymized.to_dict()

        kdsf_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kdsf_category, Unset):
            kdsf_category = self.kdsf_category.to_dict()

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

        lid = self.lid

        lock_version = self.lock_version

        longtext = self.longtext

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        obj_guid = self.obj_guid

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        project_objective: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_objective, Unset):
            project_objective = self.project_objective.to_dict()

        project_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_status, Unset):
            project_status = self.project_status.to_dict()

        project_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_type, Unset):
            project_type = self.project_type.to_dict()

        pseudonymized_research_partner = self.pseudonymized_research_partner

        pseudonymized_title = self.pseudonymized_title

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

        shorttext = self.shorttext

        startdate = self.startdate

        still_available_details = self.still_available_details

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

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
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
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
        if lid is not UNSET:
            field_dict["lid"] = lid
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if members is not UNSET:
            field_dict["members"] = members
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
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
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract  # noqa: PLC0415
        from ..models.fs_res_project_project_foreigntext import FsResProjectProjectForeigntext  # noqa: PLC0415
        from ..models.fs_res_project_project_member_position import FsResProjectProjectMemberPosition  # noqa: PLC0415
        from ..models.fs_res_project_project_orgunit import FsResProjectProjectOrgunit  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResProjectProjectForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResProjectProjectForeigntext.from_dict(_field_foreigntext)

        _can_view_original_data = d.pop("canViewOriginalData", UNSET)
        can_view_original_data: CsSysValueGenericValue | Unset
        if isinstance(_can_view_original_data, Unset):
            can_view_original_data = UNSET
        else:
            can_view_original_data = CsSysValueGenericValue.from_dict(_can_view_original_data)

        commentary = d.pop("commentary", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        enddate = d.pop("enddate", UNSET)

        _funding_programs = d.pop("fundingPrograms", UNSET)
        funding_programs: list[FsResFinanceResearchContract] | Unset = UNSET
        if _funding_programs is not UNSET:
            funding_programs = []
            for funding_programs_item_data in _funding_programs:
                funding_programs_item = FsResFinanceResearchContract.from_dict(funding_programs_item_data)

                funding_programs.append(funding_programs_item)

        id = d.pop("id", UNSET)

        _is_economical = d.pop("isEconomical", UNSET)
        is_economical: CsSysValueGenericValue | Unset
        if isinstance(_is_economical, Unset):
            is_economical = UNSET
        else:
            is_economical = CsSysValueGenericValue.from_dict(_is_economical)

        _is_pseudonymized = d.pop("isPseudonymized", UNSET)
        is_pseudonymized: CsSysValueGenericValue | Unset
        if isinstance(_is_pseudonymized, Unset):
            is_pseudonymized = UNSET
        else:
            is_pseudonymized = CsSysValueGenericValue.from_dict(_is_pseudonymized)

        _kdsf_category = d.pop("kdsfCategory", UNSET)
        kdsf_category: CsSysValueGenericValue | Unset
        if isinstance(_kdsf_category, Unset):
            kdsf_category = UNSET
        else:
            kdsf_category = CsSysValueGenericValue.from_dict(_kdsf_category)

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

        lid = d.pop("lid", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        _members = d.pop("members", UNSET)
        members: list[FsResProjectProjectMemberPosition] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = FsResProjectProjectMemberPosition.from_dict(members_item_data)

                members.append(members_item)

        obj_guid = d.pop("objGuid", UNSET)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[FsResProjectProjectOrgunit] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = FsResProjectProjectOrgunit.from_dict(organizations_item_data)

                organizations.append(organizations_item)

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

        _project_type = d.pop("projectType", UNSET)
        project_type: CsSysValueGenericValue | Unset
        if isinstance(_project_type, Unset):
            project_type = UNSET
        else:
            project_type = CsSysValueGenericValue.from_dict(_project_type)

        pseudonymized_research_partner = d.pop("pseudonymizedResearchPartner", UNSET)

        pseudonymized_title = d.pop("pseudonymizedTitle", UNSET)

        reference_number = d.pop("referenceNumber", UNSET)

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

        shorttext = d.pop("shorttext", UNSET)

        startdate = d.pop("startdate", UNSET)

        still_available_details = d.pop("stillAvailableDetails", UNSET)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        uniquename = d.pop("uniquename", UNSET)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        fs_res_project_project = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            can_view_original_data=can_view_original_data,
            commentary=commentary,
            defaulttext=defaulttext,
            enddate=enddate,
            funding_programs=funding_programs,
            id=id,
            is_economical=is_economical,
            is_pseudonymized=is_pseudonymized,
            kdsf_category=kdsf_category,
            kdsf_category_details=kdsf_category_details,
            key_words=key_words,
            language=language,
            lid=lid,
            lock_version=lock_version,
            longtext=longtext,
            members=members,
            obj_guid=obj_guid,
            organizations=organizations,
            project_objective=project_objective,
            project_status=project_status,
            project_type=project_type,
            pseudonymized_research_partner=pseudonymized_research_partner,
            pseudonymized_title=pseudonymized_title,
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

        fs_res_project_project.additional_properties = d
        return fs_res_project_project

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
