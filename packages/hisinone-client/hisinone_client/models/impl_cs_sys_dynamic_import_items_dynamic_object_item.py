from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_import_items_dynamic_value_item import ImplCsSysDynamicImportItemsDynamicValueItem


T = TypeVar("T", bound="ImplCsSysDynamicImportItemsDynamicObjectItem")


@_attrs_define
class ImplCsSysDynamicImportItemsDynamicObjectItem:
    """
    Attributes:
        dynamic_class_name (str | Unset):
        values (list[ImplCsSysDynamicImportItemsDynamicValueItem] | Unset):
    """

    dynamic_class_name: str | Unset = UNSET
    values: list[ImplCsSysDynamicImportItemsDynamicValueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        dynamic_class_name = self.dynamic_class_name

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dynamic_class_name is not UNSET:
            field_dict["dynamicClassName"] = dynamic_class_name
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_import_items_dynamic_value_item import (
            ImplCsSysDynamicImportItemsDynamicValueItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        dynamic_class_name = d.pop("dynamicClassName", UNSET)

        _values = d.pop("values", UNSET)
        values: list[ImplCsSysDynamicImportItemsDynamicValueItem] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = ImplCsSysDynamicImportItemsDynamicValueItem.from_dict(values_item_data)

                values.append(values_item)

        impl_cs_sys_dynamic_import_items_dynamic_object_item = cls(
            dynamic_class_name=dynamic_class_name,
            values=values,
        )

        impl_cs_sys_dynamic_import_items_dynamic_object_item.additional_properties = d
        return impl_cs_sys_dynamic_import_items_dynamic_object_item

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
