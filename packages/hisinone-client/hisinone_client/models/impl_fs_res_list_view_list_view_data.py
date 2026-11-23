from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue
    from ..models.impl_fs_res_list_view_details_object import ImplFsResListViewDetailsObject
    from ..models.impl_fs_res_list_view_list_view_data_foreigntext import ImplFsResListViewListViewDataForeigntext
    from ..models.impl_fs_res_list_view_list_view_data_view_query_params import (
        ImplFsResListViewListViewDataViewQueryParams,
    )


T = TypeVar("T", bound="ImplFsResListViewListViewData")


@_attrs_define
class ImplFsResListViewListViewData:
    """
    Attributes:
        field_foreigntext (ImplFsResListViewListViewDataForeigntext | Unset):
        details (str | Unset):
        details_object (ImplFsResListViewDetailsObject | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        name_title (str | Unset):
        obj_guid (str | Unset):
        object_name (str | Unset):
        secondary_details (str | Unset):
        view_query_params (ImplFsResListViewListViewDataViewQueryParams | Unset):
        view_url (str | Unset):
        view_url_tooltip (str | Unset):
    """

    field_foreigntext: ImplFsResListViewListViewDataForeigntext | Unset = UNSET
    details: str | Unset = UNSET
    details_object: ImplFsResListViewDetailsObject | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    name_title: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    object_name: str | Unset = UNSET
    secondary_details: str | Unset = UNSET
    view_query_params: ImplFsResListViewListViewDataViewQueryParams | Unset = UNSET
    view_url: str | Unset = UNSET
    view_url_tooltip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        details = self.details

        details_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details_object, Unset):
            details_object = self.details_object.to_dict()

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        name_title = self.name_title

        obj_guid = self.obj_guid

        object_name = self.object_name

        secondary_details = self.secondary_details

        view_query_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view_query_params, Unset):
            view_query_params = self.view_query_params.to_dict()

        view_url = self.view_url

        view_url_tooltip = self.view_url_tooltip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if details is not UNSET:
            field_dict["details"] = details
        if details_object is not UNSET:
            field_dict["detailsObject"] = details_object
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name_title is not UNSET:
            field_dict["nameTitle"] = name_title
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if secondary_details is not UNSET:
            field_dict["secondaryDetails"] = secondary_details
        if view_query_params is not UNSET:
            field_dict["viewQueryParams"] = view_query_params
        if view_url is not UNSET:
            field_dict["viewUrl"] = view_url
        if view_url_tooltip is not UNSET:
            field_dict["viewUrlTooltip"] = view_url_tooltip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415
        from ..models.impl_fs_res_list_view_details_object import ImplFsResListViewDetailsObject  # noqa: PLC0415
        from ..models.impl_fs_res_list_view_list_view_data_foreigntext import ImplFsResListViewListViewDataForeigntext  # noqa: PLC0415
        from ..models.impl_fs_res_list_view_list_view_data_view_query_params import (
            ImplFsResListViewListViewDataViewQueryParams,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplFsResListViewListViewDataForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplFsResListViewListViewDataForeigntext.from_dict(_field_foreigntext)

        details = d.pop("details", UNSET)

        _details_object = d.pop("detailsObject", UNSET)
        details_object: ImplFsResListViewDetailsObject | Unset
        if isinstance(_details_object, Unset):
            details_object = UNSET
        else:
            details_object = ImplFsResListViewDetailsObject.from_dict(_details_object)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        name_title = d.pop("nameTitle", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        object_name = d.pop("objectName", UNSET)

        secondary_details = d.pop("secondaryDetails", UNSET)

        _view_query_params = d.pop("viewQueryParams", UNSET)
        view_query_params: ImplFsResListViewListViewDataViewQueryParams | Unset
        if isinstance(_view_query_params, Unset):
            view_query_params = UNSET
        else:
            view_query_params = ImplFsResListViewListViewDataViewQueryParams.from_dict(_view_query_params)

        view_url = d.pop("viewUrl", UNSET)

        view_url_tooltip = d.pop("viewUrlTooltip", UNSET)

        impl_fs_res_list_view_list_view_data = cls(
            field_foreigntext=field_foreigntext,
            details=details,
            details_object=details_object,
            id=id,
            language=language,
            lock_version=lock_version,
            name_title=name_title,
            obj_guid=obj_guid,
            object_name=object_name,
            secondary_details=secondary_details,
            view_query_params=view_query_params,
            view_url=view_url,
            view_url_tooltip=view_url_tooltip,
        )

        impl_fs_res_list_view_list_view_data.additional_properties = d
        return impl_fs_res_list_view_list_view_data

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
