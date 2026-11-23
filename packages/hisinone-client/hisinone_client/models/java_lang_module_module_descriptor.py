from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaLangModuleModuleDescriptor")


@_attrs_define
class JavaLangModuleModuleDescriptor:
    """
    Attributes:
        automatic (bool | Unset):
        open_ (bool | Unset):
    """

    automatic: bool | Unset = UNSET
    open_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        automatic = self.automatic

        open_ = self.open_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automatic is not UNSET:
            field_dict["automatic"] = automatic
        if open_ is not UNSET:
            field_dict["open"] = open_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automatic = d.pop("automatic", UNSET)

        open_ = d.pop("open", UNSET)

        java_lang_module_module_descriptor = cls(
            automatic=automatic,
            open_=open_,
        )

        java_lang_module_module_descriptor.additional_properties = d
        return java_lang_module_module_descriptor

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
