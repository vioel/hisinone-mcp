from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_absence_application_foreigntext import (
        RmErpAbsencemanagementAbsenceApplicationForeigntext,
    )
    from ..models.rm_erp_absencemanagement_absence_booking import RmErpAbsencemanagementAbsenceBooking
    from ..models.rm_erp_absencemanagement_absence_master_record import RmErpAbsencemanagementAbsenceMasterRecord
    from ..models.rm_erp_absencemanagement_absence_type_value import RmErpAbsencemanagementAbsenceTypeValue
    from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData
    from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value import (
        RmErpCommonWorkflowErpWorkflowProcessingStepValue,
    )


T = TypeVar("T", bound="RmErpAbsencemanagementAbsenceApplication")


@_attrs_define
class RmErpAbsencemanagementAbsenceApplication:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementAbsenceApplicationForeigntext | Unset):
        absence_address (str | Unset):
        absence_from (int | Unset):
        absence_reason (str | Unset):
        absence_to (int | Unset):
        absence_type (RmErpAbsencemanagementAbsenceTypeValue | Unset):
        amount_of_absence_days (float | Unset):
        application_related_person (RmErpCommonPersonPersonBasicDataCoreData | Unset):
        application_related_person_id (int | Unset):
        application_timestamp (int | Unset):
        deletion_date (int | Unset):
        error_message (str | Unset):
        executing_person (RmErpCommonPersonPersonBasicDataCoreData | Unset):
        executing_person_id (int | Unset):
        id (int | Unset):
        last_executed_processing_step (RmErpCommonWorkflowErpWorkflowProcessingStepValue | Unset):
        last_executed_processing_step_id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        pseudonymized_application_related_person_id (str | Unset):
        related_absence_booking (RmErpAbsencemanagementAbsenceBooking | Unset):
        related_absence_master_record (RmErpAbsencemanagementAbsenceMasterRecord | Unset):
        related_year (int | Unset):
        sick_leave_with_certificate_of_incapacity (bool | Unset):
        substitute_person_name (str | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementAbsenceApplicationForeigntext | Unset = UNSET
    absence_address: str | Unset = UNSET
    absence_from: int | Unset = UNSET
    absence_reason: str | Unset = UNSET
    absence_to: int | Unset = UNSET
    absence_type: RmErpAbsencemanagementAbsenceTypeValue | Unset = UNSET
    amount_of_absence_days: float | Unset = UNSET
    application_related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset = UNSET
    application_related_person_id: int | Unset = UNSET
    application_timestamp: int | Unset = UNSET
    deletion_date: int | Unset = UNSET
    error_message: str | Unset = UNSET
    executing_person: RmErpCommonPersonPersonBasicDataCoreData | Unset = UNSET
    executing_person_id: int | Unset = UNSET
    id: int | Unset = UNSET
    last_executed_processing_step: RmErpCommonWorkflowErpWorkflowProcessingStepValue | Unset = UNSET
    last_executed_processing_step_id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    pseudonymized_application_related_person_id: str | Unset = UNSET
    related_absence_booking: RmErpAbsencemanagementAbsenceBooking | Unset = UNSET
    related_absence_master_record: RmErpAbsencemanagementAbsenceMasterRecord | Unset = UNSET
    related_year: int | Unset = UNSET
    sick_leave_with_certificate_of_incapacity: bool | Unset = UNSET
    substitute_person_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        absence_address = self.absence_address

        absence_from = self.absence_from

        absence_reason = self.absence_reason

        absence_to = self.absence_to

        absence_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.absence_type, Unset):
            absence_type = self.absence_type.to_dict()

        amount_of_absence_days = self.amount_of_absence_days

        application_related_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_related_person, Unset):
            application_related_person = self.application_related_person.to_dict()

        application_related_person_id = self.application_related_person_id

        application_timestamp = self.application_timestamp

        deletion_date = self.deletion_date

        error_message = self.error_message

        executing_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executing_person, Unset):
            executing_person = self.executing_person.to_dict()

        executing_person_id = self.executing_person_id

        id = self.id

        last_executed_processing_step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_executed_processing_step, Unset):
            last_executed_processing_step = self.last_executed_processing_step.to_dict()

        last_executed_processing_step_id = self.last_executed_processing_step_id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        pseudonymized_application_related_person_id = self.pseudonymized_application_related_person_id

        related_absence_booking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_absence_booking, Unset):
            related_absence_booking = self.related_absence_booking.to_dict()

        related_absence_master_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_absence_master_record, Unset):
            related_absence_master_record = self.related_absence_master_record.to_dict()

        related_year = self.related_year

        sick_leave_with_certificate_of_incapacity = self.sick_leave_with_certificate_of_incapacity

        substitute_person_name = self.substitute_person_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if absence_address is not UNSET:
            field_dict["absenceAddress"] = absence_address
        if absence_from is not UNSET:
            field_dict["absenceFrom"] = absence_from
        if absence_reason is not UNSET:
            field_dict["absenceReason"] = absence_reason
        if absence_to is not UNSET:
            field_dict["absenceTo"] = absence_to
        if absence_type is not UNSET:
            field_dict["absenceType"] = absence_type
        if amount_of_absence_days is not UNSET:
            field_dict["amountOfAbsenceDays"] = amount_of_absence_days
        if application_related_person is not UNSET:
            field_dict["applicationRelatedPerson"] = application_related_person
        if application_related_person_id is not UNSET:
            field_dict["applicationRelatedPersonId"] = application_related_person_id
        if application_timestamp is not UNSET:
            field_dict["applicationTimestamp"] = application_timestamp
        if deletion_date is not UNSET:
            field_dict["deletionDate"] = deletion_date
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if executing_person is not UNSET:
            field_dict["executingPerson"] = executing_person
        if executing_person_id is not UNSET:
            field_dict["executingPersonId"] = executing_person_id
        if id is not UNSET:
            field_dict["id"] = id
        if last_executed_processing_step is not UNSET:
            field_dict["lastExecutedProcessingStep"] = last_executed_processing_step
        if last_executed_processing_step_id is not UNSET:
            field_dict["lastExecutedProcessingStepId"] = last_executed_processing_step_id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if pseudonymized_application_related_person_id is not UNSET:
            field_dict["pseudonymizedApplicationRelatedPersonId"] = pseudonymized_application_related_person_id
        if related_absence_booking is not UNSET:
            field_dict["relatedAbsenceBooking"] = related_absence_booking
        if related_absence_master_record is not UNSET:
            field_dict["relatedAbsenceMasterRecord"] = related_absence_master_record
        if related_year is not UNSET:
            field_dict["relatedYear"] = related_year
        if sick_leave_with_certificate_of_incapacity is not UNSET:
            field_dict["sickLeaveWithCertificateOfIncapacity"] = sick_leave_with_certificate_of_incapacity
        if substitute_person_name is not UNSET:
            field_dict["substitutePersonName"] = substitute_person_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_absence_application_foreigntext import (
            RmErpAbsencemanagementAbsenceApplicationForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_absencemanagement_absence_booking import RmErpAbsencemanagementAbsenceBooking  # noqa: PLC0415
        from ..models.rm_erp_absencemanagement_absence_master_record import RmErpAbsencemanagementAbsenceMasterRecord  # noqa: PLC0415
        from ..models.rm_erp_absencemanagement_absence_type_value import RmErpAbsencemanagementAbsenceTypeValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData  # noqa: PLC0415
        from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value import (
            RmErpCommonWorkflowErpWorkflowProcessingStepValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementAbsenceApplicationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementAbsenceApplicationForeigntext.from_dict(_field_foreigntext)

        absence_address = d.pop("absenceAddress", UNSET)

        absence_from = d.pop("absenceFrom", UNSET)

        absence_reason = d.pop("absenceReason", UNSET)

        absence_to = d.pop("absenceTo", UNSET)

        _absence_type = d.pop("absenceType", UNSET)
        absence_type: RmErpAbsencemanagementAbsenceTypeValue | Unset
        if isinstance(_absence_type, Unset):
            absence_type = UNSET
        else:
            absence_type = RmErpAbsencemanagementAbsenceTypeValue.from_dict(_absence_type)

        amount_of_absence_days = d.pop("amountOfAbsenceDays", UNSET)

        _application_related_person = d.pop("applicationRelatedPerson", UNSET)
        application_related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset
        if isinstance(_application_related_person, Unset):
            application_related_person = UNSET
        else:
            application_related_person = RmErpCommonPersonPersonBasicDataCoreData.from_dict(_application_related_person)

        application_related_person_id = d.pop("applicationRelatedPersonId", UNSET)

        application_timestamp = d.pop("applicationTimestamp", UNSET)

        deletion_date = d.pop("deletionDate", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        _executing_person = d.pop("executingPerson", UNSET)
        executing_person: RmErpCommonPersonPersonBasicDataCoreData | Unset
        if isinstance(_executing_person, Unset):
            executing_person = UNSET
        else:
            executing_person = RmErpCommonPersonPersonBasicDataCoreData.from_dict(_executing_person)

        executing_person_id = d.pop("executingPersonId", UNSET)

        id = d.pop("id", UNSET)

        _last_executed_processing_step = d.pop("lastExecutedProcessingStep", UNSET)
        last_executed_processing_step: RmErpCommonWorkflowErpWorkflowProcessingStepValue | Unset
        if isinstance(_last_executed_processing_step, Unset):
            last_executed_processing_step = UNSET
        else:
            last_executed_processing_step = RmErpCommonWorkflowErpWorkflowProcessingStepValue.from_dict(
                _last_executed_processing_step
            )

        last_executed_processing_step_id = d.pop("lastExecutedProcessingStepId", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        pseudonymized_application_related_person_id = d.pop("pseudonymizedApplicationRelatedPersonId", UNSET)

        _related_absence_booking = d.pop("relatedAbsenceBooking", UNSET)
        related_absence_booking: RmErpAbsencemanagementAbsenceBooking | Unset
        if isinstance(_related_absence_booking, Unset):
            related_absence_booking = UNSET
        else:
            related_absence_booking = RmErpAbsencemanagementAbsenceBooking.from_dict(_related_absence_booking)

        _related_absence_master_record = d.pop("relatedAbsenceMasterRecord", UNSET)
        related_absence_master_record: RmErpAbsencemanagementAbsenceMasterRecord | Unset
        if isinstance(_related_absence_master_record, Unset):
            related_absence_master_record = UNSET
        else:
            related_absence_master_record = RmErpAbsencemanagementAbsenceMasterRecord.from_dict(
                _related_absence_master_record
            )

        related_year = d.pop("relatedYear", UNSET)

        sick_leave_with_certificate_of_incapacity = d.pop("sickLeaveWithCertificateOfIncapacity", UNSET)

        substitute_person_name = d.pop("substitutePersonName", UNSET)

        rm_erp_absencemanagement_absence_application = cls(
            field_foreigntext=field_foreigntext,
            absence_address=absence_address,
            absence_from=absence_from,
            absence_reason=absence_reason,
            absence_to=absence_to,
            absence_type=absence_type,
            amount_of_absence_days=amount_of_absence_days,
            application_related_person=application_related_person,
            application_related_person_id=application_related_person_id,
            application_timestamp=application_timestamp,
            deletion_date=deletion_date,
            error_message=error_message,
            executing_person=executing_person,
            executing_person_id=executing_person_id,
            id=id,
            last_executed_processing_step=last_executed_processing_step,
            last_executed_processing_step_id=last_executed_processing_step_id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            pseudonymized_application_related_person_id=pseudonymized_application_related_person_id,
            related_absence_booking=related_absence_booking,
            related_absence_master_record=related_absence_master_record,
            related_year=related_year,
            sick_leave_with_certificate_of_incapacity=sick_leave_with_certificate_of_incapacity,
            substitute_person_name=substitute_person_name,
        )

        rm_erp_absencemanagement_absence_application.additional_properties = d
        return rm_erp_absencemanagement_absence_application

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
