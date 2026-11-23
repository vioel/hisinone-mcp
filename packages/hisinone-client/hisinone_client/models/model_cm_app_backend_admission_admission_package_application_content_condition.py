from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_admission_package_application_content_condition_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentConditionForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageApplicationContentConditionForeigntext | Unset):
        defaulttext (str | Unset):
        description (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        unique_name (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentConditionForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    unique_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        description = self.description

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        unique_name = self.unique_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_admission_package_application_content_condition_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentConditionForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentConditionForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                ModelCmAppBackendAdmissionAdmissionPackageApplicationContentConditionForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        defaulttext = d.pop("defaulttext", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        unique_name = d.pop("uniqueName", UNSET)

        model_cm_app_backend_admission_admission_package_application_content_condition = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            description=description,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            unique_name=unique_name,
        )

        model_cm_app_backend_admission_admission_package_application_content_condition.additional_properties = d
        return model_cm_app_backend_admission_admission_package_application_content_condition

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
