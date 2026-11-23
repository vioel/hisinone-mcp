from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_assessment_type import DeMathplanMosesEdciAssessmentType
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciAwardingProcessType")


@_attrs_define
class DeMathplanMosesEdciAwardingProcessType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        awarding_body (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        location (DeMathplanMosesEdciLocationType | Unset):
        used (list[DeMathplanMosesEdciAssessmentType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    awarding_body: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    location: DeMathplanMosesEdciLocationType | Unset = UNSET
    used: list[DeMathplanMosesEdciAssessmentType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        awarding_body: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.awarding_body, Unset):
            awarding_body = []
            for awarding_body_item_data in self.awarding_body:
                awarding_body_item = awarding_body_item_data.to_dict()
                awarding_body.append(awarding_body_item)

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

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

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        used: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.used, Unset):
            used = []
            for used_item_data in self.used:
                used_item = used_item_data.to_dict()
                used.append(used_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if awarding_body is not UNSET:
            field_dict["awardingBody"] = awarding_body
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if location is not UNSET:
            field_dict["location"] = location
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_assessment_type import DeMathplanMosesEdciAssessmentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _additional_note = d.pop("additionalNote", UNSET)
        additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _additional_note is not UNSET:
            additional_note = []
            for additional_note_item_data in _additional_note:
                additional_note_item = DeMathplanMosesEdciNoteType.from_dict(additional_note_item_data)

                additional_note.append(additional_note_item)

        _awarding_body = d.pop("awardingBody", UNSET)
        awarding_body: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _awarding_body is not UNSET:
            awarding_body = []
            for awarding_body_item_data in _awarding_body:
                awarding_body_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(awarding_body_item_data)

                awarding_body.append(awarding_body_item)

        _date = d.pop("date", UNSET)
        date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_date)

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

        _location = d.pop("location", UNSET)
        location: DeMathplanMosesEdciLocationType | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = DeMathplanMosesEdciLocationType.from_dict(_location)

        _used = d.pop("used", UNSET)
        used: list[DeMathplanMosesEdciAssessmentType] | Unset = UNSET
        if _used is not UNSET:
            used = []
            for used_item_data in _used:
                used_item = DeMathplanMosesEdciAssessmentType.from_dict(used_item_data)

                used.append(used_item)

        de_mathplan_moses_edci_awarding_process_type = cls(
            additional_note=additional_note,
            awarding_body=awarding_body,
            date=date,
            description=description,
            id=id,
            identifier=identifier,
            location=location,
            used=used,
        )

        de_mathplan_moses_edci_awarding_process_type.additional_properties = d
        return de_mathplan_moses_edci_awarding_process_type

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
