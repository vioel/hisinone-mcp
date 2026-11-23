from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_achievement_type import DeMathplanMosesEdciAchievementType
    from ..models.de_mathplan_moses_edci_activity_type import DeMathplanMosesEdciActivityType
    from ..models.de_mathplan_moses_edci_agent_type_type import DeMathplanMosesEdciAgentTypeType
    from ..models.de_mathplan_moses_edci_contact_point_type import DeMathplanMosesEdciContactPointType
    from ..models.de_mathplan_moses_edci_entitlement_type import DeMathplanMosesEdciEntitlementType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_legal_identifier_type import DeMathplanMosesEdciLegalIdentifierType
    from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_person_type_citizenship_country import (
        DeMathplanMosesEdciPersonTypeCitizenshipCountry,
    )
    from ..models.de_mathplan_moses_edci_person_type_gender import DeMathplanMosesEdciPersonTypeGender
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciGenericCredentialSubjectType")


@_attrs_define
class DeMathplanMosesEdciGenericCredentialSubjectType:
    """
    Attributes:
        achievements (list[DeMathplanMosesEdciAchievementType] | Unset):
        activities (list[DeMathplanMosesEdciActivityType] | Unset):
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        alt_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        birth_name (list[DeMathplanMosesEdciTextType] | Unset):
        citizenship_country (list[DeMathplanMosesEdciPersonTypeCitizenshipCountry] | Unset):
        contact_point (list[DeMathplanMosesEdciContactPointType] | Unset):
        date_of_birth (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        entitlements (list[DeMathplanMosesEdciEntitlementType] | Unset):
        family_name (list[DeMathplanMosesEdciTextType] | Unset):
        full_name (list[DeMathplanMosesEdciTextType] | Unset):
        gender (DeMathplanMosesEdciPersonTypeGender | Unset):
        given_names (list[DeMathplanMosesEdciTextType] | Unset):
        has_location (list[DeMathplanMosesEdciLocationType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        national_id (DeMathplanMosesEdciLegalIdentifierType | Unset):
        patronymic_name (list[DeMathplanMosesEdciTextType] | Unset):
        place_of_birth (DeMathplanMosesEdciLocationType | Unset):
        pref_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        type_ (list[DeMathplanMosesEdciAgentTypeType] | Unset):
    """

    achievements: list[DeMathplanMosesEdciAchievementType] | Unset = UNSET
    activities: list[DeMathplanMosesEdciActivityType] | Unset = UNSET
    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    birth_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    citizenship_country: list[DeMathplanMosesEdciPersonTypeCitizenshipCountry] | Unset = UNSET
    contact_point: list[DeMathplanMosesEdciContactPointType] | Unset = UNSET
    date_of_birth: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    entitlements: list[DeMathplanMosesEdciEntitlementType] | Unset = UNSET
    family_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    full_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    gender: DeMathplanMosesEdciPersonTypeGender | Unset = UNSET
    given_names: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    has_location: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    national_id: DeMathplanMosesEdciLegalIdentifierType | Unset = UNSET
    patronymic_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    place_of_birth: DeMathplanMosesEdciLocationType | Unset = UNSET
    pref_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    type_: list[DeMathplanMosesEdciAgentTypeType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        achievements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.achievements, Unset):
            achievements = []
            for achievements_item_data in self.achievements:
                achievements_item = achievements_item_data.to_dict()
                achievements.append(achievements_item)

        activities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activities, Unset):
            activities = []
            for activities_item_data in self.activities:
                activities_item = activities_item_data.to_dict()
                activities.append(activities_item)

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

        birth_name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.birth_name, Unset):
            birth_name = []
            for birth_name_item_data in self.birth_name:
                birth_name_item = birth_name_item_data.to_dict()
                birth_name.append(birth_name_item)

        citizenship_country: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.citizenship_country, Unset):
            citizenship_country = []
            for citizenship_country_item_data in self.citizenship_country:
                citizenship_country_item = citizenship_country_item_data.to_dict()
                citizenship_country.append(citizenship_country_item)

        contact_point: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contact_point, Unset):
            contact_point = []
            for contact_point_item_data in self.contact_point:
                contact_point_item = contact_point_item_data.to_dict()
                contact_point.append(contact_point_item)

        date_of_birth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.to_dict()

        entitlements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = []
            for entitlements_item_data in self.entitlements:
                entitlements_item = entitlements_item_data.to_dict()
                entitlements.append(entitlements_item)

        family_name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.family_name, Unset):
            family_name = []
            for family_name_item_data in self.family_name:
                family_name_item = family_name_item_data.to_dict()
                family_name.append(family_name_item)

        full_name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.full_name, Unset):
            full_name = []
            for full_name_item_data in self.full_name:
                full_name_item = full_name_item_data.to_dict()
                full_name.append(full_name_item)

        gender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        given_names: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.given_names, Unset):
            given_names = []
            for given_names_item_data in self.given_names:
                given_names_item = given_names_item_data.to_dict()
                given_names.append(given_names_item)

        has_location: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_location, Unset):
            has_location = []
            for has_location_item_data in self.has_location:
                has_location_item = has_location_item_data.to_dict()
                has_location.append(has_location_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        national_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.national_id, Unset):
            national_id = self.national_id.to_dict()

        patronymic_name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.patronymic_name, Unset):
            patronymic_name = []
            for patronymic_name_item_data in self.patronymic_name:
                patronymic_name_item = patronymic_name_item_data.to_dict()
                patronymic_name.append(patronymic_name_item)

        place_of_birth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.place_of_birth, Unset):
            place_of_birth = self.place_of_birth.to_dict()

        pref_label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pref_label, Unset):
            pref_label = []
            for pref_label_item_data in self.pref_label:
                pref_label_item = pref_label_item_data.to_dict()
                pref_label.append(pref_label_item)

        type_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item = type_item_data.to_dict()
                type_.append(type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if achievements is not UNSET:
            field_dict["achievements"] = achievements
        if activities is not UNSET:
            field_dict["activities"] = activities
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if alt_label is not UNSET:
            field_dict["altLabel"] = alt_label
        if birth_name is not UNSET:
            field_dict["birthName"] = birth_name
        if citizenship_country is not UNSET:
            field_dict["citizenshipCountry"] = citizenship_country
        if contact_point is not UNSET:
            field_dict["contactPoint"] = contact_point
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if given_names is not UNSET:
            field_dict["givenNames"] = given_names
        if has_location is not UNSET:
            field_dict["hasLocation"] = has_location
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if national_id is not UNSET:
            field_dict["nationalId"] = national_id
        if patronymic_name is not UNSET:
            field_dict["patronymicName"] = patronymic_name
        if place_of_birth is not UNSET:
            field_dict["placeOfBirth"] = place_of_birth
        if pref_label is not UNSET:
            field_dict["prefLabel"] = pref_label
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_achievement_type import DeMathplanMosesEdciAchievementType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_activity_type import DeMathplanMosesEdciActivityType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_agent_type_type import DeMathplanMosesEdciAgentTypeType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_contact_point_type import DeMathplanMosesEdciContactPointType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_entitlement_type import DeMathplanMosesEdciEntitlementType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_legal_identifier_type import DeMathplanMosesEdciLegalIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_person_type_citizenship_country import (
            DeMathplanMosesEdciPersonTypeCitizenshipCountry,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_person_type_gender import DeMathplanMosesEdciPersonTypeGender  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _achievements = d.pop("achievements", UNSET)
        achievements: list[DeMathplanMosesEdciAchievementType] | Unset = UNSET
        if _achievements is not UNSET:
            achievements = []
            for achievements_item_data in _achievements:
                achievements_item = DeMathplanMosesEdciAchievementType.from_dict(achievements_item_data)

                achievements.append(achievements_item)

        _activities = d.pop("activities", UNSET)
        activities: list[DeMathplanMosesEdciActivityType] | Unset = UNSET
        if _activities is not UNSET:
            activities = []
            for activities_item_data in _activities:
                activities_item = DeMathplanMosesEdciActivityType.from_dict(activities_item_data)

                activities.append(activities_item)

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

        _birth_name = d.pop("birthName", UNSET)
        birth_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _birth_name is not UNSET:
            birth_name = []
            for birth_name_item_data in _birth_name:
                birth_name_item = DeMathplanMosesEdciTextType.from_dict(birth_name_item_data)

                birth_name.append(birth_name_item)

        _citizenship_country = d.pop("citizenshipCountry", UNSET)
        citizenship_country: list[DeMathplanMosesEdciPersonTypeCitizenshipCountry] | Unset = UNSET
        if _citizenship_country is not UNSET:
            citizenship_country = []
            for citizenship_country_item_data in _citizenship_country:
                citizenship_country_item = DeMathplanMosesEdciPersonTypeCitizenshipCountry.from_dict(
                    citizenship_country_item_data
                )

                citizenship_country.append(citizenship_country_item)

        _contact_point = d.pop("contactPoint", UNSET)
        contact_point: list[DeMathplanMosesEdciContactPointType] | Unset = UNSET
        if _contact_point is not UNSET:
            contact_point = []
            for contact_point_item_data in _contact_point:
                contact_point_item = DeMathplanMosesEdciContactPointType.from_dict(contact_point_item_data)

                contact_point.append(contact_point_item)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_date_of_birth)

        _entitlements = d.pop("entitlements", UNSET)
        entitlements: list[DeMathplanMosesEdciEntitlementType] | Unset = UNSET
        if _entitlements is not UNSET:
            entitlements = []
            for entitlements_item_data in _entitlements:
                entitlements_item = DeMathplanMosesEdciEntitlementType.from_dict(entitlements_item_data)

                entitlements.append(entitlements_item)

        _family_name = d.pop("familyName", UNSET)
        family_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _family_name is not UNSET:
            family_name = []
            for family_name_item_data in _family_name:
                family_name_item = DeMathplanMosesEdciTextType.from_dict(family_name_item_data)

                family_name.append(family_name_item)

        _full_name = d.pop("fullName", UNSET)
        full_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _full_name is not UNSET:
            full_name = []
            for full_name_item_data in _full_name:
                full_name_item = DeMathplanMosesEdciTextType.from_dict(full_name_item_data)

                full_name.append(full_name_item)

        _gender = d.pop("gender", UNSET)
        gender: DeMathplanMosesEdciPersonTypeGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = DeMathplanMosesEdciPersonTypeGender.from_dict(_gender)

        _given_names = d.pop("givenNames", UNSET)
        given_names: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _given_names is not UNSET:
            given_names = []
            for given_names_item_data in _given_names:
                given_names_item = DeMathplanMosesEdciTextType.from_dict(given_names_item_data)

                given_names.append(given_names_item)

        _has_location = d.pop("hasLocation", UNSET)
        has_location: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
        if _has_location is not UNSET:
            has_location = []
            for has_location_item_data in _has_location:
                has_location_item = DeMathplanMosesEdciLocationType.from_dict(has_location_item_data)

                has_location.append(has_location_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _national_id = d.pop("nationalId", UNSET)
        national_id: DeMathplanMosesEdciLegalIdentifierType | Unset
        if isinstance(_national_id, Unset):
            national_id = UNSET
        else:
            national_id = DeMathplanMosesEdciLegalIdentifierType.from_dict(_national_id)

        _patronymic_name = d.pop("patronymicName", UNSET)
        patronymic_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _patronymic_name is not UNSET:
            patronymic_name = []
            for patronymic_name_item_data in _patronymic_name:
                patronymic_name_item = DeMathplanMosesEdciTextType.from_dict(patronymic_name_item_data)

                patronymic_name.append(patronymic_name_item)

        _place_of_birth = d.pop("placeOfBirth", UNSET)
        place_of_birth: DeMathplanMosesEdciLocationType | Unset
        if isinstance(_place_of_birth, Unset):
            place_of_birth = UNSET
        else:
            place_of_birth = DeMathplanMosesEdciLocationType.from_dict(_place_of_birth)

        _pref_label = d.pop("prefLabel", UNSET)
        pref_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _pref_label is not UNSET:
            pref_label = []
            for pref_label_item_data in _pref_label:
                pref_label_item = DeMathplanMosesEdciLanguageStringType.from_dict(pref_label_item_data)

                pref_label.append(pref_label_item)

        _type_ = d.pop("type", UNSET)
        type_: list[DeMathplanMosesEdciAgentTypeType] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = DeMathplanMosesEdciAgentTypeType.from_dict(type_item_data)

                type_.append(type_item)

        de_mathplan_moses_edci_generic_credential_subject_type = cls(
            achievements=achievements,
            activities=activities,
            additional_note=additional_note,
            alt_label=alt_label,
            birth_name=birth_name,
            citizenship_country=citizenship_country,
            contact_point=contact_point,
            date_of_birth=date_of_birth,
            entitlements=entitlements,
            family_name=family_name,
            full_name=full_name,
            gender=gender,
            given_names=given_names,
            has_location=has_location,
            id=id,
            identifier=identifier,
            national_id=national_id,
            patronymic_name=patronymic_name,
            place_of_birth=place_of_birth,
            pref_label=pref_label,
            type_=type_,
        )

        de_mathplan_moses_edci_generic_credential_subject_type.additional_properties = d
        return de_mathplan_moses_edci_generic_credential_subject_type

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
