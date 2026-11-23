from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_image_object_type import DeMathplanMosesEdciImageObjectType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_learning_opportunity_type_learning_schedule import (
        DeMathplanMosesEdciLearningOpportunityTypeLearningSchedule,
    )
    from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_price_details_type import DeMathplanMosesEdciPriceDetailsType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_duration import JavaxXmlDatatypeDuration
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciLearningOpportunityType")


@_attrs_define
class DeMathplanMosesEdciLearningOpportunityType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        admission_procedure (DeMathplanMosesEdciNoteType | Unset):
        alt_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        banner_image (DeMathplanMosesEdciImageObjectType | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        duration (JavaxXmlDatatypeDuration | Unset):
        ended_at_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        has_part (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        homepage (list[DeMathplanMosesEdciDocumentType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        learning_schedule (DeMathplanMosesEdciLearningOpportunityTypeLearningSchedule | Unset):
        price_details (list[DeMathplanMosesEdciPriceDetailsType] | Unset):
        provided_at (list[DeMathplanMosesEdciLocationType] | Unset):
        provided_by (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        schedule_information (list[DeMathplanMosesEdciNoteType] | Unset):
        specified_by (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        started_at_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        supplementary_doc (list[DeMathplanMosesEdciDocumentType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    admission_procedure: DeMathplanMosesEdciNoteType | Unset = UNSET
    alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    banner_image: DeMathplanMosesEdciImageObjectType | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    duration: JavaxXmlDatatypeDuration | Unset = UNSET
    ended_at_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    has_part: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    homepage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    learning_schedule: DeMathplanMosesEdciLearningOpportunityTypeLearningSchedule | Unset = UNSET
    price_details: list[DeMathplanMosesEdciPriceDetailsType] | Unset = UNSET
    provided_at: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
    provided_by: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    schedule_information: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    started_at_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    supplementary_doc: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        admission_procedure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.admission_procedure, Unset):
            admission_procedure = self.admission_procedure.to_dict()

        alt_label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alt_label, Unset):
            alt_label = []
            for alt_label_item_data in self.alt_label:
                alt_label_item = alt_label_item_data.to_dict()
                alt_label.append(alt_label_item)

        banner_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.banner_image, Unset):
            banner_image = self.banner_image.to_dict()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        duration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.to_dict()

        ended_at_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ended_at_date, Unset):
            ended_at_date = self.ended_at_date.to_dict()

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

        learning_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.learning_schedule, Unset):
            learning_schedule = self.learning_schedule.to_dict()

        price_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.price_details, Unset):
            price_details = []
            for price_details_item_data in self.price_details:
                price_details_item = price_details_item_data.to_dict()
                price_details.append(price_details_item)

        provided_at: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.provided_at, Unset):
            provided_at = []
            for provided_at_item_data in self.provided_at:
                provided_at_item = provided_at_item_data.to_dict()
                provided_at.append(provided_at_item)

        provided_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.provided_by, Unset):
            provided_by = []
            for provided_by_item_data in self.provided_by:
                provided_by_item = provided_by_item_data.to_dict()
                provided_by.append(provided_by_item)

        schedule_information: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.schedule_information, Unset):
            schedule_information = []
            for schedule_information_item_data in self.schedule_information:
                schedule_information_item = schedule_information_item_data.to_dict()
                schedule_information.append(schedule_information_item)

        specified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specified_by, Unset):
            specified_by = self.specified_by.to_dict()

        started_at_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.started_at_date, Unset):
            started_at_date = self.started_at_date.to_dict()

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
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if admission_procedure is not UNSET:
            field_dict["admissionProcedure"] = admission_procedure
        if alt_label is not UNSET:
            field_dict["altLabel"] = alt_label
        if banner_image is not UNSET:
            field_dict["bannerImage"] = banner_image
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if ended_at_date is not UNSET:
            field_dict["endedAtDate"] = ended_at_date
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if learning_schedule is not UNSET:
            field_dict["learningSchedule"] = learning_schedule
        if price_details is not UNSET:
            field_dict["priceDetails"] = price_details
        if provided_at is not UNSET:
            field_dict["providedAt"] = provided_at
        if provided_by is not UNSET:
            field_dict["providedBy"] = provided_by
        if schedule_information is not UNSET:
            field_dict["scheduleInformation"] = schedule_information
        if specified_by is not UNSET:
            field_dict["specifiedBy"] = specified_by
        if started_at_date is not UNSET:
            field_dict["startedAtDate"] = started_at_date
        if supplementary_doc is not UNSET:
            field_dict["supplementaryDoc"] = supplementary_doc
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_image_object_type import DeMathplanMosesEdciImageObjectType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_learning_opportunity_type_learning_schedule import (
            DeMathplanMosesEdciLearningOpportunityTypeLearningSchedule,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_price_details_type import DeMathplanMosesEdciPriceDetailsType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415
        from ..models.javax_xml_datatype_duration import JavaxXmlDatatypeDuration  # noqa: PLC0415
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _additional_note = d.pop("additionalNote", UNSET)
        additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _additional_note is not UNSET:
            additional_note = []
            for additional_note_item_data in _additional_note:
                additional_note_item = DeMathplanMosesEdciNoteType.from_dict(additional_note_item_data)

                additional_note.append(additional_note_item)

        _admission_procedure = d.pop("admissionProcedure", UNSET)
        admission_procedure: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_admission_procedure, Unset):
            admission_procedure = UNSET
        else:
            admission_procedure = DeMathplanMosesEdciNoteType.from_dict(_admission_procedure)

        _alt_label = d.pop("altLabel", UNSET)
        alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _alt_label is not UNSET:
            alt_label = []
            for alt_label_item_data in _alt_label:
                alt_label_item = DeMathplanMosesEdciLanguageStringType.from_dict(alt_label_item_data)

                alt_label.append(alt_label_item)

        _banner_image = d.pop("bannerImage", UNSET)
        banner_image: DeMathplanMosesEdciImageObjectType | Unset
        if isinstance(_banner_image, Unset):
            banner_image = UNSET
        else:
            banner_image = DeMathplanMosesEdciImageObjectType.from_dict(_banner_image)

        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        _duration = d.pop("duration", UNSET)
        duration: JavaxXmlDatatypeDuration | Unset
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = JavaxXmlDatatypeDuration.from_dict(_duration)

        _ended_at_date = d.pop("endedAtDate", UNSET)
        ended_at_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_ended_at_date, Unset):
            ended_at_date = UNSET
        else:
            ended_at_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_ended_at_date)

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

        _learning_schedule = d.pop("learningSchedule", UNSET)
        learning_schedule: DeMathplanMosesEdciLearningOpportunityTypeLearningSchedule | Unset
        if isinstance(_learning_schedule, Unset):
            learning_schedule = UNSET
        else:
            learning_schedule = DeMathplanMosesEdciLearningOpportunityTypeLearningSchedule.from_dict(_learning_schedule)

        _price_details = d.pop("priceDetails", UNSET)
        price_details: list[DeMathplanMosesEdciPriceDetailsType] | Unset = UNSET
        if _price_details is not UNSET:
            price_details = []
            for price_details_item_data in _price_details:
                price_details_item = DeMathplanMosesEdciPriceDetailsType.from_dict(price_details_item_data)

                price_details.append(price_details_item)

        _provided_at = d.pop("providedAt", UNSET)
        provided_at: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
        if _provided_at is not UNSET:
            provided_at = []
            for provided_at_item_data in _provided_at:
                provided_at_item = DeMathplanMosesEdciLocationType.from_dict(provided_at_item_data)

                provided_at.append(provided_at_item)

        _provided_by = d.pop("providedBy", UNSET)
        provided_by: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _provided_by is not UNSET:
            provided_by = []
            for provided_by_item_data in _provided_by:
                provided_by_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(provided_by_item_data)

                provided_by.append(provided_by_item)

        _schedule_information = d.pop("scheduleInformation", UNSET)
        schedule_information: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _schedule_information is not UNSET:
            schedule_information = []
            for schedule_information_item_data in _schedule_information:
                schedule_information_item = DeMathplanMosesEdciNoteType.from_dict(schedule_information_item_data)

                schedule_information.append(schedule_information_item)

        _specified_by = d.pop("specifiedBy", UNSET)
        specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_specified_by, Unset):
            specified_by = UNSET
        else:
            specified_by = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_specified_by)

        _started_at_date = d.pop("startedAtDate", UNSET)
        started_at_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_started_at_date, Unset):
            started_at_date = UNSET
        else:
            started_at_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_started_at_date)

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

        de_mathplan_moses_edci_learning_opportunity_type = cls(
            additional_note=additional_note,
            admission_procedure=admission_procedure,
            alt_label=alt_label,
            banner_image=banner_image,
            description=description,
            duration=duration,
            ended_at_date=ended_at_date,
            has_part=has_part,
            homepage=homepage,
            id=id,
            identifier=identifier,
            learning_schedule=learning_schedule,
            price_details=price_details,
            provided_at=provided_at,
            provided_by=provided_by,
            schedule_information=schedule_information,
            specified_by=specified_by,
            started_at_date=started_at_date,
            supplementary_doc=supplementary_doc,
            title=title,
        )

        de_mathplan_moses_edci_learning_opportunity_type.additional_properties = d
        return de_mathplan_moses_edci_learning_opportunity_type

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
