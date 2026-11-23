from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_profile_person_profile_entry_value_foreigntext import (
        CsPsvPersonProfilePersonProfileEntryValueForeigntext,
    )


T = TypeVar("T", bound="CsPsvPersonProfilePersonProfileEntryValue")


@_attrs_define
class CsPsvPersonProfilePersonProfileEntryValue:
    """
    Attributes:
        field_foreigntext (CsPsvPersonProfilePersonProfileEntryValueForeigntext | Unset):
        datatype (str | Unset):
        defaulttext (str | Unset):
        hiskey_id (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
    """

    field_foreigntext: CsPsvPersonProfilePersonProfileEntryValueForeigntext | Unset = UNSET
    datatype: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        datatype = self.datatype

        defaulttext = self.defaulttext

        hiskey_id = self.hiskey_id

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if datatype is not UNSET:
            field_dict["datatype"] = datatype
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_profile_person_profile_entry_value_foreigntext import (
            CsPsvPersonProfilePersonProfileEntryValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPersonProfilePersonProfileEntryValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPersonProfilePersonProfileEntryValueForeigntext.from_dict(_field_foreigntext)

        datatype = d.pop("datatype", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        cs_psv_person_profile_person_profile_entry_value = cls(
            field_foreigntext=field_foreigntext,
            datatype=datatype,
            defaulttext=defaulttext,
            hiskey_id=hiskey_id,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
        )

        cs_psv_person_profile_person_profile_entry_value.additional_properties = d
        return cs_psv_person_profile_person_profile_entry_value

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
