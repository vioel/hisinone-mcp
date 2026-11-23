from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPersonProfileEmploymentClassification")


@_attrs_define
class CsPsvPersonProfileEmploymentClassification:
    """
    Attributes:
        all_research_areas (list[CsSysValueGenericValue] | Unset):
        employment_id (int | Unset):
        orgunit_defaulttext (str | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    all_research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    employment_id: int | Unset = UNSET
    orgunit_defaulttext: str | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        all_research_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_research_areas, Unset):
            all_research_areas = []
            for all_research_areas_item_data in self.all_research_areas:
                all_research_areas_item = all_research_areas_item_data.to_dict()
                all_research_areas.append(all_research_areas_item)

        employment_id = self.employment_id

        orgunit_defaulttext = self.orgunit_defaulttext

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

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_research_areas is not UNSET:
            field_dict["allResearchAreas"] = all_research_areas
        if employment_id is not UNSET:
            field_dict["employmentId"] = employment_id
        if orgunit_defaulttext is not UNSET:
            field_dict["orgunitDefaulttext"] = orgunit_defaulttext
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _all_research_areas = d.pop("allResearchAreas", UNSET)
        all_research_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _all_research_areas is not UNSET:
            all_research_areas = []
            for all_research_areas_item_data in _all_research_areas:
                all_research_areas_item = CsSysValueGenericValue.from_dict(all_research_areas_item_data)

                all_research_areas.append(all_research_areas_item)

        employment_id = d.pop("employmentId", UNSET)

        orgunit_defaulttext = d.pop("orgunitDefaulttext", UNSET)

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

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        cs_psv_person_profile_employment_classification = cls(
            all_research_areas=all_research_areas,
            employment_id=employment_id,
            orgunit_defaulttext=orgunit_defaulttext,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            subject_areas=subject_areas,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        cs_psv_person_profile_employment_classification.additional_properties = d
        return cs_psv_person_profile_employment_classification

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
