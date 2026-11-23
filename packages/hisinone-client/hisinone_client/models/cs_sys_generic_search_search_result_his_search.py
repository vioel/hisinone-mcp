from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search_group import (
        CsSysGenericSearchSearchResultHisSearchGroup,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchResultHisSearch")


@_attrs_define
class CsSysGenericSearchSearchResultHisSearch:
    """
    Attributes:
        config_file (str | Unset):
        groups (list[CsSysGenericSearchSearchResultHisSearchGroup] | Unset):
    """

    config_file: str | Unset = UNSET
    groups: list[CsSysGenericSearchSearchResultHisSearchGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_file = self.config_file

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search_group import (
            CsSysGenericSearchSearchResultHisSearchGroup,  # noqa: PLC0415
        )

        d = dict(src_dict)
        config_file = d.pop("configFile", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[CsSysGenericSearchSearchResultHisSearchGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = CsSysGenericSearchSearchResultHisSearchGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        cs_sys_generic_search_search_result_his_search = cls(
            config_file=config_file,
            groups=groups,
        )

        cs_sys_generic_search_search_result_his_search.additional_properties = d
        return cs_sys_generic_search_search_result_his_search

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
