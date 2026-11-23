from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaTimeChronoIsoChronology")


@_attrs_define
class JavaTimeChronoIsoChronology:
    """
    Attributes:
        calendar_type (str | Unset):
        id (str | Unset):
    """

    calendar_type: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        calendar_type = self.calendar_type

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calendar_type is not UNSET:
            field_dict["calendarType"] = calendar_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calendar_type = d.pop("calendarType", UNSET)

        id = d.pop("id", UNSET)

        java_time_chrono_iso_chronology = cls(
            calendar_type=calendar_type,
            id=id,
        )

        java_time_chrono_iso_chronology.additional_properties = d
        return java_time_chrono_iso_chronology

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
