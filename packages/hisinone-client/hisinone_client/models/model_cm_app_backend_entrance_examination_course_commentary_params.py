from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_entrance_examination_course_commentary_params_foreigntext import (
        ModelCmAppBackendEntranceExaminationCourseCommentaryParamsForeigntext,
    )
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
        ModelCmAppBackendEntranceExaminationEntranceExamTerm,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationCourseCommentaryParams")


@_attrs_define
class ModelCmAppBackendEntranceExaminationCourseCommentaryParams:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationCourseCommentaryParamsForeigntext | Unset):
        course_commentary (str | Unset):
        entrance_exam_appointment_obj_guids (list[str] | Unset):
        entrance_exam_guid (str | Unset):
        entrance_exam_term (ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationCourseCommentaryParamsForeigntext | Unset = UNSET
    course_commentary: str | Unset = UNSET
    entrance_exam_appointment_obj_guids: list[str] | Unset = UNSET
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

        course_commentary = self.course_commentary

        entrance_exam_appointment_obj_guids: list[str] | Unset = UNSET
        if not isinstance(self.entrance_exam_appointment_obj_guids, Unset):
            entrance_exam_appointment_obj_guids = self.entrance_exam_appointment_obj_guids

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
        if course_commentary is not UNSET:
            field_dict["courseCommentary"] = course_commentary
        if entrance_exam_appointment_obj_guids is not UNSET:
            field_dict["entranceExamAppointmentObjGuids"] = entrance_exam_appointment_obj_guids
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
        from ..models.model_cm_app_backend_entrance_examination_course_commentary_params_foreigntext import (
            ModelCmAppBackendEntranceExaminationCourseCommentaryParamsForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
            ModelCmAppBackendEntranceExaminationEntranceExamTerm,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationCourseCommentaryParamsForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationCourseCommentaryParamsForeigntext.from_dict(
                _field_foreigntext
            )

        course_commentary = d.pop("courseCommentary", UNSET)

        entrance_exam_appointment_obj_guids = cast(list[str], d.pop("entranceExamAppointmentObjGuids", UNSET))

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

        model_cm_app_backend_entrance_examination_course_commentary_params = cls(
            field_foreigntext=field_foreigntext,
            course_commentary=course_commentary,
            entrance_exam_appointment_obj_guids=entrance_exam_appointment_obj_guids,
            entrance_exam_guid=entrance_exam_guid,
            entrance_exam_term=entrance_exam_term,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_entrance_examination_course_commentary_params.additional_properties = d
        return model_cm_app_backend_entrance_examination_course_commentary_params

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
