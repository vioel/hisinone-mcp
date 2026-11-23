from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_calendar_absence_calendar_event_foreigntext import (
        RmErpAbsencemanagementCalendarAbsenceCalendarEventForeigntext,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementCalendarAbsenceCalendarEvent")


@_attrs_define
class RmErpAbsencemanagementCalendarAbsenceCalendarEvent:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementCalendarAbsenceCalendarEventForeigntext | Unset):
        abbreviation (str | Unset):
        css (str | Unset):
        description (str | Unset):
        id (int | Unset):
        identifier (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarEventForeigntext | Unset = UNSET
    abbreviation: str | Unset = UNSET
    css: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        abbreviation = self.abbreviation

        css = self.css

        description = self.description

        id = self.id

        identifier = self.identifier

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if css is not UNSET:
            field_dict["css"] = css
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_calendar_absence_calendar_event_foreigntext import (
            RmErpAbsencemanagementCalendarAbsenceCalendarEventForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementCalendarAbsenceCalendarEventForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementCalendarAbsenceCalendarEventForeigntext.from_dict(
                _field_foreigntext
            )

        abbreviation = d.pop("abbreviation", UNSET)

        css = d.pop("css", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        rm_erp_absencemanagement_calendar_absence_calendar_event = cls(
            field_foreigntext=field_foreigntext,
            abbreviation=abbreviation,
            css=css,
            description=description,
            id=id,
            identifier=identifier,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        rm_erp_absencemanagement_calendar_absence_calendar_event.additional_properties = d
        return rm_erp_absencemanagement_calendar_absence_calendar_event

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
