from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_attachment_identifier import EuEmrexElmoAttachmentIdentifier
    from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer
    from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
        EuEmrexElmoPlaintextMultilineStringWithOptionalLang,
    )
    from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang


T = TypeVar("T", bound="EuEmrexElmoAttachment")


@_attrs_define
class EuEmrexElmoAttachment:
    """
    Attributes:
        content (list[EuEmrexElmoTokenWithOptionalLang] | Unset):
        description (list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset):
        extension (EuEmrexElmoCustomExtensionsContainer | Unset):
        identifier (list[EuEmrexElmoAttachmentIdentifier] | Unset):
        title (list[EuEmrexElmoTokenWithOptionalLang] | Unset):
        type_ (str | Unset):
    """

    content: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
    description: list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset = UNSET
    extension: EuEmrexElmoCustomExtensionsContainer | Unset = UNSET
    identifier: list[EuEmrexElmoAttachmentIdentifier] | Unset = UNSET
    title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension, Unset):
            extension = self.extension.to_dict()

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if description is not UNSET:
            field_dict["description"] = description
        if extension is not UNSET:
            field_dict["extension"] = extension
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_attachment_identifier import EuEmrexElmoAttachmentIdentifier  # noqa: PLC0415
        from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer  # noqa: PLC0415
        from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
            EuEmrexElmoPlaintextMultilineStringWithOptionalLang,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang  # noqa: PLC0415

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = EuEmrexElmoTokenWithOptionalLang.from_dict(content_item_data)

                content.append(content_item)

        _description = d.pop("description", UNSET)
        description: list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = EuEmrexElmoPlaintextMultilineStringWithOptionalLang.from_dict(description_item_data)

                description.append(description_item)

        _extension = d.pop("extension", UNSET)
        extension: EuEmrexElmoCustomExtensionsContainer | Unset
        if isinstance(_extension, Unset):
            extension = UNSET
        else:
            extension = EuEmrexElmoCustomExtensionsContainer.from_dict(_extension)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[EuEmrexElmoAttachmentIdentifier] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = EuEmrexElmoAttachmentIdentifier.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _title = d.pop("title", UNSET)
        title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = EuEmrexElmoTokenWithOptionalLang.from_dict(title_item_data)

                title.append(title_item)

        type_ = d.pop("type", UNSET)

        eu_emrex_elmo_attachment = cls(
            content=content,
            description=description,
            extension=extension,
            identifier=identifier,
            title=title,
            type_=type_,
        )

        eu_emrex_elmo_attachment.additional_properties = d
        return eu_emrex_elmo_attachment

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
