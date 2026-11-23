from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_dynamic_class import ImplCsSysDynamicDynamicClass
    from ..models.impl_cs_sys_dynamic_dynamic_object_foreigntext import ImplCsSysDynamicDynamicObjectForeigntext
    from ..models.impl_cs_sys_dynamic_dynamic_value import ImplCsSysDynamicDynamicValue


T = TypeVar("T", bound="ImplCsSysDynamicDynamicObject")


@_attrs_define
class ImplCsSysDynamicDynamicObject:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicDynamicObjectForeigntext | Unset):
        belongs_to_pk (int | Unset):
        children (list[ImplCsSysDynamicDynamicObject] | Unset):
        dynamic_class (ImplCsSysDynamicDynamicClass | Unset):
        dynamic_values (list[ImplCsSysDynamicDynamicValue] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        parent_id (int | Unset):
    """

    field_foreigntext: ImplCsSysDynamicDynamicObjectForeigntext | Unset = UNSET
    belongs_to_pk: int | Unset = UNSET
    children: list[ImplCsSysDynamicDynamicObject] | Unset = UNSET
    dynamic_class: ImplCsSysDynamicDynamicClass | Unset = UNSET
    dynamic_values: list[ImplCsSysDynamicDynamicValue] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        belongs_to_pk = self.belongs_to_pk

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        dynamic_class: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_class, Unset):
            dynamic_class = self.dynamic_class.to_dict()

        dynamic_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dynamic_values, Unset):
            dynamic_values = []
            for dynamic_values_item_data in self.dynamic_values:
                dynamic_values_item = dynamic_values_item_data.to_dict()
                dynamic_values.append(dynamic_values_item)

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if belongs_to_pk is not UNSET:
            field_dict["belongsToPk"] = belongs_to_pk
        if children is not UNSET:
            field_dict["children"] = children
        if dynamic_class is not UNSET:
            field_dict["dynamicClass"] = dynamic_class
        if dynamic_values is not UNSET:
            field_dict["dynamicValues"] = dynamic_values
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_dynamic_class import ImplCsSysDynamicDynamicClass  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_object_foreigntext import ImplCsSysDynamicDynamicObjectForeigntext  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_value import ImplCsSysDynamicDynamicValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicDynamicObjectForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicDynamicObjectForeigntext.from_dict(_field_foreigntext)

        belongs_to_pk = d.pop("belongsToPk", UNSET)

        _children = d.pop("children", UNSET)
        children: list[ImplCsSysDynamicDynamicObject] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ImplCsSysDynamicDynamicObject.from_dict(children_item_data)

                children.append(children_item)

        _dynamic_class = d.pop("dynamicClass", UNSET)
        dynamic_class: ImplCsSysDynamicDynamicClass | Unset
        if isinstance(_dynamic_class, Unset):
            dynamic_class = UNSET
        else:
            dynamic_class = ImplCsSysDynamicDynamicClass.from_dict(_dynamic_class)

        _dynamic_values = d.pop("dynamicValues", UNSET)
        dynamic_values: list[ImplCsSysDynamicDynamicValue] | Unset = UNSET
        if _dynamic_values is not UNSET:
            dynamic_values = []
            for dynamic_values_item_data in _dynamic_values:
                dynamic_values_item = ImplCsSysDynamicDynamicValue.from_dict(dynamic_values_item_data)

                dynamic_values.append(dynamic_values_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        parent_id = d.pop("parentId", UNSET)

        impl_cs_sys_dynamic_dynamic_object = cls(
            field_foreigntext=field_foreigntext,
            belongs_to_pk=belongs_to_pk,
            children=children,
            dynamic_class=dynamic_class,
            dynamic_values=dynamic_values,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            parent_id=parent_id,
        )

        impl_cs_sys_dynamic_dynamic_object.additional_properties = d
        return impl_cs_sys_dynamic_dynamic_object

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
