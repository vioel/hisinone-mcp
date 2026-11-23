from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionTermRest")


@_attrs_define
class ConditionTermRest:
    """
    Attributes:
        left_operand (str | Unset):
        operator (str | Unset):
        right_operand (str | Unset):
    """

    left_operand: str | Unset = UNSET
    operator: str | Unset = UNSET
    right_operand: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        left_operand = self.left_operand

        operator = self.operator

        right_operand = self.right_operand

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_operand is not UNSET:
            field_dict["leftOperand"] = left_operand
        if operator is not UNSET:
            field_dict["operator"] = operator
        if right_operand is not UNSET:
            field_dict["rightOperand"] = right_operand

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        left_operand = d.pop("leftOperand", UNSET)

        operator = d.pop("operator", UNSET)

        right_operand = d.pop("rightOperand", UNSET)

        condition_term_rest = cls(
            left_operand=left_operand,
            operator=operator,
            right_operand=right_operand,
        )

        condition_term_rest.additional_properties = d
        return condition_term_rest

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
