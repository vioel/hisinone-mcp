from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_profile_employment_classification import CsPsvPersonProfileEmploymentClassification
    from ..models.cs_psv_person_profile_person_classification import CsPsvPersonProfilePersonClassification
    from ..models.cs_psv_person_profile_person_profile_entry import CsPsvPersonProfilePersonProfileEntry


T = TypeVar("T", bound="CsPsvPersonProfilePersonProfile")


@_attrs_define
class CsPsvPersonProfilePersonProfile:
    """
    Attributes:
        employment_classifications (list[CsPsvPersonProfileEmploymentClassification] | Unset):
        employment_classifications_data_source (bool | Unset):
        person_classifications (CsPsvPersonProfilePersonClassification | Unset):
        profile_entries (list[CsPsvPersonProfilePersonProfileEntry] | Unset):
    """

    employment_classifications: list[CsPsvPersonProfileEmploymentClassification] | Unset = UNSET
    employment_classifications_data_source: bool | Unset = UNSET
    person_classifications: CsPsvPersonProfilePersonClassification | Unset = UNSET
    profile_entries: list[CsPsvPersonProfilePersonProfileEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        employment_classifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.employment_classifications, Unset):
            employment_classifications = []
            for employment_classifications_item_data in self.employment_classifications:
                employment_classifications_item = employment_classifications_item_data.to_dict()
                employment_classifications.append(employment_classifications_item)

        employment_classifications_data_source = self.employment_classifications_data_source

        person_classifications: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person_classifications, Unset):
            person_classifications = self.person_classifications.to_dict()

        profile_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.profile_entries, Unset):
            profile_entries = []
            for profile_entries_item_data in self.profile_entries:
                profile_entries_item = profile_entries_item_data.to_dict()
                profile_entries.append(profile_entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employment_classifications is not UNSET:
            field_dict["employmentClassifications"] = employment_classifications
        if employment_classifications_data_source is not UNSET:
            field_dict["employmentClassificationsDataSource"] = employment_classifications_data_source
        if person_classifications is not UNSET:
            field_dict["personClassifications"] = person_classifications
        if profile_entries is not UNSET:
            field_dict["profileEntries"] = profile_entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_profile_employment_classification import CsPsvPersonProfileEmploymentClassification  # noqa: PLC0415
        from ..models.cs_psv_person_profile_person_classification import CsPsvPersonProfilePersonClassification  # noqa: PLC0415
        from ..models.cs_psv_person_profile_person_profile_entry import CsPsvPersonProfilePersonProfileEntry  # noqa: PLC0415

        d = dict(src_dict)
        _employment_classifications = d.pop("employmentClassifications", UNSET)
        employment_classifications: list[CsPsvPersonProfileEmploymentClassification] | Unset = UNSET
        if _employment_classifications is not UNSET:
            employment_classifications = []
            for employment_classifications_item_data in _employment_classifications:
                employment_classifications_item = CsPsvPersonProfileEmploymentClassification.from_dict(
                    employment_classifications_item_data
                )

                employment_classifications.append(employment_classifications_item)

        employment_classifications_data_source = d.pop("employmentClassificationsDataSource", UNSET)

        _person_classifications = d.pop("personClassifications", UNSET)
        person_classifications: CsPsvPersonProfilePersonClassification | Unset
        if isinstance(_person_classifications, Unset):
            person_classifications = UNSET
        else:
            person_classifications = CsPsvPersonProfilePersonClassification.from_dict(_person_classifications)

        _profile_entries = d.pop("profileEntries", UNSET)
        profile_entries: list[CsPsvPersonProfilePersonProfileEntry] | Unset = UNSET
        if _profile_entries is not UNSET:
            profile_entries = []
            for profile_entries_item_data in _profile_entries:
                profile_entries_item = CsPsvPersonProfilePersonProfileEntry.from_dict(profile_entries_item_data)

                profile_entries.append(profile_entries_item)

        cs_psv_person_profile_person_profile = cls(
            employment_classifications=employment_classifications,
            employment_classifications_data_source=employment_classifications_data_source,
            person_classifications=person_classifications,
            profile_entries=profile_entries,
        )

        cs_psv_person_profile_person_profile.additional_properties = d
        return cs_psv_person_profile_person_profile

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
