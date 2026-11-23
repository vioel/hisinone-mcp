from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_attachment import EuEmrexElmoAttachment
    from ..models.eu_emrex_elmo_diploma_supplement_section_content import EuEmrexElmoDiplomaSupplementSectionContent


T = TypeVar("T", bound="EuEmrexElmoDiplomaSupplementSection")


@_attrs_define
class EuEmrexElmoDiplomaSupplementSection:
    """
    Attributes:
        additional_information (list[str] | Unset):
        attachment (list[EuEmrexElmoAttachment] | Unset):
        content (EuEmrexElmoDiplomaSupplementSectionContent | Unset):
        number (str | Unset):
        section (list[EuEmrexElmoDiplomaSupplementSection] | Unset):
        title (str | Unset):
    """

    additional_information: list[str] | Unset = UNSET
    attachment: list[EuEmrexElmoAttachment] | Unset = UNSET
    content: EuEmrexElmoDiplomaSupplementSectionContent | Unset = UNSET
    number: str | Unset = UNSET
    section: list[EuEmrexElmoDiplomaSupplementSection] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_information: list[str] | Unset = UNSET
        if not isinstance(self.additional_information, Unset):
            additional_information = self.additional_information

        attachment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = []
            for attachment_item_data in self.attachment:
                attachment_item = attachment_item_data.to_dict()
                attachment.append(attachment_item)

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        number = self.number

        section: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.section, Unset):
            section = []
            for section_item_data in self.section:
                section_item = section_item_data.to_dict()
                section.append(section_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_information is not UNSET:
            field_dict["additionalInformation"] = additional_information
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if content is not UNSET:
            field_dict["content"] = content
        if number is not UNSET:
            field_dict["number"] = number
        if section is not UNSET:
            field_dict["section"] = section
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_attachment import EuEmrexElmoAttachment  # noqa: PLC0415
        from ..models.eu_emrex_elmo_diploma_supplement_section_content import EuEmrexElmoDiplomaSupplementSectionContent  # noqa: PLC0415

        d = dict(src_dict)
        additional_information = cast(list[str], d.pop("additionalInformation", UNSET))

        _attachment = d.pop("attachment", UNSET)
        attachment: list[EuEmrexElmoAttachment] | Unset = UNSET
        if _attachment is not UNSET:
            attachment = []
            for attachment_item_data in _attachment:
                attachment_item = EuEmrexElmoAttachment.from_dict(attachment_item_data)

                attachment.append(attachment_item)

        _content = d.pop("content", UNSET)
        content: EuEmrexElmoDiplomaSupplementSectionContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = EuEmrexElmoDiplomaSupplementSectionContent.from_dict(_content)

        number = d.pop("number", UNSET)

        _section = d.pop("section", UNSET)
        section: list[EuEmrexElmoDiplomaSupplementSection] | Unset = UNSET
        if _section is not UNSET:
            section = []
            for section_item_data in _section:
                section_item = EuEmrexElmoDiplomaSupplementSection.from_dict(section_item_data)

                section.append(section_item)

        title = d.pop("title", UNSET)

        eu_emrex_elmo_diploma_supplement_section = cls(
            additional_information=additional_information,
            attachment=attachment,
            content=content,
            number=number,
            section=section,
            title=title,
        )

        eu_emrex_elmo_diploma_supplement_section.additional_properties = d
        return eu_emrex_elmo_diploma_supplement_section

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
