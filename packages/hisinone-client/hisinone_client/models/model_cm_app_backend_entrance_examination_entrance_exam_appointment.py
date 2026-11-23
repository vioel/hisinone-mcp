from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_time_local_date import JavaTimeLocalDate
    from ..models.java_time_local_time import JavaTimeLocalTime
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_appointment_foreigntext import (
        ModelCmAppBackendEntranceExaminationEntranceExamAppointmentForeigntext,
    )
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
        ModelCmAppBackendEntranceExaminationEntranceExamTerm,
    )
    from ..models.model_cm_app_backend_entrance_examination_entrance_examination import (
        ModelCmAppBackendEntranceExaminationEntranceExamination,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationEntranceExamAppointment")


@_attrs_define
class ModelCmAppBackendEntranceExaminationEntranceExamAppointment:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationEntranceExamAppointmentForeigntext | Unset):
        assigned_applicants (list[int] | Unset):
        attendee_maximum (int | Unset):
        date (JavaTimeLocalDate | Unset):
        end_time (JavaTimeLocalTime | Unset):
        entrance_exam_term (ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset):
        entrance_examination (ModelCmAppBackendEntranceExaminationEntranceExamination | Unset):
        examiners (list[str] | Unset):
        grid_entrance_exam_appointments (list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        notice_for_applicants (str | Unset):
        obj_guid (str | Unset):
        planelement_editing_state (str | Unset):
        room (str | Unset):
        start_time (JavaTimeLocalTime | Unset):
        terminnummer (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentForeigntext | Unset = UNSET
    assigned_applicants: list[int] | Unset = UNSET
    attendee_maximum: int | Unset = UNSET
    date: JavaTimeLocalDate | Unset = UNSET
    end_time: JavaTimeLocalTime | Unset = UNSET
    entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset = UNSET
    entrance_examination: ModelCmAppBackendEntranceExaminationEntranceExamination | Unset = UNSET
    examiners: list[str] | Unset = UNSET
    grid_entrance_exam_appointments: list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    notice_for_applicants: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    planelement_editing_state: str | Unset = UNSET
    room: str | Unset = UNSET
    start_time: JavaTimeLocalTime | Unset = UNSET
    terminnummer: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        assigned_applicants: list[int] | Unset = UNSET
        if not isinstance(self.assigned_applicants, Unset):
            assigned_applicants = self.assigned_applicants

        attendee_maximum = self.attendee_maximum

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        end_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.to_dict()

        entrance_exam_term: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrance_exam_term, Unset):
            entrance_exam_term = self.entrance_exam_term.to_dict()

        entrance_examination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrance_examination, Unset):
            entrance_examination = self.entrance_examination.to_dict()

        examiners: list[str] | Unset = UNSET
        if not isinstance(self.examiners, Unset):
            examiners = self.examiners

        grid_entrance_exam_appointments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grid_entrance_exam_appointments, Unset):
            grid_entrance_exam_appointments = []
            for grid_entrance_exam_appointments_item_data in self.grid_entrance_exam_appointments:
                grid_entrance_exam_appointments_item = grid_entrance_exam_appointments_item_data.to_dict()
                grid_entrance_exam_appointments.append(grid_entrance_exam_appointments_item)

        id = self.id

        lock_version = self.lock_version

        notice_for_applicants = self.notice_for_applicants

        obj_guid = self.obj_guid

        planelement_editing_state = self.planelement_editing_state

        room = self.room

        start_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.to_dict()

        terminnummer = self.terminnummer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if assigned_applicants is not UNSET:
            field_dict["assignedApplicants"] = assigned_applicants
        if attendee_maximum is not UNSET:
            field_dict["attendeeMaximum"] = attendee_maximum
        if date is not UNSET:
            field_dict["date"] = date
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if entrance_exam_term is not UNSET:
            field_dict["entranceExamTerm"] = entrance_exam_term
        if entrance_examination is not UNSET:
            field_dict["entranceExamination"] = entrance_examination
        if examiners is not UNSET:
            field_dict["examiners"] = examiners
        if grid_entrance_exam_appointments is not UNSET:
            field_dict["gridEntranceExamAppointments"] = grid_entrance_exam_appointments
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if notice_for_applicants is not UNSET:
            field_dict["noticeForApplicants"] = notice_for_applicants
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if planelement_editing_state is not UNSET:
            field_dict["planelementEditingState"] = planelement_editing_state
        if room is not UNSET:
            field_dict["room"] = room
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if terminnummer is not UNSET:
            field_dict["terminnummer"] = terminnummer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_time_local_date import JavaTimeLocalDate  # noqa: PLC0415
        from ..models.java_time_local_time import JavaTimeLocalTime  # noqa: PLC0415
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_appointment_foreigntext import (
            ModelCmAppBackendEntranceExaminationEntranceExamAppointmentForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
            ModelCmAppBackendEntranceExaminationEntranceExamTerm,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_entrance_examination import (
            ModelCmAppBackendEntranceExaminationEntranceExamination,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamAppointmentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationEntranceExamAppointmentForeigntext.from_dict(
                _field_foreigntext
            )

        assigned_applicants = cast(list[int], d.pop("assignedApplicants", UNSET))

        attendee_maximum = d.pop("attendeeMaximum", UNSET)

        _date = d.pop("date", UNSET)
        date: JavaTimeLocalDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = JavaTimeLocalDate.from_dict(_date)

        _end_time = d.pop("endTime", UNSET)
        end_time: JavaTimeLocalTime | Unset
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = JavaTimeLocalTime.from_dict(_end_time)

        _entrance_exam_term = d.pop("entranceExamTerm", UNSET)
        entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset
        if isinstance(_entrance_exam_term, Unset):
            entrance_exam_term = UNSET
        else:
            entrance_exam_term = ModelCmAppBackendEntranceExaminationEntranceExamTerm.from_dict(_entrance_exam_term)

        _entrance_examination = d.pop("entranceExamination", UNSET)
        entrance_examination: ModelCmAppBackendEntranceExaminationEntranceExamination | Unset
        if isinstance(_entrance_examination, Unset):
            entrance_examination = UNSET
        else:
            entrance_examination = ModelCmAppBackendEntranceExaminationEntranceExamination.from_dict(
                _entrance_examination
            )

        examiners = cast(list[str], d.pop("examiners", UNSET))

        _grid_entrance_exam_appointments = d.pop("gridEntranceExamAppointments", UNSET)
        grid_entrance_exam_appointments: list[ModelCmAppBackendEntranceExaminationEntranceExamAppointment] | Unset = (
            UNSET
        )
        if _grid_entrance_exam_appointments is not UNSET:
            grid_entrance_exam_appointments = []
            for grid_entrance_exam_appointments_item_data in _grid_entrance_exam_appointments:
                grid_entrance_exam_appointments_item = (
                    ModelCmAppBackendEntranceExaminationEntranceExamAppointment.from_dict(
                        grid_entrance_exam_appointments_item_data
                    )
                )

                grid_entrance_exam_appointments.append(grid_entrance_exam_appointments_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        notice_for_applicants = d.pop("noticeForApplicants", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        planelement_editing_state = d.pop("planelementEditingState", UNSET)

        room = d.pop("room", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: JavaTimeLocalTime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = JavaTimeLocalTime.from_dict(_start_time)

        terminnummer = d.pop("terminnummer", UNSET)

        model_cm_app_backend_entrance_examination_entrance_exam_appointment = cls(
            field_foreigntext=field_foreigntext,
            assigned_applicants=assigned_applicants,
            attendee_maximum=attendee_maximum,
            date=date,
            end_time=end_time,
            entrance_exam_term=entrance_exam_term,
            entrance_examination=entrance_examination,
            examiners=examiners,
            grid_entrance_exam_appointments=grid_entrance_exam_appointments,
            id=id,
            lock_version=lock_version,
            notice_for_applicants=notice_for_applicants,
            obj_guid=obj_guid,
            planelement_editing_state=planelement_editing_state,
            room=room,
            start_time=start_time,
            terminnummer=terminnummer,
        )

        model_cm_app_backend_entrance_examination_entrance_exam_appointment.additional_properties = d
        return model_cm_app_backend_entrance_examination_entrance_exam_appointment

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
