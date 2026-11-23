from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_fs_res_list_view_list_view_data import ImplFsResListViewListViewData
    from ..models.impl_fs_res_list_view_list_view_foreigntext import ImplFsResListViewListViewForeigntext
    from ..models.impl_fs_res_list_view_list_view_search_query_params import ImplFsResListViewListViewSearchQueryParams


T = TypeVar("T", bound="ImplFsResListViewListView")


@_attrs_define
class ImplFsResListViewListView:
    """
    Attributes:
        field_foreigntext (ImplFsResListViewListViewForeigntext | Unset):
        icon (str | Unset):
        id (int | Unset):
        is_hidden (bool | Unset):
        list_view_data (list[ImplFsResListViewListViewData] | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        search_query_params (ImplFsResListViewListViewSearchQueryParams | Unset):
        search_title (str | Unset):
        search_url (str | Unset):
        title (str | Unset):
        total_count (int | Unset):
    """

    field_foreigntext: ImplFsResListViewListViewForeigntext | Unset = UNSET
    icon: str | Unset = UNSET
    id: int | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    list_view_data: list[ImplFsResListViewListViewData] | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    search_query_params: ImplFsResListViewListViewSearchQueryParams | Unset = UNSET
    search_title: str | Unset = UNSET
    search_url: str | Unset = UNSET
    title: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        icon = self.icon

        id = self.id

        is_hidden = self.is_hidden

        list_view_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_view_data, Unset):
            list_view_data = []
            for list_view_data_item_data in self.list_view_data:
                list_view_data_item = list_view_data_item_data.to_dict()
                list_view_data.append(list_view_data_item)

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        search_query_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_query_params, Unset):
            search_query_params = self.search_query_params.to_dict()

        search_title = self.search_title

        search_url = self.search_url

        title = self.title

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if list_view_data is not UNSET:
            field_dict["listViewData"] = list_view_data
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if search_query_params is not UNSET:
            field_dict["searchQueryParams"] = search_query_params
        if search_title is not UNSET:
            field_dict["searchTitle"] = search_title
        if search_url is not UNSET:
            field_dict["searchUrl"] = search_url
        if title is not UNSET:
            field_dict["title"] = title
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_fs_res_list_view_list_view_data import ImplFsResListViewListViewData  # noqa: PLC0415
        from ..models.impl_fs_res_list_view_list_view_foreigntext import ImplFsResListViewListViewForeigntext  # noqa: PLC0415
        from ..models.impl_fs_res_list_view_list_view_search_query_params import (
            ImplFsResListViewListViewSearchQueryParams,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplFsResListViewListViewForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplFsResListViewListViewForeigntext.from_dict(_field_foreigntext)

        icon = d.pop("icon", UNSET)

        id = d.pop("id", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        _list_view_data = d.pop("listViewData", UNSET)
        list_view_data: list[ImplFsResListViewListViewData] | Unset = UNSET
        if _list_view_data is not UNSET:
            list_view_data = []
            for list_view_data_item_data in _list_view_data:
                list_view_data_item = ImplFsResListViewListViewData.from_dict(list_view_data_item_data)

                list_view_data.append(list_view_data_item)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _search_query_params = d.pop("searchQueryParams", UNSET)
        search_query_params: ImplFsResListViewListViewSearchQueryParams | Unset
        if isinstance(_search_query_params, Unset):
            search_query_params = UNSET
        else:
            search_query_params = ImplFsResListViewListViewSearchQueryParams.from_dict(_search_query_params)

        search_title = d.pop("searchTitle", UNSET)

        search_url = d.pop("searchUrl", UNSET)

        title = d.pop("title", UNSET)

        total_count = d.pop("totalCount", UNSET)

        impl_fs_res_list_view_list_view = cls(
            field_foreigntext=field_foreigntext,
            icon=icon,
            id=id,
            is_hidden=is_hidden,
            list_view_data=list_view_data,
            lock_version=lock_version,
            obj_guid=obj_guid,
            search_query_params=search_query_params,
            search_title=search_title,
            search_url=search_url,
            title=title,
            total_count=total_count,
        )

        impl_fs_res_list_view_list_view.additional_properties = d
        return impl_fs_res_list_view_list_view

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
