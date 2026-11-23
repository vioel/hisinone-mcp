from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysRestOpenApiSecurityRequirement")


@_attrs_define
class CsSysRestOpenApiSecurityRequirement:
    """
    Attributes:
        http (list[str] | Unset):
    """

    http: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        http: list[str] | Unset = UNSET
        if not isinstance(self.http, Unset):
            http = self.http

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if http is not UNSET:
            field_dict["http"] = http

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        http = cast(list[str], d.pop("http", UNSET))

        cs_sys_rest_open_api_security_requirement = cls(
            http=http,
        )

        cs_sys_rest_open_api_security_requirement.additional_properties = d
        return cs_sys_rest_open_api_security_requirement

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
