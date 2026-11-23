from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysAdminutilsEntityexplorerSysEntityExplorerQueryHqlRequest")


@_attrs_define
class CsSysAdminutilsEntityexplorerSysEntityExplorerQueryHqlRequest:
    """
    Attributes:
        hql (str | Unset):
    """

    hql: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        hql = self.hql

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hql is not UNSET:
            field_dict["hql"] = hql

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hql = d.pop("hql", UNSET)

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_query_hql_request = cls(
            hql=hql,
        )

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_query_hql_request.additional_properties = d
        return cs_sys_adminutils_entityexplorer_sys_entity_explorer_query_hql_request

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
