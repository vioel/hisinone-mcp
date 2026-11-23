from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_identity_provider_identity_provider_foreigntext import (
        CsPsvIdentityProviderIdentityProviderForeigntext,
    )
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.impl_psv_identityprovider_identity_provider_configuration_rest import (
        ImplPsvIdentityproviderIdentityProviderConfigurationRest,
    )


T = TypeVar("T", bound="CsPsvIdentityProviderIdentityProvider")


@_attrs_define
class CsPsvIdentityProviderIdentityProvider:
    """
    Attributes:
        field_foreigntext (CsPsvIdentityProviderIdentityProviderForeigntext | Unset):
        defaulttext (str | Unset):
        description (str | Unset):
        id (int | Unset):
        identity_provider_configurations (list[ImplPsvIdentityproviderIdentityProviderConfigurationRest] | Unset):
        lock_version (int | Unset):
        logo (CsSysUploadConfigurationHisUploadFile | Unset):
        obj_guid (str | Unset):
        redirect_url (str | Unset):
        selected_context (list[int] | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: CsPsvIdentityProviderIdentityProviderForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    identity_provider_configurations: list[ImplPsvIdentityproviderIdentityProviderConfigurationRest] | Unset = UNSET
    lock_version: int | Unset = UNSET
    logo: CsSysUploadConfigurationHisUploadFile | Unset = UNSET
    obj_guid: str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    selected_context: list[int] | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        description = self.description

        id = self.id

        identity_provider_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identity_provider_configurations, Unset):
            identity_provider_configurations = []
            for identity_provider_configurations_item_data in self.identity_provider_configurations:
                identity_provider_configurations_item = identity_provider_configurations_item_data.to_dict()
                identity_provider_configurations.append(identity_provider_configurations_item)

        lock_version = self.lock_version

        logo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        obj_guid = self.obj_guid

        redirect_url = self.redirect_url

        selected_context: list[int] | Unset = UNSET
        if not isinstance(self.selected_context, Unset):
            selected_context = self.selected_context

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

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
        if identity_provider_configurations is not UNSET:
            field_dict["identityProviderConfigurations"] = identity_provider_configurations
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if logo is not UNSET:
            field_dict["logo"] = logo
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if selected_context is not UNSET:
            field_dict["selectedContext"] = selected_context
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_identity_provider_identity_provider_foreigntext import (
            CsPsvIdentityProviderIdentityProviderForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.impl_psv_identityprovider_identity_provider_configuration_rest import (
            ImplPsvIdentityproviderIdentityProviderConfigurationRest,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvIdentityProviderIdentityProviderForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvIdentityProviderIdentityProviderForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _identity_provider_configurations = d.pop("identityProviderConfigurations", UNSET)
        identity_provider_configurations: list[ImplPsvIdentityproviderIdentityProviderConfigurationRest] | Unset = UNSET
        if _identity_provider_configurations is not UNSET:
            identity_provider_configurations = []
            for identity_provider_configurations_item_data in _identity_provider_configurations:
                identity_provider_configurations_item = (
                    ImplPsvIdentityproviderIdentityProviderConfigurationRest.from_dict(
                        identity_provider_configurations_item_data
                    )
                )

                identity_provider_configurations.append(identity_provider_configurations_item)

        lock_version = d.pop("lockVersion", UNSET)

        _logo = d.pop("logo", UNSET)
        logo: CsSysUploadConfigurationHisUploadFile | Unset
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = CsSysUploadConfigurationHisUploadFile.from_dict(_logo)

        obj_guid = d.pop("objGuid", UNSET)

        redirect_url = d.pop("redirectUrl", UNSET)

        selected_context = cast(list[int], d.pop("selectedContext", UNSET))

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        cs_psv_identity_provider_identity_provider = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            description=description,
            id=id,
            identity_provider_configurations=identity_provider_configurations,
            lock_version=lock_version,
            logo=logo,
            obj_guid=obj_guid,
            redirect_url=redirect_url,
            selected_context=selected_context,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        cs_psv_identity_provider_identity_provider.additional_properties = d
        return cs_psv_identity_provider_identity_provider

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
