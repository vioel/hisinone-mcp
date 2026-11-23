from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeMathplanMosesEdciTextScoreType")


@_attrs_define
class DeMathplanMosesEdciTextScoreType:
    """
    Attributes:
        scheme_id (str | Unset):
        value (str | Unset):
    """

    scheme_id: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        scheme_id = self.scheme_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheme_id is not UNSET:
            field_dict["schemeID"] = scheme_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheme_id = d.pop("schemeID", UNSET)

        value = d.pop("value", UNSET)

        de_mathplan_moses_edci_text_score_type = cls(
            scheme_id=scheme_id,
            value=value,
        )

        de_mathplan_moses_edci_text_score_type.additional_properties = d
        return de_mathplan_moses_edci_text_score_type

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
