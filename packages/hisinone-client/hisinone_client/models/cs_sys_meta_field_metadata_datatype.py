from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysMetaFieldMetadataDatatype")


@_attrs_define
class CsSysMetaFieldMetadataDatatype:
    """
    Attributes:
        declaring_class (Any | Unset):
        message_key (str | Unset):
        name (str | Unset):
    """

    declaring_class: Any | Unset = UNSET
    message_key: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        declaring_class = self.declaring_class

        message_key = self.message_key

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declaring_class = d.pop("declaringClass", UNSET)

        message_key = d.pop("messageKey", UNSET)

        name = d.pop("name", UNSET)

        cs_sys_meta_field_metadata_datatype = cls(
            declaring_class=declaring_class,
            message_key=message_key,
            name=name,
        )

        cs_sys_meta_field_metadata_datatype.additional_properties = d
        return cs_sys_meta_field_metadata_datatype

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
