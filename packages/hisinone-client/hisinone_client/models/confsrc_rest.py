from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfsrcRest")


@_attrs_define
class ConfsrcRest:
    """
    Attributes:
        active (bool | Unset):
        editable (bool | Unset):
        his_confsrc (bool | Unset):
        id (int | Unset):
        priority (int | Unset):
        uniquename (str | Unset):
    """

    active: bool | Unset = UNSET
    editable: bool | Unset = UNSET
    his_confsrc: bool | Unset = UNSET
    id: int | Unset = UNSET
    priority: int | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        editable = self.editable

        his_confsrc = self.his_confsrc

        id = self.id

        priority = self.priority

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if editable is not UNSET:
            field_dict["editable"] = editable
        if his_confsrc is not UNSET:
            field_dict["hisConfsrc"] = his_confsrc
        if id is not UNSET:
            field_dict["id"] = id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        editable = d.pop("editable", UNSET)

        his_confsrc = d.pop("hisConfsrc", UNSET)

        id = d.pop("id", UNSET)

        priority = d.pop("priority", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        confsrc_rest = cls(
            active=active,
            editable=editable,
            his_confsrc=his_confsrc,
            id=id,
            priority=priority,
            uniquename=uniquename,
        )

        confsrc_rest.additional_properties = d
        return confsrc_rest

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
