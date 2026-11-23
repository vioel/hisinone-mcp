from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_document_type_language import DeMathplanMosesEdciDocumentTypeLanguage
    from ..models.de_mathplan_moses_edci_document_type_subject import DeMathplanMosesEdciDocumentTypeSubject
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciDocumentType")


@_attrs_define
class DeMathplanMosesEdciDocumentType:
    """
    Attributes:
        language (list[DeMathplanMosesEdciDocumentTypeLanguage] | Unset):
        subject (list[DeMathplanMosesEdciDocumentTypeSubject] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        uri (str | Unset):
    """

    language: list[DeMathplanMosesEdciDocumentTypeLanguage] | Unset = UNSET
    subject: list[DeMathplanMosesEdciDocumentTypeSubject] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        language: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = []
            for language_item_data in self.language:
                language_item = language_item_data.to_dict()
                language.append(language_item)

        subject: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject, Unset):
            subject = []
            for subject_item_data in self.subject:
                subject_item = subject_item_data.to_dict()
                subject.append(subject_item)

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if subject is not UNSET:
            field_dict["subject"] = subject
        if title is not UNSET:
            field_dict["title"] = title
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_document_type_language import DeMathplanMosesEdciDocumentTypeLanguage  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_document_type_subject import DeMathplanMosesEdciDocumentTypeSubject  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

        d = dict(src_dict)
        _language = d.pop("language", UNSET)
        language: list[DeMathplanMosesEdciDocumentTypeLanguage] | Unset = UNSET
        if _language is not UNSET:
            language = []
            for language_item_data in _language:
                language_item = DeMathplanMosesEdciDocumentTypeLanguage.from_dict(language_item_data)

                language.append(language_item)

        _subject = d.pop("subject", UNSET)
        subject: list[DeMathplanMosesEdciDocumentTypeSubject] | Unset = UNSET
        if _subject is not UNSET:
            subject = []
            for subject_item_data in _subject:
                subject_item = DeMathplanMosesEdciDocumentTypeSubject.from_dict(subject_item_data)

                subject.append(subject_item)

        _title = d.pop("title", UNSET)
        title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = DeMathplanMosesEdciTextType.from_dict(title_item_data)

                title.append(title_item)

        uri = d.pop("uri", UNSET)

        de_mathplan_moses_edci_document_type = cls(
            language=language,
            subject=subject,
            title=title,
            uri=uri,
        )

        de_mathplan_moses_edci_document_type.additional_properties = d
        return de_mathplan_moses_edci_document_type

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
