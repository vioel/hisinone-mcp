from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_configuration_his_criteria_group import (
        CsSysGenericSearchSearchConfigurationHisCriteriaGroup,
    )
    from ..models.cs_sys_generic_search_search_configuration_his_search_criterion import (
        CsSysGenericSearchSearchConfigurationHisSearchCriterion,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationHisSearchGroup")


@_attrs_define
class CsSysGenericSearchSearchConfigurationHisSearchGroup:
    """
    Attributes:
        combine_criteria_groups_by_or (bool | Unset):
        criteria (list[CsSysGenericSearchSearchConfigurationHisSearchCriterion] | Unset):
        criteria_group (bool | Unset):
        criteria_groups (list[CsSysGenericSearchSearchConfigurationHisCriteriaGroup] | Unset):
        helptext (str | Unset):
        label (str | Unset):
        quick_search_group (bool | Unset):
    """

    combine_criteria_groups_by_or: bool | Unset = UNSET
    criteria: list[CsSysGenericSearchSearchConfigurationHisSearchCriterion] | Unset = UNSET
    criteria_group: bool | Unset = UNSET
    criteria_groups: list[CsSysGenericSearchSearchConfigurationHisCriteriaGroup] | Unset = UNSET
    helptext: str | Unset = UNSET
    label: str | Unset = UNSET
    quick_search_group: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        combine_criteria_groups_by_or = self.combine_criteria_groups_by_or

        criteria: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        criteria_group = self.criteria_group

        criteria_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.criteria_groups, Unset):
            criteria_groups = []
            for criteria_groups_item_data in self.criteria_groups:
                criteria_groups_item = criteria_groups_item_data.to_dict()
                criteria_groups.append(criteria_groups_item)

        helptext = self.helptext

        label = self.label

        quick_search_group = self.quick_search_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combine_criteria_groups_by_or is not UNSET:
            field_dict["combineCriteriaGroupsByOr"] = combine_criteria_groups_by_or
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if criteria_group is not UNSET:
            field_dict["criteriaGroup"] = criteria_group
        if criteria_groups is not UNSET:
            field_dict["criteriaGroups"] = criteria_groups
        if helptext is not UNSET:
            field_dict["helptext"] = helptext
        if label is not UNSET:
            field_dict["label"] = label
        if quick_search_group is not UNSET:
            field_dict["quickSearchGroup"] = quick_search_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_configuration_his_criteria_group import (
            CsSysGenericSearchSearchConfigurationHisCriteriaGroup,  # noqa: PLC0415
        )
        from ..models.cs_sys_generic_search_search_configuration_his_search_criterion import (
            CsSysGenericSearchSearchConfigurationHisSearchCriterion,  # noqa: PLC0415
        )

        d = dict(src_dict)
        combine_criteria_groups_by_or = d.pop("combineCriteriaGroupsByOr", UNSET)

        _criteria = d.pop("criteria", UNSET)
        criteria: list[CsSysGenericSearchSearchConfigurationHisSearchCriterion] | Unset = UNSET
        if _criteria is not UNSET:
            criteria = []
            for criteria_item_data in _criteria:
                criteria_item = CsSysGenericSearchSearchConfigurationHisSearchCriterion.from_dict(criteria_item_data)

                criteria.append(criteria_item)

        criteria_group = d.pop("criteriaGroup", UNSET)

        _criteria_groups = d.pop("criteriaGroups", UNSET)
        criteria_groups: list[CsSysGenericSearchSearchConfigurationHisCriteriaGroup] | Unset = UNSET
        if _criteria_groups is not UNSET:
            criteria_groups = []
            for criteria_groups_item_data in _criteria_groups:
                criteria_groups_item = CsSysGenericSearchSearchConfigurationHisCriteriaGroup.from_dict(
                    criteria_groups_item_data
                )

                criteria_groups.append(criteria_groups_item)

        helptext = d.pop("helptext", UNSET)

        label = d.pop("label", UNSET)

        quick_search_group = d.pop("quickSearchGroup", UNSET)

        cs_sys_generic_search_search_configuration_his_search_group = cls(
            combine_criteria_groups_by_or=combine_criteria_groups_by_or,
            criteria=criteria,
            criteria_group=criteria_group,
            criteria_groups=criteria_groups,
            helptext=helptext,
            label=label,
            quick_search_group=quick_search_group,
        )

        cs_sys_generic_search_search_configuration_his_search_group.additional_properties = d
        return cs_sys_generic_search_search_configuration_his_search_group

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
