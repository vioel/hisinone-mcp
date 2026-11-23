from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_admission_package_usages_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsagesForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsages")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsages:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsagesForeigntext | Unset):
        id (int | Unset):
        in_use_in_released_rankings (bool | Unset):
        in_use_in_request_subjects (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsagesForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    in_use_in_released_rankings: bool | Unset = UNSET
    in_use_in_request_subjects: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        in_use_in_released_rankings = self.in_use_in_released_rankings

        in_use_in_request_subjects = self.in_use_in_request_subjects

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if in_use_in_released_rankings is not UNSET:
            field_dict["inUseInReleasedRankings"] = in_use_in_released_rankings
        if in_use_in_request_subjects is not UNSET:
            field_dict["inUseInRequestSubjects"] = in_use_in_request_subjects
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_admission_package_usages_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsagesForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsagesForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackageUsagesForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        in_use_in_released_rankings = d.pop("inUseInReleasedRankings", UNSET)

        in_use_in_request_subjects = d.pop("inUseInRequestSubjects", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_admission_admission_package_admission_package_usages = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            in_use_in_released_rankings=in_use_in_released_rankings,
            in_use_in_request_subjects=in_use_in_request_subjects,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_admission_admission_package_admission_package_usages.additional_properties = d
        return model_cm_app_backend_admission_admission_package_admission_package_usages

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
