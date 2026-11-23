from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue
    from ..models.impl_fs_res_list_view_details_object_foreigntext import ImplFsResListViewDetailsObjectForeigntext


T = TypeVar("T", bound="ImplFsResListViewDetailsObject")


@_attrs_define
class ImplFsResListViewDetailsObject:
    """
    Attributes:
        field_foreigntext (ImplFsResListViewDetailsObjectForeigntext | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        prefix (str | Unset):
        suffix (str | Unset):
        title (str | Unset):
    """

    field_foreigntext: ImplFsResListViewDetailsObjectForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    prefix: str | Unset = UNSET
    suffix: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        prefix = self.prefix

        suffix = self.suffix

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415
        from ..models.impl_fs_res_list_view_details_object_foreigntext import ImplFsResListViewDetailsObjectForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplFsResListViewDetailsObjectForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplFsResListViewDetailsObjectForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        title = d.pop("title", UNSET)

        impl_fs_res_list_view_details_object = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            prefix=prefix,
            suffix=suffix,
            title=title,
        )

        impl_fs_res_list_view_details_object.additional_properties = d
        return impl_fs_res_list_view_details_object

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
