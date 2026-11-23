from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search import CsSysGenericSearchSearchResultHisSearch
    from ..models.cs_sys_generic_search_search_result_his_sort_criterion import (
        CsSysGenericSearchSearchResultHisSortCriterion,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchResultHisSearchRequest")


@_attrs_define
class CsSysGenericSearchSearchResultHisSearchRequest:
    """
    Example:
        {'offset': 0, 'configFile': 'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key':
            'Publication.publicationType.id', 'selectList': [5]}]}

    Attributes:
        limit (int | Unset):
        offset (int | Unset):
        search (CsSysGenericSearchSearchResultHisSearch | Unset):
        sort_criteria (list[CsSysGenericSearchSearchResultHisSortCriterion] | Unset):
    """

    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    search: CsSysGenericSearchSearchResultHisSearch | Unset = UNSET
    sort_criteria: list[CsSysGenericSearchSearchResultHisSortCriterion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        search: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        sort_criteria: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort_criteria, Unset):
            sort_criteria = []
            for sort_criteria_item_data in self.sort_criteria:
                sort_criteria_item = sort_criteria_item_data.to_dict()
                sort_criteria.append(sort_criteria_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if search is not UNSET:
            field_dict["search"] = search
        if sort_criteria is not UNSET:
            field_dict["sortCriteria"] = sort_criteria

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search import CsSysGenericSearchSearchResultHisSearch  # noqa: PLC0415
        from ..models.cs_sys_generic_search_search_result_his_sort_criterion import (
            CsSysGenericSearchSearchResultHisSortCriterion,  # noqa: PLC0415
        )

        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _search = d.pop("search", UNSET)
        search: CsSysGenericSearchSearchResultHisSearch | Unset
        if isinstance(_search, Unset):
            search = UNSET
        else:
            search = CsSysGenericSearchSearchResultHisSearch.from_dict(_search)

        _sort_criteria = d.pop("sortCriteria", UNSET)
        sort_criteria: list[CsSysGenericSearchSearchResultHisSortCriterion] | Unset = UNSET
        if _sort_criteria is not UNSET:
            sort_criteria = []
            for sort_criteria_item_data in _sort_criteria:
                sort_criteria_item = CsSysGenericSearchSearchResultHisSortCriterion.from_dict(sort_criteria_item_data)

                sort_criteria.append(sort_criteria_item)

        cs_sys_generic_search_search_result_his_search_request = cls(
            limit=limit,
            offset=offset,
            search=search,
            sort_criteria=sort_criteria,
        )

        cs_sys_generic_search_search_result_his_search_request.additional_properties = d
        return cs_sys_generic_search_search_result_his_search_request

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
