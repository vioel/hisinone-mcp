from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_absence_application import RmErpAbsencemanagementAbsenceApplication
    from ..models.rm_erp_absencemanagement_absence_booking_foreigntext import (
        RmErpAbsencemanagementAbsenceBookingForeigntext,
    )
    from ..models.rm_erp_absencemanagement_absence_master_record import RmErpAbsencemanagementAbsenceMasterRecord
    from ..models.rm_erp_absencemanagement_absence_type_value import RmErpAbsencemanagementAbsenceTypeValue
    from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData


T = TypeVar("T", bound="RmErpAbsencemanagementAbsenceBooking")


@_attrs_define
class RmErpAbsencemanagementAbsenceBooking:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementAbsenceBookingForeigntext | Unset):
        absence_from (int | Unset):
        absence_reason (str | Unset):
        absence_reason_by_system (str | Unset):
        absence_to (int | Unset):
        absence_type (RmErpAbsencemanagementAbsenceTypeValue | Unset):
        amount_of_absent_hours (float | Unset):
        amount_of_absent_working_days (float | Unset):
        amount_of_calendar_days_in_absence_interval (float | Unset):
        effective_year (int | Unset):
        error_message (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        related_absence_application (RmErpAbsencemanagementAbsenceApplication | Unset):
        related_absence_master_record (RmErpAbsencemanagementAbsenceMasterRecord | Unset):
        related_absence_master_record_error_message (str | Unset):
        related_person (RmErpCommonPersonPersonBasicDataCoreData | Unset):
        serialversionuid (int | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementAbsenceBookingForeigntext | Unset = UNSET
    absence_from: int | Unset = UNSET
    absence_reason: str | Unset = UNSET
    absence_reason_by_system: str | Unset = UNSET
    absence_to: int | Unset = UNSET
    absence_type: RmErpAbsencemanagementAbsenceTypeValue | Unset = UNSET
    amount_of_absent_hours: float | Unset = UNSET
    amount_of_absent_working_days: float | Unset = UNSET
    amount_of_calendar_days_in_absence_interval: float | Unset = UNSET
    effective_year: int | Unset = UNSET
    error_message: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    related_absence_application: RmErpAbsencemanagementAbsenceApplication | Unset = UNSET
    related_absence_master_record: RmErpAbsencemanagementAbsenceMasterRecord | Unset = UNSET
    related_absence_master_record_error_message: str | Unset = UNSET
    related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset = UNSET
    serialversionuid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        absence_from = self.absence_from

        absence_reason = self.absence_reason

        absence_reason_by_system = self.absence_reason_by_system

        absence_to = self.absence_to

        absence_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.absence_type, Unset):
            absence_type = self.absence_type.to_dict()

        amount_of_absent_hours = self.amount_of_absent_hours

        amount_of_absent_working_days = self.amount_of_absent_working_days

        amount_of_calendar_days_in_absence_interval = self.amount_of_calendar_days_in_absence_interval

        effective_year = self.effective_year

        error_message = self.error_message

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        related_absence_application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_absence_application, Unset):
            related_absence_application = self.related_absence_application.to_dict()

        related_absence_master_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_absence_master_record, Unset):
            related_absence_master_record = self.related_absence_master_record.to_dict()

        related_absence_master_record_error_message = self.related_absence_master_record_error_message

        related_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_person, Unset):
            related_person = self.related_person.to_dict()

        serialversionuid = self.serialversionuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if absence_from is not UNSET:
            field_dict["absenceFrom"] = absence_from
        if absence_reason is not UNSET:
            field_dict["absenceReason"] = absence_reason
        if absence_reason_by_system is not UNSET:
            field_dict["absenceReasonBySystem"] = absence_reason_by_system
        if absence_to is not UNSET:
            field_dict["absenceTo"] = absence_to
        if absence_type is not UNSET:
            field_dict["absenceType"] = absence_type
        if amount_of_absent_hours is not UNSET:
            field_dict["amountOfAbsentHours"] = amount_of_absent_hours
        if amount_of_absent_working_days is not UNSET:
            field_dict["amountOfAbsentWorkingDays"] = amount_of_absent_working_days
        if amount_of_calendar_days_in_absence_interval is not UNSET:
            field_dict["amountOfCalendarDaysInAbsenceInterval"] = amount_of_calendar_days_in_absence_interval
        if effective_year is not UNSET:
            field_dict["effectiveYear"] = effective_year
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if related_absence_application is not UNSET:
            field_dict["relatedAbsenceApplication"] = related_absence_application
        if related_absence_master_record is not UNSET:
            field_dict["relatedAbsenceMasterRecord"] = related_absence_master_record
        if related_absence_master_record_error_message is not UNSET:
            field_dict["relatedAbsenceMasterRecordErrorMessage"] = related_absence_master_record_error_message
        if related_person is not UNSET:
            field_dict["relatedPerson"] = related_person
        if serialversionuid is not UNSET:
            field_dict["serialversionuid"] = serialversionuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_absence_application import RmErpAbsencemanagementAbsenceApplication  # noqa: PLC0415
        from ..models.rm_erp_absencemanagement_absence_booking_foreigntext import (
            RmErpAbsencemanagementAbsenceBookingForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_absence_master_record import RmErpAbsencemanagementAbsenceMasterRecord  # noqa: PLC0415
        from ..models.rm_erp_absencemanagement_absence_type_value import RmErpAbsencemanagementAbsenceTypeValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementAbsenceBookingForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementAbsenceBookingForeigntext.from_dict(_field_foreigntext)

        absence_from = d.pop("absenceFrom", UNSET)

        absence_reason = d.pop("absenceReason", UNSET)

        absence_reason_by_system = d.pop("absenceReasonBySystem", UNSET)

        absence_to = d.pop("absenceTo", UNSET)

        _absence_type = d.pop("absenceType", UNSET)
        absence_type: RmErpAbsencemanagementAbsenceTypeValue | Unset
        if isinstance(_absence_type, Unset):
            absence_type = UNSET
        else:
            absence_type = RmErpAbsencemanagementAbsenceTypeValue.from_dict(_absence_type)

        amount_of_absent_hours = d.pop("amountOfAbsentHours", UNSET)

        amount_of_absent_working_days = d.pop("amountOfAbsentWorkingDays", UNSET)

        amount_of_calendar_days_in_absence_interval = d.pop("amountOfCalendarDaysInAbsenceInterval", UNSET)

        effective_year = d.pop("effectiveYear", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _related_absence_application = d.pop("relatedAbsenceApplication", UNSET)
        related_absence_application: RmErpAbsencemanagementAbsenceApplication | Unset
        if isinstance(_related_absence_application, Unset):
            related_absence_application = UNSET
        else:
            related_absence_application = RmErpAbsencemanagementAbsenceApplication.from_dict(
                _related_absence_application
            )

        _related_absence_master_record = d.pop("relatedAbsenceMasterRecord", UNSET)
        related_absence_master_record: RmErpAbsencemanagementAbsenceMasterRecord | Unset
        if isinstance(_related_absence_master_record, Unset):
            related_absence_master_record = UNSET
        else:
            related_absence_master_record = RmErpAbsencemanagementAbsenceMasterRecord.from_dict(
                _related_absence_master_record
            )

        related_absence_master_record_error_message = d.pop("relatedAbsenceMasterRecordErrorMessage", UNSET)

        _related_person = d.pop("relatedPerson", UNSET)
        related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset
        if isinstance(_related_person, Unset):
            related_person = UNSET
        else:
            related_person = RmErpCommonPersonPersonBasicDataCoreData.from_dict(_related_person)

        serialversionuid = d.pop("serialversionuid", UNSET)

        rm_erp_absencemanagement_absence_booking = cls(
            field_foreigntext=field_foreigntext,
            absence_from=absence_from,
            absence_reason=absence_reason,
            absence_reason_by_system=absence_reason_by_system,
            absence_to=absence_to,
            absence_type=absence_type,
            amount_of_absent_hours=amount_of_absent_hours,
            amount_of_absent_working_days=amount_of_absent_working_days,
            amount_of_calendar_days_in_absence_interval=amount_of_calendar_days_in_absence_interval,
            effective_year=effective_year,
            error_message=error_message,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            related_absence_application=related_absence_application,
            related_absence_master_record=related_absence_master_record,
            related_absence_master_record_error_message=related_absence_master_record_error_message,
            related_person=related_person,
            serialversionuid=serialversionuid,
        )

        rm_erp_absencemanagement_absence_booking.additional_properties = d
        return rm_erp_absencemanagement_absence_booking

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
