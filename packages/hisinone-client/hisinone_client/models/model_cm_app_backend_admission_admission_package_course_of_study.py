from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_course_of_study_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudyForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudyForeigntext | Unset):
        course_specialization (str | Unset):
        defaulttext (str | Unset):
        degree (str | Unset):
        enrollment_type (str | Unset):
        examinationversion (str | Unset):
        form_of_studies (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        major_field_of_study (str | Unset):
        obj_guid (str | Unset):
        place_of_studies (str | Unset):
        shorttext (str | Unset):
        subject (str | Unset):
        subject_indicator (str | Unset):
        type_of_study (str | Unset):
        uniquename (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudyForeigntext | Unset = UNSET
    course_specialization: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    degree: str | Unset = UNSET
    enrollment_type: str | Unset = UNSET
    examinationversion: str | Unset = UNSET
    form_of_studies: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    major_field_of_study: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    place_of_studies: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    subject: str | Unset = UNSET
    subject_indicator: str | Unset = UNSET
    type_of_study: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        course_specialization = self.course_specialization

        defaulttext = self.defaulttext

        degree = self.degree

        enrollment_type = self.enrollment_type

        examinationversion = self.examinationversion

        form_of_studies = self.form_of_studies

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        major_field_of_study = self.major_field_of_study

        obj_guid = self.obj_guid

        place_of_studies = self.place_of_studies

        shorttext = self.shorttext

        subject = self.subject

        subject_indicator = self.subject_indicator

        type_of_study = self.type_of_study

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if course_specialization is not UNSET:
            field_dict["courseSpecialization"] = course_specialization
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if degree is not UNSET:
            field_dict["degree"] = degree
        if enrollment_type is not UNSET:
            field_dict["enrollmentType"] = enrollment_type
        if examinationversion is not UNSET:
            field_dict["examinationversion"] = examinationversion
        if form_of_studies is not UNSET:
            field_dict["formOfStudies"] = form_of_studies
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if major_field_of_study is not UNSET:
            field_dict["majorFieldOfStudy"] = major_field_of_study
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if place_of_studies is not UNSET:
            field_dict["placeOfStudies"] = place_of_studies
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if subject is not UNSET:
            field_dict["subject"] = subject
        if subject_indicator is not UNSET:
            field_dict["subjectIndicator"] = subject_indicator
        if type_of_study is not UNSET:
            field_dict["typeOfStudy"] = type_of_study
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_course_of_study_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudyForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudyForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudyForeigntext.from_dict(
                _field_foreigntext
            )

        course_specialization = d.pop("courseSpecialization", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        degree = d.pop("degree", UNSET)

        enrollment_type = d.pop("enrollmentType", UNSET)

        examinationversion = d.pop("examinationversion", UNSET)

        form_of_studies = d.pop("formOfStudies", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        major_field_of_study = d.pop("majorFieldOfStudy", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        place_of_studies = d.pop("placeOfStudies", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        subject = d.pop("subject", UNSET)

        subject_indicator = d.pop("subjectIndicator", UNSET)

        type_of_study = d.pop("typeOfStudy", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        model_cm_app_backend_admission_admission_package_course_of_study = cls(
            field_foreigntext=field_foreigntext,
            course_specialization=course_specialization,
            defaulttext=defaulttext,
            degree=degree,
            enrollment_type=enrollment_type,
            examinationversion=examinationversion,
            form_of_studies=form_of_studies,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            major_field_of_study=major_field_of_study,
            obj_guid=obj_guid,
            place_of_studies=place_of_studies,
            shorttext=shorttext,
            subject=subject,
            subject_indicator=subject_indicator,
            type_of_study=type_of_study,
            uniquename=uniquename,
        )

        model_cm_app_backend_admission_admission_package_course_of_study.additional_properties = d
        return model_cm_app_backend_admission_admission_package_course_of_study

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
