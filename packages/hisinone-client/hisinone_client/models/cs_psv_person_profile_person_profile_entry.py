from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_profile_person_profile_entry_foreigntext import (
        CsPsvPersonProfilePersonProfileEntryForeigntext,
    )
    from ..models.cs_psv_person_profile_person_profile_entry_value import CsPsvPersonProfilePersonProfileEntryValue
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPersonProfilePersonProfileEntry")


@_attrs_define
class CsPsvPersonProfilePersonProfileEntry:
    """
    Attributes:
        field_foreigntext (CsPsvPersonProfilePersonProfileEntryForeigntext | Unset):
        entrytext (str | Unset):
        id (int | Unset):
        language (CsSysValueGenericValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person_profile_entry_value (CsPsvPersonProfilePersonProfileEntryValue | Unset):
    """

    field_foreigntext: CsPsvPersonProfilePersonProfileEntryForeigntext | Unset = UNSET
    entrytext: str | Unset = UNSET
    id: int | Unset = UNSET
    language: CsSysValueGenericValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person_profile_entry_value: CsPsvPersonProfilePersonProfileEntryValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        entrytext = self.entrytext

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person_profile_entry_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person_profile_entry_value, Unset):
            person_profile_entry_value = self.person_profile_entry_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if entrytext is not UNSET:
            field_dict["entrytext"] = entrytext
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person_profile_entry_value is not UNSET:
            field_dict["personProfileEntryValue"] = person_profile_entry_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_profile_person_profile_entry_foreigntext import (
            CsPsvPersonProfilePersonProfileEntryForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_psv_person_profile_person_profile_entry_value import CsPsvPersonProfilePersonProfileEntryValue  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPersonProfilePersonProfileEntryForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPersonProfilePersonProfileEntryForeigntext.from_dict(_field_foreigntext)

        entrytext = d.pop("entrytext", UNSET)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: CsSysValueGenericValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = CsSysValueGenericValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _person_profile_entry_value = d.pop("personProfileEntryValue", UNSET)
        person_profile_entry_value: CsPsvPersonProfilePersonProfileEntryValue | Unset
        if isinstance(_person_profile_entry_value, Unset):
            person_profile_entry_value = UNSET
        else:
            person_profile_entry_value = CsPsvPersonProfilePersonProfileEntryValue.from_dict(
                _person_profile_entry_value
            )

        cs_psv_person_profile_person_profile_entry = cls(
            field_foreigntext=field_foreigntext,
            entrytext=entrytext,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person_profile_entry_value=person_profile_entry_value,
        )

        cs_psv_person_profile_person_profile_entry.additional_properties = d
        return cs_psv_person_profile_person_profile_entry

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
