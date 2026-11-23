from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.impl_cs_sys_dynamic_dynamic_class import ImplCsSysDynamicDynamicClass
    from ..models.impl_cs_sys_dynamic_dynamic_rule_foreigntext import ImplCsSysDynamicDynamicRuleForeigntext


T = TypeVar("T", bound="ImplCsSysDynamicDynamicRule")


@_attrs_define
class ImplCsSysDynamicDynamicRule:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicDynamicRuleForeigntext | Unset):
        attribute_name (str | Unset):
        children (list[ImplCsSysDynamicDynamicRule] | Unset):
        dynamic_class (ImplCsSysDynamicDynamicClass | Unset):
        hiskey_id (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        parent_id (int | Unset):
        position (int | Unset):
        rule_name (str | Unset):
        rule_type (CsSysValueGenericValue | Unset):
        sortorder (int | Unset):
    """

    field_foreigntext: ImplCsSysDynamicDynamicRuleForeigntext | Unset = UNSET
    attribute_name: str | Unset = UNSET
    children: list[ImplCsSysDynamicDynamicRule] | Unset = UNSET
    dynamic_class: ImplCsSysDynamicDynamicClass | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent_id: int | Unset = UNSET
    position: int | Unset = UNSET
    rule_name: str | Unset = UNSET
    rule_type: CsSysValueGenericValue | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        attribute_name = self.attribute_name

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        dynamic_class: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_class, Unset):
            dynamic_class = self.dynamic_class.to_dict()

        hiskey_id = self.hiskey_id

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        parent_id = self.parent_id

        position = self.position

        rule_name = self.rule_name

        rule_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule_type, Unset):
            rule_type = self.rule_type.to_dict()

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if children is not UNSET:
            field_dict["children"] = children
        if dynamic_class is not UNSET:
            field_dict["dynamicClass"] = dynamic_class
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if position is not UNSET:
            field_dict["position"] = position
        if rule_name is not UNSET:
            field_dict["ruleName"] = rule_name
        if rule_type is not UNSET:
            field_dict["ruleType"] = rule_type
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_class import ImplCsSysDynamicDynamicClass  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_rule_foreigntext import ImplCsSysDynamicDynamicRuleForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicDynamicRuleForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicDynamicRuleForeigntext.from_dict(_field_foreigntext)

        attribute_name = d.pop("attributeName", UNSET)

        _children = d.pop("children", UNSET)
        children: list[ImplCsSysDynamicDynamicRule] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ImplCsSysDynamicDynamicRule.from_dict(children_item_data)

                children.append(children_item)

        _dynamic_class = d.pop("dynamicClass", UNSET)
        dynamic_class: ImplCsSysDynamicDynamicClass | Unset
        if isinstance(_dynamic_class, Unset):
            dynamic_class = UNSET
        else:
            dynamic_class = ImplCsSysDynamicDynamicClass.from_dict(_dynamic_class)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        parent_id = d.pop("parentId", UNSET)

        position = d.pop("position", UNSET)

        rule_name = d.pop("ruleName", UNSET)

        _rule_type = d.pop("ruleType", UNSET)
        rule_type: CsSysValueGenericValue | Unset
        if isinstance(_rule_type, Unset):
            rule_type = UNSET
        else:
            rule_type = CsSysValueGenericValue.from_dict(_rule_type)

        sortorder = d.pop("sortorder", UNSET)

        impl_cs_sys_dynamic_dynamic_rule = cls(
            field_foreigntext=field_foreigntext,
            attribute_name=attribute_name,
            children=children,
            dynamic_class=dynamic_class,
            hiskey_id=hiskey_id,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            parent_id=parent_id,
            position=position,
            rule_name=rule_name,
            rule_type=rule_type,
            sortorder=sortorder,
        )

        impl_cs_sys_dynamic_dynamic_rule.additional_properties = d
        return impl_cs_sys_dynamic_dynamic_rule

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
