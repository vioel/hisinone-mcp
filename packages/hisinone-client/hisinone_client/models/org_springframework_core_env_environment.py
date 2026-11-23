from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrgSpringframeworkCoreEnvEnvironment")


@_attrs_define
class OrgSpringframeworkCoreEnvEnvironment:
    """
    Attributes:
        active_profiles (list[str] | Unset):
        default_profiles (list[str] | Unset):
    """

    active_profiles: list[str] | Unset = UNSET
    default_profiles: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        active_profiles: list[str] | Unset = UNSET
        if not isinstance(self.active_profiles, Unset):
            active_profiles = self.active_profiles

        default_profiles: list[str] | Unset = UNSET
        if not isinstance(self.default_profiles, Unset):
            default_profiles = self.default_profiles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_profiles is not UNSET:
            field_dict["activeProfiles"] = active_profiles
        if default_profiles is not UNSET:
            field_dict["defaultProfiles"] = default_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_profiles = cast(list[str], d.pop("activeProfiles", UNSET))

        default_profiles = cast(list[str], d.pop("defaultProfiles", UNSET))

        org_springframework_core_env_environment = cls(
            active_profiles=active_profiles,
            default_profiles=default_profiles,
        )

        org_springframework_core_env_environment.additional_properties = d
        return org_springframework_core_env_environment

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
