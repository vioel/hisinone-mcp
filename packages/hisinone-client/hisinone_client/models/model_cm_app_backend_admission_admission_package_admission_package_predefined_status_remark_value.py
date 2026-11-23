from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,
    )
    from ..models.model_cm_app_backend_admission_admission_package_admission_package_predefined_status_remark_value_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValueForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValue")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValue:
    """
    Attributes:
        field_foreigntext
            (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValueForeigntext | Unset):
        admission_package (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        predefined_status_remark_value (CsSysValueGenericValue | Unset):
        sortorder (int | Unset):
    """

    field_foreigntext: (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValueForeigntext | Unset
    ) = UNSET
    admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    predefined_status_remark_value: CsSysValueGenericValue | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_package: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admission_package, Unset):
            admission_package = self.admission_package.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        predefined_status_remark_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.predefined_status_remark_value, Unset):
            predefined_status_remark_value = self.predefined_status_remark_value.to_dict()

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_package is not UNSET:
            field_dict["admissionPackage"] = admission_package
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if predefined_status_remark_value is not UNSET:
            field_dict["predefinedStatusRemarkValue"] = predefined_status_remark_value
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_admission_package_predefined_status_remark_value_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValueForeigntext | Unset
        )
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackagePredefinedStatusRemarkValueForeigntext.from_dict(
                _field_foreigntext
            )

        _admission_package = d.pop("admissionPackage", UNSET)
        admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset
        if isinstance(_admission_package, Unset):
            admission_package = UNSET
        else:
            admission_package = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage.from_dict(_admission_package)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _predefined_status_remark_value = d.pop("predefinedStatusRemarkValue", UNSET)
        predefined_status_remark_value: CsSysValueGenericValue | Unset
        if isinstance(_predefined_status_remark_value, Unset):
            predefined_status_remark_value = UNSET
        else:
            predefined_status_remark_value = CsSysValueGenericValue.from_dict(_predefined_status_remark_value)

        sortorder = d.pop("sortorder", UNSET)

        model_cm_app_backend_admission_admission_package_admission_package_predefined_status_remark_value = cls(
            field_foreigntext=field_foreigntext,
            admission_package=admission_package,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            predefined_status_remark_value=predefined_status_remark_value,
            sortorder=sortorder,
        )

        model_cm_app_backend_admission_admission_package_admission_package_predefined_status_remark_value.additional_properties = d
        return model_cm_app_backend_admission_admission_package_admission_package_predefined_status_remark_value

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
