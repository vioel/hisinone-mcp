from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry_foreigntext import (
        RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntryForeigntext,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry")


@_attrs_define
class RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntry:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntryForeigntext | Unset):
        effective_year (int | Unset):
        expiration_date (int | Unset):
        id (int | Unset):
        initial_amount_of_vacation_days_in_related_year (float | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        related_year (int | Unset):
        remaining_amount_of_vacation_days_in_related_year (float | Unset):
        vacation_entitlement_type (str | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntryForeigntext | Unset = UNSET
    effective_year: int | Unset = UNSET
    expiration_date: int | Unset = UNSET
    id: int | Unset = UNSET
    initial_amount_of_vacation_days_in_related_year: float | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    related_year: int | Unset = UNSET
    remaining_amount_of_vacation_days_in_related_year: float | Unset = UNSET
    vacation_entitlement_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        effective_year = self.effective_year

        expiration_date = self.expiration_date

        id = self.id

        initial_amount_of_vacation_days_in_related_year = self.initial_amount_of_vacation_days_in_related_year

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        related_year = self.related_year

        remaining_amount_of_vacation_days_in_related_year = self.remaining_amount_of_vacation_days_in_related_year

        vacation_entitlement_type = self.vacation_entitlement_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if effective_year is not UNSET:
            field_dict["effectiveYear"] = effective_year
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if id is not UNSET:
            field_dict["id"] = id
        if initial_amount_of_vacation_days_in_related_year is not UNSET:
            field_dict["initialAmountOfVacationDaysInRelatedYear"] = initial_amount_of_vacation_days_in_related_year
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if related_year is not UNSET:
            field_dict["relatedYear"] = related_year
        if remaining_amount_of_vacation_days_in_related_year is not UNSET:
            field_dict["remainingAmountOfVacationDaysInRelatedYear"] = remaining_amount_of_vacation_days_in_related_year
        if vacation_entitlement_type is not UNSET:
            field_dict["vacationEntitlementType"] = vacation_entitlement_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry_foreigntext import (
            RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntryForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntryForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                RmErpAbsencemanagementCalendarVacationEntitlementBookingOverviewEntryForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        effective_year = d.pop("effectiveYear", UNSET)

        expiration_date = d.pop("expirationDate", UNSET)

        id = d.pop("id", UNSET)

        initial_amount_of_vacation_days_in_related_year = d.pop("initialAmountOfVacationDaysInRelatedYear", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        related_year = d.pop("relatedYear", UNSET)

        remaining_amount_of_vacation_days_in_related_year = d.pop("remainingAmountOfVacationDaysInRelatedYear", UNSET)

        vacation_entitlement_type = d.pop("vacationEntitlementType", UNSET)

        rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry = cls(
            field_foreigntext=field_foreigntext,
            effective_year=effective_year,
            expiration_date=expiration_date,
            id=id,
            initial_amount_of_vacation_days_in_related_year=initial_amount_of_vacation_days_in_related_year,
            lock_version=lock_version,
            obj_guid=obj_guid,
            related_year=related_year,
            remaining_amount_of_vacation_days_in_related_year=remaining_amount_of_vacation_days_in_related_year,
            vacation_entitlement_type=vacation_entitlement_type,
        )

        rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry.additional_properties = d
        return rm_erp_absencemanagement_calendar_vacation_entitlement_booking_overview_entry

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
