from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_day_attribute import (
        RmErpAbsencemanagementCalendarAbsenceCalendarDayAttribute,
    )
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_day_foreigntext import (
        RmErpAbsencemanagementCalendarAbsenceCalendarDayForeigntext,
    )
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_event import (
        RmErpAbsencemanagementCalendarAbsenceCalendarEvent,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementCalendarAbsenceCalendarDay")


@_attrs_define
class RmErpAbsencemanagementCalendarAbsenceCalendarDay:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementCalendarAbsenceCalendarDayForeigntext | Unset):
        day_attributes (list[RmErpAbsencemanagementCalendarAbsenceCalendarDayAttribute] | Unset):
        day_id (int | Unset):
        day_of_week (str | Unset):
        events (list[RmErpAbsencemanagementCalendarAbsenceCalendarEvent] | Unset):
        id (int | Unset):
        is_selected (bool | Unset):
        is_today (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarDayForeigntext | Unset = UNSET
    day_attributes: list[RmErpAbsencemanagementCalendarAbsenceCalendarDayAttribute] | Unset = UNSET
    day_id: int | Unset = UNSET
    day_of_week: str | Unset = UNSET
    events: list[RmErpAbsencemanagementCalendarAbsenceCalendarEvent] | Unset = UNSET
    id: int | Unset = UNSET
    is_selected: bool | Unset = UNSET
    is_today: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        day_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.day_attributes, Unset):
            day_attributes = []
            for day_attributes_item_data in self.day_attributes:
                day_attributes_item = day_attributes_item_data.to_dict()
                day_attributes.append(day_attributes_item)

        day_id = self.day_id

        day_of_week = self.day_of_week

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        id = self.id

        is_selected = self.is_selected

        is_today = self.is_today

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if day_attributes is not UNSET:
            field_dict["dayAttributes"] = day_attributes
        if day_id is not UNSET:
            field_dict["dayId"] = day_id
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if events is not UNSET:
            field_dict["events"] = events
        if id is not UNSET:
            field_dict["id"] = id
        if is_selected is not UNSET:
            field_dict["isSelected"] = is_selected
        if is_today is not UNSET:
            field_dict["isToday"] = is_today
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_day_attribute import (
            RmErpAbsencemanagementCalendarAbsenceCalendarDayAttribute,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_day_foreigntext import (
            RmErpAbsencemanagementCalendarAbsenceCalendarDayForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_event import (
            RmErpAbsencemanagementCalendarAbsenceCalendarEvent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarDayForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementCalendarAbsenceCalendarDayForeigntext.from_dict(
                _field_foreigntext
            )

        _day_attributes = d.pop("dayAttributes", UNSET)
        day_attributes: list[RmErpAbsencemanagementCalendarAbsenceCalendarDayAttribute] | Unset = UNSET
        if _day_attributes is not UNSET:
            day_attributes = []
            for day_attributes_item_data in _day_attributes:
                day_attributes_item = RmErpAbsencemanagementCalendarAbsenceCalendarDayAttribute.from_dict(
                    day_attributes_item_data
                )

                day_attributes.append(day_attributes_item)

        day_id = d.pop("dayId", UNSET)

        day_of_week = d.pop("dayOfWeek", UNSET)

        _events = d.pop("events", UNSET)
        events: list[RmErpAbsencemanagementCalendarAbsenceCalendarEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = RmErpAbsencemanagementCalendarAbsenceCalendarEvent.from_dict(events_item_data)

                events.append(events_item)

        id = d.pop("id", UNSET)

        is_selected = d.pop("isSelected", UNSET)

        is_today = d.pop("isToday", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        rm_erp_absencemanagement_calendar_absence_calendar_day = cls(
            field_foreigntext=field_foreigntext,
            day_attributes=day_attributes,
            day_id=day_id,
            day_of_week=day_of_week,
            events=events,
            id=id,
            is_selected=is_selected,
            is_today=is_today,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        rm_erp_absencemanagement_calendar_absence_calendar_day.additional_properties = d
        return rm_erp_absencemanagement_calendar_absence_calendar_day

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
