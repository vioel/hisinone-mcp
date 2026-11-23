from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cm_app_application_content_application_content_type import (
        CmAppApplicationContentApplicationContentType,
    )
    from ..models.cm_app_application_content_verification_relevance import CmAppApplicationContentVerificationRelevance
    from ..models.model_cm_app_backend_admission_admission_package_application_content_definition_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionForeigntext | Unset):
        content_type (CmAppApplicationContentApplicationContentType | Unset):
        defaulttext (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        uniquename (str | Unset):
        verification_relevance (CmAppApplicationContentVerificationRelevance | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionForeigntext | Unset = UNSET
    content_type: CmAppApplicationContentApplicationContentType | Unset = UNSET
    defaulttext: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    verification_relevance: CmAppApplicationContentVerificationRelevance | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        content_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        defaulttext = self.defaulttext

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        uniquename = self.uniquename

        verification_relevance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification_relevance, Unset):
            verification_relevance = self.verification_relevance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if verification_relevance is not UNSET:
            field_dict["verificationRelevance"] = verification_relevance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cm_app_application_content_application_content_type import (
            CmAppApplicationContentApplicationContentType,  # noqa: PLC0415
        )
        from ..models.cm_app_application_content_verification_relevance import (
            CmAppApplicationContentVerificationRelevance,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_application_content_definition_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        _content_type = d.pop("contentType", UNSET)
        content_type: CmAppApplicationContentApplicationContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = CmAppApplicationContentApplicationContentType.from_dict(_content_type)

        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        _verification_relevance = d.pop("verificationRelevance", UNSET)
        verification_relevance: CmAppApplicationContentVerificationRelevance | Unset
        if isinstance(_verification_relevance, Unset):
            verification_relevance = UNSET
        else:
            verification_relevance = CmAppApplicationContentVerificationRelevance.from_dict(_verification_relevance)

        model_cm_app_backend_admission_admission_package_application_content_definition = cls(
            field_foreigntext=field_foreigntext,
            content_type=content_type,
            defaulttext=defaulttext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            uniquename=uniquename,
            verification_relevance=verification_relevance,
        )

        model_cm_app_backend_admission_admission_package_application_content_definition.additional_properties = d
        return model_cm_app_backend_admission_admission_package_application_content_definition

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
