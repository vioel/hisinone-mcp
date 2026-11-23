from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType
    from ..models.de_mathplan_moses_edci_entitlement_specification_type_limit_jurisdiction import (
        DeMathplanMosesEdciEntitlementSpecificationTypeLimitJurisdiction,
    )
    from ..models.de_mathplan_moses_edci_entitlement_specification_type_limit_national_occupation import (
        DeMathplanMosesEdciEntitlementSpecificationTypeLimitNationalOccupation,
    )
    from ..models.de_mathplan_moses_edci_entitlement_specification_type_limit_occupation import (
        DeMathplanMosesEdciEntitlementSpecificationTypeLimitOccupation,
    )
    from ..models.de_mathplan_moses_edci_entitlement_specification_type_status import (
        DeMathplanMosesEdciEntitlementSpecificationTypeStatus,
    )
    from ..models.de_mathplan_moses_edci_entitlement_specification_type_type import (
        DeMathplanMosesEdciEntitlementSpecificationTypeType,
    )
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciEntitlementSpecificationType")


@_attrs_define
class DeMathplanMosesEdciEntitlementSpecificationType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        alt_label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        has_part (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        homepage (list[DeMathplanMosesEdciDocumentType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        limit_jurisdiction (list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitJurisdiction] | Unset):
        limit_national_occupation (list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitNationalOccupation] |
            Unset):
        limit_occupation (list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitOccupation] | Unset):
        limit_organization (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        may_result_from (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        specialization_of (list[DeMathplanMosesEdciGenericIdReferenceType] | Unset):
        status (DeMathplanMosesEdciEntitlementSpecificationTypeStatus | Unset):
        supplementary_doc (list[DeMathplanMosesEdciDocumentType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        type_ (DeMathplanMosesEdciEntitlementSpecificationTypeType | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    alt_label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    has_part: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    homepage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    limit_jurisdiction: list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitJurisdiction] | Unset = UNSET
    limit_national_occupation: list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitNationalOccupation] | Unset = (
        UNSET
    )
    limit_occupation: list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitOccupation] | Unset = UNSET
    limit_organization: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    may_result_from: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    specialization_of: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
    status: DeMathplanMosesEdciEntitlementSpecificationTypeStatus | Unset = UNSET
    supplementary_doc: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    type_: DeMathplanMosesEdciEntitlementSpecificationTypeType | Unset = UNSET
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

        limit_jurisdiction: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_jurisdiction, Unset):
            limit_jurisdiction = []
            for limit_jurisdiction_item_data in self.limit_jurisdiction:
                limit_jurisdiction_item = limit_jurisdiction_item_data.to_dict()
                limit_jurisdiction.append(limit_jurisdiction_item)

        limit_national_occupation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_national_occupation, Unset):
            limit_national_occupation = []
            for limit_national_occupation_item_data in self.limit_national_occupation:
                limit_national_occupation_item = limit_national_occupation_item_data.to_dict()
                limit_national_occupation.append(limit_national_occupation_item)

        limit_occupation: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_occupation, Unset):
            limit_occupation = []
            for limit_occupation_item_data in self.limit_occupation:
                limit_occupation_item = limit_occupation_item_data.to_dict()
                limit_occupation.append(limit_occupation_item)

        limit_organization: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_organization, Unset):
            limit_organization = []
            for limit_organization_item_data in self.limit_organization:
                limit_organization_item = limit_organization_item_data.to_dict()
                limit_organization.append(limit_organization_item)

        may_result_from: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.may_result_from, Unset):
            may_result_from = []
            for may_result_from_item_data in self.may_result_from:
                may_result_from_item = may_result_from_item_data.to_dict()
                may_result_from.append(may_result_from_item)

        specialization_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.specialization_of, Unset):
            specialization_of = []
            for specialization_of_item_data in self.specialization_of:
                specialization_of_item = specialization_of_item_data.to_dict()
                specialization_of.append(specialization_of_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

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

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if alt_label is not UNSET:
            field_dict["altLabel"] = alt_label
        if description is not UNSET:
            field_dict["description"] = description
        if has_part is not UNSET:
            field_dict["hasPart"] = has_part
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if limit_jurisdiction is not UNSET:
            field_dict["limitJurisdiction"] = limit_jurisdiction
        if limit_national_occupation is not UNSET:
            field_dict["limitNationalOccupation"] = limit_national_occupation
        if limit_occupation is not UNSET:
            field_dict["limitOccupation"] = limit_occupation
        if limit_organization is not UNSET:
            field_dict["limitOrganization"] = limit_organization
        if may_result_from is not UNSET:
            field_dict["mayResultFrom"] = may_result_from
        if specialization_of is not UNSET:
            field_dict["specializationOf"] = specialization_of
        if status is not UNSET:
            field_dict["status"] = status
        if supplementary_doc is not UNSET:
            field_dict["supplementaryDoc"] = supplementary_doc
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_entitlement_specification_type_limit_jurisdiction import (
            DeMathplanMosesEdciEntitlementSpecificationTypeLimitJurisdiction,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_entitlement_specification_type_limit_national_occupation import (
            DeMathplanMosesEdciEntitlementSpecificationTypeLimitNationalOccupation,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_entitlement_specification_type_limit_occupation import (
            DeMathplanMosesEdciEntitlementSpecificationTypeLimitOccupation,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_entitlement_specification_type_status import (
            DeMathplanMosesEdciEntitlementSpecificationTypeStatus,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_entitlement_specification_type_type import (
            DeMathplanMosesEdciEntitlementSpecificationTypeType,  # noqa: PLC0415
        )
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

        _limit_jurisdiction = d.pop("limitJurisdiction", UNSET)
        limit_jurisdiction: list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitJurisdiction] | Unset = UNSET
        if _limit_jurisdiction is not UNSET:
            limit_jurisdiction = []
            for limit_jurisdiction_item_data in _limit_jurisdiction:
                limit_jurisdiction_item = DeMathplanMosesEdciEntitlementSpecificationTypeLimitJurisdiction.from_dict(
                    limit_jurisdiction_item_data
                )

                limit_jurisdiction.append(limit_jurisdiction_item)

        _limit_national_occupation = d.pop("limitNationalOccupation", UNSET)
        limit_national_occupation: (
            list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitNationalOccupation] | Unset
        ) = UNSET
        if _limit_national_occupation is not UNSET:
            limit_national_occupation = []
            for limit_national_occupation_item_data in _limit_national_occupation:
                limit_national_occupation_item = (
                    DeMathplanMosesEdciEntitlementSpecificationTypeLimitNationalOccupation.from_dict(
                        limit_national_occupation_item_data
                    )
                )

                limit_national_occupation.append(limit_national_occupation_item)

        _limit_occupation = d.pop("limitOccupation", UNSET)
        limit_occupation: list[DeMathplanMosesEdciEntitlementSpecificationTypeLimitOccupation] | Unset = UNSET
        if _limit_occupation is not UNSET:
            limit_occupation = []
            for limit_occupation_item_data in _limit_occupation:
                limit_occupation_item = DeMathplanMosesEdciEntitlementSpecificationTypeLimitOccupation.from_dict(
                    limit_occupation_item_data
                )

                limit_occupation.append(limit_occupation_item)

        _limit_organization = d.pop("limitOrganization", UNSET)
        limit_organization: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _limit_organization is not UNSET:
            limit_organization = []
            for limit_organization_item_data in _limit_organization:
                limit_organization_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(
                    limit_organization_item_data
                )

                limit_organization.append(limit_organization_item)

        _may_result_from = d.pop("mayResultFrom", UNSET)
        may_result_from: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _may_result_from is not UNSET:
            may_result_from = []
            for may_result_from_item_data in _may_result_from:
                may_result_from_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(may_result_from_item_data)

                may_result_from.append(may_result_from_item)

        _specialization_of = d.pop("specializationOf", UNSET)
        specialization_of: list[DeMathplanMosesEdciGenericIdReferenceType] | Unset = UNSET
        if _specialization_of is not UNSET:
            specialization_of = []
            for specialization_of_item_data in _specialization_of:
                specialization_of_item = DeMathplanMosesEdciGenericIdReferenceType.from_dict(
                    specialization_of_item_data
                )

                specialization_of.append(specialization_of_item)

        _status = d.pop("status", UNSET)
        status: DeMathplanMosesEdciEntitlementSpecificationTypeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeMathplanMosesEdciEntitlementSpecificationTypeStatus.from_dict(_status)

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
        type_: DeMathplanMosesEdciEntitlementSpecificationTypeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DeMathplanMosesEdciEntitlementSpecificationTypeType.from_dict(_type_)

        de_mathplan_moses_edci_entitlement_specification_type = cls(
            additional_note=additional_note,
            alt_label=alt_label,
            description=description,
            has_part=has_part,
            homepage=homepage,
            id=id,
            identifier=identifier,
            limit_jurisdiction=limit_jurisdiction,
            limit_national_occupation=limit_national_occupation,
            limit_occupation=limit_occupation,
            limit_organization=limit_organization,
            may_result_from=may_result_from,
            specialization_of=specialization_of,
            status=status,
            supplementary_doc=supplementary_doc,
            title=title,
            type_=type_,
        )

        de_mathplan_moses_edci_entitlement_specification_type.additional_properties = d
        return de_mathplan_moses_edci_entitlement_specification_type

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
