from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImplCsSysDynamicImportItemsDynamicValueItem")


@_attrs_define
class ImplCsSysDynamicImportItemsDynamicValueItem:
    """
    Attributes:
        attribute_name (str | Unset):
        hiskey_id (int | Unset):
        obj_guid (str | Unset):
        value (str | Unset):
    """

    attribute_name: str | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attribute_name = self.attribute_name

        hiskey_id = self.hiskey_id

        obj_guid = self.obj_guid

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attribute_name = d.pop("attributeName", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        value = d.pop("value", UNSET)

        impl_cs_sys_dynamic_import_items_dynamic_value_item = cls(
            attribute_name=attribute_name,
            hiskey_id=hiskey_id,
            obj_guid=obj_guid,
            value=value,
        )

        impl_cs_sys_dynamic_import_items_dynamic_value_item.additional_properties = d
        return impl_cs_sys_dynamic_import_items_dynamic_value_item

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
