from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciScoringSchemeType")


@_attrs_define
class DeMathplanMosesEdciScoringSchemeType:
    """
    Attributes:
        description (DeMathplanMosesEdciNoteType | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        supplementary_doc (list[DeMathplanMosesEdciDocumentType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
    """

    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    supplementary_doc: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        supplementary_doc: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.supplementary_doc, Unset):
            supplementary_doc = []
            for supplementary_doc_item_data in self.supplementary_doc:
                supplementary_doc_item = supplementary_doc_item_data.to_dict()
                supplementary_doc.append(supplementary_doc_item)

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if supplementary_doc is not UNSET:
            field_dict["supplementaryDoc"] = supplementary_doc
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _supplementary_doc = d.pop("supplementaryDoc", UNSET)
        supplementary_doc: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
        if _supplementary_doc is not UNSET:
            supplementary_doc = []
            for supplementary_doc_item_data in _supplementary_doc:
                supplementary_doc_item = DeMathplanMosesEdciDocumentType.from_dict(supplementary_doc_item_data)

                supplementary_doc.append(supplementary_doc_item)

        _title = d.pop("title", UNSET)
        title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = DeMathplanMosesEdciTextType.from_dict(title_item_data)

                title.append(title_item)

        de_mathplan_moses_edci_scoring_scheme_type = cls(
            description=description,
            id=id,
            identifier=identifier,
            supplementary_doc=supplementary_doc,
            title=title,
        )

        de_mathplan_moses_edci_scoring_scheme_type.additional_properties = d
        return de_mathplan_moses_edci_scoring_scheme_type

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
