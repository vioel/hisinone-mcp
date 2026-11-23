from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysGenericSearchSearchCriteriaSetHisSearchCriteriaSetRequest")


@_attrs_define
class CsSysGenericSearchSearchCriteriaSetHisSearchCriteriaSetRequest:
    """
    Attributes:
        config_file (str | Unset):
        context (str | Unset):
        flow_name (str | Unset):
    """

    config_file: str | Unset = UNSET
    context: str | Unset = UNSET
    flow_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_file = self.config_file

        context = self.context

        flow_name = self.flow_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if context is not UNSET:
            field_dict["context"] = context
        if flow_name is not UNSET:
            field_dict["flowName"] = flow_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_file = d.pop("configFile", UNSET)

        context = d.pop("context", UNSET)

        flow_name = d.pop("flowName", UNSET)

        cs_sys_generic_search_search_criteria_set_his_search_criteria_set_request = cls(
            config_file=config_file,
            context=context,
            flow_name=flow_name,
        )

        cs_sys_generic_search_search_criteria_set_his_search_criteria_set_request.additional_properties = d
        return cs_sys_generic_search_search_criteria_set_his_search_criteria_set_request

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
