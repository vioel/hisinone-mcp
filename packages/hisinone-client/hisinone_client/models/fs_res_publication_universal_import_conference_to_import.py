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


T = TypeVar("T", bound="FsResPublicationUniversalImportConferenceToImport")


@_attrs_define
class FsResPublicationUniversalImportConferenceToImport:
    """
    Attributes:
        city (str | Unset):
        conference_event_type (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        country (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        defaulttext (str | Unset):
        end_date (str | Unset):
        language (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        obj_guid (str | Unset):
        shorttext (str | Unset):
        start_date (str | Unset):
        status (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        website (str | Unset):
    """

    city: str | Unset = UNSET
    conference_event_type: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    country: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    defaulttext: str | Unset = UNSET
    end_date: str | Unset = UNSET
    language: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    obj_guid: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    start_date: str | Unset = UNSET
    status: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        conference_event_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_event_type, Unset):
            conference_event_type = self.conference_event_type.to_dict()

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        defaulttext = self.defaulttext

        end_date = self.end_date

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        obj_guid = self.obj_guid

        shorttext = self.shorttext

        start_date = self.start_date

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if conference_event_type is not UNSET:
            field_dict["conferenceEventType"] = conference_event_type
        if country is not UNSET:
            field_dict["country"] = country
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if language is not UNSET:
            field_dict["language"] = language
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if status is not UNSET:
            field_dict["status"] = status
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_simple_generic_value import (
            FsResPublicationUniversalImportSimpleGenericValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        city = d.pop("city", UNSET)

        _conference_event_type = d.pop("conferenceEventType", UNSET)
        conference_event_type: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_conference_event_type, Unset):
            conference_event_type = UNSET
        else:
            conference_event_type = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_conference_event_type)

        _country = d.pop("country", UNSET)
        country: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_country)

        defaulttext = d.pop("defaulttext", UNSET)

        end_date = d.pop("endDate", UNSET)

        _language = d.pop("language", UNSET)
        language: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_language)

        obj_guid = d.pop("objGuid", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        start_date = d.pop("startDate", UNSET)

        _status = d.pop("status", UNSET)
        status: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_status)

        website = d.pop("website", UNSET)

        fs_res_publication_universal_import_conference_to_import = cls(
            city=city,
            conference_event_type=conference_event_type,
            country=country,
            defaulttext=defaulttext,
            end_date=end_date,
            language=language,
            obj_guid=obj_guid,
            shorttext=shorttext,
            start_date=start_date,
            status=status,
            website=website,
        )

        fs_res_publication_universal_import_conference_to_import.additional_properties = d
        return fs_res_publication_universal_import_conference_to_import

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
