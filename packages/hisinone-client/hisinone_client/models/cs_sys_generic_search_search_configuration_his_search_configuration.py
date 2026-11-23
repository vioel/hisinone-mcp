from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_configuration_his_search_criteria import (
        CsSysGenericSearchSearchConfigurationHisSearchCriteria,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationHisSearchConfiguration")


@_attrs_define
class CsSysGenericSearchSearchConfigurationHisSearchConfiguration:
    """
    Attributes:
        config_file (str | Unset):
        page_title (str | Unset):
        search_criteria (CsSysGenericSearchSearchConfigurationHisSearchCriteria | Unset):
        search_entity (str | Unset):
        table_title (str | Unset):
    """

    config_file: str | Unset = UNSET
    page_title: str | Unset = UNSET
    search_criteria: CsSysGenericSearchSearchConfigurationHisSearchCriteria | Unset = UNSET
    search_entity: str | Unset = UNSET
    table_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_file = self.config_file

        page_title = self.page_title

        search_criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_criteria, Unset):
            search_criteria = self.search_criteria.to_dict()

        search_entity = self.search_entity

        table_title = self.table_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if page_title is not UNSET:
            field_dict["pageTitle"] = page_title
        if search_criteria is not UNSET:
            field_dict["searchCriteria"] = search_criteria
        if search_entity is not UNSET:
            field_dict["searchEntity"] = search_entity
        if table_title is not UNSET:
            field_dict["tableTitle"] = table_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_configuration_his_search_criteria import (
            CsSysGenericSearchSearchConfigurationHisSearchCriteria,  # noqa: PLC0415
        )

        d = dict(src_dict)
        config_file = d.pop("configFile", UNSET)

        page_title = d.pop("pageTitle", UNSET)

        _search_criteria = d.pop("searchCriteria", UNSET)
        search_criteria: CsSysGenericSearchSearchConfigurationHisSearchCriteria | Unset
        if isinstance(_search_criteria, Unset):
            search_criteria = UNSET
        else:
            search_criteria = CsSysGenericSearchSearchConfigurationHisSearchCriteria.from_dict(_search_criteria)

        search_entity = d.pop("searchEntity", UNSET)

        table_title = d.pop("tableTitle", UNSET)

        cs_sys_generic_search_search_configuration_his_search_configuration = cls(
            config_file=config_file,
            page_title=page_title,
            search_criteria=search_criteria,
            search_entity=search_entity,
            table_title=table_title,
        )

        cs_sys_generic_search_search_configuration_his_search_configuration.additional_properties = d
        return cs_sys_generic_search_search_configuration_his_search_configuration

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
