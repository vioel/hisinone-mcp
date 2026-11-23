from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysAdminutilsEntityexplorerSysEntityExplorerPathRequest")


@_attrs_define
class CsSysAdminutilsEntityexplorerSysEntityExplorerPathRequest:
    """
    Attributes:
        max_path_length (int | Unset):
        start_class_name (str | Unset):
        target_class_name (str | Unset):
    """

    max_path_length: int | Unset = UNSET
    start_class_name: str | Unset = UNSET
    target_class_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        max_path_length = self.max_path_length

        start_class_name = self.start_class_name

        target_class_name = self.target_class_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_path_length is not UNSET:
            field_dict["maxPathLength"] = max_path_length
        if start_class_name is not UNSET:
            field_dict["startClassName"] = start_class_name
        if target_class_name is not UNSET:
            field_dict["targetClassName"] = target_class_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_path_length = d.pop("maxPathLength", UNSET)

        start_class_name = d.pop("startClassName", UNSET)

        target_class_name = d.pop("targetClassName", UNSET)

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_path_request = cls(
            max_path_length=max_path_length,
            start_class_name=start_class_name,
            target_class_name=target_class_name,
        )

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_path_request.additional_properties = d
        return cs_sys_adminutils_entityexplorer_sys_entity_explorer_path_request

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
