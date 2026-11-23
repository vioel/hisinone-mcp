from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
        EuEmrexElmoPlaintextMultilineStringWithOptionalLang,
    )


T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel:
    """
    Attributes:
        description (EuEmrexElmoPlaintextMultilineStringWithOptionalLang | Unset):
        type_ (str | Unset):
        value (str | Unset):
    """

    description: EuEmrexElmoPlaintextMultilineStringWithOptionalLang | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
            EuEmrexElmoPlaintextMultilineStringWithOptionalLang,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: EuEmrexElmoPlaintextMultilineStringWithOptionalLang | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = EuEmrexElmoPlaintextMultilineStringWithOptionalLang.from_dict(_description)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_level = cls(
            description=description,
            type_=type_,
            value=value,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_level.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_level

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
