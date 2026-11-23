from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_psv_identityprovider_identity_provider_configuration_parameter_rest_foreigntext import (
        ImplPsvIdentityproviderIdentityProviderConfigurationParameterRestForeigntext,
    )
    from ..models.impl_psv_identityprovider_identity_provider_context_value_rest import (
        ImplPsvIdentityproviderIdentityProviderContextValueRest,
    )


T = TypeVar("T", bound="ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest")


@_attrs_define
class ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest:
    """
    Attributes:
        field_foreigntext (ImplPsvIdentityproviderIdentityProviderConfigurationParameterRestForeigntext | Unset):
        id (int | Unset):
        identity_provider_configuration_id (int | Unset):
        identity_provider_context_value (ImplPsvIdentityproviderIdentityProviderContextValueRest | Unset):
        identity_verification (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        parameter_name (str | Unset):
        parameter_type (str | Unset):
        parameter_value (str | Unset):
    """

    field_foreigntext: ImplPsvIdentityproviderIdentityProviderConfigurationParameterRestForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    identity_provider_configuration_id: int | Unset = UNSET
    identity_provider_context_value: ImplPsvIdentityproviderIdentityProviderContextValueRest | Unset = UNSET
    identity_verification: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    parameter_type: str | Unset = UNSET
    parameter_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        identity_provider_configuration_id = self.identity_provider_configuration_id

        identity_provider_context_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identity_provider_context_value, Unset):
            identity_provider_context_value = self.identity_provider_context_value.to_dict()

        identity_verification = self.identity_verification

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        parameter_name = self.parameter_name

        parameter_type = self.parameter_type

        parameter_value = self.parameter_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if identity_provider_configuration_id is not UNSET:
            field_dict["identityProviderConfigurationId"] = identity_provider_configuration_id
        if identity_provider_context_value is not UNSET:
            field_dict["identityProviderContextValue"] = identity_provider_context_value
        if identity_verification is not UNSET:
            field_dict["identityVerification"] = identity_verification
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if parameter_type is not UNSET:
            field_dict["parameterType"] = parameter_type
        if parameter_value is not UNSET:
            field_dict["parameterValue"] = parameter_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_psv_identityprovider_identity_provider_configuration_parameter_rest_foreigntext import (
            ImplPsvIdentityproviderIdentityProviderConfigurationParameterRestForeigntext,  # noqa: PLC0415
        )
        from ..models.impl_psv_identityprovider_identity_provider_context_value_rest import (
            ImplPsvIdentityproviderIdentityProviderContextValueRest,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplPsvIdentityproviderIdentityProviderConfigurationParameterRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplPsvIdentityproviderIdentityProviderConfigurationParameterRestForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        identity_provider_configuration_id = d.pop("identityProviderConfigurationId", UNSET)

        _identity_provider_context_value = d.pop("identityProviderContextValue", UNSET)
        identity_provider_context_value: ImplPsvIdentityproviderIdentityProviderContextValueRest | Unset
        if isinstance(_identity_provider_context_value, Unset):
            identity_provider_context_value = UNSET
        else:
            identity_provider_context_value = ImplPsvIdentityproviderIdentityProviderContextValueRest.from_dict(
                _identity_provider_context_value
            )

        identity_verification = d.pop("identityVerification", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        parameter_type = d.pop("parameterType", UNSET)

        parameter_value = d.pop("parameterValue", UNSET)

        impl_psv_identityprovider_identity_provider_configuration_parameter_rest = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            identity_provider_configuration_id=identity_provider_configuration_id,
            identity_provider_context_value=identity_provider_context_value,
            identity_verification=identity_verification,
            lock_version=lock_version,
            obj_guid=obj_guid,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            parameter_value=parameter_value,
        )

        impl_psv_identityprovider_identity_provider_configuration_parameter_rest.additional_properties = d
        return impl_psv_identityprovider_identity_provider_configuration_parameter_rest

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
