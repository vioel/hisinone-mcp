from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,
    )
    from ..models.model_cm_app_backend_admission_admission_package_admissionshare_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionshareForeigntext,
    )
    from ..models.model_cm_app_backend_admission_admission_package_course_of_study import (
        ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageAdmissionshare")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageAdmissionshare:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageAdmissionshareForeigntext | Unset):
        admission_package (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset):
        course_of_study (ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy | Unset):
        denominator (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        numerator (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionshareForeigntext | Unset = UNSET
    admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset = UNSET
    course_of_study: ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy | Unset = UNSET
    denominator: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    numerator: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_package: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admission_package, Unset):
            admission_package = self.admission_package.to_dict()

        course_of_study: dict[str, Any] | Unset = UNSET
        if not isinstance(self.course_of_study, Unset):
            course_of_study = self.course_of_study.to_dict()

        denominator = self.denominator

        id = self.id

        lock_version = self.lock_version

        numerator = self.numerator

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_package is not UNSET:
            field_dict["admissionPackage"] = admission_package
        if course_of_study is not UNSET:
            field_dict["courseOfStudy"] = course_of_study
        if denominator is not UNSET:
            field_dict["denominator"] = denominator
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if numerator is not UNSET:
            field_dict["numerator"] = numerator
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_admissionshare_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionshareForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_course_of_study import (
            ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionshareForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageAdmissionshareForeigntext.from_dict(
                _field_foreigntext
            )

        _admission_package = d.pop("admissionPackage", UNSET)
        admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset
        if isinstance(_admission_package, Unset):
            admission_package = UNSET
        else:
            admission_package = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage.from_dict(_admission_package)

        _course_of_study = d.pop("courseOfStudy", UNSET)
        course_of_study: ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy | Unset
        if isinstance(_course_of_study, Unset):
            course_of_study = UNSET
        else:
            course_of_study = ModelCmAppBackendAdmissionAdmissionPackageCourseOfStudy.from_dict(_course_of_study)

        denominator = d.pop("denominator", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        numerator = d.pop("numerator", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_admission_admission_package_admissionshare = cls(
            field_foreigntext=field_foreigntext,
            admission_package=admission_package,
            course_of_study=course_of_study,
            denominator=denominator,
            id=id,
            lock_version=lock_version,
            numerator=numerator,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_admission_admission_package_admissionshare.additional_properties = d
        return model_cm_app_backend_admission_admission_package_admissionshare

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
