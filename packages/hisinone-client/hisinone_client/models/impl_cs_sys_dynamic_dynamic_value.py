from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_dynamic_attribute import ImplCsSysDynamicDynamicAttribute
    from ..models.impl_cs_sys_dynamic_dynamic_value_foreigntext import ImplCsSysDynamicDynamicValueForeigntext


T = TypeVar("T", bound="ImplCsSysDynamicDynamicValue")


@_attrs_define
class ImplCsSysDynamicDynamicValue:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicDynamicValueForeigntext | Unset):
        dynamic_attribute (ImplCsSysDynamicDynamicAttribute | Unset):
        dynamic_object_id (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        val (str | Unset):
    """

    field_foreigntext: ImplCsSysDynamicDynamicValueForeigntext | Unset = UNSET
    dynamic_attribute: ImplCsSysDynamicDynamicAttribute | Unset = UNSET
    dynamic_object_id: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    val: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        dynamic_attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_attribute, Unset):
            dynamic_attribute = self.dynamic_attribute.to_dict()

        dynamic_object_id = self.dynamic_object_id

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        val = self.val

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if dynamic_attribute is not UNSET:
            field_dict["dynamicAttribute"] = dynamic_attribute
        if dynamic_object_id is not UNSET:
            field_dict["dynamicObjectId"] = dynamic_object_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if val is not UNSET:
            field_dict["val"] = val

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_dynamic_attribute import ImplCsSysDynamicDynamicAttribute  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_value_foreigntext import ImplCsSysDynamicDynamicValueForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicDynamicValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicDynamicValueForeigntext.from_dict(_field_foreigntext)

        _dynamic_attribute = d.pop("dynamicAttribute", UNSET)
        dynamic_attribute: ImplCsSysDynamicDynamicAttribute | Unset
        if isinstance(_dynamic_attribute, Unset):
            dynamic_attribute = UNSET
        else:
            dynamic_attribute = ImplCsSysDynamicDynamicAttribute.from_dict(_dynamic_attribute)

        dynamic_object_id = d.pop("dynamicObjectId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        val = d.pop("val", UNSET)

        impl_cs_sys_dynamic_dynamic_value = cls(
            field_foreigntext=field_foreigntext,
            dynamic_attribute=dynamic_attribute,
            dynamic_object_id=dynamic_object_id,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            val=val,
        )

        impl_cs_sys_dynamic_dynamic_value.additional_properties = d
        return impl_cs_sys_dynamic_dynamic_value

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
