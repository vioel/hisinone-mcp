from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_language_char_code_enum_type import DeMathplanMosesEdciLanguageCharCodeEnumType
    from ..models.de_mathplan_moses_edci_text_content_type_code_enum_type import (
        DeMathplanMosesEdciTextContentTypeCodeEnumType,
    )


T = TypeVar("T", bound="DeMathplanMosesEdciTextType")


@_attrs_define
class DeMathplanMosesEdciTextType:
    """
    Attributes:
        content_type (DeMathplanMosesEdciTextContentTypeCodeEnumType | Unset):
        lang (DeMathplanMosesEdciLanguageCharCodeEnumType | Unset):
        value (str | Unset):
    """

    content_type: DeMathplanMosesEdciTextContentTypeCodeEnumType | Unset = UNSET
    lang: DeMathplanMosesEdciLanguageCharCodeEnumType | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        content_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        lang: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lang, Unset):
            lang = self.lang.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if lang is not UNSET:
            field_dict["lang"] = lang
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_language_char_code_enum_type import (
            DeMathplanMosesEdciLanguageCharCodeEnumType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_text_content_type_code_enum_type import (
            DeMathplanMosesEdciTextContentTypeCodeEnumType,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _content_type = d.pop("contentType", UNSET)
        content_type: DeMathplanMosesEdciTextContentTypeCodeEnumType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = DeMathplanMosesEdciTextContentTypeCodeEnumType.from_dict(_content_type)

        _lang = d.pop("lang", UNSET)
        lang: DeMathplanMosesEdciLanguageCharCodeEnumType | Unset
        if isinstance(_lang, Unset):
            lang = UNSET
        else:
            lang = DeMathplanMosesEdciLanguageCharCodeEnumType.from_dict(_lang)

        value = d.pop("value", UNSET)

        de_mathplan_moses_edci_text_type = cls(
            content_type=content_type,
            lang=lang,
            value=value,
        )

        de_mathplan_moses_edci_text_type.additional_properties = d
        return de_mathplan_moses_edci_text_type

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
