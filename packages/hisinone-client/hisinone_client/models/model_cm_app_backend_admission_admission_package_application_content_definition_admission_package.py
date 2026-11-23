from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cm_app_application_content_verification_relevance import CmAppApplicationContentVerificationRelevance
    from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
        ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,
    )
    from ..models.model_cm_app_backend_admission_admission_package_application_content_condition import (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition,
    )
    from ..models.model_cm_app_backend_admission_admission_package_application_content_definition import (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition,
    )
    from ..models.model_cm_app_backend_admission_admission_package_application_content_definition_admission_package_foreigntext import (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackageForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage")


@_attrs_define
class ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackage:
    """
    Attributes:
        field_foreigntext
            (ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackageForeigntext | Unset):
        admission_package (ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset):
        application_content_definition (ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition | Unset):
        condition (ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition | Unset):
        id (int | Unset):
        is_optional (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        optional (bool | Unset):
        sortorder (int | Unset):
        verification_condition (ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition | Unset):
        verification_relevance (CmAppApplicationContentVerificationRelevance | Unset):
    """

    field_foreigntext: (
        ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackageForeigntext | Unset
    ) = UNSET
    admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset = UNSET
    application_content_definition: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition | Unset = (
        UNSET
    )
    condition: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition | Unset = UNSET
    id: int | Unset = UNSET
    is_optional: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    optional: bool | Unset = UNSET
    sortorder: int | Unset = UNSET
    verification_condition: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition | Unset = UNSET
    verification_relevance: CmAppApplicationContentVerificationRelevance | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_package: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admission_package, Unset):
            admission_package = self.admission_package.to_dict()

        application_content_definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_content_definition, Unset):
            application_content_definition = self.application_content_definition.to_dict()

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        id = self.id

        is_optional = self.is_optional

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        optional = self.optional

        sortorder = self.sortorder

        verification_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification_condition, Unset):
            verification_condition = self.verification_condition.to_dict()

        verification_relevance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification_relevance, Unset):
            verification_relevance = self.verification_relevance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_package is not UNSET:
            field_dict["admissionPackage"] = admission_package
        if application_content_definition is not UNSET:
            field_dict["applicationContentDefinition"] = application_content_definition
        if condition is not UNSET:
            field_dict["condition"] = condition
        if id is not UNSET:
            field_dict["id"] = id
        if is_optional is not UNSET:
            field_dict["isOptional"] = is_optional
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if optional is not UNSET:
            field_dict["optional"] = optional
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if verification_condition is not UNSET:
            field_dict["verificationCondition"] = verification_condition
        if verification_relevance is not UNSET:
            field_dict["verificationRelevance"] = verification_relevance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cm_app_application_content_verification_relevance import (
            CmAppApplicationContentVerificationRelevance,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_admission_package import (
            ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_application_content_condition import (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_application_content_definition import (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_admission_package_application_content_definition_admission_package_foreigntext import (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackageForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: (
            ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackageForeigntext | Unset
        )
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinitionAdmissionPackageForeigntext.from_dict(
                _field_foreigntext
            )

        _admission_package = d.pop("admissionPackage", UNSET)
        admission_package: ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage | Unset
        if isinstance(_admission_package, Unset):
            admission_package = UNSET
        else:
            admission_package = ModelCmAppBackendAdmissionAdmissionPackageAdmissionPackage.from_dict(_admission_package)

        _application_content_definition = d.pop("applicationContentDefinition", UNSET)
        application_content_definition: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition | Unset
        if isinstance(_application_content_definition, Unset):
            application_content_definition = UNSET
        else:
            application_content_definition = (
                ModelCmAppBackendAdmissionAdmissionPackageApplicationContentDefinition.from_dict(
                    _application_content_definition
                )
            )

        _condition = d.pop("condition", UNSET)
        condition: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition.from_dict(_condition)

        id = d.pop("id", UNSET)

        is_optional = d.pop("isOptional", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        optional = d.pop("optional", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        _verification_condition = d.pop("verificationCondition", UNSET)
        verification_condition: ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition | Unset
        if isinstance(_verification_condition, Unset):
            verification_condition = UNSET
        else:
            verification_condition = ModelCmAppBackendAdmissionAdmissionPackageApplicationContentCondition.from_dict(
                _verification_condition
            )

        _verification_relevance = d.pop("verificationRelevance", UNSET)
        verification_relevance: CmAppApplicationContentVerificationRelevance | Unset
        if isinstance(_verification_relevance, Unset):
            verification_relevance = UNSET
        else:
            verification_relevance = CmAppApplicationContentVerificationRelevance.from_dict(_verification_relevance)

        model_cm_app_backend_admission_admission_package_application_content_definition_admission_package = cls(
            field_foreigntext=field_foreigntext,
            admission_package=admission_package,
            application_content_definition=application_content_definition,
            condition=condition,
            id=id,
            is_optional=is_optional,
            lock_version=lock_version,
            obj_guid=obj_guid,
            optional=optional,
            sortorder=sortorder,
            verification_condition=verification_condition,
            verification_relevance=verification_relevance,
        )

        model_cm_app_backend_admission_admission_package_application_content_definition_admission_package.additional_properties = d
        return model_cm_app_backend_admission_admission_package_application_content_definition_admission_package

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
