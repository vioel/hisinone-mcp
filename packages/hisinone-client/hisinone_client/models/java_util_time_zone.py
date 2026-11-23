from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaUtilTimeZone")


@_attrs_define
class JavaUtilTimeZone:
    """
    Attributes:
        available_i_ds (list[str] | Unset):
        d_st_savings (int | Unset):
        default (JavaUtilTimeZone | Unset):
        display_name (str | Unset):
        i_d (str | Unset):
        raw_offset (int | Unset):
    """

    available_i_ds: list[str] | Unset = UNSET
    d_st_savings: int | Unset = UNSET
    default: JavaUtilTimeZone | Unset = UNSET
    display_name: str | Unset = UNSET
    i_d: str | Unset = UNSET
    raw_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        available_i_ds: list[str] | Unset = UNSET
        if not isinstance(self.available_i_ds, Unset):
            available_i_ds = self.available_i_ds

        d_st_savings = self.d_st_savings

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        display_name = self.display_name

        i_d = self.i_d

        raw_offset = self.raw_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_i_ds is not UNSET:
            field_dict["availableIDs"] = available_i_ds
        if d_st_savings is not UNSET:
            field_dict["dSTSavings"] = d_st_savings
        if default is not UNSET:
            field_dict["default"] = default
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if i_d is not UNSET:
            field_dict["iD"] = i_d
        if raw_offset is not UNSET:
            field_dict["rawOffset"] = raw_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_i_ds = cast(list[str], d.pop("availableIDs", UNSET))

        d_st_savings = d.pop("dSTSavings", UNSET)

        _default = d.pop("default", UNSET)
        default: JavaUtilTimeZone | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = JavaUtilTimeZone.from_dict(_default)

        display_name = d.pop("displayName", UNSET)

        i_d = d.pop("iD", UNSET)

        raw_offset = d.pop("rawOffset", UNSET)

        java_util_time_zone = cls(
            available_i_ds=available_i_ds,
            d_st_savings=d_st_savings,
            default=default,
            display_name=display_name,
            i_d=i_d,
            raw_offset=raw_offset,
        )

        java_util_time_zone.additional_properties = d
        return java_util_time_zone

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
