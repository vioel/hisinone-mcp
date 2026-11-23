from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading"
)


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading:
    """
    Attributes:
        percentage_equal (float | Unset):
        percentage_higher (float | Unset):
        percentage_lower (float | Unset):
    """

    percentage_equal: float | Unset = UNSET
    percentage_higher: float | Unset = UNSET
    percentage_lower: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        percentage_equal = self.percentage_equal

        percentage_higher = self.percentage_higher

        percentage_lower = self.percentage_lower

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if percentage_equal is not UNSET:
            field_dict["percentageEqual"] = percentage_equal
        if percentage_higher is not UNSET:
            field_dict["percentageHigher"] = percentage_higher
        if percentage_lower is not UNSET:
            field_dict["percentageLower"] = percentage_lower

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        percentage_equal = d.pop("percentageEqual", UNSET)

        percentage_higher = d.pop("percentageHigher", UNSET)

        percentage_lower = d.pop("percentageLower", UNSET)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_shortened_grading = (
            cls(
                percentage_equal=percentage_equal,
                percentage_higher=percentage_higher,
                percentage_lower=percentage_lower,
            )
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_shortened_grading.additional_properties = d
        return (
            eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_shortened_grading
        )

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
