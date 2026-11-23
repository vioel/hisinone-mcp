from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.impl_fs_res_list_view_list_view import ImplFsResListViewListView


T = TypeVar("T", bound="FsResResearchInfrastructureResearchInfrastructureListviewsType0")


@_attrs_define
class FsResResearchInfrastructureResearchInfrastructureListviewsType0:
    additional_properties: dict[str, ImplFsResListViewListView] = _attrs_field(
        init=False, factory=dict[str, "ImplFsResListViewListView"]
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_fs_res_list_view_list_view import ImplFsResListViewListView  # noqa: PLC0415

        d = dict(src_dict)
        fs_res_research_infrastructure_research_infrastructure_listviews_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ImplFsResListViewListView.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        fs_res_research_infrastructure_research_infrastructure_listviews_type_0.additional_properties = (
            additional_properties
        )
        return fs_res_research_infrastructure_research_infrastructure_listviews_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ImplFsResListViewListView:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ImplFsResListViewListView) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
