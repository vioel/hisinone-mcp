from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_math_big_integer import JavaMathBigInteger


T = TypeVar(
    "T",
    bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory",
)


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory:
    """
    Attributes:
        count (JavaMathBigInteger | Unset):
        label (str | Unset):
    """

    count: JavaMathBigInteger | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_math_big_integer import JavaMathBigInteger  # noqa: PLC0415

        d = dict(src_dict)
        _count = d.pop("count", UNSET)
        count: JavaMathBigInteger | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = JavaMathBigInteger.from_dict(_count)

        label = d.pop("label", UNSET)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution_category = cls(
            count=count,
            label=label,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution_category.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution_category

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
