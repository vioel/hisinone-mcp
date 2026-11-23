from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_postaddress_foreigntext import (
        CsPsvExternalOrganisationPostaddressForeigntext,
    )
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvExternalOrganisationPostaddress")


@_attrs_define
class CsPsvExternalOrganisationPostaddress:
    """
    Attributes:
        field_foreigntext (CsPsvExternalOrganisationPostaddressForeigntext | Unset):
        city (str | Unset):
        country (CsSysValueGenericValue | Unset):
        district (CsSysValueGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        postcode (str | Unset):
        street (str | Unset):
    """

    field_foreigntext: CsPsvExternalOrganisationPostaddressForeigntext | Unset = UNSET
    city: str | Unset = UNSET
    country: CsSysValueGenericValue | Unset = UNSET
    district: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    postcode: str | Unset = UNSET
    street: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        city = self.city

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        district: dict[str, Any] | Unset = UNSET
        if not isinstance(self.district, Unset):
            district = self.district.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        postcode = self.postcode

        street = self.street

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if district is not UNSET:
            field_dict["district"] = district
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if street is not UNSET:
            field_dict["street"] = street

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_postaddress_foreigntext import (
            CsPsvExternalOrganisationPostaddressForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvExternalOrganisationPostaddressForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvExternalOrganisationPostaddressForeigntext.from_dict(_field_foreigntext)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: CsSysValueGenericValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = CsSysValueGenericValue.from_dict(_country)

        _district = d.pop("district", UNSET)
        district: CsSysValueGenericValue | Unset
        if isinstance(_district, Unset):
            district = UNSET
        else:
            district = CsSysValueGenericValue.from_dict(_district)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        postcode = d.pop("postcode", UNSET)

        street = d.pop("street", UNSET)

        cs_psv_external_organisation_postaddress = cls(
            field_foreigntext=field_foreigntext,
            city=city,
            country=country,
            district=district,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            postcode=postcode,
            street=street,
        )

        cs_psv_external_organisation_postaddress.additional_properties = d
        return cs_psv_external_organisation_postaddress

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
