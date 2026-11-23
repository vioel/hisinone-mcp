from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest")


@_attrs_define
class CsSysAdminutilsEntityexplorerSysEntityExplorerSimulationRequest:
    """
    Attributes:
        selected_path (str | Unset):
        start_class (str | Unset):
        start_class_attribute (str | Unset):
        start_class_attribute_value (str | Unset):
        target_class (str | Unset):
        target_class_attribute (str | Unset):
    """

    selected_path: str | Unset = UNSET
    start_class: str | Unset = UNSET
    start_class_attribute: str | Unset = UNSET
    start_class_attribute_value: str | Unset = UNSET
    target_class: str | Unset = UNSET
    target_class_attribute: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        selected_path = self.selected_path

        start_class = self.start_class

        start_class_attribute = self.start_class_attribute

        start_class_attribute_value = self.start_class_attribute_value

        target_class = self.target_class

        target_class_attribute = self.target_class_attribute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selected_path is not UNSET:
            field_dict["selectedPath"] = selected_path
        if start_class is not UNSET:
            field_dict["startClass"] = start_class
        if start_class_attribute is not UNSET:
            field_dict["startClassAttribute"] = start_class_attribute
        if start_class_attribute_value is not UNSET:
            field_dict["startClassAttributeValue"] = start_class_attribute_value
        if target_class is not UNSET:
            field_dict["targetClass"] = target_class
        if target_class_attribute is not UNSET:
            field_dict["targetClassAttribute"] = target_class_attribute

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        selected_path = d.pop("selectedPath", UNSET)

        start_class = d.pop("startClass", UNSET)

        start_class_attribute = d.pop("startClassAttribute", UNSET)

        start_class_attribute_value = d.pop("startClassAttributeValue", UNSET)

        target_class = d.pop("targetClass", UNSET)

        target_class_attribute = d.pop("targetClassAttribute", UNSET)

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_simulation_request = cls(
            selected_path=selected_path,
            start_class=start_class,
            start_class_attribute=start_class_attribute,
            start_class_attribute_value=start_class_attribute_value,
            target_class=target_class,
            target_class_attribute=target_class_attribute,
        )

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_simulation_request.additional_properties = d
        return cs_sys_adminutils_entityexplorer_sys_entity_explorer_simulation_request

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
