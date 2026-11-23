from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_time_chrono_chronology import JavaTimeChronoChronology
    from ..models.java_time_day_of_week import JavaTimeDayOfWeek
    from ..models.java_time_month import JavaTimeMonth


T = TypeVar("T", bound="JavaTimeLocalDateTime")


@_attrs_define
class JavaTimeLocalDateTime:
    """
    Attributes:
        chronology (JavaTimeChronoChronology | Unset):
        day_of_month (int | Unset):
        day_of_week (JavaTimeDayOfWeek | Unset):
        day_of_year (int | Unset):
        hour (int | Unset):
        minute (int | Unset):
        month (JavaTimeMonth | Unset):
        month_value (int | Unset):
        nano (int | Unset):
        second (int | Unset):
        year (int | Unset):
    """

    chronology: JavaTimeChronoChronology | Unset = UNSET
    day_of_month: int | Unset = UNSET
    day_of_week: JavaTimeDayOfWeek | Unset = UNSET
    day_of_year: int | Unset = UNSET
    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    month: JavaTimeMonth | Unset = UNSET
    month_value: int | Unset = UNSET
    nano: int | Unset = UNSET
    second: int | Unset = UNSET
    year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        chronology: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chronology, Unset):
            chronology = self.chronology.to_dict()

        day_of_month = self.day_of_month

        day_of_week: dict[str, Any] | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.to_dict()

        day_of_year = self.day_of_year

        hour = self.hour

        minute = self.minute

        month: dict[str, Any] | Unset = UNSET
        if not isinstance(self.month, Unset):
            month = self.month.to_dict()

        month_value = self.month_value

        nano = self.nano

        second = self.second

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chronology is not UNSET:
            field_dict["chronology"] = chronology
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_of_year is not UNSET:
            field_dict["dayOfYear"] = day_of_year
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute
        if month is not UNSET:
            field_dict["month"] = month
        if month_value is not UNSET:
            field_dict["monthValue"] = month_value
        if nano is not UNSET:
            field_dict["nano"] = nano
        if second is not UNSET:
            field_dict["second"] = second
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_time_chrono_chronology import JavaTimeChronoChronology  # noqa: PLC0415
        from ..models.java_time_day_of_week import JavaTimeDayOfWeek  # noqa: PLC0415
        from ..models.java_time_month import JavaTimeMonth  # noqa: PLC0415

        d = dict(src_dict)
        _chronology = d.pop("chronology", UNSET)
        chronology: JavaTimeChronoChronology | Unset
        if isinstance(_chronology, Unset):
            chronology = UNSET
        else:
            chronology = JavaTimeChronoChronology.from_dict(_chronology)

        day_of_month = d.pop("dayOfMonth", UNSET)

        _day_of_week = d.pop("dayOfWeek", UNSET)
        day_of_week: JavaTimeDayOfWeek | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = JavaTimeDayOfWeek.from_dict(_day_of_week)

        day_of_year = d.pop("dayOfYear", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        _month = d.pop("month", UNSET)
        month: JavaTimeMonth | Unset
        if isinstance(_month, Unset):
            month = UNSET
        else:
            month = JavaTimeMonth.from_dict(_month)

        month_value = d.pop("monthValue", UNSET)

        nano = d.pop("nano", UNSET)

        second = d.pop("second", UNSET)

        year = d.pop("year", UNSET)

        java_time_local_date_time = cls(
            chronology=chronology,
            day_of_month=day_of_month,
            day_of_week=day_of_week,
            day_of_year=day_of_year,
            hour=hour,
            minute=minute,
            month=month,
            month_value=month_value,
            nano=nano,
            second=second,
            year=year,
        )

        java_time_local_date_time.additional_properties = d
        return java_time_local_date_time

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
