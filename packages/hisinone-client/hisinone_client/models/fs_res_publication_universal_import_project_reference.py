from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FsResPublicationUniversalImportProjectReference")


@_attrs_define
class FsResPublicationUniversalImportProjectReference:
    """
    Attributes:
        defaulttext (str | Unset):
        external_reference_number (str | Unset):
        obj_guid (str | Unset):
        shorttext (str | Unset):
    """

    defaulttext: str | Unset = UNSET
    external_reference_number: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defaulttext = self.defaulttext

        external_reference_number = self.external_reference_number

        obj_guid = self.obj_guid

        shorttext = self.shorttext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if external_reference_number is not UNSET:
            field_dict["externalReferenceNumber"] = external_reference_number
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        defaulttext = d.pop("defaulttext", UNSET)

        external_reference_number = d.pop("externalReferenceNumber", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        fs_res_publication_universal_import_project_reference = cls(
            defaulttext=defaulttext,
            external_reference_number=external_reference_number,
            obj_guid=obj_guid,
            shorttext=shorttext,
        )

        fs_res_publication_universal_import_project_reference.additional_properties = d
        return fs_res_publication_universal_import_project_reference

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
