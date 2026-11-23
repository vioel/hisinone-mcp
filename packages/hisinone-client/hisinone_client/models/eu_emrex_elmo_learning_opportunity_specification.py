from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer
    from ..models.eu_emrex_elmo_learning_opportunity_specification_has_part import (
        EuEmrexElmoLearningOpportunitySpecificationHasPart,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_identifier import (
        EuEmrexElmoLearningOpportunitySpecificationIdentifier,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifies,
    )
    from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
        EuEmrexElmoPlaintextMultilineStringWithOptionalLang,
    )
    from ..models.eu_emrex_elmo_simple_html_string_with_optional_lang import EuEmrexElmoSimpleHtmlStringWithOptionalLang
    from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang


T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecification")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecification:
    """
    Attributes:
        description (list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset):
        description_html (list[EuEmrexElmoSimpleHtmlStringWithOptionalLang] | Unset):
        extension (EuEmrexElmoCustomExtensionsContainer | Unset):
        has_part (list[EuEmrexElmoLearningOpportunitySpecificationHasPart] | Unset):
        identifier (list[EuEmrexElmoLearningOpportunitySpecificationIdentifier] | Unset):
        isced_code (str | Unset):
        specifies (EuEmrexElmoLearningOpportunitySpecificationSpecifies | Unset):
        subject_area (str | Unset):
        title (list[EuEmrexElmoTokenWithOptionalLang] | Unset):
        type_ (str | Unset):
        url (str | Unset):
    """

    description: list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset = UNSET
    description_html: list[EuEmrexElmoSimpleHtmlStringWithOptionalLang] | Unset = UNSET
    extension: EuEmrexElmoCustomExtensionsContainer | Unset = UNSET
    has_part: list[EuEmrexElmoLearningOpportunitySpecificationHasPart] | Unset = UNSET
    identifier: list[EuEmrexElmoLearningOpportunitySpecificationIdentifier] | Unset = UNSET
    isced_code: str | Unset = UNSET
    specifies: EuEmrexElmoLearningOpportunitySpecificationSpecifies | Unset = UNSET
    subject_area: str | Unset = UNSET
    title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        description_html: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description_html, Unset):
            description_html = []
            for description_html_item_data in self.description_html:
                description_html_item = description_html_item_data.to_dict()
                description_html.append(description_html_item)

        extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension, Unset):
            extension = self.extension.to_dict()

        has_part: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_part, Unset):
            has_part = []
            for has_part_item_data in self.has_part:
                has_part_item = has_part_item_data.to_dict()
                has_part.append(has_part_item)

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        isced_code = self.isced_code

        specifies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specifies, Unset):
            specifies = self.specifies.to_dict()

        subject_area = self.subject_area

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if description_html is not UNSET:
            field_dict["descriptionHtml"] = description_html
        if extension is not UNSET:
            field_dict["extension"] = extension
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if isced_code is not UNSET:
            field_dict["iscedCode"] = isced_code
        if specifies is not UNSET:
            field_dict["specifies"] = specifies
        if subject_area is not UNSET:
            field_dict["subjectArea"] = subject_area
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer  # noqa: PLC0415
        from ..models.eu_emrex_elmo_learning_opportunity_specification_has_part import (
            EuEmrexElmoLearningOpportunitySpecificationHasPart,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_identifier import (
            EuEmrexElmoLearningOpportunitySpecificationIdentifier,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifies,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
            EuEmrexElmoPlaintextMultilineStringWithOptionalLang,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_simple_html_string_with_optional_lang import (
            EuEmrexElmoSimpleHtmlStringWithOptionalLang,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang  # noqa: PLC0415

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = EuEmrexElmoPlaintextMultilineStringWithOptionalLang.from_dict(description_item_data)

                description.append(description_item)

        _description_html = d.pop("descriptionHtml", UNSET)
        description_html: list[EuEmrexElmoSimpleHtmlStringWithOptionalLang] | Unset = UNSET
        if _description_html is not UNSET:
            description_html = []
            for description_html_item_data in _description_html:
                description_html_item = EuEmrexElmoSimpleHtmlStringWithOptionalLang.from_dict(
                    description_html_item_data
                )

                description_html.append(description_html_item)

        _extension = d.pop("extension", UNSET)
        extension: EuEmrexElmoCustomExtensionsContainer | Unset
        if isinstance(_extension, Unset):
            extension = UNSET
        else:
            extension = EuEmrexElmoCustomExtensionsContainer.from_dict(_extension)

        _has_part = d.pop("hasPart", UNSET)
        has_part: list[EuEmrexElmoLearningOpportunitySpecificationHasPart] | Unset = UNSET
        if _has_part is not UNSET:
            has_part = []
            for has_part_item_data in _has_part:
                has_part_item = EuEmrexElmoLearningOpportunitySpecificationHasPart.from_dict(has_part_item_data)

                has_part.append(has_part_item)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[EuEmrexElmoLearningOpportunitySpecificationIdentifier] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = EuEmrexElmoLearningOpportunitySpecificationIdentifier.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        isced_code = d.pop("iscedCode", UNSET)

        _specifies = d.pop("specifies", UNSET)
        specifies: EuEmrexElmoLearningOpportunitySpecificationSpecifies | Unset
        if isinstance(_specifies, Unset):
            specifies = UNSET
        else:
            specifies = EuEmrexElmoLearningOpportunitySpecificationSpecifies.from_dict(_specifies)

        subject_area = d.pop("subjectArea", UNSET)

        _title = d.pop("title", UNSET)
        title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = EuEmrexElmoTokenWithOptionalLang.from_dict(title_item_data)

                title.append(title_item)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        eu_emrex_elmo_learning_opportunity_specification = cls(
            description=description,
            description_html=description_html,
            extension=extension,
            has_part=has_part,
            identifier=identifier,
            isced_code=isced_code,
            specifies=specifies,
            subject_area=subject_area,
            title=title,
            type_=type_,
            url=url,
        )

        eu_emrex_elmo_learning_opportunity_specification.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification

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
