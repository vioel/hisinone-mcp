from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_psv_identityprovider_identity_provider_conf_src_rest_foreigntext import (
        ImplPsvIdentityproviderIdentityProviderConfSrcRestForeigntext,
    )


T = TypeVar("T", bound="ImplPsvIdentityproviderIdentityProviderConfSrcRest")


@_attrs_define
class ImplPsvIdentityproviderIdentityProviderConfSrcRest:
    """
    Attributes:
        field_foreigntext (ImplPsvIdentityproviderIdentityProviderConfSrcRestForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        priority (int | Unset):
        uniquename (str | Unset):
    """

    field_foreigntext: ImplPsvIdentityproviderIdentityProviderConfSrcRestForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    priority: int | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        priority = self.priority

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if priority is not UNSET:
            field_dict["priority"] = priority
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_psv_identityprovider_identity_provider_conf_src_rest_foreigntext import (
            ImplPsvIdentityproviderIdentityProviderConfSrcRestForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplPsvIdentityproviderIdentityProviderConfSrcRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplPsvIdentityproviderIdentityProviderConfSrcRestForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        priority = d.pop("priority", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        impl_psv_identityprovider_identity_provider_conf_src_rest = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            priority=priority,
            uniquename=uniquename,
        )

        impl_psv_identityprovider_identity_provider_conf_src_rest.additional_properties = d
        return impl_psv_identityprovider_identity_provider_conf_src_rest

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
