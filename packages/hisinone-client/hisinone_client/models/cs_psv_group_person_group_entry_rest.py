from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_group_person_group_entry_rest_foreigntext import CsPsvGroupPersonGroupEntryRestForeigntext


T = TypeVar("T", bound="CsPsvGroupPersonGroupEntryRest")


@_attrs_define
class CsPsvGroupPersonGroupEntryRest:
    """
    Attributes:
        field_foreigntext (CsPsvGroupPersonGroupEntryRestForeigntext | Unset):
        firstname (str | Unset):
        functions (str | Unset):
        id (int | Unset):
        is_active (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        roles (str | Unset):
        surname (str | Unset):
    """

    field_foreigntext: CsPsvGroupPersonGroupEntryRestForeigntext | Unset = UNSET
    firstname: str | Unset = UNSET
    functions: str | Unset = UNSET
    id: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    roles: str | Unset = UNSET
    surname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        firstname = self.firstname

        functions = self.functions

        id = self.id

        is_active = self.is_active

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        roles = self.roles

        surname = self.surname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if functions is not UNSET:
            field_dict["functions"] = functions
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if roles is not UNSET:
            field_dict["roles"] = roles
        if surname is not UNSET:
            field_dict["surname"] = surname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_group_person_group_entry_rest_foreigntext import CsPsvGroupPersonGroupEntryRestForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvGroupPersonGroupEntryRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvGroupPersonGroupEntryRestForeigntext.from_dict(_field_foreigntext)

        firstname = d.pop("firstname", UNSET)

        functions = d.pop("functions", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("isActive", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        roles = d.pop("roles", UNSET)

        surname = d.pop("surname", UNSET)

        cs_psv_group_person_group_entry_rest = cls(
            field_foreigntext=field_foreigntext,
            firstname=firstname,
            functions=functions,
            id=id,
            is_active=is_active,
            lock_version=lock_version,
            obj_guid=obj_guid,
            roles=roles,
            surname=surname,
        )

        cs_psv_group_person_group_entry_rest.additional_properties = d
        return cs_psv_group_person_group_entry_rest

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
