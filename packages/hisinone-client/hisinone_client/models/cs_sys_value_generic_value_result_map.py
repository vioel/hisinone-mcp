from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CsSysValueGenericValueResultMap")


@_attrs_define
class CsSysValueGenericValueResultMap:
    """
    Attributes:
        key (str | Unset):
        value (JavaLangObject | Unset):
    """

    key: str | Unset = UNSET
    value: JavaLangObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _value = d.pop("value", UNSET)
        value: JavaLangObject | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = JavaLangObject.from_dict(_value)

        cs_sys_value_generic_value_result_map = cls(
            key=key,
            value=value,
        )

        cs_sys_value_generic_value_result_map.additional_properties = d
        return cs_sys_value_generic_value_result_map

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
