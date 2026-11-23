from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation")


@_attrs_define
class ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation:
    """
    Attributes:
        annotations (str | Unset):
        association_name (str | Unset):
        class_name (str | Unset):
        i_18_n_key (str | Unset):
        ignore_in_path_search (bool | Unset):
        java_doc (str | Unset):
        relation_type (str | Unset):
    """

    annotations: str | Unset = UNSET
    association_name: str | Unset = UNSET
    class_name: str | Unset = UNSET
    i_18_n_key: str | Unset = UNSET
    ignore_in_path_search: bool | Unset = UNSET
    java_doc: str | Unset = UNSET
    relation_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        annotations = self.annotations

        association_name = self.association_name

        class_name = self.class_name

        i_18_n_key = self.i_18_n_key

        ignore_in_path_search = self.ignore_in_path_search

        java_doc = self.java_doc

        relation_type = self.relation_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if association_name is not UNSET:
            field_dict["associationName"] = association_name
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if i_18_n_key is not UNSET:
            field_dict["i18nKey"] = i_18_n_key
        if ignore_in_path_search is not UNSET:
            field_dict["ignoreInPathSearch"] = ignore_in_path_search
        if java_doc is not UNSET:
            field_dict["javaDoc"] = java_doc
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        annotations = d.pop("annotations", UNSET)

        association_name = d.pop("associationName", UNSET)

        class_name = d.pop("className", UNSET)

        i_18_n_key = d.pop("i18nKey", UNSET)

        ignore_in_path_search = d.pop("ignoreInPathSearch", UNSET)

        java_doc = d.pop("javaDoc", UNSET)

        relation_type = d.pop("relationType", UNSET)

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_association = cls(
            annotations=annotations,
            association_name=association_name,
            class_name=class_name,
            i_18_n_key=i_18_n_key,
            ignore_in_path_search=ignore_in_path_search,
            java_doc=java_doc,
            relation_type=relation_type,
        )

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_association.additional_properties = d
        return impl_cs_sys_adminutils_entityexplorer_entity_explorer_association

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
