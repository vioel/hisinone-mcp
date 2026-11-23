from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_assessment_type_id_verification_method import (
        DeMathplanMosesEdciAssessmentTypeIdVerificationMethod,
    )
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_result_distribution import DeMathplanMosesEdciResultDistribution
    from ..models.de_mathplan_moses_edci_shortened_grading import DeMathplanMosesEdciShortenedGrading
    from ..models.de_mathplan_moses_edci_text_score_type import DeMathplanMosesEdciTextScoreType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciAssessmentType")


@_attrs_define
class DeMathplanMosesEdciAssessmentType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        assessed_by (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        grade (DeMathplanMosesEdciTextScoreType | Unset):
        has_part (list[DeMathplanMosesEdciAssessmentType] | Unset):
        id (str | Unset):
        id_verification_method (DeMathplanMosesEdciAssessmentTypeIdVerificationMethod | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        issued_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        result_distribution (DeMathplanMosesEdciResultDistribution | Unset):
        shortened_grading (DeMathplanMosesEdciShortenedGrading | Unset):
        specified_by (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    assessed_by: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    grade: DeMathplanMosesEdciTextScoreType | Unset = UNSET
    has_part: list[DeMathplanMosesEdciAssessmentType] | Unset = UNSET
    id: str | Unset = UNSET
    id_verification_method: DeMathplanMosesEdciAssessmentTypeIdVerificationMethod | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    result_distribution: DeMathplanMosesEdciResultDistribution | Unset = UNSET
    shortened_grading: DeMathplanMosesEdciShortenedGrading | Unset = UNSET
    specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        assessed_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assessed_by, Unset):
            assessed_by = []
            for assessed_by_item_data in self.assessed_by:
                assessed_by_item = assessed_by_item_data.to_dict()
                assessed_by.append(assessed_by_item)

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        grade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grade, Unset):
            grade = self.grade.to_dict()

        has_part: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_part, Unset):
            has_part = []
            for has_part_item_data in self.has_part:
                has_part_item = has_part_item_data.to_dict()
                has_part.append(has_part_item)

        id = self.id

        id_verification_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.id_verification_method, Unset):
            id_verification_method = self.id_verification_method.to_dict()

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        issued_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.to_dict()

        result_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result_distribution, Unset):
            result_distribution = self.result_distribution.to_dict()

        shortened_grading: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shortened_grading, Unset):
            shortened_grading = self.shortened_grading.to_dict()

        specified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specified_by, Unset):
            specified_by = self.specified_by.to_dict()

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if assessed_by is not UNSET:
            field_dict["assessedBy"] = assessed_by
        if description is not UNSET:
            field_dict["description"] = description
        if grade is not UNSET:
            field_dict["grade"] = grade
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if id is not UNSET:
            field_dict["id"] = id
        if id_verification_method is not UNSET:
            field_dict["idVerificationMethod"] = id_verification_method
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if result_distribution is not UNSET:
            field_dict["resultDistribution"] = result_distribution
        if shortened_grading is not UNSET:
            field_dict["shortenedGrading"] = shortened_grading
        if specified_by is not UNSET:
            field_dict["specifiedBy"] = specified_by
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_assessment_type_id_verification_method import (
            DeMathplanMosesEdciAssessmentTypeIdVerificationMethod,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_result_distribution import DeMathplanMosesEdciResultDistribution  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_shortened_grading import DeMathplanMosesEdciShortenedGrading  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_score_type import DeMathplanMosesEdciTextScoreType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _additional_note = d.pop("additionalNote", UNSET)
        additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _additional_note is not UNSET:
            additional_note = []
            for additional_note_item_data in _additional_note:
                additional_note_item = DeMathplanMosesEdciNoteType.from_dict(additional_note_item_data)

                additional_note.append(additional_note_item)

        _assessed_by = d.pop("assessedBy", UNSET)
        assessed_by: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _assessed_by is not UNSET:
            assessed_by = []
            for assessed_by_item_data in _assessed_by:
                assessed_by_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(assessed_by_item_data)

                assessed_by.append(assessed_by_item)

        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        _grade = d.pop("grade", UNSET)
        grade: DeMathplanMosesEdciTextScoreType | Unset
        if isinstance(_grade, Unset):
            grade = UNSET
        else:
            grade = DeMathplanMosesEdciTextScoreType.from_dict(_grade)

        _has_part = d.pop("hasPart", UNSET)
        has_part: list[DeMathplanMosesEdciAssessmentType] | Unset = UNSET
        if _has_part is not UNSET:
            has_part = []
            for has_part_item_data in _has_part:
                has_part_item = DeMathplanMosesEdciAssessmentType.from_dict(has_part_item_data)

                has_part.append(has_part_item)

        id = d.pop("id", UNSET)

        _id_verification_method = d.pop("idVerificationMethod", UNSET)
        id_verification_method: DeMathplanMosesEdciAssessmentTypeIdVerificationMethod | Unset
        if isinstance(_id_verification_method, Unset):
            id_verification_method = UNSET
        else:
            id_verification_method = DeMathplanMosesEdciAssessmentTypeIdVerificationMethod.from_dict(
                _id_verification_method
            )

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _issued_date = d.pop("issuedDate", UNSET)
        issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_issued_date)

        _result_distribution = d.pop("resultDistribution", UNSET)
        result_distribution: DeMathplanMosesEdciResultDistribution | Unset
        if isinstance(_result_distribution, Unset):
            result_distribution = UNSET
        else:
            result_distribution = DeMathplanMosesEdciResultDistribution.from_dict(_result_distribution)

        _shortened_grading = d.pop("shortenedGrading", UNSET)
        shortened_grading: DeMathplanMosesEdciShortenedGrading | Unset
        if isinstance(_shortened_grading, Unset):
            shortened_grading = UNSET
        else:
            shortened_grading = DeMathplanMosesEdciShortenedGrading.from_dict(_shortened_grading)

        _specified_by = d.pop("specifiedBy", UNSET)
        specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_specified_by, Unset):
            specified_by = UNSET
        else:
            specified_by = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_specified_by)

        _title = d.pop("title", UNSET)
        title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = DeMathplanMosesEdciTextType.from_dict(title_item_data)

                title.append(title_item)

        de_mathplan_moses_edci_assessment_type = cls(
            additional_note=additional_note,
            assessed_by=assessed_by,
            description=description,
            grade=grade,
            has_part=has_part,
            id=id,
            id_verification_method=id_verification_method,
            identifier=identifier,
            issued_date=issued_date,
            result_distribution=result_distribution,
            shortened_grading=shortened_grading,
            specified_by=specified_by,
            title=title,
        )

        de_mathplan_moses_edci_assessment_type.additional_properties = d
        return de_mathplan_moses_edci_assessment_type

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
