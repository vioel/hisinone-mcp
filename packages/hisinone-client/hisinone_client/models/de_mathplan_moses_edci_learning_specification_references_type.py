from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="DeMathplanMosesEdciLearningSpecificationReferencesType")


@_attrs_define
class DeMathplanMosesEdciLearningSpecificationReferencesType:
    """
    Attributes:
        learning_specification_or_qualification (list[JavaLangObject] | Unset):
        study_programme_or_stupo_or_study_section (list[JavaLangObject] | Unset):
    """

    learning_specification_or_qualification: list[JavaLangObject] | Unset = UNSET
    study_programme_or_stupo_or_study_section: list[JavaLangObject] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        learning_specification_or_qualification: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.learning_specification_or_qualification, Unset):
            learning_specification_or_qualification = []
            for learning_specification_or_qualification_item_data in self.learning_specification_or_qualification:
                learning_specification_or_qualification_item = (
                    learning_specification_or_qualification_item_data.to_dict()
                )
                learning_specification_or_qualification.append(learning_specification_or_qualification_item)

        study_programme_or_stupo_or_study_section: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.study_programme_or_stupo_or_study_section, Unset):
            study_programme_or_stupo_or_study_section = []
            for study_programme_or_stupo_or_study_section_item_data in self.study_programme_or_stupo_or_study_section:
                study_programme_or_stupo_or_study_section_item = (
                    study_programme_or_stupo_or_study_section_item_data.to_dict()
                )
                study_programme_or_stupo_or_study_section.append(study_programme_or_stupo_or_study_section_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if learning_specification_or_qualification is not UNSET:
            field_dict["learningSpecificationOrQualification"] = learning_specification_or_qualification
        if study_programme_or_stupo_or_study_section is not UNSET:
            field_dict["studyProgrammeOrStupoOrStudySection"] = study_programme_or_stupo_or_study_section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        _learning_specification_or_qualification = d.pop("learningSpecificationOrQualification", UNSET)
        learning_specification_or_qualification: list[JavaLangObject] | Unset = UNSET
        if _learning_specification_or_qualification is not UNSET:
            learning_specification_or_qualification = []
            for learning_specification_or_qualification_item_data in _learning_specification_or_qualification:
                learning_specification_or_qualification_item = JavaLangObject.from_dict(
                    learning_specification_or_qualification_item_data
                )

                learning_specification_or_qualification.append(learning_specification_or_qualification_item)

        _study_programme_or_stupo_or_study_section = d.pop("studyProgrammeOrStupoOrStudySection", UNSET)
        study_programme_or_stupo_or_study_section: list[JavaLangObject] | Unset = UNSET
        if _study_programme_or_stupo_or_study_section is not UNSET:
            study_programme_or_stupo_or_study_section = []
            for study_programme_or_stupo_or_study_section_item_data in _study_programme_or_stupo_or_study_section:
                study_programme_or_stupo_or_study_section_item = JavaLangObject.from_dict(
                    study_programme_or_stupo_or_study_section_item_data
                )

                study_programme_or_stupo_or_study_section.append(study_programme_or_stupo_or_study_section_item)

        de_mathplan_moses_edci_learning_specification_references_type = cls(
            learning_specification_or_qualification=learning_specification_or_qualification,
            study_programme_or_stupo_or_study_section=study_programme_or_stupo_or_study_section,
        )

        de_mathplan_moses_edci_learning_specification_references_type.additional_properties = d
        return de_mathplan_moses_edci_learning_specification_references_type

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
