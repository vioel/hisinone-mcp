from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_app_key_enum_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnumForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnum:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnumForeigntext | Unset):
        id (int | Unset):
        key (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        translated_i18_n_key (str | Unset):
        type_ (Any | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnumForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    key: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    translated_i18_n_key: str | Unset = UNSET
    type_: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        key = self.key

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        translated_i18_n_key = self.translated_i18_n_key

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if translated_i18_n_key is not UNSET:
            field_dict["translatedI18nKey"] = translated_i18_n_key
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_app_key_enum_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnumForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnumForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageAPPKeyEnumForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        translated_i18_n_key = d.pop("translatedI18nKey", UNSET)

        type_ = d.pop("type", UNSET)

        model_cm_app_backend_admission_admission_package_app_key_enum = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            key=key,
            lock_version=lock_version,
            obj_guid=obj_guid,
            translated_i18_n_key=translated_i18_n_key,
            type_=type_,
        )

        model_cm_app_backend_admission_admission_package_app_key_enum.additional_properties = d
        return model_cm_app_backend_admission_admission_package_app_key_enum

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
