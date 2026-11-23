from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContextUsageRest")


@_attrs_define
class ContextUsageRest:
    """
    Attributes:
        confsrc_ids (list[int] | Unset):
        identifier (str | Unset):
    """

    confsrc_ids: list[int] | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        confsrc_ids: list[int] | Unset = UNSET
        if not isinstance(self.confsrc_ids, Unset):
            confsrc_ids = self.confsrc_ids

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confsrc_ids is not UNSET:
            field_dict["confsrcIds"] = confsrc_ids
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confsrc_ids = cast(list[int], d.pop("confsrcIds", UNSET))

        identifier = d.pop("identifier", UNSET)

        context_usage_rest = cls(
            confsrc_ids=confsrc_ids,
            identifier=identifier,
        )

        context_usage_rest.additional_properties = d
        return context_usage_rest

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
