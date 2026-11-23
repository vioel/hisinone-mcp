from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FsResPublicationUniversalImportSimpleGenericValue")


@_attrs_define
class FsResPublicationUniversalImportSimpleGenericValue:
    """
    Attributes:
        defaulttext (str | Unset):
        hiskey_id (int | Unset):
        id (int | Unset):
        obj_guid (str | Unset):
        uniquename (str | Unset):
    """

    defaulttext: str | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    id: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defaulttext = self.defaulttext

        hiskey_id = self.hiskey_id

        id = self.id

        obj_guid = self.obj_guid

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        defaulttext = d.pop("defaulttext", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        fs_res_publication_universal_import_simple_generic_value = cls(
            defaulttext=defaulttext,
            hiskey_id=hiskey_id,
            id=id,
            obj_guid=obj_guid,
            uniquename=uniquename,
        )

        fs_res_publication_universal_import_simple_generic_value.additional_properties = d
        return fs_res_publication_universal_import_simple_generic_value

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
