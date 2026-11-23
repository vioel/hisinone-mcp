from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_note_type_subject import DeMathplanMosesEdciNoteTypeSubject
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciNoteType")


@_attrs_define
class DeMathplanMosesEdciNoteType:
    """
    Attributes:
        subject (list[DeMathplanMosesEdciNoteTypeSubject] | Unset):
        text (DeMathplanMosesEdciTextType | Unset):
    """

    subject: list[DeMathplanMosesEdciNoteTypeSubject] | Unset = UNSET
    text: DeMathplanMosesEdciTextType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        subject: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject, Unset):
            subject = []
            for subject_item_data in self.subject:
                subject_item = subject_item_data.to_dict()
                subject.append(subject_item)

        text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_note_type_subject import DeMathplanMosesEdciNoteTypeSubject  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

        d = dict(src_dict)
        _subject = d.pop("subject", UNSET)
        subject: list[DeMathplanMosesEdciNoteTypeSubject] | Unset = UNSET
        if _subject is not UNSET:
            subject = []
            for subject_item_data in _subject:
                subject_item = DeMathplanMosesEdciNoteTypeSubject.from_dict(subject_item_data)

                subject.append(subject_item)

        _text = d.pop("text", UNSET)
        text: DeMathplanMosesEdciTextType | Unset
        if isinstance(_text, Unset):
            text = UNSET
        else:
            text = DeMathplanMosesEdciTextType.from_dict(_text)

        de_mathplan_moses_edci_note_type = cls(
            subject=subject,
            text=text,
        )

        de_mathplan_moses_edci_note_type.additional_properties = d
        return de_mathplan_moses_edci_note_type

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
