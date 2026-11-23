from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysRestSiteMapUrl")


@_attrs_define
class CsSysRestSiteMapUrl:
    """
    Attributes:
        last_mod (str | Unset):
        loc (str | Unset):
    """

    last_mod: str | Unset = UNSET
    loc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        last_mod = self.last_mod

        loc = self.loc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_mod is not UNSET:
            field_dict["lastMod"] = last_mod
        if loc is not UNSET:
            field_dict["loc"] = loc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_mod = d.pop("lastMod", UNSET)

        loc = d.pop("loc", UNSET)

        cs_sys_rest_site_map_url = cls(
            last_mod=last_mod,
            loc=loc,
        )

        cs_sys_rest_site_map_url.additional_properties = d
        return cs_sys_rest_site_map_url

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
