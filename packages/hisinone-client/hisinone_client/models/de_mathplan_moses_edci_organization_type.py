from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_contact_point_type import DeMathplanMosesEdciContactPointType
    from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_image_object_type import DeMathplanMosesEdciImageObjectType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_legal_identifier_type import DeMathplanMosesEdciLegalIdentifierType
    from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_organization_type_type import DeMathplanMosesEdciOrganizationTypeType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciOrganizationType")


@_attrs_define
class DeMathplanMosesEdciOrganizationType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        alt_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        contact_point (list[DeMathplanMosesEdciContactPointType] | Unset):
        has_accreditation (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        has_location (list[DeMathplanMosesEdciLocationType] | Unset):
        has_unit (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        homepage (list[DeMathplanMosesEdciDocumentType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        logo (DeMathplanMosesEdciImageObjectType | Unset):
        pref_label (list[DeMathplanMosesEdciTextType] | Unset):
        registration (DeMathplanMosesEdciGenericIdentifierType | Unset):
        tax_identifier (list[DeMathplanMosesEdciLegalIdentifierType] | Unset):
        type_ (list[DeMathplanMosesEdciOrganizationTypeType] | Unset):
        unit_of (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        vat_identifier (list[DeMathplanMosesEdciLegalIdentifierType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    contact_point: list[DeMathplanMosesEdciContactPointType] | Unset = UNSET
    has_accreditation: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    has_location: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
    has_unit: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    homepage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    logo: DeMathplanMosesEdciImageObjectType | Unset = UNSET
    pref_label: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    registration: DeMathplanMosesEdciGenericIdentifierType | Unset = UNSET
    tax_identifier: list[DeMathplanMosesEdciLegalIdentifierType] | Unset = UNSET
    type_: list[DeMathplanMosesEdciOrganizationTypeType] | Unset = UNSET
    unit_of: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    vat_identifier: list[DeMathplanMosesEdciLegalIdentifierType] | Unset = UNSET
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

        contact_point: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contact_point, Unset):
            contact_point = []
            for contact_point_item_data in self.contact_point:
                contact_point_item = contact_point_item_data.to_dict()
                contact_point.append(contact_point_item)

        has_accreditation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_accreditation, Unset):
            has_accreditation = []
            for has_accreditation_item_data in self.has_accreditation:
                has_accreditation_item = has_accreditation_item_data.to_dict()
                has_accreditation.append(has_accreditation_item)

        has_location: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_location, Unset):
            has_location = []
            for has_location_item_data in self.has_location:
                has_location_item = has_location_item_data.to_dict()
                has_location.append(has_location_item)

        has_unit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_unit, Unset):
            has_unit = []
            for has_unit_item_data in self.has_unit:
                has_unit_item = has_unit_item_data.to_dict()
                has_unit.append(has_unit_item)

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

        logo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        pref_label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pref_label, Unset):
            pref_label = []
            for pref_label_item_data in self.pref_label:
                pref_label_item = pref_label_item_data.to_dict()
                pref_label.append(pref_label_item)

        registration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration, Unset):
            registration = self.registration.to_dict()

        tax_identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tax_identifier, Unset):
            tax_identifier = []
            for tax_identifier_item_data in self.tax_identifier:
                tax_identifier_item = tax_identifier_item_data.to_dict()
                tax_identifier.append(tax_identifier_item)

        type_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = []
            for type_item_data in self.type_:
                type_item = type_item_data.to_dict()
                type_.append(type_item)

        unit_of: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit_of, Unset):
            unit_of = self.unit_of.to_dict()

        vat_identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vat_identifier, Unset):
            vat_identifier = []
            for vat_identifier_item_data in self.vat_identifier:
                vat_identifier_item = vat_identifier_item_data.to_dict()
                vat_identifier.append(vat_identifier_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if alt_label is not UNSET:
            field_dict["altLabel"] = alt_label
        if contact_point is not UNSET:
            field_dict["contactPoint"] = contact_point
        if has_accreditation is not UNSET:
            field_dict["hasAccreditation"] = has_accreditation
        if has_location is not UNSET:
            field_dict["hasLocation"] = has_location
        if has_unit is not UNSET:
            field_dict["hasUnit"] = has_unit
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if logo is not UNSET:
            field_dict["logo"] = logo
        if pref_label is not UNSET:
            field_dict["prefLabel"] = pref_label
        if registration is not UNSET:
            field_dict["registration"] = registration
        if tax_identifier is not UNSET:
            field_dict["taxIdentifier"] = tax_identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unit_of is not UNSET:
            field_dict["unitOf"] = unit_of
        if vat_identifier is not UNSET:
            field_dict["vatIdentifier"] = vat_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_contact_point_type import DeMathplanMosesEdciContactPointType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_image_object_type import DeMathplanMosesEdciImageObjectType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_legal_identifier_type import DeMathplanMosesEdciLegalIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_location_type import DeMathplanMosesEdciLocationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_organization_type_type import DeMathplanMosesEdciOrganizationTypeType  # noqa: PLC0415
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

        _contact_point = d.pop("contactPoint", UNSET)
        contact_point: list[DeMathplanMosesEdciContactPointType] | Unset = UNSET
        if _contact_point is not UNSET:
            contact_point = []
            for contact_point_item_data in _contact_point:
                contact_point_item = DeMathplanMosesEdciContactPointType.from_dict(contact_point_item_data)

                contact_point.append(contact_point_item)

        _has_accreditation = d.pop("hasAccreditation", UNSET)
        has_accreditation: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _has_accreditation is not UNSET:
            has_accreditation = []
            for has_accreditation_item_data in _has_accreditation:
                has_accreditation_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(
                    has_accreditation_item_data
                )

                has_accreditation.append(has_accreditation_item)

        _has_location = d.pop("hasLocation", UNSET)
        has_location: list[DeMathplanMosesEdciLocationType] | Unset = UNSET
        if _has_location is not UNSET:
            has_location = []
            for has_location_item_data in _has_location:
                has_location_item = DeMathplanMosesEdciLocationType.from_dict(has_location_item_data)

                has_location.append(has_location_item)

        _has_unit = d.pop("hasUnit", UNSET)
        has_unit: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _has_unit is not UNSET:
            has_unit = []
            for has_unit_item_data in _has_unit:
                has_unit_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(has_unit_item_data)

                has_unit.append(has_unit_item)

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

        _logo = d.pop("logo", UNSET)
        logo: DeMathplanMosesEdciImageObjectType | Unset
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = DeMathplanMosesEdciImageObjectType.from_dict(_logo)

        _pref_label = d.pop("prefLabel", UNSET)
        pref_label: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _pref_label is not UNSET:
            pref_label = []
            for pref_label_item_data in _pref_label:
                pref_label_item = DeMathplanMosesEdciTextType.from_dict(pref_label_item_data)

                pref_label.append(pref_label_item)

        _registration = d.pop("registration", UNSET)
        registration: DeMathplanMosesEdciGenericIdentifierType | Unset
        if isinstance(_registration, Unset):
            registration = UNSET
        else:
            registration = DeMathplanMosesEdciGenericIdentifierType.from_dict(_registration)

        _tax_identifier = d.pop("taxIdentifier", UNSET)
        tax_identifier: list[DeMathplanMosesEdciLegalIdentifierType] | Unset = UNSET
        if _tax_identifier is not UNSET:
            tax_identifier = []
            for tax_identifier_item_data in _tax_identifier:
                tax_identifier_item = DeMathplanMosesEdciLegalIdentifierType.from_dict(tax_identifier_item_data)

                tax_identifier.append(tax_identifier_item)

        _type_ = d.pop("type", UNSET)
        type_: list[DeMathplanMosesEdciOrganizationTypeType] | Unset = UNSET
        if _type_ is not UNSET:
            type_ = []
            for type_item_data in _type_:
                type_item = DeMathplanMosesEdciOrganizationTypeType.from_dict(type_item_data)

                type_.append(type_item)

        _unit_of = d.pop("unitOf", UNSET)
        unit_of: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_unit_of, Unset):
            unit_of = UNSET
        else:
            unit_of = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_unit_of)

        _vat_identifier = d.pop("vatIdentifier", UNSET)
        vat_identifier: list[DeMathplanMosesEdciLegalIdentifierType] | Unset = UNSET
        if _vat_identifier is not UNSET:
            vat_identifier = []
            for vat_identifier_item_data in _vat_identifier:
                vat_identifier_item = DeMathplanMosesEdciLegalIdentifierType.from_dict(vat_identifier_item_data)

                vat_identifier.append(vat_identifier_item)

        de_mathplan_moses_edci_organization_type = cls(
            additional_note=additional_note,
            alt_label=alt_label,
            contact_point=contact_point,
            has_accreditation=has_accreditation,
            has_location=has_location,
            has_unit=has_unit,
            homepage=homepage,
            id=id,
            identifier=identifier,
            logo=logo,
            pref_label=pref_label,
            registration=registration,
            tax_identifier=tax_identifier,
            type_=type_,
            unit_of=unit_of,
            vat_identifier=vat_identifier,
        )

        de_mathplan_moses_edci_organization_type.additional_properties = d
        return de_mathplan_moses_edci_organization_type

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
