from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_day import (
        RmErpAbsencemanagementCalendarAbsenceCalendarDay,
    )
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_month_foreigntext import (
        RmErpAbsencemanagementCalendarAbsenceCalendarMonthForeigntext,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementCalendarAbsenceCalendarMonth")


@_attrs_define
class RmErpAbsencemanagementCalendarAbsenceCalendarMonth:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementCalendarAbsenceCalendarMonthForeigntext | Unset):
        days (list[RmErpAbsencemanagementCalendarAbsenceCalendarDay] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        month_id (int | Unset):
        month_of_year (str | Unset):
        obj_guid (str | Unset):
        year (int | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarMonthForeigntext | Unset = UNSET
    days: list[RmErpAbsencemanagementCalendarAbsenceCalendarDay] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    month_id: int | Unset = UNSET
    month_of_year: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        id = self.id

        lock_version = self.lock_version

        month_id = self.month_id

        month_of_year = self.month_of_year

        obj_guid = self.obj_guid

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if days is not UNSET:
            field_dict["days"] = days
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if month_id is not UNSET:
            field_dict["monthId"] = month_id
        if month_of_year is not UNSET:
            field_dict["monthOfYear"] = month_of_year
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_day import (
            RmErpAbsencemanagementCalendarAbsenceCalendarDay,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_month_foreigntext import (
            RmErpAbsencemanagementCalendarAbsenceCalendarMonthForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarMonthForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementCalendarAbsenceCalendarMonthForeigntext.from_dict(
                _field_foreigntext
            )

        _days = d.pop("days", UNSET)
        days: list[RmErpAbsencemanagementCalendarAbsenceCalendarDay] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = RmErpAbsencemanagementCalendarAbsenceCalendarDay.from_dict(days_item_data)

                days.append(days_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        month_id = d.pop("monthId", UNSET)

        month_of_year = d.pop("monthOfYear", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        year = d.pop("year", UNSET)

        rm_erp_absencemanagement_calendar_absence_calendar_month = cls(
            field_foreigntext=field_foreigntext,
            days=days,
            id=id,
            lock_version=lock_version,
            month_id=month_id,
            month_of_year=month_of_year,
            obj_guid=obj_guid,
            year=year,
        )

        rm_erp_absencemanagement_calendar_absence_calendar_month.additional_properties = d
        return rm_erp_absencemanagement_calendar_absence_calendar_month

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
