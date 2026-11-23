from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaMathBigInteger")


@_attrs_define
class JavaMathBigInteger:
    """
    Attributes:
        lowest_set_bit (int | Unset):
    """

    lowest_set_bit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        lowest_set_bit = self.lowest_set_bit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lowest_set_bit is not UNSET:
            field_dict["lowestSetBit"] = lowest_set_bit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lowest_set_bit = d.pop("lowestSetBit", UNSET)

        java_math_big_integer = cls(
            lowest_set_bit=lowest_set_bit,
        )

        java_math_big_integer.additional_properties = d
        return java_math_big_integer

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
