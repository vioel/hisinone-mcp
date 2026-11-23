from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContextDefinitionRest")


@_attrs_define
class ContextDefinitionRest:
    """
    Attributes:
        id (int | Unset):
        reference_context (str | Unset):
        uniquename (str | Unset):
    """

    id: int | Unset = UNSET
    reference_context: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reference_context = self.reference_context

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if reference_context is not UNSET:
            field_dict["referenceContext"] = reference_context
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        reference_context = d.pop("referenceContext", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        context_definition_rest = cls(
            id=id,
            reference_context=reference_context,
            uniquename=uniquename,
        )

        context_definition_rest.additional_properties = d
        return context_definition_rest

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
