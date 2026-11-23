from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_post_address_rest_foreigntext import CsPsvPostAddressRestForeigntext
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPostAddressRest")


@_attrs_define
class CsPsvPostAddressRest:
    """
    Attributes:
        field_foreigntext (CsPsvPostAddressRestForeigntext | Unset):
        addressaddition (str | Unset):
        city (str | Unset):
        company (str | Unset):
        country (str | Unset):
        district (str | Unset):
        division_name (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        postcode (str | Unset):
        postofficebox (str | Unset):
        state (str | Unset):
        street (str | Unset):
        type_ (CsSysValueGenericValue | Unset):
    """

    field_foreigntext: CsPsvPostAddressRestForeigntext | Unset = UNSET
    addressaddition: str | Unset = UNSET
    city: str | Unset = UNSET
    company: str | Unset = UNSET
    country: str | Unset = UNSET
    district: str | Unset = UNSET
    division_name: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    postcode: str | Unset = UNSET
    postofficebox: str | Unset = UNSET
    state: str | Unset = UNSET
    street: str | Unset = UNSET
    type_: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        addressaddition = self.addressaddition

        city = self.city

        company = self.company

        country = self.country

        district = self.district

        division_name = self.division_name

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        postcode = self.postcode

        postofficebox = self.postofficebox

        state = self.state

        street = self.street

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if addressaddition is not UNSET:
            field_dict["addressaddition"] = addressaddition
        if city is not UNSET:
            field_dict["city"] = city
        if company is not UNSET:
            field_dict["company"] = company
        if country is not UNSET:
            field_dict["country"] = country
        if district is not UNSET:
            field_dict["district"] = district
        if division_name is not UNSET:
            field_dict["divisionName"] = division_name
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if postofficebox is not UNSET:
            field_dict["postofficebox"] = postofficebox
        if state is not UNSET:
            field_dict["state"] = state
        if street is not UNSET:
            field_dict["street"] = street
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_post_address_rest_foreigntext import CsPsvPostAddressRestForeigntext  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPostAddressRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPostAddressRestForeigntext.from_dict(_field_foreigntext)

        addressaddition = d.pop("addressaddition", UNSET)

        city = d.pop("city", UNSET)

        company = d.pop("company", UNSET)

        country = d.pop("country", UNSET)

        district = d.pop("district", UNSET)

        division_name = d.pop("divisionName", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        postcode = d.pop("postcode", UNSET)

        postofficebox = d.pop("postofficebox", UNSET)

        state = d.pop("state", UNSET)

        street = d.pop("street", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CsSysValueGenericValue | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CsSysValueGenericValue.from_dict(_type_)

        cs_psv_post_address_rest = cls(
            field_foreigntext=field_foreigntext,
            addressaddition=addressaddition,
            city=city,
            company=company,
            country=country,
            district=district,
            division_name=division_name,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            postcode=postcode,
            postofficebox=postofficebox,
            state=state,
            street=street,
            type_=type_,
        )

        cs_psv_post_address_rest.additional_properties = d
        return cs_psv_post_address_rest

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
