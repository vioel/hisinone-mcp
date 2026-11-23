from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorRest")


@_attrs_define
class OperatorRest:
    """
    Attributes:
        i_18_n_key (str | Unset):
        uniquename (str | Unset):
    """

    i_18_n_key: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        i_18_n_key = self.i_18_n_key

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if i_18_n_key is not UNSET:
            field_dict["i18nKey"] = i_18_n_key
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        i_18_n_key = d.pop("i18nKey", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        operator_rest = cls(
            i_18_n_key=i_18_n_key,
            uniquename=uniquename,
        )

        operator_rest.additional_properties = d
        return operator_rest

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
