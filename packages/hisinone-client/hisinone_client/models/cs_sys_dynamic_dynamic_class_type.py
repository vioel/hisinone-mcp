from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysDynamicDynamicClassType")


@_attrs_define
class CsSysDynamicDynamicClassType:
    """
    Attributes:
        custom_content_type (bool | Unset):
        declaring_class (Any | Unset):
        key (int | Unset):
        message_key (str | Unset):
        static_content_type (bool | Unset):
    """

    custom_content_type: bool | Unset = UNSET
    declaring_class: Any | Unset = UNSET
    key: int | Unset = UNSET
    message_key: str | Unset = UNSET
    static_content_type: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        custom_content_type = self.custom_content_type

        declaring_class = self.declaring_class

        key = self.key

        message_key = self.message_key

        static_content_type = self.static_content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_content_type is not UNSET:
            field_dict["customContentType"] = custom_content_type
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if key is not UNSET:
            field_dict["key"] = key
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key
        if static_content_type is not UNSET:
            field_dict["staticContentType"] = static_content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_content_type = d.pop("customContentType", UNSET)

        declaring_class = d.pop("declaringClass", UNSET)

        key = d.pop("key", UNSET)

        message_key = d.pop("messageKey", UNSET)

        static_content_type = d.pop("staticContentType", UNSET)

        cs_sys_dynamic_dynamic_class_type = cls(
            custom_content_type=custom_content_type,
            declaring_class=declaring_class,
            key=key,
            message_key=message_key,
            static_content_type=static_content_type,
        )

        cs_sys_dynamic_dynamic_class_type.additional_properties = d
        return cs_sys_dynamic_dynamic_class_type

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
