from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_restricted_achievements_type import (
        DeMathplanMosesEdciRestrictedAchievementsType,
    )
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciEntitlementType")


@_attrs_define
class DeMathplanMosesEdciEntitlementType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        expiry_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        has_part (list[DeMathplanMosesEdciEntitlementType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        issued_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        specified_by (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        was_derived_from (list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    expiry_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    has_part: list[DeMathplanMosesEdciEntitlementType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    specified_by: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    was_derived_from: list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset = UNSET
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

        expiry_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.to_dict()

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

        issued_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.to_dict()

        specified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specified_by, Unset):
            specified_by = self.specified_by.to_dict()

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        was_derived_from: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.was_derived_from, Unset):
            was_derived_from = []
            for was_derived_from_item_data in self.was_derived_from:
                was_derived_from_item = was_derived_from_item_data.to_dict()
                was_derived_from.append(was_derived_from_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if description is not UNSET:
            field_dict["description"] = description
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if specified_by is not UNSET:
            field_dict["specifiedBy"] = specified_by
        if title is not UNSET:
            field_dict["title"] = title
        if was_derived_from is not UNSET:
            field_dict["wasDerivedFrom"] = was_derived_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_restricted_achievements_type import (
            DeMathplanMosesEdciRestrictedAchievementsType,  # noqa: PLC0415
        )
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

        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        _expiry_date = d.pop("expiryDate", UNSET)
        expiry_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_expiry_date)

        _has_part = d.pop("hasPart", UNSET)
        has_part: list[DeMathplanMosesEdciEntitlementType] | Unset = UNSET
        if _has_part is not UNSET:
            has_part = []
            for has_part_item_data in _has_part:
                has_part_item = DeMathplanMosesEdciEntitlementType.from_dict(has_part_item_data)

                has_part.append(has_part_item)

        id = d.pop("id", UNSET)

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

        _was_derived_from = d.pop("wasDerivedFrom", UNSET)
        was_derived_from: list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset = UNSET
        if _was_derived_from is not UNSET:
            was_derived_from = []
            for was_derived_from_item_data in _was_derived_from:
                was_derived_from_item = DeMathplanMosesEdciRestrictedAchievementsType.from_dict(
                    was_derived_from_item_data
                )

                was_derived_from.append(was_derived_from_item)

        de_mathplan_moses_edci_entitlement_type = cls(
            additional_note=additional_note,
            description=description,
            expiry_date=expiry_date,
            has_part=has_part,
            id=id,
            identifier=identifier,
            issued_date=issued_date,
            specified_by=specified_by,
            title=title,
            was_derived_from=was_derived_from,
        )

        de_mathplan_moses_edci_entitlement_type.additional_properties = d
        return de_mathplan_moses_edci_entitlement_type

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
