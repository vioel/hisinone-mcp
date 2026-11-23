from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_foreigntext import (
        RmErpAbsencemanagementCalendarAbsenceCalendarForeigntext,
    )
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_month import (
        RmErpAbsencemanagementCalendarAbsenceCalendarMonth,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementCalendarAbsenceCalendar")


@_attrs_define
class RmErpAbsencemanagementCalendarAbsenceCalendar:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementCalendarAbsenceCalendarForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        maximum_timestamp (int | Unset):
        minimum_timestamp (int | Unset):
        months (list[RmErpAbsencemanagementCalendarAbsenceCalendarMonth] | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    maximum_timestamp: int | Unset = UNSET
    minimum_timestamp: int | Unset = UNSET
    months: list[RmErpAbsencemanagementCalendarAbsenceCalendarMonth] | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        maximum_timestamp = self.maximum_timestamp

        minimum_timestamp = self.minimum_timestamp

        months: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.months, Unset):
            months = []
            for months_item_data in self.months:
                months_item = months_item_data.to_dict()
                months.append(months_item)

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if maximum_timestamp is not UNSET:
            field_dict["maximumTimestamp"] = maximum_timestamp
        if minimum_timestamp is not UNSET:
            field_dict["minimumTimestamp"] = minimum_timestamp
        if months is not UNSET:
            field_dict["months"] = months
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_foreigntext import (
            RmErpAbsencemanagementCalendarAbsenceCalendarForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_month import (
            RmErpAbsencemanagementCalendarAbsenceCalendarMonth,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementCalendarAbsenceCalendarForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        maximum_timestamp = d.pop("maximumTimestamp", UNSET)

        minimum_timestamp = d.pop("minimumTimestamp", UNSET)

        _months = d.pop("months", UNSET)
        months: list[RmErpAbsencemanagementCalendarAbsenceCalendarMonth] | Unset = UNSET
        if _months is not UNSET:
            months = []
            for months_item_data in _months:
                months_item = RmErpAbsencemanagementCalendarAbsenceCalendarMonth.from_dict(months_item_data)

                months.append(months_item)

        obj_guid = d.pop("objGuid", UNSET)

        rm_erp_absencemanagement_calendar_absence_calendar = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            maximum_timestamp=maximum_timestamp,
            minimum_timestamp=minimum_timestamp,
            months=months,
            obj_guid=obj_guid,
        )

        rm_erp_absencemanagement_calendar_absence_calendar.additional_properties = d
        return rm_erp_absencemanagement_calendar_absence_calendar

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
