from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_simple_dynamic_value_foreigntext import (
        ImplCsSysDynamicSimpleDynamicValueForeigntext,
    )


T = TypeVar("T", bound="ImplCsSysDynamicSimpleDynamicValue")


@_attrs_define
class ImplCsSysDynamicSimpleDynamicValue:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicSimpleDynamicValueForeigntext | Unset):
        attribute_name (str | Unset):
        attribute_type (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        old_value (str | Unset):
        source (str | Unset):
        use_old_value (bool | Unset):
        value (str | Unset):
    """

    field_foreigntext: ImplCsSysDynamicSimpleDynamicValueForeigntext | Unset = UNSET
    attribute_name: str | Unset = UNSET
    attribute_type: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    old_value: str | Unset = UNSET
    source: str | Unset = UNSET
    use_old_value: bool | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        attribute_name = self.attribute_name

        attribute_type = self.attribute_type

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        old_value = self.old_value

        source = self.source

        use_old_value = self.use_old_value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if attribute_type is not UNSET:
            field_dict["attributeType"] = attribute_type
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if source is not UNSET:
            field_dict["source"] = source
        if use_old_value is not UNSET:
            field_dict["useOldValue"] = use_old_value
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_simple_dynamic_value_foreigntext import (
            ImplCsSysDynamicSimpleDynamicValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicSimpleDynamicValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicSimpleDynamicValueForeigntext.from_dict(_field_foreigntext)

        attribute_name = d.pop("attributeName", UNSET)

        attribute_type = d.pop("attributeType", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        old_value = d.pop("oldValue", UNSET)

        source = d.pop("source", UNSET)

        use_old_value = d.pop("useOldValue", UNSET)

        value = d.pop("value", UNSET)

        impl_cs_sys_dynamic_simple_dynamic_value = cls(
            field_foreigntext=field_foreigntext,
            attribute_name=attribute_name,
            attribute_type=attribute_type,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            old_value=old_value,
            source=source,
            use_old_value=use_old_value,
            value=value,
        )

        impl_cs_sys_dynamic_simple_dynamic_value.additional_properties = d
        return impl_cs_sys_dynamic_simple_dynamic_value

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
