from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,
    )
    from ..models.model_cm_app_backend_admission_admission_package_application_content_definition_admission_package import (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage,
    )
    from ..models.model_cm_app_backend_admission_admission_package_copy_admission_package_parameters_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParametersForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParameters")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParameters:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParametersForeigntext | Unset):
        admission_package (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset):
        application_content_definition_admission_packages
            (list[ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage] | Unset):
        course_of_study_ids (list[int] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        predefined_status_remark_ids (list[int] | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParametersForeigntext | Unset = (
        UNSET
    )
    admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset = UNSET
    application_content_definition_admission_packages: (
        list[ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage] | Unset
    ) = UNSET
    course_of_study_ids: list[int] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    predefined_status_remark_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_package: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admission_package, Unset):
            admission_package = self.admission_package.to_dict()

        application_content_definition_admission_packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.application_content_definition_admission_packages, Unset):
            application_content_definition_admission_packages = []
            for (
                application_content_definition_admission_packages_item_data
            ) in self.application_content_definition_admission_packages:
                application_content_definition_admission_packages_item = (
                    application_content_definition_admission_packages_item_data.to_dict()
                )
                application_content_definition_admission_packages.append(
                    application_content_definition_admission_packages_item
                )

        course_of_study_ids: list[int] | Unset = UNSET
        if not isinstance(self.course_of_study_ids, Unset):
            course_of_study_ids = self.course_of_study_ids

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        predefined_status_remark_ids: list[int] | Unset = UNSET
        if not isinstance(self.predefined_status_remark_ids, Unset):
            predefined_status_remark_ids = self.predefined_status_remark_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_package is not UNSET:
            field_dict["admissionPackage"] = admission_package
        if application_content_definition_admission_packages is not UNSET:
            field_dict["applicationContentDefinitionAdmissionPackages"] = (
                application_content_definition_admission_packages
            )
        if course_of_study_ids is not UNSET:
            field_dict["courseOfStudyIds"] = course_of_study_ids
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if predefined_status_remark_ids is not UNSET:
            field_dict["predefinedStatusRemarkIds"] = predefined_status_remark_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_application_content_definition_admission_package import (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_copy_admission_package_parameters_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParametersForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParametersForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                ModelCmAppBackendAdmissionAdmissionPackageCopyAdmissionPackageParametersForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        _admission_package = d.pop("admissionPackage", UNSET)
        admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset
        if isinstance(_admission_package, Unset):
            admission_package = UNSET
        else:
            admission_package = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage.from_dict(_admission_package)

        _application_content_definition_admission_packages = d.pop(
            "applicationContentDefinitionAdmissionPackages", UNSET
        )
        application_content_definition_admission_packages: (
            list[ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage] | Unset
        ) = UNSET
        if _application_content_definition_admission_packages is not UNSET:
            application_content_definition_admission_packages = []
            for (
                application_content_definition_admission_packages_item_data
            ) in _application_content_definition_admission_packages:
                application_content_definition_admission_packages_item = (
                    ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage.from_dict(
                        application_content_definition_admission_packages_item_data
                    )
                )

                application_content_definition_admission_packages.append(
                    application_content_definition_admission_packages_item
                )

        course_of_study_ids = cast(list[int], d.pop("courseOfStudyIds", UNSET))

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        predefined_status_remark_ids = cast(list[int], d.pop("predefinedStatusRemarkIds", UNSET))

        model_cm_app_backend_admission_admission_package_copy_admission_package_parameters = cls(
            field_foreigntext=field_foreigntext,
            admission_package=admission_package,
            application_content_definition_admission_packages=application_content_definition_admission_packages,
            course_of_study_ids=course_of_study_ids,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            predefined_status_remark_ids=predefined_status_remark_ids,
        )

        model_cm_app_backend_admission_admission_package_copy_admission_package_parameters.additional_properties = d
        return model_cm_app_backend_admission_admission_package_copy_admission_package_parameters

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
