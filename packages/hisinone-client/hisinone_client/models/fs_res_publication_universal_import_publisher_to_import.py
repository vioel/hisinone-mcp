from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_simple_generic_value import (
        FsResPublicationUniversalImportSimpleGenericValue,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportPublisherToImport")


@_attrs_define
class FsResPublicationUniversalImportPublisherToImport:
    """
    Attributes:
        defaulttext (str | Unset):
        language (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        place (str | Unset):
        shorttext (str | Unset):
        uniquename (str | Unset):
    """

    defaulttext: str | Unset = UNSET
    language: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    place: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defaulttext = self.defaulttext

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        longtext = self.longtext

        obj_guid = self.obj_guid

        place = self.place

        shorttext = self.shorttext

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if language is not UNSET:
            field_dict["language"] = language
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if place is not UNSET:
            field_dict["place"] = place
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_simple_generic_value import (
            FsResPublicationUniversalImportSimpleGenericValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        defaulttext = d.pop("defaulttext", UNSET)

        _language = d.pop("language", UNSET)
        language: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_language)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        place = d.pop("place", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        fs_res_publication_universal_import_publisher_to_import = cls(
            defaulttext=defaulttext,
            language=language,
            longtext=longtext,
            obj_guid=obj_guid,
            place=place,
            shorttext=shorttext,
            uniquename=uniquename,
        )

        fs_res_publication_universal_import_publisher_to_import.additional_properties = d
        return fs_res_publication_universal_import_publisher_to_import

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
