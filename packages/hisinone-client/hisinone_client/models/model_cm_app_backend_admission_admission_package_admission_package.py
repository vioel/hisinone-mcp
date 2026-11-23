from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_error_message import CsSysRestErrorMessage
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.model_cm_app_backend_admission_admission_package_admission_package_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageForeigntext,
    )
    from ..models.model_cm_app_backend_admission_admission_package_app_key_enum import (
        ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum,
    )
    from ..models.model_cm_app_backend_admission_allocation_scheme_allocation_scheme import (
        ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme,
    )
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
        ModelCmAppBackendEntranceExaminationEntranceExamTerm,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageForeigntext | Unset):
        admission_package_predefined_status_remark_values (list[int] | Unset):
        admission_priority (ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum | Unset):
        admissionshares (list[int] | Unset):
        admissiontype (CsSysValueGenericValue | Unset):
        allocation_scheme (ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme | Unset):
        application_content_definition_admission_packages (list[int] | Unset):
        application_procedure (CsSysValueGenericValue | Unset):
        capacity (int | Unset):
        defaulttext (str | Unset):
        error_description (str | Unset):
        error_messages (list[CsSysRestErrorMessage] | Unset):
        from_studysemester (int | Unset):
        has_request_prioritization (bool | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        participation_in_central_succession (ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum | Unset):
        planned_absolute_overbooking (int | Unset):
        planned_relative_overbooking (int | Unset):
        shorttext (str | Unset):
        term (ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset):
        to_studysemester (int | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageForeigntext | Unset = UNSET
    admission_package_predefined_status_remark_values: list[int] | Unset = UNSET
    admission_priority: ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum | Unset = UNSET
    admissionshares: list[int] | Unset = UNSET
    admissiontype: CsSysValueGenericValue | Unset = UNSET
    allocation_scheme: ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme | Unset = UNSET
    application_content_definition_admission_packages: list[int] | Unset = UNSET
    application_procedure: CsSysValueGenericValue | Unset = UNSET
    capacity: int | Unset = UNSET
    defaulttext: str | Unset = UNSET
    error_description: str | Unset = UNSET
    error_messages: list[CsSysRestErrorMessage] | Unset = UNSET
    from_studysemester: int | Unset = UNSET
    has_request_prioritization: bool | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    participation_in_central_succession: ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum | Unset = UNSET
    planned_absolute_overbooking: int | Unset = UNSET
    planned_relative_overbooking: int | Unset = UNSET
    shorttext: str | Unset = UNSET
    term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset = UNSET
    to_studysemester: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_package_predefined_status_remark_values: list[int] | Unset = UNSET
        if not isinstance(self.admission_package_predefined_status_remark_values, Unset):
            admission_package_predefined_status_remark_values = self.admission_package_predefined_status_remark_values

        admission_priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admission_priority, Unset):
            admission_priority = self.admission_priority.to_dict()

        admissionshares: list[int] | Unset = UNSET
        if not isinstance(self.admissionshares, Unset):
            admissionshares = self.admissionshares

        admissiontype: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admissiontype, Unset):
            admissiontype = self.admissiontype.to_dict()

        allocation_scheme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.allocation_scheme, Unset):
            allocation_scheme = self.allocation_scheme.to_dict()

        application_content_definition_admission_packages: list[int] | Unset = UNSET
        if not isinstance(self.application_content_definition_admission_packages, Unset):
            application_content_definition_admission_packages = self.application_content_definition_admission_packages

        application_procedure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_procedure, Unset):
            application_procedure = self.application_procedure.to_dict()

        capacity = self.capacity

        defaulttext = self.defaulttext

        error_description = self.error_description

        error_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = []
            for error_messages_item_data in self.error_messages:
                error_messages_item = error_messages_item_data.to_dict()
                error_messages.append(error_messages_item)

        from_studysemester = self.from_studysemester

        has_request_prioritization = self.has_request_prioritization

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        participation_in_central_succession: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_in_central_succession, Unset):
            participation_in_central_succession = self.participation_in_central_succession.to_dict()

        planned_absolute_overbooking = self.planned_absolute_overbooking

        planned_relative_overbooking = self.planned_relative_overbooking

        shorttext = self.shorttext

        term: dict[str, Any] | Unset = UNSET
        if not isinstance(self.term, Unset):
            term = self.term.to_dict()

        to_studysemester = self.to_studysemester

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_package_predefined_status_remark_values is not UNSET:
            field_dict["admissionPackagePredefinedStatusRemarkValues"] = (
                admission_package_predefined_status_remark_values
            )
        if admission_priority is not UNSET:
            field_dict["admissionPriority"] = admission_priority
        if admissionshares is not UNSET:
            field_dict["admissionshares"] = admissionshares
        if admissiontype is not UNSET:
            field_dict["admissiontype"] = admissiontype
        if allocation_scheme is not UNSET:
            field_dict["allocationScheme"] = allocation_scheme
        if application_content_definition_admission_packages is not UNSET:
            field_dict["applicationContentDefinitionAdmissionPackages"] = (
                application_content_definition_admission_packages
            )
        if application_procedure is not UNSET:
            field_dict["applicationProcedure"] = application_procedure
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_messages is not UNSET:
            field_dict["errorMessages"] = error_messages
        if from_studysemester is not UNSET:
            field_dict["fromStudysemester"] = from_studysemester
        if has_request_prioritization is not UNSET:
            field_dict["hasRequestPrioritization"] = has_request_prioritization
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if participation_in_central_succession is not UNSET:
            field_dict["participationInCentralSuccession"] = participation_in_central_succession
        if planned_absolute_overbooking is not UNSET:
            field_dict["plannedAbsoluteOverbooking"] = planned_absolute_overbooking
        if planned_relative_overbooking is not UNSET:
            field_dict["plannedRelativeOverbooking"] = planned_relative_overbooking
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if term is not UNSET:
            field_dict["term"] = term
        if to_studysemester is not UNSET:
            field_dict["toStudysemester"] = to_studysemester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_error_message import CsSysRestErrorMessage  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.model_cm_app_backend_admission_admission_package_admission_package_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_app_key_enum import (
            ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_allocation_scheme_allocation_scheme import (
            ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
            ModelCmAppBackendEntranceExaminationEntranceExamTerm,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageForeigntext.from_dict(
                _field_foreigntext
            )

        admission_package_predefined_status_remark_values = cast(
            list[int], d.pop("admissionPackagePredefinedStatusRemarkValues", UNSET)
        )

        _admission_priority = d.pop("admissionPriority", UNSET)
        admission_priority: ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum | Unset
        if isinstance(_admission_priority, Unset):
            admission_priority = UNSET
        else:
            admission_priority = ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum.from_dict(_admission_priority)

        admissionshares = cast(list[int], d.pop("admissionshares", UNSET))

        _admissiontype = d.pop("admissiontype", UNSET)
        admissiontype: CsSysValueGenericValue | Unset
        if isinstance(_admissiontype, Unset):
            admissiontype = UNSET
        else:
            admissiontype = CsSysValueGenericValue.from_dict(_admissiontype)

        _allocation_scheme = d.pop("allocationScheme", UNSET)
        allocation_scheme: ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme | Unset
        if isinstance(_allocation_scheme, Unset):
            allocation_scheme = UNSET
        else:
            allocation_scheme = ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme.from_dict(_allocation_scheme)

        application_content_definition_admission_packages = cast(
            list[int], d.pop("applicationContentDefinitionAdmissionPackages", UNSET)
        )

        _application_procedure = d.pop("applicationProcedure", UNSET)
        application_procedure: CsSysValueGenericValue | Unset
        if isinstance(_application_procedure, Unset):
            application_procedure = UNSET
        else:
            application_procedure = CsSysValueGenericValue.from_dict(_application_procedure)

        capacity = d.pop("capacity", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_messages = d.pop("errorMessages", UNSET)
        error_messages: list[CsSysRestErrorMessage] | Unset = UNSET
        if _error_messages is not UNSET:
            error_messages = []
            for error_messages_item_data in _error_messages:
                error_messages_item = CsSysRestErrorMessage.from_dict(error_messages_item_data)

                error_messages.append(error_messages_item)

        from_studysemester = d.pop("fromStudysemester", UNSET)

        has_request_prioritization = d.pop("hasRequestPrioritization", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _participation_in_central_succession = d.pop("participationInCentralSuccession", UNSET)
        participation_in_central_succession: ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum | Unset
        if isinstance(_participation_in_central_succession, Unset):
            participation_in_central_succession = UNSET
        else:
            participation_in_central_succession = ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum.from_dict(
                _participation_in_central_succession
            )

        planned_absolute_overbooking = d.pop("plannedAbsoluteOverbooking", UNSET)

        planned_relative_overbooking = d.pop("plannedRelativeOverbooking", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        _term = d.pop("term", UNSET)
        term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset
        if isinstance(_term, Unset):
            term = UNSET
        else:
            term = ModelCmAppBackendEntranceExaminationEntranceExamTerm.from_dict(_term)

        to_studysemester = d.pop("toStudysemester", UNSET)

        model_cm_app_backend_admission_admission_package_admission_package = cls(
            field_foreigntext=field_foreigntext,
            admission_package_predefined_status_remark_values=admission_package_predefined_status_remark_values,
            admission_priority=admission_priority,
            admissionshares=admissionshares,
            admissiontype=admissiontype,
            allocation_scheme=allocation_scheme,
            application_content_definition_admission_packages=application_content_definition_admission_packages,
            application_procedure=application_procedure,
            capacity=capacity,
            defaulttext=defaulttext,
            error_description=error_description,
            error_messages=error_messages,
            from_studysemester=from_studysemester,
            has_request_prioritization=has_request_prioritization,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            participation_in_central_succession=participation_in_central_succession,
            planned_absolute_overbooking=planned_absolute_overbooking,
            planned_relative_overbooking=planned_relative_overbooking,
            shorttext=shorttext,
            term=term,
            to_studysemester=to_studysemester,
        )

        model_cm_app_backend_admission_admission_package_admission_package.additional_properties = d
        return model_cm_app_backend_admission_admission_package_admission_package

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
