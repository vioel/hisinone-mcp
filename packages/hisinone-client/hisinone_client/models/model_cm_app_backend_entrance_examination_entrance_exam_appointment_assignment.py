from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_appointment_assignment_foreigntext import (
        ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignmentForeigntext,
    )
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
        ModelCmAppBackendEntranceExaminationEntranceExamTerm,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment")


@_attrs_define
class ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignment:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignmentForeigntext | Unset):
        entrance_exam_appointment_guid (str | Unset):
        entrance_exam_guid (str | Unset):
        entrance_exam_term (ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person_id (int | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignmentForeigntext | Unset = UNSET
    entrance_exam_appointment_guid: str | Unset = UNSET
    entrance_exam_guid: str | Unset = UNSET
    entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        entrance_exam_appointment_guid = self.entrance_exam_appointment_guid

        entrance_exam_guid = self.entrance_exam_guid

        entrance_exam_term: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrance_exam_term, Unset):
            entrance_exam_term = self.entrance_exam_term.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if entrance_exam_appointment_guid is not UNSET:
            field_dict["entranceExamAppointmentGuid"] = entrance_exam_appointment_guid
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
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_appointment_assignment_foreigntext import (
            ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignmentForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
            ModelCmAppBackendEntranceExaminationEntranceExamTerm,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignmentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                ModelCmAppBackendEntranceExaminationEntranceExamAppointmentAssignmentForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        entrance_exam_appointment_guid = d.pop("entranceExamAppointmentGuid", UNSET)

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

        person_id = d.pop("personId", UNSET)

        model_cm_app_backend_entrance_examination_entrance_exam_appointment_assignment = cls(
            field_foreigntext=field_foreigntext,
            entrance_exam_appointment_guid=entrance_exam_appointment_guid,
            entrance_exam_guid=entrance_exam_guid,
            entrance_exam_term=entrance_exam_term,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person_id=person_id,
        )

        model_cm_app_backend_entrance_examination_entrance_exam_appointment_assignment.additional_properties = d
        return model_cm_app_backend_entrance_examination_entrance_exam_appointment_assignment

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
