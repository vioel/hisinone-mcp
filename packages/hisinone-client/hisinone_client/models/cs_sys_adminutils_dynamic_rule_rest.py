from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysAdminutilsDynamicRuleRest")


@_attrs_define
class CsSysAdminutilsDynamicRuleRest:
    """
    Attributes:
        anchor_position (int | Unset):
        attribute (str | Unset):
        dynamic_class_id (int | Unset):
        dynamic_class_name (str | Unset):
        id (int | Unset):
        name (str | Unset):
        parent_rule_id (int | Unset):
        rule_type_id (int | Unset):
        sortorder (int | Unset):
    """

    anchor_position: int | Unset = UNSET
    attribute: str | Unset = UNSET
    dynamic_class_id: int | Unset = UNSET
    dynamic_class_name: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    parent_rule_id: int | Unset = UNSET
    rule_type_id: int | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        anchor_position = self.anchor_position

        attribute = self.attribute

        dynamic_class_id = self.dynamic_class_id

        dynamic_class_name = self.dynamic_class_name

        id = self.id

        name = self.name

        parent_rule_id = self.parent_rule_id

        rule_type_id = self.rule_type_id

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anchor_position is not UNSET:
            field_dict["anchorPosition"] = anchor_position
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if dynamic_class_id is not UNSET:
            field_dict["dynamicClassId"] = dynamic_class_id
        if dynamic_class_name is not UNSET:
            field_dict["dynamicClassName"] = dynamic_class_name
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_rule_id is not UNSET:
            field_dict["parentRuleId"] = parent_rule_id
        if rule_type_id is not UNSET:
            field_dict["ruleTypeId"] = rule_type_id
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anchor_position = d.pop("anchorPosition", UNSET)

        attribute = d.pop("attribute", UNSET)

        dynamic_class_id = d.pop("dynamicClassId", UNSET)

        dynamic_class_name = d.pop("dynamicClassName", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parent_rule_id = d.pop("parentRuleId", UNSET)

        rule_type_id = d.pop("ruleTypeId", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        cs_sys_adminutils_dynamic_rule_rest = cls(
            anchor_position=anchor_position,
            attribute=attribute,
            dynamic_class_id=dynamic_class_id,
            dynamic_class_name=dynamic_class_name,
            id=id,
            name=name,
            parent_rule_id=parent_rule_id,
            rule_type_id=rule_type_id,
            sortorder=sortorder,
        )

        cs_sys_adminutils_dynamic_rule_rest.additional_properties = d
        return cs_sys_adminutils_dynamic_rule_rest

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
