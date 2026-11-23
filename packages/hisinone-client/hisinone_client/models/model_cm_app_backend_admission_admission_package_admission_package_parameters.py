from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_admission_package_parameters_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParametersForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParameters")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParameters:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParametersForeigntext | Unset):
        admission_package_id (int | Unset):
        application_procedure_obj_guid (str | Unset):
        course_of_study_ids (list[int] | Unset):
        from_studysemester (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        term_type_id (int | Unset):
        term_year (int | Unset):
        to_studysemester (int | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParametersForeigntext | Unset = UNSET
    admission_package_id: int | Unset = UNSET
    application_procedure_obj_guid: str | Unset = UNSET
    course_of_study_ids: list[int] | Unset = UNSET
    from_studysemester: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    term_type_id: int | Unset = UNSET
    term_year: int | Unset = UNSET
    to_studysemester: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_package_id = self.admission_package_id

        application_procedure_obj_guid = self.application_procedure_obj_guid

        course_of_study_ids: list[int] | Unset = UNSET
        if not isinstance(self.course_of_study_ids, Unset):
            course_of_study_ids = self.course_of_study_ids

        from_studysemester = self.from_studysemester

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        term_type_id = self.term_type_id

        term_year = self.term_year

        to_studysemester = self.to_studysemester

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_package_id is not UNSET:
            field_dict["admissionPackageId"] = admission_package_id
        if application_procedure_obj_guid is not UNSET:
            field_dict["applicationProcedureObjGuid"] = application_procedure_obj_guid
        if course_of_study_ids is not UNSET:
            field_dict["courseOfStudyIds"] = course_of_study_ids
        if from_studysemester is not UNSET:
            field_dict["fromStudysemester"] = from_studysemester
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if term_type_id is not UNSET:
            field_dict["termTypeId"] = term_type_id
        if term_year is not UNSET:
            field_dict["termYear"] = term_year
        if to_studysemester is not UNSET:
            field_dict["toStudysemester"] = to_studysemester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_admission_package_parameters_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParametersForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParametersForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageParametersForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        admission_package_id = d.pop("admissionPackageId", UNSET)

        application_procedure_obj_guid = d.pop("applicationProcedureObjGuid", UNSET)

        course_of_study_ids = cast(list[int], d.pop("courseOfStudyIds", UNSET))

        from_studysemester = d.pop("fromStudysemester", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        term_type_id = d.pop("termTypeId", UNSET)

        term_year = d.pop("termYear", UNSET)

        to_studysemester = d.pop("toStudysemester", UNSET)

        model_cm_app_backend_admission_admission_package_admission_package_parameters = cls(
            field_foreigntext=field_foreigntext,
            admission_package_id=admission_package_id,
            application_procedure_obj_guid=application_procedure_obj_guid,
            course_of_study_ids=course_of_study_ids,
            from_studysemester=from_studysemester,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            term_type_id=term_type_id,
            term_year=term_year,
            to_studysemester=to_studysemester,
        )

        model_cm_app_backend_admission_admission_package_admission_package_parameters.additional_properties = d
        return model_cm_app_backend_admission_admission_package_admission_package_parameters

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
