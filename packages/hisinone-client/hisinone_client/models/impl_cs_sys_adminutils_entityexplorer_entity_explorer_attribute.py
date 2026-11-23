from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute")


@_attrs_define
class ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute:
    """
    Attributes:
        annotations (str | Unset):
        attribute_name (str | Unset):
        class_name (str | Unset):
        i_18_n_key (str | Unset):
        java_doc (str | Unset):
    """

    annotations: str | Unset = UNSET
    attribute_name: str | Unset = UNSET
    class_name: str | Unset = UNSET
    i_18_n_key: str | Unset = UNSET
    java_doc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        annotations = self.annotations

        attribute_name = self.attribute_name

        class_name = self.class_name

        i_18_n_key = self.i_18_n_key

        java_doc = self.java_doc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if i_18_n_key is not UNSET:
            field_dict["i18nKey"] = i_18_n_key
        if java_doc is not UNSET:
            field_dict["javaDoc"] = java_doc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        annotations = d.pop("annotations", UNSET)

        attribute_name = d.pop("attributeName", UNSET)

        class_name = d.pop("className", UNSET)

        i_18_n_key = d.pop("i18nKey", UNSET)

        java_doc = d.pop("javaDoc", UNSET)

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_attribute = cls(
            annotations=annotations,
            attribute_name=attribute_name,
            class_name=class_name,
            i_18_n_key=i_18_n_key,
            java_doc=java_doc,
        )

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_attribute.additional_properties = d
        return impl_cs_sys_adminutils_entityexplorer_entity_explorer_attribute

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
