from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RmErpTimemanagementWebTimeRecordTypeEnum")


@_attrs_define
class RmErpTimemanagementWebTimeRecordTypeEnum:
    """
    Attributes:
        declaring_class (Any | Unset):
        record_type_ident (int | Unset):
    """

    declaring_class: Any | Unset = UNSET
    record_type_ident: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        declaring_class = self.declaring_class

        record_type_ident = self.record_type_ident

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if record_type_ident is not UNSET:
            field_dict["recordTypeIdent"] = record_type_ident

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declaring_class = d.pop("declaringClass", UNSET)

        record_type_ident = d.pop("recordTypeIdent", UNSET)

        rm_erp_timemanagement_web_time_record_type_enum = cls(
            declaring_class=declaring_class,
            record_type_ident=record_type_ident,
        )

        rm_erp_timemanagement_web_time_record_type_enum.additional_properties = d
        return rm_erp_timemanagement_web_time_record_type_enum

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
