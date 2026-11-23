from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgW3CDomTypeInfo")


@_attrs_define
class OrgW3CDomTypeInfo:
    """
    Attributes:
        type_name (str | Unset):
        type_namespace (str | Unset):
    """

    type_name: str | Unset = UNSET
    type_namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name

        type_namespace = self.type_namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if type_namespace is not UNSET:
            field_dict["typeNamespace"] = type_namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = d.pop("typeName", UNSET)

        type_namespace = d.pop("typeNamespace", UNSET)

        org_w3c_dom_type_info = cls(
            type_name=type_name,
            type_namespace=type_namespace,
        )

        org_w3c_dom_type_info.additional_properties = d
        return org_w3c_dom_type_info

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
