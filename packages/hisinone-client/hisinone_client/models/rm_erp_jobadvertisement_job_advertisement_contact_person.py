from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RmErpJobadvertisementJobAdvertisementContactPerson")


@_attrs_define
class RmErpJobadvertisementJobAdvertisementContactPerson:
    """
    Attributes:
        description (str | Unset):
        firstname (str | Unset):
        gender (int | Unset):
        lastname (str | Unset):
        mail (str | Unset):
        phone (str | Unset):
        salutation (str | Unset):
    """

    description: str | Unset = UNSET
    firstname: str | Unset = UNSET
    gender: int | Unset = UNSET
    lastname: str | Unset = UNSET
    mail: str | Unset = UNSET
    phone: str | Unset = UNSET
    salutation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        firstname = self.firstname

        gender = self.gender

        lastname = self.lastname

        mail = self.mail

        phone = self.phone

        salutation = self.salutation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if gender is not UNSET:
            field_dict["gender"] = gender
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if mail is not UNSET:
            field_dict["mail"] = mail
        if phone is not UNSET:
            field_dict["phone"] = phone
        if salutation is not UNSET:
            field_dict["salutation"] = salutation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        firstname = d.pop("firstname", UNSET)

        gender = d.pop("gender", UNSET)

        lastname = d.pop("lastname", UNSET)

        mail = d.pop("mail", UNSET)

        phone = d.pop("phone", UNSET)

        salutation = d.pop("salutation", UNSET)

        rm_erp_jobadvertisement_job_advertisement_contact_person = cls(
            description=description,
            firstname=firstname,
            gender=gender,
            lastname=lastname,
            mail=mail,
            phone=phone,
            salutation=salutation,
        )

        rm_erp_jobadvertisement_job_advertisement_contact_person.additional_properties = d
        return rm_erp_jobadvertisement_job_advertisement_contact_person

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
