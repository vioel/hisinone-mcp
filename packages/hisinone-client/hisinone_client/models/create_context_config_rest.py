from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateContextConfigRest")


@_attrs_define
class CreateContextConfigRest:
    """
    Attributes:
        confsrc_id (int | Unset):
        context_id (int | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    confsrc_id: int | Unset = UNSET
    context_id: int | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        confsrc_id = self.confsrc_id

        context_id = self.context_id

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confsrc_id is not UNSET:
            field_dict["confsrcId"] = confsrc_id
        if context_id is not UNSET:
            field_dict["contextId"] = context_id
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confsrc_id = d.pop("confsrcId", UNSET)

        context_id = d.pop("contextId", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        create_context_config_rest = cls(
            confsrc_id=confsrc_id,
            context_id=context_id,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        create_context_config_rest.additional_properties = d
        return create_context_config_rest

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
