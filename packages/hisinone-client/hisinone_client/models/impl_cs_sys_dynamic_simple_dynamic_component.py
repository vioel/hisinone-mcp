from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_simple_dynamic_component_foreigntext_type_0 import (
        ImplCsSysDynamicSimpleDynamicComponentForeigntextType0,
    )
    from ..models.impl_cs_sys_dynamic_simple_dynamic_field_component import ImplCsSysDynamicSimpleDynamicFieldComponent


T = TypeVar("T", bound="ImplCsSysDynamicSimpleDynamicComponent")


@_attrs_define
class ImplCsSysDynamicSimpleDynamicComponent:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicSimpleDynamicComponentForeigntextType0 | None | Unset):
        children (list[ImplCsSysDynamicSimpleDynamicComponent] | Unset):
        control_type (None | str | Unset):
        fields (list[ImplCsSysDynamicSimpleDynamicFieldComponent] | Unset):
        id (int | None | Unset):
        label (None | str | Unset):
        lock_version (int | None | Unset):
        name (None | str | Unset):
        obj_guid (None | str | Unset):
        position (int | None | Unset):
        sortorder (int | None | Unset):
        visible_attributes (bool | None | Unset):
    """

    field_foreigntext: ImplCsSysDynamicSimpleDynamicComponentForeigntextType0 | None | Unset = UNSET
    children: list[ImplCsSysDynamicSimpleDynamicComponent] | Unset = UNSET
    control_type: None | str | Unset = UNSET
    fields: list[ImplCsSysDynamicSimpleDynamicFieldComponent] | Unset = UNSET
    id: int | None | Unset = UNSET
    label: None | str | Unset = UNSET
    lock_version: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    sortorder: int | None | Unset = UNSET
    visible_attributes: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.impl_cs_sys_dynamic_simple_dynamic_component_foreigntext_type_0 import (
            ImplCsSysDynamicSimpleDynamicComponentForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, ImplCsSysDynamicSimpleDynamicComponentForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        control_type: None | str | Unset
        if isinstance(self.control_type, Unset):
            control_type = UNSET
        else:
            control_type = self.control_type

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        lock_version: int | None | Unset
        if isinstance(self.lock_version, Unset):
            lock_version = UNSET
        else:
            lock_version = self.lock_version

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        sortorder: int | None | Unset
        if isinstance(self.sortorder, Unset):
            sortorder = UNSET
        else:
            sortorder = self.sortorder

        visible_attributes: bool | None | Unset
        if isinstance(self.visible_attributes, Unset):
            visible_attributes = UNSET
        else:
            visible_attributes = self.visible_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if children is not UNSET:
            field_dict["children"] = children
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if position is not UNSET:
            field_dict["position"] = position
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if visible_attributes is not UNSET:
            field_dict["visibleAttributes"] = visible_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_simple_dynamic_component_foreigntext_type_0 import (
            ImplCsSysDynamicSimpleDynamicComponentForeigntextType0,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_simple_dynamic_field_component import (
            ImplCsSysDynamicSimpleDynamicFieldComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_field_foreigntext(
            data: object,
        ) -> ImplCsSysDynamicSimpleDynamicComponentForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = ImplCsSysDynamicSimpleDynamicComponentForeigntextType0.from_dict(
                cast(dict[str, Any], data)
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        _children = d.pop("children", UNSET)
        children: list[ImplCsSysDynamicSimpleDynamicComponent] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = ImplCsSysDynamicSimpleDynamicComponent.from_dict(children_item_data)

                children.append(children_item)

        def _parse_control_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        control_type = _parse_control_type(d.pop("controlType", UNSET))

        _fields = d.pop("fields", UNSET)
        fields: list[ImplCsSysDynamicSimpleDynamicFieldComponent] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = ImplCsSysDynamicSimpleDynamicFieldComponent.from_dict(fields_item_data)

                fields.append(fields_item)

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_lock_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lock_version = _parse_lock_version(d.pop("lockVersion", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_sortorder(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sortorder = _parse_sortorder(d.pop("sortorder", UNSET))

        def _parse_visible_attributes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        visible_attributes = _parse_visible_attributes(d.pop("visibleAttributes", UNSET))

        impl_cs_sys_dynamic_simple_dynamic_component = cls(
            field_foreigntext=field_foreigntext,
            children=children,
            control_type=control_type,
            fields=fields,
            id=id,
            label=label,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
            position=position,
            sortorder=sortorder,
            visible_attributes=visible_attributes,
        )

        impl_cs_sys_dynamic_simple_dynamic_component.additional_properties = d
        return impl_cs_sys_dynamic_simple_dynamic_component

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
