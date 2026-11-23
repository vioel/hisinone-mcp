from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_person_person_basic_data_foreigntext import RmErpCommonPersonPersonBasicDataForeigntext


T = TypeVar("T", bound="RmErpCommonPersonPersonBasicData")


@_attrs_define
class RmErpCommonPersonPersonBasicData:
    """
    Attributes:
        field_foreigntext (RmErpCommonPersonPersonBasicDataForeigntext | Unset):
        birthdate (int | Unset):
        firstname (str | Unset):
        gender (RmErpCommonErpGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        salutation (RmErpCommonErpGenericValue | Unset):
        status (int | Unset):
        surname (str | Unset):
    """

    field_foreigntext: RmErpCommonPersonPersonBasicDataForeigntext | Unset = UNSET
    birthdate: int | Unset = UNSET
    firstname: str | Unset = UNSET
    gender: RmErpCommonErpGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    salutation: RmErpCommonErpGenericValue | Unset = UNSET
    status: int | Unset = UNSET
    surname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        birthdate = self.birthdate

        firstname = self.firstname

        gender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        salutation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.to_dict()

        status = self.status

        surname = self.surname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if gender is not UNSET:
            field_dict["gender"] = gender
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if status is not UNSET:
            field_dict["status"] = status
        if surname is not UNSET:
            field_dict["surname"] = surname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_person_basic_data_foreigntext import (
            RmErpCommonPersonPersonBasicDataForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonPersonPersonBasicDataForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonPersonPersonBasicDataForeigntext.from_dict(_field_foreigntext)

        birthdate = d.pop("birthdate", UNSET)

        firstname = d.pop("firstname", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: RmErpCommonErpGenericValue | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = RmErpCommonErpGenericValue.from_dict(_gender)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: RmErpCommonErpGenericValue | Unset
        if isinstance(_salutation, Unset):
            salutation = UNSET
        else:
            salutation = RmErpCommonErpGenericValue.from_dict(_salutation)

        status = d.pop("status", UNSET)

        surname = d.pop("surname", UNSET)

        rm_erp_common_person_person_basic_data = cls(
            field_foreigntext=field_foreigntext,
            birthdate=birthdate,
            firstname=firstname,
            gender=gender,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            salutation=salutation,
            status=status,
            surname=surname,
        )

        rm_erp_common_person_person_basic_data.additional_properties = d
        return rm_erp_common_person_person_basic_data

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
