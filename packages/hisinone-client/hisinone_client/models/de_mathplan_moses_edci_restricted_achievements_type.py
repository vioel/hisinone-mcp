from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_achievement_type import DeMathplanMosesEdciAchievementType


T = TypeVar("T", bound="DeMathplanMosesEdciRestrictedAchievementsType")


@_attrs_define
class DeMathplanMosesEdciRestrictedAchievementsType:
    """
    Attributes:
        learning_achievement_or_qualification_award (list[DeMathplanMosesEdciAchievementType] | Unset):
    """

    learning_achievement_or_qualification_award: list[DeMathplanMosesEdciAchievementType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        learning_achievement_or_qualification_award: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.learning_achievement_or_qualification_award, Unset):
            learning_achievement_or_qualification_award = []
            for (
                learning_achievement_or_qualification_award_item_data
            ) in self.learning_achievement_or_qualification_award:
                learning_achievement_or_qualification_award_item = (
                    learning_achievement_or_qualification_award_item_data.to_dict()
                )
                learning_achievement_or_qualification_award.append(learning_achievement_or_qualification_award_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if learning_achievement_or_qualification_award is not UNSET:
            field_dict["learningAchievementOrQualificationAward"] = learning_achievement_or_qualification_award

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_achievement_type import DeMathplanMosesEdciAchievementType  # noqa: PLC0415

        d = dict(src_dict)
        _learning_achievement_or_qualification_award = d.pop("learningAchievementOrQualificationAward", UNSET)
        learning_achievement_or_qualification_award: list[DeMathplanMosesEdciAchievementType] | Unset = UNSET
        if _learning_achievement_or_qualification_award is not UNSET:
            learning_achievement_or_qualification_award = []
            for learning_achievement_or_qualification_award_item_data in _learning_achievement_or_qualification_award:
                learning_achievement_or_qualification_award_item = DeMathplanMosesEdciAchievementType.from_dict(
                    learning_achievement_or_qualification_award_item_data
                )

                learning_achievement_or_qualification_award.append(learning_achievement_or_qualification_award_item)

        de_mathplan_moses_edci_restricted_achievements_type = cls(
            learning_achievement_or_qualification_award=learning_achievement_or_qualification_award,
        )

        de_mathplan_moses_edci_restricted_achievements_type.additional_properties = d
        return de_mathplan_moses_edci_restricted_achievements_type

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
