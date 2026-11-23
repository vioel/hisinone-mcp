from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_sitemap_site_map_index import CsSysRestSitemapSiteMapIndex


T = TypeVar("T", bound="CsSysRestSitemapSiteMapIndexDtoList")


@_attrs_define
class CsSysRestSitemapSiteMapIndexDtoList:
    """
    Attributes:
        sitemap_list (list[CsSysRestSitemapSiteMapIndex] | Unset):
    """

    sitemap_list: list[CsSysRestSitemapSiteMapIndex] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        sitemap_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sitemap_list, Unset):
            sitemap_list = []
            for sitemap_list_item_data in self.sitemap_list:
                sitemap_list_item = sitemap_list_item_data.to_dict()
                sitemap_list.append(sitemap_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sitemap_list is not UNSET:
            field_dict["sitemapList"] = sitemap_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_sitemap_site_map_index import CsSysRestSitemapSiteMapIndex  # noqa: PLC0415

        d = dict(src_dict)
        _sitemap_list = d.pop("sitemapList", UNSET)
        sitemap_list: list[CsSysRestSitemapSiteMapIndex] | Unset = UNSET
        if _sitemap_list is not UNSET:
            sitemap_list = []
            for sitemap_list_item_data in _sitemap_list:
                sitemap_list_item = CsSysRestSitemapSiteMapIndex.from_dict(sitemap_list_item_data)

                sitemap_list.append(sitemap_list_item)

        cs_sys_rest_sitemap_site_map_index_dto_list = cls(
            sitemap_list=sitemap_list,
        )

        cs_sys_rest_sitemap_site_map_index_dto_list.additional_properties = d
        return cs_sys_rest_sitemap_site_map_index_dto_list

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
