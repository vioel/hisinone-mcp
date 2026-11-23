from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_accreditation_type_limit_eqf_level import (
        DeMathplanMosesEdciAccreditationTypeLimitEQFLevel,
    )
    from ..models.de_mathplan_moses_edci_accreditation_type_limit_field import (
        DeMathplanMosesEdciAccreditationTypeLimitField,
    )
    from ..models.de_mathplan_moses_edci_accreditation_type_limit_jurisdiction import (
        DeMathplanMosesEdciAccreditationTypeLimitJurisdiction,
    )
    from ..models.de_mathplan_moses_edci_accreditation_type_type import DeMathplanMosesEdciAccreditationTypeType
    from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType
    from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_text_score_type import DeMathplanMosesEdciTextScoreType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciAccreditationType")


@_attrs_define
class DeMathplanMosesEdciAccreditationType:
    """
    Attributes:
        accrediting_agent (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        decision (DeMathplanMosesEdciTextScoreType | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
        expiry_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        homepage (list[DeMathplanMosesEdciDocumentType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        issued_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        landingpage (list[DeMathplanMosesEdciDocumentType] | Unset):
        limit_eqf_level (list[DeMathplanMosesEdciAccreditationTypeLimitEQFLevel] | Unset):
        limit_field (list[DeMathplanMosesEdciAccreditationTypeLimitField] | Unset):
        limit_jurisdiction (list[DeMathplanMosesEdciAccreditationTypeLimitJurisdiction] | Unset):
        limit_qualification (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        organization (DeMathplanMosesEdciGenericIdReferenceType | Unset):
        report (DeMathplanMosesEdciDocumentType | Unset):
        review_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        supplementary_doc (list[DeMathplanMosesEdciDocumentType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        type_ (DeMathplanMosesEdciAccreditationTypeType | Unset):
    """

    accrediting_agent: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    decision: DeMathplanMosesEdciTextScoreType | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    expiry_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    homepage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    landingpage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    limit_eqf_level: list[DeMathplanMosesEdciAccreditationTypeLimitEQFLevel] | Unset = UNSET
    limit_field: list[DeMathplanMosesEdciAccreditationTypeLimitField] | Unset = UNSET
    limit_jurisdiction: list[DeMathplanMosesEdciAccreditationTypeLimitJurisdiction] | Unset = UNSET
    limit_qualification: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    organization: DeMathplanMosesEdciGenericIdReferenceType | Unset = UNSET
    report: DeMathplanMosesEdciDocumentType | Unset = UNSET
    review_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    supplementary_doc: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    type_: DeMathplanMosesEdciAccreditationTypeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        accrediting_agent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accrediting_agent, Unset):
            accrediting_agent = self.accrediting_agent.to_dict()

        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        decision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.to_dict()

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        expiry_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiry_date, Unset):
            expiry_date = self.expiry_date.to_dict()

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

        issued_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.to_dict()

        landingpage: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.landingpage, Unset):
            landingpage = []
            for landingpage_item_data in self.landingpage:
                landingpage_item = landingpage_item_data.to_dict()
                landingpage.append(landingpage_item)

        limit_eqf_level: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_eqf_level, Unset):
            limit_eqf_level = []
            for limit_eqf_level_item_data in self.limit_eqf_level:
                limit_eqf_level_item = limit_eqf_level_item_data.to_dict()
                limit_eqf_level.append(limit_eqf_level_item)

        limit_field: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_field, Unset):
            limit_field = []
            for limit_field_item_data in self.limit_field:
                limit_field_item = limit_field_item_data.to_dict()
                limit_field.append(limit_field_item)

        limit_jurisdiction: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_jurisdiction, Unset):
            limit_jurisdiction = []
            for limit_jurisdiction_item_data in self.limit_jurisdiction:
                limit_jurisdiction_item = limit_jurisdiction_item_data.to_dict()
                limit_jurisdiction.append(limit_jurisdiction_item)

        limit_qualification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit_qualification, Unset):
            limit_qualification = self.limit_qualification.to_dict()

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        review_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.review_date, Unset):
            review_date = self.review_date.to_dict()

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
        if accrediting_agent is not UNSET:
            field_dict["accreditingAgent"] = accrediting_agent
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if decision is not UNSET:
            field_dict["decision"] = decision
        if description is not UNSET:
            field_dict["description"] = description
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if landingpage is not UNSET:
            field_dict["landingpage"] = landingpage
        if limit_eqf_level is not UNSET:
            field_dict["limitEQFLevel"] = limit_eqf_level
        if limit_field is not UNSET:
            field_dict["limitField"] = limit_field
        if limit_jurisdiction is not UNSET:
            field_dict["limitJurisdiction"] = limit_jurisdiction
        if limit_qualification is not UNSET:
            field_dict["limitQualification"] = limit_qualification
        if organization is not UNSET:
            field_dict["organization"] = organization
        if report is not UNSET:
            field_dict["report"] = report
        if review_date is not UNSET:
            field_dict["reviewDate"] = review_date
        if supplementary_doc is not UNSET:
            field_dict["supplementaryDoc"] = supplementary_doc
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_accreditation_type_limit_eqf_level import (
            DeMathplanMosesEdciAccreditationTypeLimitEQFLevel,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_accreditation_type_limit_field import (
            DeMathplanMosesEdciAccreditationTypeLimitField,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_accreditation_type_limit_jurisdiction import (
            DeMathplanMosesEdciAccreditationTypeLimitJurisdiction,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_accreditation_type_type import DeMathplanMosesEdciAccreditationTypeType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_document_type import DeMathplanMosesEdciDocumentType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_id_reference_type import DeMathplanMosesEdciGenericIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_score_type import DeMathplanMosesEdciTextScoreType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _accrediting_agent = d.pop("accreditingAgent", UNSET)
        accrediting_agent: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_accrediting_agent, Unset):
            accrediting_agent = UNSET
        else:
            accrediting_agent = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_accrediting_agent)

        _additional_note = d.pop("additionalNote", UNSET)
        additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _additional_note is not UNSET:
            additional_note = []
            for additional_note_item_data in _additional_note:
                additional_note_item = DeMathplanMosesEdciNoteType.from_dict(additional_note_item_data)

                additional_note.append(additional_note_item)

        _decision = d.pop("decision", UNSET)
        decision: DeMathplanMosesEdciTextScoreType | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = DeMathplanMosesEdciTextScoreType.from_dict(_decision)

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

        _issued_date = d.pop("issuedDate", UNSET)
        issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_issued_date)

        _landingpage = d.pop("landingpage", UNSET)
        landingpage: list[DeMathplanMosesEdciDocumentType] | Unset = UNSET
        if _landingpage is not UNSET:
            landingpage = []
            for landingpage_item_data in _landingpage:
                landingpage_item = DeMathplanMosesEdciDocumentType.from_dict(landingpage_item_data)

                landingpage.append(landingpage_item)

        _limit_eqf_level = d.pop("limitEQFLevel", UNSET)
        limit_eqf_level: list[DeMathplanMosesEdciAccreditationTypeLimitEQFLevel] | Unset = UNSET
        if _limit_eqf_level is not UNSET:
            limit_eqf_level = []
            for limit_eqf_level_item_data in _limit_eqf_level:
                limit_eqf_level_item = DeMathplanMosesEdciAccreditationTypeLimitEQFLevel.from_dict(
                    limit_eqf_level_item_data
                )

                limit_eqf_level.append(limit_eqf_level_item)

        _limit_field = d.pop("limitField", UNSET)
        limit_field: list[DeMathplanMosesEdciAccreditationTypeLimitField] | Unset = UNSET
        if _limit_field is not UNSET:
            limit_field = []
            for limit_field_item_data in _limit_field:
                limit_field_item = DeMathplanMosesEdciAccreditationTypeLimitField.from_dict(limit_field_item_data)

                limit_field.append(limit_field_item)

        _limit_jurisdiction = d.pop("limitJurisdiction", UNSET)
        limit_jurisdiction: list[DeMathplanMosesEdciAccreditationTypeLimitJurisdiction] | Unset = UNSET
        if _limit_jurisdiction is not UNSET:
            limit_jurisdiction = []
            for limit_jurisdiction_item_data in _limit_jurisdiction:
                limit_jurisdiction_item = DeMathplanMosesEdciAccreditationTypeLimitJurisdiction.from_dict(
                    limit_jurisdiction_item_data
                )

                limit_jurisdiction.append(limit_jurisdiction_item)

        _limit_qualification = d.pop("limitQualification", UNSET)
        limit_qualification: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_limit_qualification, Unset):
            limit_qualification = UNSET
        else:
            limit_qualification = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_limit_qualification)

        _organization = d.pop("organization", UNSET)
        organization: DeMathplanMosesEdciGenericIdReferenceType | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = DeMathplanMosesEdciGenericIdReferenceType.from_dict(_organization)

        _report = d.pop("report", UNSET)
        report: DeMathplanMosesEdciDocumentType | Unset
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = DeMathplanMosesEdciDocumentType.from_dict(_report)

        _review_date = d.pop("reviewDate", UNSET)
        review_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_review_date, Unset):
            review_date = UNSET
        else:
            review_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_review_date)

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
        type_: DeMathplanMosesEdciAccreditationTypeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DeMathplanMosesEdciAccreditationTypeType.from_dict(_type_)

        de_mathplan_moses_edci_accreditation_type = cls(
            accrediting_agent=accrediting_agent,
            additional_note=additional_note,
            decision=decision,
            description=description,
            expiry_date=expiry_date,
            homepage=homepage,
            id=id,
            identifier=identifier,
            issued_date=issued_date,
            landingpage=landingpage,
            limit_eqf_level=limit_eqf_level,
            limit_field=limit_field,
            limit_jurisdiction=limit_jurisdiction,
            limit_qualification=limit_qualification,
            organization=organization,
            report=report,
            review_date=review_date,
            supplementary_doc=supplementary_doc,
            title=title,
            type_=type_,
        )

        de_mathplan_moses_edci_accreditation_type.additional_properties = d
        return de_mathplan_moses_edci_accreditation_type

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
