from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_util_locale import JavaUtilLocale
    from ..models.java_util_time_zone import JavaUtilTimeZone


T = TypeVar("T", bound="JavaUtilCalendar")


@_attrs_define
class JavaUtilCalendar:
    """
    Attributes:
        available_calendar_types (list[str] | Unset):
        available_locales (list[JavaUtilLocale] | Unset):
        calendar_type (str | Unset):
        first_day_of_week (int | Unset):
        instance (JavaUtilCalendar | Unset):
        lenient (bool | Unset):
        minimal_days_in_first_week (int | Unset):
        time (int | Unset):
        time_in_millis (int | Unset):
        time_zone (JavaUtilTimeZone | Unset):
        week_date_supported (bool | Unset):
        week_year (int | Unset):
        weeks_in_week_year (int | Unset):
    """

    available_calendar_types: list[str] | Unset = UNSET
    available_locales: list[JavaUtilLocale] | Unset = UNSET
    calendar_type: str | Unset = UNSET
    first_day_of_week: int | Unset = UNSET
    instance: JavaUtilCalendar | Unset = UNSET
    lenient: bool | Unset = UNSET
    minimal_days_in_first_week: int | Unset = UNSET
    time: int | Unset = UNSET
    time_in_millis: int | Unset = UNSET
    time_zone: JavaUtilTimeZone | Unset = UNSET
    week_date_supported: bool | Unset = UNSET
    week_year: int | Unset = UNSET
    weeks_in_week_year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        available_calendar_types: list[str] | Unset = UNSET
        if not isinstance(self.available_calendar_types, Unset):
            available_calendar_types = self.available_calendar_types

        available_locales: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_locales, Unset):
            available_locales = []
            for available_locales_item_data in self.available_locales:
                available_locales_item = available_locales_item_data.to_dict()
                available_locales.append(available_locales_item)

        calendar_type = self.calendar_type

        first_day_of_week = self.first_day_of_week

        instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance, Unset):
            instance = self.instance.to_dict()

        lenient = self.lenient

        minimal_days_in_first_week = self.minimal_days_in_first_week

        time = self.time

        time_in_millis = self.time_in_millis

        time_zone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone.to_dict()

        week_date_supported = self.week_date_supported

        week_year = self.week_year

        weeks_in_week_year = self.weeks_in_week_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_calendar_types is not UNSET:
            field_dict["availableCalendarTypes"] = available_calendar_types
        if available_locales is not UNSET:
            field_dict["availableLocales"] = available_locales
        if calendar_type is not UNSET:
            field_dict["calendarType"] = calendar_type
        if first_day_of_week is not UNSET:
            field_dict["firstDayOfWeek"] = first_day_of_week
        if instance is not UNSET:
            field_dict["instance"] = instance
        if lenient is not UNSET:
            field_dict["lenient"] = lenient
        if minimal_days_in_first_week is not UNSET:
            field_dict["minimalDaysInFirstWeek"] = minimal_days_in_first_week
        if time is not UNSET:
            field_dict["time"] = time
        if time_in_millis is not UNSET:
            field_dict["timeInMillis"] = time_in_millis
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if week_date_supported is not UNSET:
            field_dict["weekDateSupported"] = week_date_supported
        if week_year is not UNSET:
            field_dict["weekYear"] = week_year
        if weeks_in_week_year is not UNSET:
            field_dict["weeksInWeekYear"] = weeks_in_week_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_util_locale import JavaUtilLocale  # noqa: PLC0415
        from ..models.java_util_time_zone import JavaUtilTimeZone  # noqa: PLC0415

        d = dict(src_dict)
        available_calendar_types = cast(list[str], d.pop("availableCalendarTypes", UNSET))

        _available_locales = d.pop("availableLocales", UNSET)
        available_locales: list[JavaUtilLocale] | Unset = UNSET
        if _available_locales is not UNSET:
            available_locales = []
            for available_locales_item_data in _available_locales:
                available_locales_item = JavaUtilLocale.from_dict(available_locales_item_data)

                available_locales.append(available_locales_item)

        calendar_type = d.pop("calendarType", UNSET)

        first_day_of_week = d.pop("firstDayOfWeek", UNSET)

        _instance = d.pop("instance", UNSET)
        instance: JavaUtilCalendar | Unset
        if isinstance(_instance, Unset):
            instance = UNSET
        else:
            instance = JavaUtilCalendar.from_dict(_instance)

        lenient = d.pop("lenient", UNSET)

        minimal_days_in_first_week = d.pop("minimalDaysInFirstWeek", UNSET)

        time = d.pop("time", UNSET)

        time_in_millis = d.pop("timeInMillis", UNSET)

        _time_zone = d.pop("timeZone", UNSET)
        time_zone: JavaUtilTimeZone | Unset
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = JavaUtilTimeZone.from_dict(_time_zone)

        week_date_supported = d.pop("weekDateSupported", UNSET)

        week_year = d.pop("weekYear", UNSET)

        weeks_in_week_year = d.pop("weeksInWeekYear", UNSET)

        java_util_calendar = cls(
            available_calendar_types=available_calendar_types,
            available_locales=available_locales,
            calendar_type=calendar_type,
            first_day_of_week=first_day_of_week,
            instance=instance,
            lenient=lenient,
            minimal_days_in_first_week=minimal_days_in_first_week,
            time=time,
            time_in_millis=time_in_millis,
            time_zone=time_zone,
            week_date_supported=week_date_supported,
            week_year=week_year,
            weeks_in_week_year=weeks_in_week_year,
        )

        java_util_calendar.additional_properties = d
        return java_util_calendar

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
