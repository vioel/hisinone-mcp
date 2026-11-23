from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_group_object_group_entry_rest_foreigntext import CsPsvGroupObjectGroupEntryRestForeigntext
    from ..models.cs_psv_group_person_group_entry_rest import CsPsvGroupPersonGroupEntryRest


T = TypeVar("T", bound="CsPsvGroupObjectGroupEntryRest")


@_attrs_define
class CsPsvGroupObjectGroupEntryRest:
    """
    Attributes:
        field_foreigntext (CsPsvGroupObjectGroupEntryRestForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        object_group_id (int | Unset):
        person_group_entry (CsPsvGroupPersonGroupEntryRest | Unset):
    """

    field_foreigntext: CsPsvGroupObjectGroupEntryRestForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    object_group_id: int | Unset = UNSET
    person_group_entry: CsPsvGroupPersonGroupEntryRest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        object_group_id = self.object_group_id

        person_group_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person_group_entry, Unset):
            person_group_entry = self.person_group_entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if object_group_id is not UNSET:
            field_dict["objectGroupId"] = object_group_id
        if person_group_entry is not UNSET:
            field_dict["personGroupEntry"] = person_group_entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_group_object_group_entry_rest_foreigntext import CsPsvGroupObjectGroupEntryRestForeigntext  # noqa: PLC0415
        from ..models.cs_psv_group_person_group_entry_rest import CsPsvGroupPersonGroupEntryRest  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvGroupObjectGroupEntryRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvGroupObjectGroupEntryRestForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        object_group_id = d.pop("objectGroupId", UNSET)

        _person_group_entry = d.pop("personGroupEntry", UNSET)
        person_group_entry: CsPsvGroupPersonGroupEntryRest | Unset
        if isinstance(_person_group_entry, Unset):
            person_group_entry = UNSET
        else:
            person_group_entry = CsPsvGroupPersonGroupEntryRest.from_dict(_person_group_entry)

        cs_psv_group_object_group_entry_rest = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            object_group_id=object_group_id,
            person_group_entry=person_group_entry,
        )

        cs_psv_group_object_group_entry_rest.additional_properties = d
        return cs_psv_group_object_group_entry_rest

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
