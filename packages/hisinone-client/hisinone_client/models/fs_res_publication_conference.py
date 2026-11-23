from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_publication_conference_foreigntext import FsResPublicationConferenceForeigntext
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResPublicationConference")


@_attrs_define
class FsResPublicationConference:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResPublicationConferenceForeigntext | Unset):
        city (str | Unset):
        conference_event_type (CsSysValueGenericValue | Unset):
        country (CsSysValueGenericValue | Unset):
        defaulttext (str | Unset):
        end_date (int | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        shorttext (str | Unset):
        start_date (int | Unset):
        status (CsSysValueGenericValue | Unset):
        website (str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResPublicationConferenceForeigntext | Unset = UNSET
    city: str | Unset = UNSET
    conference_event_type: CsSysValueGenericValue | Unset = UNSET
    country: CsSysValueGenericValue | Unset = UNSET
    defaulttext: str | Unset = UNSET
    end_date: int | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    start_date: int | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        city = self.city

        conference_event_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conference_event_type, Unset):
            conference_event_type = self.conference_event_type.to_dict()

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        defaulttext = self.defaulttext

        end_date = self.end_date

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

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
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
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
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
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
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_conference_foreigntext import FsResPublicationConferenceForeigntext  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationConferenceForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationConferenceForeigntext.from_dict(_field_foreigntext)

        city = d.pop("city", UNSET)

        _conference_event_type = d.pop("conferenceEventType", UNSET)
        conference_event_type: CsSysValueGenericValue | Unset
        if isinstance(_conference_event_type, Unset):
            conference_event_type = UNSET
        else:
            conference_event_type = CsSysValueGenericValue.from_dict(_conference_event_type)

        _country = d.pop("country", UNSET)
        country: CsSysValueGenericValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = CsSysValueGenericValue.from_dict(_country)

        defaulttext = d.pop("defaulttext", UNSET)

        end_date = d.pop("endDate", UNSET)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        start_date = d.pop("startDate", UNSET)

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        website = d.pop("website", UNSET)

        fs_res_publication_conference = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            city=city,
            conference_event_type=conference_event_type,
            country=country,
            defaulttext=defaulttext,
            end_date=end_date,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            shorttext=shorttext,
            start_date=start_date,
            status=status,
            website=website,
        )

        fs_res_publication_conference.additional_properties = d
        return fs_res_publication_conference

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
