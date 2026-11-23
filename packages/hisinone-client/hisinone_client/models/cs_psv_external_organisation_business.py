from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_business_foreigntext import CsPsvExternalOrganisationBusinessForeigntext
    from ..models.cs_psv_external_organisation_postaddress import CsPsvExternalOrganisationPostaddress


T = TypeVar("T", bound="CsPsvExternalOrganisationBusiness")


@_attrs_define
class CsPsvExternalOrganisationBusiness:
    """
    Attributes:
        field_foreigntext (CsPsvExternalOrganisationBusinessForeigntext | Unset):
        defaulttext (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        post_addresses (list[CsPsvExternalOrganisationPostaddress] | Unset):
    """

    field_foreigntext: CsPsvExternalOrganisationBusinessForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    post_addresses: list[CsPsvExternalOrganisationPostaddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        post_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_addresses, Unset):
            post_addresses = []
            for post_addresses_item_data in self.post_addresses:
                post_addresses_item = post_addresses_item_data.to_dict()
                post_addresses.append(post_addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if post_addresses is not UNSET:
            field_dict["postAddresses"] = post_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_business_foreigntext import (
            CsPsvExternalOrganisationBusinessForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_psv_external_organisation_postaddress import CsPsvExternalOrganisationPostaddress  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvExternalOrganisationBusinessForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvExternalOrganisationBusinessForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _post_addresses = d.pop("postAddresses", UNSET)
        post_addresses: list[CsPsvExternalOrganisationPostaddress] | Unset = UNSET
        if _post_addresses is not UNSET:
            post_addresses = []
            for post_addresses_item_data in _post_addresses:
                post_addresses_item = CsPsvExternalOrganisationPostaddress.from_dict(post_addresses_item_data)

                post_addresses.append(post_addresses_item)

        cs_psv_external_organisation_business = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            post_addresses=post_addresses,
        )

        cs_psv_external_organisation_business.additional_properties = d
        return cs_psv_external_organisation_business

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
