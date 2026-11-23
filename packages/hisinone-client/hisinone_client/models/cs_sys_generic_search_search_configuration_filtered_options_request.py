from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationFilteredOptionsRequest")


@_attrs_define
class CsSysGenericSearchSearchConfigurationFilteredOptionsRequest:
    """
    Attributes:
        config_file (str | Unset):
        limit (int | Unset):
        search_entity (str | Unset):
        where_column (str | Unset):
        where_value (str | Unset):
    """

    config_file: str | Unset = UNSET
    limit: int | Unset = UNSET
    search_entity: str | Unset = UNSET
    where_column: str | Unset = UNSET
    where_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_file = self.config_file

        limit = self.limit

        search_entity = self.search_entity

        where_column = self.where_column

        where_value = self.where_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if limit is not UNSET:
            field_dict["limit"] = limit
        if search_entity is not UNSET:
            field_dict["searchEntity"] = search_entity
        if where_column is not UNSET:
            field_dict["whereColumn"] = where_column
        if where_value is not UNSET:
            field_dict["whereValue"] = where_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_file = d.pop("configFile", UNSET)

        limit = d.pop("limit", UNSET)

        search_entity = d.pop("searchEntity", UNSET)

        where_column = d.pop("whereColumn", UNSET)

        where_value = d.pop("whereValue", UNSET)

        cs_sys_generic_search_search_configuration_filtered_options_request = cls(
            config_file=config_file,
            limit=limit,
            search_entity=search_entity,
            where_column=where_column,
            where_value=where_value,
        )

        cs_sys_generic_search_search_configuration_filtered_options_request.additional_properties = d
        return cs_sys_generic_search_search_configuration_filtered_options_request

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
