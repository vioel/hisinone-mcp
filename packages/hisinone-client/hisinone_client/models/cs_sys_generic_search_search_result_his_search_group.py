from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search_criteria import (
        CsSysGenericSearchSearchResultHisSearchCriteria,
    )
    from ..models.cs_sys_generic_search_search_result_his_search_criteria_group import (
        CsSysGenericSearchSearchResultHisSearchCriteriaGroup,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchResultHisSearchGroup")


@_attrs_define
class CsSysGenericSearchSearchResultHisSearchGroup:
    """
    Attributes:
        criteria (list[CsSysGenericSearchSearchResultHisSearchCriteria] | Unset):
        criteria_group_and (bool | Unset):
        criteria_groups (list[CsSysGenericSearchSearchResultHisSearchCriteriaGroup] | Unset):
        group_label (str | Unset):
    """

    criteria: list[CsSysGenericSearchSearchResultHisSearchCriteria] | Unset = UNSET
    criteria_group_and: bool | Unset = UNSET
    criteria_groups: list[CsSysGenericSearchSearchResultHisSearchCriteriaGroup] | Unset = UNSET
    group_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        criteria: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        criteria_group_and = self.criteria_group_and

        criteria_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.criteria_groups, Unset):
            criteria_groups = []
            for criteria_groups_item_data in self.criteria_groups:
                criteria_groups_item = criteria_groups_item_data.to_dict()
                criteria_groups.append(criteria_groups_item)

        group_label = self.group_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if criteria_group_and is not UNSET:
            field_dict["criteriaGroupAnd"] = criteria_group_and
        if criteria_groups is not UNSET:
            field_dict["criteriaGroups"] = criteria_groups
        if group_label is not UNSET:
            field_dict["groupLabel"] = group_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search_criteria import (
            CsSysGenericSearchSearchResultHisSearchCriteria,  # noqa: PLC0415
        )
        from ..models.cs_sys_generic_search_search_result_his_search_criteria_group import (
            CsSysGenericSearchSearchResultHisSearchCriteriaGroup,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _criteria = d.pop("criteria", UNSET)
        criteria: list[CsSysGenericSearchSearchResultHisSearchCriteria] | Unset = UNSET
        if _criteria is not UNSET:
            criteria = []
            for criteria_item_data in _criteria:
                criteria_item = CsSysGenericSearchSearchResultHisSearchCriteria.from_dict(criteria_item_data)

                criteria.append(criteria_item)

        criteria_group_and = d.pop("criteriaGroupAnd", UNSET)

        _criteria_groups = d.pop("criteriaGroups", UNSET)
        criteria_groups: list[CsSysGenericSearchSearchResultHisSearchCriteriaGroup] | Unset = UNSET
        if _criteria_groups is not UNSET:
            criteria_groups = []
            for criteria_groups_item_data in _criteria_groups:
                criteria_groups_item = CsSysGenericSearchSearchResultHisSearchCriteriaGroup.from_dict(
                    criteria_groups_item_data
                )

                criteria_groups.append(criteria_groups_item)

        group_label = d.pop("groupLabel", UNSET)

        cs_sys_generic_search_search_result_his_search_group = cls(
            criteria=criteria,
            criteria_group_and=criteria_group_and,
            criteria_groups=criteria_groups,
            group_label=group_label,
        )

        cs_sys_generic_search_search_result_his_search_group.additional_properties = d
        return cs_sys_generic_search_search_result_his_search_group

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
