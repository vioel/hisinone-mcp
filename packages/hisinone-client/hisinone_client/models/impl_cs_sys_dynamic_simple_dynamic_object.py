from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_simple_dynamic_object_foreigntext_type_0 import (
        ImplCsSysDynamicSimpleDynamicObjectForeigntextType0,
    )
    from ..models.impl_cs_sys_dynamic_simple_dynamic_value import ImplCsSysDynamicSimpleDynamicValue


T = TypeVar("T", bound="ImplCsSysDynamicSimpleDynamicObject")


@_attrs_define
class ImplCsSysDynamicSimpleDynamicObject:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicSimpleDynamicObjectForeigntextType0 | None | Unset):
        dynamic_class_name (str | Unset):
        id (int | None | Unset):
        lock_version (int | None | Unset):
        obj_guid (str | Unset):
        parent_object_guid (None | str | Unset):
        values (list[ImplCsSysDynamicSimpleDynamicValue] | Unset):
    """

    field_foreigntext: ImplCsSysDynamicSimpleDynamicObjectForeigntextType0 | None | Unset = UNSET
    dynamic_class_name: str | Unset = UNSET
    id: int | None | Unset = UNSET
    lock_version: int | None | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent_object_guid: None | str | Unset = UNSET
    values: list[ImplCsSysDynamicSimpleDynamicValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.impl_cs_sys_dynamic_simple_dynamic_object_foreigntext_type_0 import (
            ImplCsSysDynamicSimpleDynamicObjectForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, ImplCsSysDynamicSimpleDynamicObjectForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        dynamic_class_name = self.dynamic_class_name

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        lock_version: int | None | Unset
        if isinstance(self.lock_version, Unset):
            lock_version = UNSET
        else:
            lock_version = self.lock_version

        obj_guid = self.obj_guid

        parent_object_guid: None | str | Unset
        if isinstance(self.parent_object_guid, Unset):
            parent_object_guid = UNSET
        else:
            parent_object_guid = self.parent_object_guid

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if dynamic_class_name is not UNSET:
            field_dict["dynamicClassName"] = dynamic_class_name
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent_object_guid is not UNSET:
            field_dict["parentObjectGuid"] = parent_object_guid
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_simple_dynamic_object_foreigntext_type_0 import (
            ImplCsSysDynamicSimpleDynamicObjectForeigntextType0,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_simple_dynamic_value import ImplCsSysDynamicSimpleDynamicValue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_field_foreigntext(
            data: object,
        ) -> ImplCsSysDynamicSimpleDynamicObjectForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = ImplCsSysDynamicSimpleDynamicObjectForeigntextType0.from_dict(
                cast(dict[str, Any], data)
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        dynamic_class_name = d.pop("dynamicClassName", UNSET)

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_lock_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lock_version = _parse_lock_version(d.pop("lockVersion", UNSET))

        obj_guid = d.pop("objGuid", UNSET)

        def _parse_parent_object_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_object_guid = _parse_parent_object_guid(d.pop("parentObjectGuid", UNSET))

        _values = d.pop("values", UNSET)
        values: list[ImplCsSysDynamicSimpleDynamicValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ImplCsSysDynamicSimpleDynamicValue.from_dict(values_item_data)

                values.append(values_item)

        impl_cs_sys_dynamic_simple_dynamic_object = cls(
            field_foreigntext=field_foreigntext,
            dynamic_class_name=dynamic_class_name,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            parent_object_guid=parent_object_guid,
            values=values,
        )

        impl_cs_sys_dynamic_simple_dynamic_object.additional_properties = d
        return impl_cs_sys_dynamic_simple_dynamic_object

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
