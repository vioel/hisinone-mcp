from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaTimeLocalTime")


@_attrs_define
class JavaTimeLocalTime:
    """
    Attributes:
        hour (int | Unset):
        minute (int | Unset):
        nano (int | Unset):
        second (int | Unset):
    """

    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    nano: int | Unset = UNSET
    second: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        hour = self.hour

        minute = self.minute

        nano = self.nano

        second = self.second

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute
        if nano is not UNSET:
            field_dict["nano"] = nano
        if second is not UNSET:
            field_dict["second"] = second

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        nano = d.pop("nano", UNSET)

        second = d.pop("second", UNSET)

        java_time_local_time = cls(
            hour=hour,
            minute=minute,
            nano=nano,
            second=second,
        )

        java_time_local_time.additional_properties = d
        return java_time_local_time

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
