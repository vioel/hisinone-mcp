from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_identifier_info_rest_foreigntext import CsPsvPersonIdentifierInfoRestForeigntext


T = TypeVar("T", bound="CsPsvPersonIdentifierInfoRest")


@_attrs_define
class CsPsvPersonIdentifierInfoRest:
    """
    Attributes:
        field_foreigntext (CsPsvPersonIdentifierInfoRestForeigntext | Unset):
        id (int | Unset):
        identifier_type (str | Unset):
        identifier_value (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person_id (int | Unset):
    """

    field_foreigntext: CsPsvPersonIdentifierInfoRestForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    identifier_type: str | Unset = UNSET
    identifier_value: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        identifier_type = self.identifier_type

        identifier_value = self.identifier_value

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if identifier_type is not UNSET:
            field_dict["identifierType"] = identifier_type
        if identifier_value is not UNSET:
            field_dict["identifierValue"] = identifier_value
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_identifier_info_rest_foreigntext import CsPsvPersonIdentifierInfoRestForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPersonIdentifierInfoRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPersonIdentifierInfoRestForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        identifier_type = d.pop("identifierType", UNSET)

        identifier_value = d.pop("identifierValue", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        person_id = d.pop("personId", UNSET)

        cs_psv_person_identifier_info_rest = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            identifier_type=identifier_type,
            identifier_value=identifier_value,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person_id=person_id,
        )

        cs_psv_person_identifier_info_rest.additional_properties = d
        return cs_psv_person_identifier_info_rest

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
