from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_publisher_foreigntext_type_0 import FsResPublicationPublisherForeigntextType0
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResPublicationPublisher")


@_attrs_define
class FsResPublicationPublisher:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | None | Unset):
        field_foreigntext (FsResPublicationPublisherForeigntextType0 | None | Unset):
        defaulttext (str | Unset):
        id (int | Unset):
        label (str | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        longtext (None | str | Unset):
        obj_guid (None | str | Unset):
        place (str | Unset):
        shorttext (None | str | Unset):
        uniquename (None | str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | None | Unset = UNSET
    field_foreigntext: FsResPublicationPublisherForeigntextType0 | None | Unset = UNSET
    defaulttext: str | Unset = UNSET
    id: int | Unset = UNSET
    label: str | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: None | str | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    place: str | Unset = UNSET
    shorttext: None | str | Unset = UNSET
    uniquename: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_res_publication_publisher_foreigntext_type_0 import FsResPublicationPublisherForeigntextType0  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        field_dynamic_component: dict[str, Any] | None | Unset
        if isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        elif isinstance(self.field_dynamic_component, ImplCsSysDynamicDynamicComponent):
            field_dynamic_component = self.field_dynamic_component.to_dict()
        else:
            field_dynamic_component = self.field_dynamic_component

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResPublicationPublisherForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        defaulttext = self.defaulttext

        id = self.id

        label = self.label

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        longtext: None | str | Unset
        if isinstance(self.longtext, Unset):
            longtext = UNSET
        else:
            longtext = self.longtext

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        place = self.place

        shorttext: None | str | Unset
        if isinstance(self.shorttext, Unset):
            shorttext = UNSET
        else:
            shorttext = self.shorttext

        uniquename: None | str | Unset
        if isinstance(self.uniquename, Unset):
            uniquename = UNSET
        else:
            uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
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
        from ..models.fs_res_publication_publisher_foreigntext_type_0 import FsResPublicationPublisherForeigntextType0  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_field_dynamic_component(data: object) -> ImplCsSysDynamicDynamicComponent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_dynamic_component_type_0 = ImplCsSysDynamicDynamicComponent.from_dict(cast(dict[str, Any], data))

            return field_dynamic_component_type_0

        field_dynamic_component = _parse_field_dynamic_component(d.pop("_dynamicComponent", UNSET))

        def _parse_field_foreigntext(data: object) -> FsResPublicationPublisherForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResPublicationPublisherForeigntextType0.from_dict(cast(dict[str, Any], data))

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_longtext(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longtext = _parse_longtext(d.pop("longtext", UNSET))

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        place = d.pop("place", UNSET)

        def _parse_shorttext(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shorttext = _parse_shorttext(d.pop("shorttext", UNSET))

        def _parse_uniquename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uniquename = _parse_uniquename(d.pop("uniquename", UNSET))

        fs_res_publication_publisher = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            id=id,
            label=label,
            language=language,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            place=place,
            shorttext=shorttext,
            uniquename=uniquename,
        )

        fs_res_publication_publisher.additional_properties = d
        return fs_res_publication_publisher

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
