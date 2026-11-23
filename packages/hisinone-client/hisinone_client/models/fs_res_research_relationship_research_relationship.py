from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_research_partner_simple import (
        CsPsvExternalOrganisationResearchPartnerSimple,
    )
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_research_relationship_research_relationship_foreigntext import (
        FsResResearchRelationshipResearchRelationshipForeigntext,
    )
    from ..models.fs_res_research_relationship_research_relationship_parent_orgunit import (
        FsResResearchRelationshipResearchRelationshipParentOrgunit,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResResearchRelationshipResearchRelationship")


@_attrs_define
class FsResResearchRelationshipResearchRelationship:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResResearchRelationshipResearchRelationshipForeigntext | Unset):
        all_research_areas (list[CsSysValueGenericValue] | Unset):
        commentary (str | Unset):
        documents (list[CsSysUploadConfigurationHisUploadFile] | Unset):
        end_date (int | Unset):
        id (int | Unset):
        is_kdsf_relevant (CsSysValueGenericValue | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        parent_orgunits (list[FsResResearchRelationshipResearchRelationshipParentOrgunit] | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        start_date (int | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResResearchRelationshipResearchRelationshipForeigntext | Unset = UNSET
    all_research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    commentary: str | Unset = UNSET
    documents: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
    end_date: int | Unset = UNSET
    id: int | Unset = UNSET
    is_kdsf_relevant: CsSysValueGenericValue | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent_orgunits: list[FsResResearchRelationshipResearchRelationshipParentOrgunit] | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    start_date: int | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        all_research_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_research_areas, Unset):
            all_research_areas = []
            for all_research_areas_item_data in self.all_research_areas:
                all_research_areas_item = all_research_areas_item_data.to_dict()
                all_research_areas.append(all_research_areas_item)

        commentary = self.commentary

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        end_date = self.end_date

        id = self.id

        is_kdsf_relevant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.is_kdsf_relevant, Unset):
            is_kdsf_relevant = self.is_kdsf_relevant.to_dict()

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        parent_orgunits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parent_orgunits, Unset):
            parent_orgunits = []
            for parent_orgunits_item_data in self.parent_orgunits:
                parent_orgunits_item = parent_orgunits_item_data.to_dict()
                parent_orgunits.append(parent_orgunits_item)

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

        research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_partner, Unset):
            research_partner = self.research_partner.to_dict()

        start_date = self.start_date

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if all_research_areas is not UNSET:
            field_dict["allResearchAreas"] = all_research_areas
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if documents is not UNSET:
            field_dict["documents"] = documents
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if is_kdsf_relevant is not UNSET:
            field_dict["isKdsfRelevant"] = is_kdsf_relevant
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent_orgunits is not UNSET:
            field_dict["parentOrgunits"] = parent_orgunits
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_research_relationship_research_relationship_foreigntext import (
            FsResResearchRelationshipResearchRelationshipForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_research_relationship_research_relationship_parent_orgunit import (
            FsResResearchRelationshipResearchRelationshipParentOrgunit,  # noqa: PLC0415
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

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResResearchRelationshipResearchRelationshipForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResResearchRelationshipResearchRelationshipForeigntext.from_dict(_field_foreigntext)

        _all_research_areas = d.pop("allResearchAreas", UNSET)
        all_research_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _all_research_areas is not UNSET:
            all_research_areas = []
            for all_research_areas_item_data in _all_research_areas:
                all_research_areas_item = CsSysValueGenericValue.from_dict(all_research_areas_item_data)

                all_research_areas.append(all_research_areas_item)

        commentary = d.pop("commentary", UNSET)

        _documents = d.pop("documents", UNSET)
        documents: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = CsSysUploadConfigurationHisUploadFile.from_dict(documents_item_data)

                documents.append(documents_item)

        end_date = d.pop("endDate", UNSET)

        id = d.pop("id", UNSET)

        _is_kdsf_relevant = d.pop("isKdsfRelevant", UNSET)
        is_kdsf_relevant: CsSysValueGenericValue | Unset
        if isinstance(_is_kdsf_relevant, Unset):
            is_kdsf_relevant = UNSET
        else:
            is_kdsf_relevant = CsSysValueGenericValue.from_dict(_is_kdsf_relevant)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _parent_orgunits = d.pop("parentOrgunits", UNSET)
        parent_orgunits: list[FsResResearchRelationshipResearchRelationshipParentOrgunit] | Unset = UNSET
        if _parent_orgunits is not UNSET:
            parent_orgunits = []
            for parent_orgunits_item_data in _parent_orgunits:
                parent_orgunits_item = FsResResearchRelationshipResearchRelationshipParentOrgunit.from_dict(
                    parent_orgunits_item_data
                )

                parent_orgunits.append(parent_orgunits_item)

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

        _research_partner = d.pop("researchPartner", UNSET)
        research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_research_partner, Unset):
            research_partner = UNSET
        else:
            research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_research_partner)

        start_date = d.pop("startDate", UNSET)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        fs_res_research_relationship_research_relationship = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            all_research_areas=all_research_areas,
            commentary=commentary,
            documents=documents,
            end_date=end_date,
            id=id,
            is_kdsf_relevant=is_kdsf_relevant,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            parent_orgunits=parent_orgunits,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            research_partner=research_partner,
            start_date=start_date,
            subject_areas=subject_areas,
        )

        fs_res_research_relationship_research_relationship.additional_properties = d
        return fs_res_research_relationship_research_relationship

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
