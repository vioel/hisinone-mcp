from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciKeyLanguageStringType")


@_attrs_define
class DeMathplanMosesEdciKeyLanguageStringType:
    """
    Attributes:
        key (str | Unset):
        text (list[DeMathplanMosesEdciTextType] | Unset):
    """

    key: str | Unset = UNSET
    text: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        text: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = []
            for text_item_data in self.text:
                text_item = text_item_data.to_dict()
                text.append(text_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

        d = dict(src_dict)
        key = d.pop("key", UNSET)

        _text = d.pop("text", UNSET)
        text: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _text is not UNSET:
            text = []
            for text_item_data in _text:
                text_item = DeMathplanMosesEdciTextType.from_dict(text_item_data)

                text.append(text_item)

        de_mathplan_moses_edci_key_language_string_type = cls(
            key=key,
            text=text,
        )

        de_mathplan_moses_edci_key_language_string_type.additional_properties = d
        return de_mathplan_moses_edci_key_language_string_type

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
