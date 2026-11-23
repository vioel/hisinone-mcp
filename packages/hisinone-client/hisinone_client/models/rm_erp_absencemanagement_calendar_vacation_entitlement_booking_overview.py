from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry import (
        RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry,
    )
    from ..models.rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_foreigntext import (
        RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewForeigntext,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementCalendarVacationEntitlementBookingOverview")


@_attrs_define
class RmErpAbsencemanagementCalendarVacationEntitlementBookingOverview:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewForeigntext | Unset):
        entries (list[RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewForeigntext | Unset = UNSET
    entries: list[RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if entries is not UNSET:
            field_dict["entries"] = entries
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry import (
            RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_foreigntext import (
            RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewForeigntext.from_dict(
                _field_foreigntext
            )

        _entries = d.pop("entries", UNSET)
        entries: list[RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry.from_dict(
                    entries_item_data
                )

                entries.append(entries_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview = cls(
            field_foreigntext=field_foreigntext,
            entries=entries,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview.additional_properties = d
        return rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview

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
