from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_generic_learning_outcome_type_learning_outcome_type import (
        DeMathplanMosesEdciGenericLearningOutcomeTypeLearningOutcomeType,
    )
    from ..models.de_mathplan_moses_edci_generic_learning_outcome_type_related_esco_skill import (
        DeMathplanMosesEdciGenericLearningOutcomeTypeRelatedEscoSkill,
    )
    from ..models.de_mathplan_moses_edci_generic_learning_outcome_type_reusability_level import (
        DeMathplanMosesEdciGenericLearningOutcomeTypeReusabilityLevel,
    )
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType


T = TypeVar("T", bound="DeMathplanMosesEdciGenericLearningOutcomeType")


@_attrs_define
class DeMathplanMosesEdciGenericLearningOutcomeType:
    """
    Attributes:
        description (list[DeMathplanMosesEdciNoteType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        learning_outcome_type (DeMathplanMosesEdciGenericLearningOutcomeTypeLearningOutcomeType | Unset):
        pref_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        related_esco_skill (list[DeMathplanMosesEdciGenericLearningOutcomeTypeRelatedEscoSkill] | Unset):
        reusability_level (DeMathplanMosesEdciGenericLearningOutcomeTypeReusabilityLevel | Unset):
    """

    description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    learning_outcome_type: DeMathplanMosesEdciGenericLearningOutcomeTypeLearningOutcomeType | Unset = UNSET
    pref_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    related_esco_skill: list[DeMathplanMosesEdciGenericLearningOutcomeTypeRelatedEscoSkill] | Unset = UNSET
    reusability_level: DeMathplanMosesEdciGenericLearningOutcomeTypeReusabilityLevel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        learning_outcome_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.learning_outcome_type, Unset):
            learning_outcome_type = self.learning_outcome_type.to_dict()

        pref_label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pref_label, Unset):
            pref_label = []
            for pref_label_item_data in self.pref_label:
                pref_label_item = pref_label_item_data.to_dict()
                pref_label.append(pref_label_item)

        related_esco_skill: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.related_esco_skill, Unset):
            related_esco_skill = []
            for related_esco_skill_item_data in self.related_esco_skill:
                related_esco_skill_item = related_esco_skill_item_data.to_dict()
                related_esco_skill.append(related_esco_skill_item)

        reusability_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reusability_level, Unset):
            reusability_level = self.reusability_level.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if learning_outcome_type is not UNSET:
            field_dict["learningOutcomeType"] = learning_outcome_type
        if pref_label is not UNSET:
            field_dict["prefLabel"] = pref_label
        if related_esco_skill is not UNSET:
            field_dict["relatedEscoSkill"] = related_esco_skill
        if reusability_level is not UNSET:
            field_dict["reusabilityLevel"] = reusability_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_learning_outcome_type_learning_outcome_type import (
            DeMathplanMosesEdciGenericLearningOutcomeTypeLearningOutcomeType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_generic_learning_outcome_type_related_esco_skill import (
            DeMathplanMosesEdciGenericLearningOutcomeTypeRelatedEscoSkill,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_generic_learning_outcome_type_reusability_level import (
            DeMathplanMosesEdciGenericLearningOutcomeTypeReusabilityLevel,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = DeMathplanMosesEdciNoteType.from_dict(description_item_data)

                description.append(description_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _learning_outcome_type = d.pop("learningOutcomeType", UNSET)
        learning_outcome_type: DeMathplanMosesEdciGenericLearningOutcomeTypeLearningOutcomeType | Unset
        if isinstance(_learning_outcome_type, Unset):
            learning_outcome_type = UNSET
        else:
            learning_outcome_type = DeMathplanMosesEdciGenericLearningOutcomeTypeLearningOutcomeType.from_dict(
                _learning_outcome_type
            )

        _pref_label = d.pop("prefLabel", UNSET)
        pref_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _pref_label is not UNSET:
            pref_label = []
            for pref_label_item_data in _pref_label:
                pref_label_item = DeMathplanMosesEdciLanguageStringType.from_dict(pref_label_item_data)

                pref_label.append(pref_label_item)

        _related_esco_skill = d.pop("relatedEscoSkill", UNSET)
        related_esco_skill: list[DeMathplanMosesEdciGenericLearningOutcomeTypeRelatedEscoSkill] | Unset = UNSET
        if _related_esco_skill is not UNSET:
            related_esco_skill = []
            for related_esco_skill_item_data in _related_esco_skill:
                related_esco_skill_item = DeMathplanMosesEdciGenericLearningOutcomeTypeRelatedEscoSkill.from_dict(
                    related_esco_skill_item_data
                )

                related_esco_skill.append(related_esco_skill_item)

        _reusability_level = d.pop("reusabilityLevel", UNSET)
        reusability_level: DeMathplanMosesEdciGenericLearningOutcomeTypeReusabilityLevel | Unset
        if isinstance(_reusability_level, Unset):
            reusability_level = UNSET
        else:
            reusability_level = DeMathplanMosesEdciGenericLearningOutcomeTypeReusabilityLevel.from_dict(
                _reusability_level
            )

        de_mathplan_moses_edci_generic_learning_outcome_type = cls(
            description=description,
            id=id,
            identifier=identifier,
            learning_outcome_type=learning_outcome_type,
            pref_label=pref_label,
            related_esco_skill=related_esco_skill,
            reusability_level=reusability_level,
        )

        de_mathplan_moses_edci_generic_learning_outcome_type.additional_properties = d
        return de_mathplan_moses_edci_generic_learning_outcome_type

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
