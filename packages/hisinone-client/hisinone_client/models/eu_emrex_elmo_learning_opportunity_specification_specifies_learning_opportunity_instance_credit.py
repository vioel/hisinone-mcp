from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit:
    """
    Attributes:
        level (str | Unset):
        scheme (str | Unset):
        value (float | Unset):
    """

    level: str | Unset = UNSET
    scheme: str | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        scheme = self.scheme

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        level = d.pop("level", UNSET)

        scheme = d.pop("scheme", UNSET)

        value = d.pop("value", UNSET)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_credit = cls(
            level=level,
            scheme=scheme,
            value=value,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_credit.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_credit

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
