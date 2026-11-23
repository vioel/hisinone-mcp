from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_activity_type import DeMathplanMosesEdciActivityType
    from ..models.de_mathplan_moses_edci_assessment_type import DeMathplanMosesEdciAssessmentType
    from ..models.de_mathplan_moses_edci_entitlement_type import DeMathplanMosesEdciEntitlementType
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_restricted_achievements_type import (
        DeMathplanMosesEdciRestrictedAchievementsType,
    )
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciAchievementType")


@_attrs_define
class DeMathplanMosesEdciAchievementType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        entitles_to (list[DeMathplanMosesEdciEntitlementType] | Unset):
        has_part (list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        was_awarded_by (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        was_derived_from (list[DeMathplanMosesEdciAssessmentType] | Unset):
        was_influenced_by (list[DeMathplanMosesEdciActivityType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    entitles_to: list[DeMathplanMosesEdciEntitlementType] | Unset = UNSET
    has_part: list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    was_awarded_by: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    was_derived_from: list[DeMathplanMosesEdciAssessmentType] | Unset = UNSET
    was_influenced_by: list[DeMathplanMosesEdciActivityType] | Unset = UNSET
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

        entitles_to: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entitles_to, Unset):
            entitles_to = []
            for entitles_to_item_data in self.entitles_to:
                entitles_to_item = entitles_to_item_data.to_dict()
                entitles_to.append(entitles_to_item)

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

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        was_awarded_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.was_awarded_by, Unset):
            was_awarded_by = self.was_awarded_by.to_dict()

        was_derived_from: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.was_derived_from, Unset):
            was_derived_from = []
            for was_derived_from_item_data in self.was_derived_from:
                was_derived_from_item = was_derived_from_item_data.to_dict()
                was_derived_from.append(was_derived_from_item)

        was_influenced_by: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.was_influenced_by, Unset):
            was_influenced_by = []
            for was_influenced_by_item_data in self.was_influenced_by:
                was_influenced_by_item = was_influenced_by_item_data.to_dict()
                was_influenced_by.append(was_influenced_by_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if description is not UNSET:
            field_dict["description"] = description
        if entitles_to is not UNSET:
            field_dict["entitlesTo"] = entitles_to
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if title is not UNSET:
            field_dict["title"] = title
        if was_awarded_by is not UNSET:
            field_dict["wasAwardedBy"] = was_awarded_by
        if was_derived_from is not UNSET:
            field_dict["wasDerivedFrom"] = was_derived_from
        if was_influenced_by is not UNSET:
            field_dict["wasInfluencedBy"] = was_influenced_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_activity_type import DeMathplanMosesEdciActivityType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_assessment_type import DeMathplanMosesEdciAssessmentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_entitlement_type import DeMathplanMosesEdciEntitlementType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_restricted_achievements_type import (
            DeMathplanMosesEdciRestrictedAchievementsType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

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

        _entitles_to = d.pop("entitlesTo", UNSET)
        entitles_to: list[DeMathplanMosesEdciEntitlementType] | Unset = UNSET
        if _entitles_to is not UNSET:
            entitles_to = []
            for entitles_to_item_data in _entitles_to:
                entitles_to_item = DeMathplanMosesEdciEntitlementType.from_dict(entitles_to_item_data)

                entitles_to.append(entitles_to_item)

        _has_part = d.pop("hasPart", UNSET)
        has_part: list[DeMathplanMosesEdciRestrictedAchievementsType] | Unset = UNSET
        if _has_part is not UNSET:
            has_part = []
            for has_part_item_data in _has_part:
                has_part_item = DeMathplanMosesEdciRestrictedAchievementsType.from_dict(has_part_item_data)

                has_part.append(has_part_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _title = d.pop("title", UNSET)
        title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = DeMathplanMosesEdciTextType.from_dict(title_item_data)

                title.append(title_item)

        _was_awarded_by = d.pop("wasAwardedBy", UNSET)
        was_awarded_by: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_was_awarded_by, Unset):
            was_awarded_by = UNSET
        else:
            was_awarded_by = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_was_awarded_by)

        _was_derived_from = d.pop("wasDerivedFrom", UNSET)
        was_derived_from: list[DeMathplanMosesEdciAssessmentType] | Unset = UNSET
        if _was_derived_from is not UNSET:
            was_derived_from = []
            for was_derived_from_item_data in _was_derived_from:
                was_derived_from_item = DeMathplanMosesEdciAssessmentType.from_dict(was_derived_from_item_data)

                was_derived_from.append(was_derived_from_item)

        _was_influenced_by = d.pop("wasInfluencedBy", UNSET)
        was_influenced_by: list[DeMathplanMosesEdciActivityType] | Unset = UNSET
        if _was_influenced_by is not UNSET:
            was_influenced_by = []
            for was_influenced_by_item_data in _was_influenced_by:
                was_influenced_by_item = DeMathplanMosesEdciActivityType.from_dict(was_influenced_by_item_data)

                was_influenced_by.append(was_influenced_by_item)

        de_mathplan_moses_edci_achievement_type = cls(
            additional_note=additional_note,
            description=description,
            entitles_to=entitles_to,
            has_part=has_part,
            id=id,
            identifier=identifier,
            title=title,
            was_awarded_by=was_awarded_by,
            was_derived_from=was_derived_from,
            was_influenced_by=was_influenced_by,
        )

        de_mathplan_moses_edci_achievement_type.additional_properties = d
        return de_mathplan_moses_edci_achievement_type

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
