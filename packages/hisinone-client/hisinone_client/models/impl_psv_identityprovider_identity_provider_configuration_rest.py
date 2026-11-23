from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.impl_psv_identityprovider_identity_provider_configuration_parameter_rest import (
        ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest,
    )
    from ..models.impl_psv_identityprovider_identity_provider_configuration_rest_foreigntext import (
        ImplPsvIdentityproviderIdentityProviderConfigurationRestForeigntext,
    )


T = TypeVar("T", bound="ImplPsvIdentityproviderIdentityProviderConfigurationRest")


@_attrs_define
class ImplPsvIdentityproviderIdentityProviderConfigurationRest:
    """
    Attributes:
        field_foreigntext (ImplPsvIdentityproviderIdentityProviderConfigurationRestForeigntext | Unset):
        conf_src (str | Unset):
        id (int | Unset):
        identity_provider_configuration_parameter_rest_dtos
            (list[ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest] | Unset):
        identity_provider_id (int | Unset):
        lock_version (int | Unset):
        notification_category (str | Unset):
        obj_guid (str | Unset):
        person_identifier_type (CsSysValueGenericValue | Unset):
        protocol_type (str | Unset):
        subscriber_message_template_id (int | Unset):
    """

    field_foreigntext: ImplPsvIdentityproviderIdentityProviderConfigurationRestForeigntext | Unset = UNSET
    conf_src: str | Unset = UNSET
    id: int | Unset = UNSET
    identity_provider_configuration_parameter_rest_dtos: (
        list[ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest] | Unset
    ) = UNSET
    identity_provider_id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    notification_category: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person_identifier_type: CsSysValueGenericValue | Unset = UNSET
    protocol_type: str | Unset = UNSET
    subscriber_message_template_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        conf_src = self.conf_src

        id = self.id

        identity_provider_configuration_parameter_rest_dtos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identity_provider_configuration_parameter_rest_dtos, Unset):
            identity_provider_configuration_parameter_rest_dtos = []
            for (
                identity_provider_configuration_parameter_rest_dtos_item_data
            ) in self.identity_provider_configuration_parameter_rest_dtos:
                identity_provider_configuration_parameter_rest_dtos_item = (
                    identity_provider_configuration_parameter_rest_dtos_item_data.to_dict()
                )
                identity_provider_configuration_parameter_rest_dtos.append(
                    identity_provider_configuration_parameter_rest_dtos_item
                )

        identity_provider_id = self.identity_provider_id

        lock_version = self.lock_version

        notification_category = self.notification_category

        obj_guid = self.obj_guid

        person_identifier_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person_identifier_type, Unset):
            person_identifier_type = self.person_identifier_type.to_dict()

        protocol_type = self.protocol_type

        subscriber_message_template_id = self.subscriber_message_template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if conf_src is not UNSET:
            field_dict["confSrc"] = conf_src
        if id is not UNSET:
            field_dict["id"] = id
        if identity_provider_configuration_parameter_rest_dtos is not UNSET:
            field_dict["identityProviderConfigurationParameterRestDtos"] = (
                identity_provider_configuration_parameter_rest_dtos
            )
        if identity_provider_id is not UNSET:
            field_dict["identityProviderId"] = identity_provider_id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if notification_category is not UNSET:
            field_dict["notificationCategory"] = notification_category
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person_identifier_type is not UNSET:
            field_dict["personIdentifierType"] = person_identifier_type
        if protocol_type is not UNSET:
            field_dict["protocolType"] = protocol_type
        if subscriber_message_template_id is not UNSET:
            field_dict["subscriberMessageTemplateId"] = subscriber_message_template_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.impl_psv_identityprovider_identity_provider_configuration_parameter_rest import (
            ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest,  # noqa: PLC0415
        )
        from ..models.impl_psv_identityprovider_identity_provider_configuration_rest_foreigntext import (
            ImplPsvIdentityproviderIdentityProviderConfigurationRestForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplPsvIdentityproviderIdentityProviderConfigurationRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplPsvIdentityproviderIdentityProviderConfigurationRestForeigntext.from_dict(
                _field_foreigntext
            )

        conf_src = d.pop("confSrc", UNSET)

        id = d.pop("id", UNSET)

        _identity_provider_configuration_parameter_rest_dtos = d.pop(
            "identityProviderConfigurationParameterRestDtos", UNSET
        )
        identity_provider_configuration_parameter_rest_dtos: (
            list[ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest] | Unset
        ) = UNSET
        if _identity_provider_configuration_parameter_rest_dtos is not UNSET:
            identity_provider_configuration_parameter_rest_dtos = []
            for (
                identity_provider_configuration_parameter_rest_dtos_item_data
            ) in _identity_provider_configuration_parameter_rest_dtos:
                identity_provider_configuration_parameter_rest_dtos_item = (
                    ImplPsvIdentityproviderIdentityProviderConfigurationParameterRest.from_dict(
                        identity_provider_configuration_parameter_rest_dtos_item_data
                    )
                )

                identity_provider_configuration_parameter_rest_dtos.append(
                    identity_provider_configuration_parameter_rest_dtos_item
                )

        identity_provider_id = d.pop("identityProviderId", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        notification_category = d.pop("notificationCategory", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _person_identifier_type = d.pop("personIdentifierType", UNSET)
        person_identifier_type: CsSysValueGenericValue | Unset
        if isinstance(_person_identifier_type, Unset):
            person_identifier_type = UNSET
        else:
            person_identifier_type = CsSysValueGenericValue.from_dict(_person_identifier_type)

        protocol_type = d.pop("protocolType", UNSET)

        subscriber_message_template_id = d.pop("subscriberMessageTemplateId", UNSET)

        impl_psv_identityprovider_identity_provider_configuration_rest = cls(
            field_foreigntext=field_foreigntext,
            conf_src=conf_src,
            id=id,
            identity_provider_configuration_parameter_rest_dtos=identity_provider_configuration_parameter_rest_dtos,
            identity_provider_id=identity_provider_id,
            lock_version=lock_version,
            notification_category=notification_category,
            obj_guid=obj_guid,
            person_identifier_type=person_identifier_type,
            protocol_type=protocol_type,
            subscriber_message_template_id=subscriber_message_template_id,
        )

        impl_psv_identityprovider_identity_provider_configuration_rest.additional_properties = d
        return impl_psv_identityprovider_identity_provider_configuration_rest

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
