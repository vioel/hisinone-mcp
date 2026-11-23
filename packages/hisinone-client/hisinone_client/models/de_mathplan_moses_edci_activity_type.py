from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_restricted_achievements_type import (
        DeMathplanMosesEdciRestrictedAchievementsType,
    )
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_duration import JavaxXmlDatatypeDuration
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciActivityType")


@_attrs_define
class DeMathplanMosesEdciActivityType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        directed_by (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        ended_at_time (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        has_part (list[DeMathplanMosesEdciActivityType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        influenced (list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset):
        location (list[DeMathplanMosesEdciLocationType] | Unset):
        specified_by (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        started_at_time (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        used_learning_opportunity (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        workload (JavaxXmlDatatypeDuration | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    directed_by: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    ended_at_time: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    has_part: list[DeMathplanMosesEdciActivityType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    influenced: list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset = UNSET
    location: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
    specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    started_at_time: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    used_learning_opportunity: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    workload: JavaxXmlDatatypeDuration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        directed_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.directed_by, Unset):
            directed_by = []
            for directed_by_item_data in self.directed_by:
                directed_by_item = directed_by_item_data.to_dict()
                directed_by.append(directed_by_item)

        ended_at_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ended_at_time, Unset):
            ended_at_time = self.ended_at_time.to_dict()

        has_part: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_part, Unset):
            has_part = []
            for has_part_item_data in self.has_part:
                has_part_item = has_part_item_data.to_dict()
                has_part.append(has_part_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        influenced: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.influenced, Unset):
            influenced = []
            for influenced_item_data in self.influenced:
                influenced_item = influenced_item_data.to_dict()
                influenced.append(influenced_item)

        location: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = []
            for location_item_data in self.location:
                location_item = location_item_data.to_dict()
                location.append(location_item)

        specified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specified_by, Unset):
            specified_by = self.specified_by.to_dict()

        started_at_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.started_at_time, Unset):
            started_at_time = self.started_at_time.to_dict()

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        used_learning_opportunity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.used_learning_opportunity, Unset):
            used_learning_opportunity = self.used_learning_opportunity.to_dict()

        workload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workload, Unset):
            workload = self.workload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if description is not UNSET:
            field_dict["description"] = description
        if directed_by is not UNSET:
            field_dict["directedBy"] = directed_by
        if ended_at_time is not UNSET:
            field_dict["endedAtTime"] = ended_at_time
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if influenced is not UNSET:
            field_dict["influenced"] = influenced
        if location is not UNSET:
            field_dict["location"] = location
        if specified_by is not UNSET:
            field_dict["specifiedBy"] = specified_by
        if started_at_time is not UNSET:
            field_dict["startedAtTime"] = started_at_time
        if title is not UNSET:
            field_dict["title"] = title
        if used_learning_opportunity is not UNSET:
            field_dict["usedLearningOpportunity"] = used_learning_opportunity
        if workload is not UNSET:
            field_dict["workload"] = workload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_restricted_achievements_type import (
            DeMathplanMosesEdciRestrictedAchievementsType,  # noqa: PLC0415
        )
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

        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        _directed_by = d.pop("directedBy", UNSET)
        directed_by: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _directed_by is not UNSET:
            directed_by = []
            for directed_by_item_data in _directed_by:
                directed_by_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(directed_by_item_data)

                directed_by.append(directed_by_item)

        _ended_at_time = d.pop("endedAtTime", UNSET)
        ended_at_time: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_ended_at_time, Unset):
            ended_at_time = UNSET
        else:
            ended_at_time = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_ended_at_time)

        _has_part = d.pop("hasPart", UNSET)
        has_part: list[DeMathplanMosesEdciActivityType] | Unset = UNSET
        if _has_part is not UNSET:
            has_part = []
            for has_part_item_data in _has_part:
                has_part_item = DeMathplanMosesEdciActivityType.from_dict(has_part_item_data)

                has_part.append(has_part_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _influenced = d.pop("influenced", UNSET)
        influenced: list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset = UNSET
        if _influenced is not UNSET:
            influenced = []
            for influenced_item_data in _influenced:
                influenced_item = DeMathplanMosesEdciRestrictedAchievementsType.from_dict(influenced_item_data)

                influenced.append(influenced_item)

        _location = d.pop("location", UNSET)
        location: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
        if _location is not UNSET:
            location = []
            for location_item_data in _location:
                location_item = DeMathplanMosesEdciLocationType.from_dict(location_item_data)

                location.append(location_item)

        _specified_by = d.pop("specifiedBy", UNSET)
        specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_specified_by, Unset):
            specified_by = UNSET
        else:
            specified_by = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_specified_by)

        _started_at_time = d.pop("startedAtTime", UNSET)
        started_at_time: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_started_at_time, Unset):
            started_at_time = UNSET
        else:
            started_at_time = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_started_at_time)

        _title = d.pop("title", UNSET)
        title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = DeMathplanMosesEdciTextType.from_dict(title_item_data)

                title.append(title_item)

        _used_learning_opportunity = d.pop("usedLearningOpportunity", UNSET)
        used_learning_opportunity: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_used_learning_opportunity, Unset):
            used_learning_opportunity = UNSET
        else:
            used_learning_opportunity = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_used_learning_opportunity)

        _workload = d.pop("workload", UNSET)
        workload: JavaxXmlDatatypeDuration | Unset
        if isinstance(_workload, Unset):
            workload = UNSET
        else:
            workload = JavaxXmlDatatypeDuration.from_dict(_workload)

        de_mathplan_moses_edci_activity_type = cls(
            additional_note=additional_note,
            description=description,
            directed_by=directed_by,
            ended_at_time=ended_at_time,
            has_part=has_part,
            id=id,
            identifier=identifier,
            influenced=influenced,
            location=location,
            specified_by=specified_by,
            started_at_time=started_at_time,
            title=title,
            used_learning_opportunity=used_learning_opportunity,
            workload=workload,
        )

        de_mathplan_moses_edci_activity_type.additional_properties = d
        return de_mathplan_moses_edci_activity_type

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
