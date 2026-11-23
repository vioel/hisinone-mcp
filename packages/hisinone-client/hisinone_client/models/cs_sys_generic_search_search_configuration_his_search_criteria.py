from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_configuration_his_search_group import (
        CsSysGenericSearchSearchConfigurationHisSearchGroup,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationHisSearchCriteria")


@_attrs_define
class CsSysGenericSearchSearchConfigurationHisSearchCriteria:
    """
    Attributes:
        group (list[CsSysGenericSearchSearchConfigurationHisSearchGroup] | Unset):
        groups (list[CsSysGenericSearchSearchConfigurationHisSearchGroup] | Unset):
        quick_search_criteria (bool | Unset):
    """

    group: list[CsSysGenericSearchSearchConfigurationHisSearchGroup] | Unset = UNSET
    groups: list[CsSysGenericSearchSearchConfigurationHisSearchGroup] | Unset = UNSET
    quick_search_criteria: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        group: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = []
            for group_item_data in self.group:
                group_item = group_item_data.to_dict()
                group.append(group_item)

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        quick_search_criteria = self.quick_search_criteria

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if groups is not UNSET:
            field_dict["groups"] = groups
        if quick_search_criteria is not UNSET:
            field_dict["quickSearchCriteria"] = quick_search_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_configuration_his_search_group import (
            CsSysGenericSearchSearchConfigurationHisSearchGroup,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: list[CsSysGenericSearchSearchConfigurationHisSearchGroup] | Unset = UNSET
        if _group is not UNSET:
            group = []
            for group_item_data in _group:
                group_item = CsSysGenericSearchSearchConfigurationHisSearchGroup.from_dict(group_item_data)

                group.append(group_item)

        _groups = d.pop("groups", UNSET)
        groups: list[CsSysGenericSearchSearchConfigurationHisSearchGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = CsSysGenericSearchSearchConfigurationHisSearchGroup.from_dict(groups_item_data)

                groups.append(groups_item)

        quick_search_criteria = d.pop("quickSearchCriteria", UNSET)

        cs_sys_generic_search_search_configuration_his_search_criteria = cls(
            group=group,
            groups=groups,
            quick_search_criteria=quick_search_criteria,
        )

        cs_sys_generic_search_search_configuration_his_search_criteria.additional_properties = d
        return cs_sys_generic_search_search_configuration_his_search_criteria

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
