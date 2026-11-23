from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
        ModelCmAppBackendEntranceExaminationEntranceExamTerm,
    )
    from ..models.model_cm_app_backend_entrance_examination_mass_assignment_params_applicant_ids_for_appointment_guids import (
        ModelCmAppBackendEntranceExaminationMassAssignmentParamsApplicantIdsForAppointmentGuids,
    )
    from ..models.model_cm_app_backend_entrance_examination_mass_assignment_params_foreigntext import (
        ModelCmAppBackendEntranceExaminationMassAssignmentParamsForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationMassAssignmentParams")


@_attrs_define
class ModelCmAppBackendEntranceExaminationMassAssignmentParams:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationMassAssignmentParamsForeigntext | Unset):
        applicant_ids_for_appointment_guids
            (ModelCmAppBackendEntranceExaminationMassAssignmentParamsApplicantIdsForAppointmentGuids | Unset):
        entrance_exam_guid (str | Unset):
        entrance_exam_term (ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationMassAssignmentParamsForeigntext | Unset = UNSET
    applicant_ids_for_appointment_guids: (
        ModelCmAppBackendEntranceExaminationMassAssignmentParamsApplicantIdsForAppointmentGuids | Unset
    ) = UNSET
    entrance_exam_guid: str | Unset = UNSET
    entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        applicant_ids_for_appointment_guids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applicant_ids_for_appointment_guids, Unset):
            applicant_ids_for_appointment_guids = self.applicant_ids_for_appointment_guids.to_dict()

        entrance_exam_guid = self.entrance_exam_guid

        entrance_exam_term: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrance_exam_term, Unset):
            entrance_exam_term = self.entrance_exam_term.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if applicant_ids_for_appointment_guids is not UNSET:
            field_dict["applicantIdsForAppointmentGuids"] = applicant_ids_for_appointment_guids
        if entrance_exam_guid is not UNSET:
            field_dict["entranceExamGuid"] = entrance_exam_guid
        if entrance_exam_term is not UNSET:
            field_dict["entranceExamTerm"] = entrance_exam_term
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
            ModelCmAppBackendEntranceExaminationEntranceExamTerm,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_mass_assignment_params_applicant_ids_for_appointment_guids import (
            ModelCmAppBackendEntranceExaminationMassAssignmentParamsApplicantIdsForAppointmentGuids,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_mass_assignment_params_foreigntext import (
            ModelCmAppBackendEntranceExaminationMassAssignmentParamsForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationMassAssignmentParamsForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationMassAssignmentParamsForeigntext.from_dict(
                _field_foreigntext
            )

        _applicant_ids_for_appointment_guids = d.pop("applicantIdsForAppointmentGuids", UNSET)
        applicant_ids_for_appointment_guids: (
            ModelCmAppBackendEntranceExaminationMassAssignmentParamsApplicantIdsForAppointmentGuids | Unset
        )
        if isinstance(_applicant_ids_for_appointment_guids, Unset):
            applicant_ids_for_appointment_guids = UNSET
        else:
            applicant_ids_for_appointment_guids = (
                ModelCmAppBackendEntranceExaminationMassAssignmentParamsApplicantIdsForAppointmentGuids.from_dict(
                    _applicant_ids_for_appointment_guids
                )
            )

        entrance_exam_guid = d.pop("entranceExamGuid", UNSET)

        _entrance_exam_term = d.pop("entranceExamTerm", UNSET)
        entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset
        if isinstance(_entrance_exam_term, Unset):
            entrance_exam_term = UNSET
        else:
            entrance_exam_term = ModelCmAppBackendEntranceExaminationEntranceExamTerm.from_dict(_entrance_exam_term)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_entrance_examination_mass_assignment_params = cls(
            field_foreigntext=field_foreigntext,
            applicant_ids_for_appointment_guids=applicant_ids_for_appointment_guids,
            entrance_exam_guid=entrance_exam_guid,
            entrance_exam_term=entrance_exam_term,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_entrance_examination_mass_assignment_params.additional_properties = d
        return model_cm_app_backend_entrance_examination_mass_assignment_params

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
