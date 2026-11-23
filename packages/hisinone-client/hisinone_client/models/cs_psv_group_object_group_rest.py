from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_group_object_group_entry_rest import CsPsvGroupObjectGroupEntryRest
    from ..models.cs_psv_group_object_group_rest_foreigntext import CsPsvGroupObjectGroupRestForeigntext


T = TypeVar("T", bound="CsPsvGroupObjectGroupRest")


@_attrs_define
class CsPsvGroupObjectGroupRest:
    """
    Attributes:
        field_foreigntext (CsPsvGroupObjectGroupRestForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
        object_group_entries (list[CsPsvGroupObjectGroupEntryRest] | Unset):
        object_type (str | Unset):
    """

    field_foreigntext: CsPsvGroupObjectGroupRestForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    object_group_entries: list[CsPsvGroupObjectGroupEntryRest] | Unset = UNSET
    object_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        name = self.name

        obj_guid = self.obj_guid

        object_group_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.object_group_entries, Unset):
            object_group_entries = []
            for object_group_entries_item_data in self.object_group_entries:
                object_group_entries_item = object_group_entries_item_data.to_dict()
                object_group_entries.append(object_group_entries_item)

        object_type = self.object_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if object_group_entries is not UNSET:
            field_dict["objectGroupEntries"] = object_group_entries
        if object_type is not UNSET:
            field_dict["objectType"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_group_object_group_entry_rest import CsPsvGroupObjectGroupEntryRest  # noqa: PLC0415
        from ..models.cs_psv_group_object_group_rest_foreigntext import CsPsvGroupObjectGroupRestForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvGroupObjectGroupRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvGroupObjectGroupRestForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _object_group_entries = d.pop("objectGroupEntries", UNSET)
        object_group_entries: list[CsPsvGroupObjectGroupEntryRest] | Unset = UNSET
        if _object_group_entries is not UNSET:
            object_group_entries = []
            for object_group_entries_item_data in _object_group_entries:
                object_group_entries_item = CsPsvGroupObjectGroupEntryRest.from_dict(object_group_entries_item_data)

                object_group_entries.append(object_group_entries_item)

        object_type = d.pop("objectType", UNSET)

        cs_psv_group_object_group_rest = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
            object_group_entries=object_group_entries,
            object_type=object_type,
        )

        cs_psv_group_object_group_rest.additional_properties = d
        return cs_psv_group_object_group_rest

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
