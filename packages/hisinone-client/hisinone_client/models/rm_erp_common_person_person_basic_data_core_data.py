from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RmErpCommonPersonPersonBasicDataCoreData")


@_attrs_define
class RmErpCommonPersonPersonBasicDataCoreData:
    """
    Attributes:
        firstname (str | Unset):
        gender (int | Unset):
        salutation (str | Unset):
        serialversionuid (int | Unset):
        surname (str | Unset):
    """

    firstname: str | Unset = UNSET
    gender: int | Unset = UNSET
    salutation: str | Unset = UNSET
    serialversionuid: int | Unset = UNSET
    surname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        firstname = self.firstname

        gender = self.gender

        salutation = self.salutation

        serialversionuid = self.serialversionuid

        surname = self.surname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if gender is not UNSET:
            field_dict["gender"] = gender
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if serialversionuid is not UNSET:
            field_dict["serialversionuid"] = serialversionuid
        if surname is not UNSET:
            field_dict["surname"] = surname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        firstname = d.pop("firstname", UNSET)

        gender = d.pop("gender", UNSET)

        salutation = d.pop("salutation", UNSET)

        serialversionuid = d.pop("serialversionuid", UNSET)

        surname = d.pop("surname", UNSET)

        rm_erp_common_person_person_basic_data_core_data = cls(
            firstname=firstname,
            gender=gender,
            salutation=salutation,
            serialversionuid=serialversionuid,
            surname=surname,
        )

        rm_erp_common_person_person_basic_data_core_data.additional_properties = d
        return rm_erp_common_person_person_basic_data_core_data

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
