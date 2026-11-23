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


T = TypeVar("T", bound="CsSysGenericSearchSearchResultHisSearchCriteriaGroup")


@_attrs_define
class CsSysGenericSearchSearchResultHisSearchCriteriaGroup:
    """
    Attributes:
        criteria (list[CsSysGenericSearchSearchResultHisSearchCriteria] | Unset):
        excluding (bool | Unset):
    """

    criteria: list[CsSysGenericSearchSearchResultHisSearchCriteria] | Unset = UNSET
    excluding: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        criteria: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()
                criteria.append(criteria_item)

        excluding = self.excluding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if excluding is not UNSET:
            field_dict["excluding"] = excluding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search_criteria import (
            CsSysGenericSearchSearchResultHisSearchCriteria,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _criteria = d.pop("criteria", UNSET)
        criteria: list[CsSysGenericSearchSearchResultHisSearchCriteria] | Unset = UNSET
        if _criteria is not UNSET:
            criteria = []
            for criteria_item_data in _criteria:
                criteria_item = CsSysGenericSearchSearchResultHisSearchCriteria.from_dict(criteria_item_data)

                criteria.append(criteria_item)

        excluding = d.pop("excluding", UNSET)

        cs_sys_generic_search_search_result_his_search_criteria_group = cls(
            criteria=criteria,
            excluding=excluding,
        )

        cs_sys_generic_search_search_result_his_search_criteria_group.additional_properties = d
        return cs_sys_generic_search_search_result_his_search_criteria_group

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
