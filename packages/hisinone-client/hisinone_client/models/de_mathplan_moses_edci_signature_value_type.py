from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeMathplanMosesEdciSignatureValueType")


@_attrs_define
class DeMathplanMosesEdciSignatureValueType:
    """
    Attributes:
        id (str | Unset):
        value (list[int] | Unset):
    """

    id: str | Unset = UNSET
    value: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value: list[int] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value = cast(list[int], d.pop("value", UNSET))

        de_mathplan_moses_edci_signature_value_type = cls(
            id=id,
            value=value,
        )

        de_mathplan_moses_edci_signature_value_type.additional_properties = d
        return de_mathplan_moses_edci_signature_value_type

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
