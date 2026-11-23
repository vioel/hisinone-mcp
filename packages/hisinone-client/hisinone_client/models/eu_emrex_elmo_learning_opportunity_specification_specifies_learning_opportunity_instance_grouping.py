from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping:
    """
    Attributes:
        idref (str | Unset):
        typeref (str | Unset):
        value (str | Unset):
    """

    idref: str | Unset = UNSET
    typeref: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        idref = self.idref

        typeref = self.typeref

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idref is not UNSET:
            field_dict["idref"] = idref
        if typeref is not UNSET:
            field_dict["typeref"] = typeref
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idref = d.pop("idref", UNSET)

        typeref = d.pop("typeref", UNSET)

        value = d.pop("value", UNSET)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_grouping = cls(
            idref=idref,
            typeref=typeref,
            value=value,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_grouping.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_grouping

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
