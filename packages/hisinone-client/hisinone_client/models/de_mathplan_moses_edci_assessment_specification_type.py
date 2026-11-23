from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_assessment_specification_type_grading_scheme import (
        DeMathplanMosesEdciAssessmentSpecificationTypeGradingScheme,
    )
    from ..models.de_mathplan_moses_edci_assessment_specification_type_language import (
        DeMathplanMosesEdciAssessmentSpecificationTypeLanguage,
    )
    from ..models.de_mathplan_moses_edci_assessment_specification_type_mode import (
        DeMathplanMosesEdciAssessmentSpecificationTypeMode,
    )
    from ..models.de_mathplan_moses_edci_assessment_specification_type_type import (
        DeMathplanMosesEdciAssessmentSpecificationTypeType,
    )
    from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciAssessmentSpecificationType")


@_attrs_define
class DeMathplanMosesEdciAssessmentSpecificationType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        alt_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        grading_scheme (DeMathplanMosesEdciAssessmentSpecificationTypeGradingScheme | Unset):
        has_part (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        homepage (list[DeMathplanMosesEdciDocumentType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        language (list[DeMathplanMosesEdciAssessmentSpecificationTypeLanguage] | Unset):
        mode (list[DeMathplanMosesEdciAssessmentSpecificationTypeMode] | Unset):
        proves (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        specialization_of (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        supplementary_doc (list[DeMathplanMosesEdciDocumentType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        type_ (list[DeMathplanMosesEdciAssessmentSpecificationTypeType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    grading_scheme: DeMathplanMosesEdciAssessmentSpecificationTypeGradingScheme | Unset = UNSET
    has_part: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    homepage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    language: list[DeMathplanMosesEdciAssessmentSpecificationTypeLanguage] | Unset = UNSET
    mode: list[DeMathplanMosesEdciAssessmentSpecificationTypeMode] | Unset = UNSET
    proves: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    specialization_of: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    supplementary_doc: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    type_: list[DeMathplanMosesEdciAssessmentSpecificationTypeType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        alt_label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alt_label, Unset):
            alt_label = []
            for alt_label_item_data in self.alt_label:
                alt_label_item = alt_label_item_data.to_dict()
                alt_label.append(alt_label_item)

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        grading_scheme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grading_scheme, Unset):
            grading_scheme = self.grading_scheme.to_dict()

        has_part: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_part, Unset):
            has_part = []
            for has_part_item_data in self.has_part:
                has_part_item = has_part_item_data.to_dict()
                has_part.append(has_part_item)

        homepage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.homepage, Unset):
            homepage = []
            for homepage_item_data in self.homepage:
                homepage_item = homepage_item_data.to_dict()
                homepage.append(homepage_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        language: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = []
            for language_item_data in self.language:
                language_item = language_item_data.to_dict()
                language.append(language_item)

        mode: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = []
            for mode_item_data in self.mode:
                mode_item = mode_item_data.to_dict()
                mode.append(mode_item)

        proves: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.proves, Unset):
            proves = []
            for proves_item_data in self.proves:
                proves_item = proves_item_data.to_dict()
                proves.append(proves_item)

        specialization_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.specialization_of, Unset):
            specialization_of = []
            for specialization_of_item_data in self.specialization_of:
                specialization_of_item = specialization_of_item_data.to_dict()
                specialization_of.append(specialization_of_item)

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

        type_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item = type_item_data.to_dict()
                type_.append(type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if alt_label is not UNSET:
            field_dict["altLabel"] = alt_label
        if description is not UNSET:
            field_dict["description"] = description
        if grading_scheme is not UNSET:
            field_dict["gradingScheme"] = grading_scheme
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if language is not UNSET:
            field_dict["language"] = language
        if mode is not UNSET:
            field_dict["mode"] = mode
        if proves is not UNSET:
            field_dict["proves"] = proves
        if specialization_of is not UNSET:
            field_dict["specializationOf"] = specialization_of
        if supplementary_doc is not UNSET:
            field_dict["supplementaryDoc"] = supplementary_doc
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_assessment_specification_type_grading_scheme import (
            DeMathplanMosesEdciAssessmentSpecificationTypeGradingScheme,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_assessment_specification_type_language import (
            DeMathplanMosesEdciAssessmentSpecificationTypeLanguage,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_assessment_specification_type_mode import (
            DeMathplanMosesEdciAssessmentSpecificationTypeMode,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_assessment_specification_type_type import (
            DeMathplanMosesEdciAssessmentSpecificationTypeType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

        d = dict(src_dict)
        _additional_note = d.pop("additionalNote", UNSET)
        additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _additional_note is not UNSET:
            additional_note = []
            for additional_note_item_data in _additional_note:
                additional_note_item = DeMathplanMosesEdciNoteType.from_dict(additional_note_item_data)

                additional_note.append(additional_note_item)

        _alt_label = d.pop("altLabel", UNSET)
        alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _alt_label is not UNSET:
            alt_label = []
            for alt_label_item_data in _alt_label:
                alt_label_item = DeMathplanMosesEdciLanguageStringType.from_dict(alt_label_item_data)

                alt_label.append(alt_label_item)

        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        _grading_scheme = d.pop("gradingScheme", UNSET)
        grading_scheme: DeMathplanMosesEdciAssessmentSpecificationTypeGradingScheme | Unset
        if isinstance(_grading_scheme, Unset):
            grading_scheme = UNSET
        else:
            grading_scheme = DeMathplanMosesEdciAssessmentSpecificationTypeGradingScheme.from_dict(_grading_scheme)

        _has_part = d.pop("hasPart", UNSET)
        has_part: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _has_part is not UNSET:
            has_part = []
            for has_part_item_data in _has_part:
                has_part_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(has_part_item_data)

                has_part.append(has_part_item)

        _homepage = d.pop("homepage", UNSET)
        homepage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
        if _homepage is not UNSET:
            homepage = []
            for homepage_item_data in _homepage:
                homepage_item = DeMathplanMosesEdciDocumentType.from_dict(homepage_item_data)

                homepage.append(homepage_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _language = d.pop("language", UNSET)
        language: list[DeMathplanMosesEdciAssessmentSpecificationTypeLanguage] | Unset = UNSET
        if _language is not UNSET:
            language = []
            for language_item_data in _language:
                language_item = DeMathplanMosesEdciAssessmentSpecificationTypeLanguage.from_dict(language_item_data)

                language.append(language_item)

        _mode = d.pop("mode", UNSET)
        mode: list[DeMathplanMosesEdciAssessmentSpecificationTypeMode] | Unset = UNSET
        if _mode is not UNSET:
            mode = []
            for mode_item_data in _mode:
                mode_item = DeMathplanMosesEdciAssessmentSpecificationTypeMode.from_dict(mode_item_data)

                mode.append(mode_item)

        _proves = d.pop("proves", UNSET)
        proves: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _proves is not UNSET:
            proves = []
            for proves_item_data in _proves:
                proves_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(proves_item_data)

                proves.append(proves_item)

        _specialization_of = d.pop("specializationOf", UNSET)
        specialization_of: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _specialization_of is not UNSET:
            specialization_of = []
            for specialization_of_item_data in _specialization_of:
                specialization_of_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(
                    specialization_of_item_data
                )

                specialization_of.append(specialization_of_item)

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

        _type_ = d.pop("type", UNSET)
        type_: list[DeMathplanMosesEdciAssessmentSpecificationTypeType] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = DeMathplanMosesEdciAssessmentSpecificationTypeType.from_dict(type_item_data)

                type_.append(type_item)

        de_mathplan_moses_edci_assessment_specification_type = cls(
            additional_note=additional_note,
            alt_label=alt_label,
            description=description,
            grading_scheme=grading_scheme,
            has_part=has_part,
            homepage=homepage,
            id=id,
            identifier=identifier,
            language=language,
            mode=mode,
            proves=proves,
            specialization_of=specialization_of,
            supplementary_doc=supplementary_doc,
            title=title,
            type_=type_,
        )

        de_mathplan_moses_edci_assessment_specification_type.additional_properties = d
        return de_mathplan_moses_edci_assessment_specification_type

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
