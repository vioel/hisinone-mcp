from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_simple_dynamic_field_component_foreigntext import (
        ImplCsSysDynamicSimpleDynamicFieldComponentForeigntext,
    )


T = TypeVar("T", bound="ImplCsSysDynamicSimpleDynamicFieldComponent")


@_attrs_define
class ImplCsSysDynamicSimpleDynamicFieldComponent:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicSimpleDynamicFieldComponentForeigntext | Unset):
        attribute_name (str | Unset):
        control_type (str | Unset):
        datasource (str | Unset):
        dd_key (str | Unset):
        id (int | Unset):
        label (str | Unset):
        lock_version (int | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
        object_uid (str | Unset):
        position (int | Unset):
        right_level (int | Unset):
        sortorder (int | Unset):
    """

    field_foreigntext: ImplCsSysDynamicSimpleDynamicFieldComponentForeigntext | Unset = UNSET
    attribute_name: str | Unset = UNSET
    control_type: str | Unset = UNSET
    datasource: str | Unset = UNSET
    dd_key: str | Unset = UNSET
    id: int | Unset = UNSET
    label: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    object_uid: str | Unset = UNSET
    position: int | Unset = UNSET
    right_level: int | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        attribute_name = self.attribute_name

        control_type = self.control_type

        datasource = self.datasource

        dd_key = self.dd_key

        id = self.id

        label = self.label

        lock_version = self.lock_version

        name = self.name

        obj_guid = self.obj_guid

        object_uid = self.object_uid

        position = self.position

        right_level = self.right_level

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if control_type is not UNSET:
            field_dict["controlType"] = control_type
        if datasource is not UNSET:
            field_dict["datasource"] = datasource
        if dd_key is not UNSET:
            field_dict["ddKey"] = dd_key
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
        if object_uid is not UNSET:
            field_dict["objectUID"] = object_uid
        if position is not UNSET:
            field_dict["position"] = position
        if right_level is not UNSET:
            field_dict["rightLevel"] = right_level
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_simple_dynamic_field_component_foreigntext import (
            ImplCsSysDynamicSimpleDynamicFieldComponentForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicSimpleDynamicFieldComponentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicSimpleDynamicFieldComponentForeigntext.from_dict(_field_foreigntext)

        attribute_name = d.pop("attributeName", UNSET)

        control_type = d.pop("controlType", UNSET)

        datasource = d.pop("datasource", UNSET)

        dd_key = d.pop("ddKey", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        object_uid = d.pop("objectUID", UNSET)

        position = d.pop("position", UNSET)

        right_level = d.pop("rightLevel", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        impl_cs_sys_dynamic_simple_dynamic_field_component = cls(
            field_foreigntext=field_foreigntext,
            attribute_name=attribute_name,
            control_type=control_type,
            datasource=datasource,
            dd_key=dd_key,
            id=id,
            label=label,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
            object_uid=object_uid,
            position=position,
            right_level=right_level,
            sortorder=sortorder,
        )

        impl_cs_sys_dynamic_simple_dynamic_field_component.additional_properties = d
        return impl_cs_sys_dynamic_simple_dynamic_field_component

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
