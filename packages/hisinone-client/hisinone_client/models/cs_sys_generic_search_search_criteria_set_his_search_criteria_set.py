from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search import CsSysGenericSearchSearchResultHisSearch


T = TypeVar("T", bound="CsSysGenericSearchSearchCriteriaSetHisSearchCriteriaSet")


@_attrs_define
class CsSysGenericSearchSearchCriteriaSetHisSearchCriteriaSet:
    """
    Attributes:
        config_file (str | Unset):
        context (str | Unset):
        defaulttext (str | Unset):
        empty_option (bool | Unset):
        flow_name (str | Unset):
        id (int | Unset):
        search (CsSysGenericSearchSearchResultHisSearch | Unset):
        standard (bool | Unset):
    """

    config_file: str | Unset = UNSET
    context: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    empty_option: bool | Unset = UNSET
    flow_name: str | Unset = UNSET
    id: int | Unset = UNSET
    search: CsSysGenericSearchSearchResultHisSearch | Unset = UNSET
    standard: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_file = self.config_file

        context = self.context

        defaulttext = self.defaulttext

        empty_option = self.empty_option

        flow_name = self.flow_name

        id = self.id

        search: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        standard = self.standard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if context is not UNSET:
            field_dict["context"] = context
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if empty_option is not UNSET:
            field_dict["emptyOption"] = empty_option
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name
        if id is not UNSET:
            field_dict["id"] = id
        if search is not UNSET:
            field_dict["search"] = search
        if standard is not UNSET:
            field_dict["standard"] = standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search import CsSysGenericSearchSearchResultHisSearch  # noqa: PLC0415

        d = dict(src_dict)
        config_file = d.pop("configFile", UNSET)

        context = d.pop("context", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        empty_option = d.pop("emptyOption", UNSET)

        flow_name = d.pop("flowName", UNSET)

        id = d.pop("id", UNSET)

        _search = d.pop("search", UNSET)
        search: CsSysGenericSearchSearchResultHisSearch | Unset
        if isinstance(_search, Unset):
            search = UNSET
        else:
            search = CsSysGenericSearchSearchResultHisSearch.from_dict(_search)

        standard = d.pop("standard", UNSET)

        cs_sys_generic_search_search_criteria_set_his_search_criteria_set = cls(
            config_file=config_file,
            context=context,
            defaulttext=defaulttext,
            empty_option=empty_option,
            flow_name=flow_name,
            id=id,
            search=search,
            standard=standard,
        )

        cs_sys_generic_search_search_criteria_set_his_search_criteria_set.additional_properties = d
        return cs_sys_generic_search_search_criteria_set_his_search_criteria_set

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
