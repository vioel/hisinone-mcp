from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_accreditation_type import DeMathplanMosesEdciAccreditationType
    from ..models.de_mathplan_moses_edci_assessment_specification_type import (
        DeMathplanMosesEdciAssessmentSpecificationType,
    )
    from ..models.de_mathplan_moses_edci_awarding_process_type import DeMathplanMosesEdciAwardingProcessType
    from ..models.de_mathplan_moses_edci_child_credentials_type import DeMathplanMosesEdciChildCredentialsType
    from ..models.de_mathplan_moses_edci_credential_type_type import DeMathplanMosesEdciCredentialTypeType
    from ..models.de_mathplan_moses_edci_display_parameters_type import DeMathplanMosesEdciDisplayParametersType
    from ..models.de_mathplan_moses_edci_entitlement_specification_type import (
        DeMathplanMosesEdciEntitlementSpecificationType,
    )
    from ..models.de_mathplan_moses_edci_europass_credential_type_proof import (
        DeMathplanMosesEdciEuropassCredentialTypeProof,
    )
    from ..models.de_mathplan_moses_edci_generic_credential_subject_type import (
        DeMathplanMosesEdciGenericCredentialSubjectType,
    )
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_generic_learning_outcome_type import (
        DeMathplanMosesEdciGenericLearningOutcomeType,
    )
    from ..models.de_mathplan_moses_edci_id_reference_type import DeMathplanMosesEdciIdReferenceType
    from ..models.de_mathplan_moses_edci_learning_activity_specification_type import (
        DeMathplanMosesEdciLearningActivitySpecificationType,
    )
    from ..models.de_mathplan_moses_edci_learning_opportunity_type import DeMathplanMosesEdciLearningOpportunityType
    from ..models.de_mathplan_moses_edci_learning_specification_references_type import (
        DeMathplanMosesEdciLearningSpecificationReferencesType,
    )
    from ..models.de_mathplan_moses_edci_media_object_type import DeMathplanMosesEdciMediaObjectType
    from ..models.de_mathplan_moses_edci_organization_type import DeMathplanMosesEdciOrganizationType
    from ..models.de_mathplan_moses_edci_scoring_scheme_type import DeMathplanMosesEdciScoringSchemeType
    from ..models.de_mathplan_moses_edci_semantic_framework_type import DeMathplanMosesEdciSemanticFrameworkType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciEuropassCredentialType")


@_attrs_define
class DeMathplanMosesEdciEuropassCredentialType:
    """
    Attributes:
        accreditation_references (list[DeMathplanMosesEdciAccreditationType] | Unset):
        agent_references (list[DeMathplanMosesEdciOrganizationType] | Unset):
        assessment_specification_references (list[DeMathplanMosesEdciAssessmentSpecificationType] | Unset):
        attachment_list (list[DeMathplanMosesEdciMediaObjectType] | Unset):
        awarding_process_references (list[DeMathplanMosesEdciAwardingProcessType] | Unset):
        child_credentials (list[DeMathplanMosesEdciChildCredentialsType] | Unset):
        credential_subject (DeMathplanMosesEdciGenericCredentialSubjectType | Unset):
        description (list[DeMathplanMosesEdciTextType] | Unset):
        display_parameters (DeMathplanMosesEdciDisplayParametersType | Unset):
        entitlement_specification_references (list[DeMathplanMosesEdciEntitlementSpecificationType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        issued (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        issuer (DeMathplanMosesEdciIdReferenceType | Unset):
        learning_activity_specification_references (list[DeMathplanMosesEdciLearningActivitySpecificationType] | Unset):
        learning_opportunity_references (list[DeMathplanMosesEdciLearningOpportunityType] | Unset):
        learning_outcome_references (list[DeMathplanMosesEdciGenericLearningOutcomeType] | Unset):
        learning_specification_references (DeMathplanMosesEdciLearningSpecificationReferencesType | Unset):
        proof (DeMathplanMosesEdciEuropassCredentialTypeProof | Unset):
        scoring_scheme_references (list[DeMathplanMosesEdciScoringSchemeType] | Unset):
        semantic_framework_references (list[DeMathplanMosesEdciSemanticFrameworkType] | Unset):
        title (list[DeMathplanMosesEdciTextType] | Unset):
        type_ (DeMathplanMosesEdciCredentialTypeType | Unset):
        valid_from (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        valid_until (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        xsd_version (str | Unset):
    """

    accreditation_references: list[DeMathplanMosesEdciAccreditationType] | Unset = UNSET
    agent_references: list[DeMathplanMosesEdciOrganizationType] | Unset = UNSET
    assessment_specification_references: list[DeMathplanMosesEdciAssessmentSpecificationType] | Unset = UNSET
    attachment_list: list[DeMathplanMosesEdciMediaObjectType] | Unset = UNSET
    awarding_process_references: list[DeMathplanMosesEdciAwardingProcessType] | Unset = UNSET
    child_credentials: list[DeMathplanMosesEdciChildCredentialsType] | Unset = UNSET
    credential_subject: DeMathplanMosesEdciGenericCredentialSubjectType | Unset = UNSET
    description: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    display_parameters: DeMathplanMosesEdciDisplayParametersType | Unset = UNSET
    entitlement_specification_references: list[DeMathplanMosesEdciEntitlementSpecificationType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    issued: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    issuer: DeMathplanMosesEdciIdReferenceType | Unset = UNSET
    learning_activity_specification_references: list[DeMathplanMosesEdciLearningActivitySpecificationType] | Unset = (
        UNSET
    )
    learning_opportunity_references: list[DeMathplanMosesEdciLearningOpportunityType] | Unset = UNSET
    learning_outcome_references: list[DeMathplanMosesEdciGenericLearningOutcomeType] | Unset = UNSET
    learning_specification_references: DeMathplanMosesEdciLearningSpecificationReferencesType | Unset = UNSET
    proof: DeMathplanMosesEdciEuropassCredentialTypeProof | Unset = UNSET
    scoring_scheme_references: list[DeMathplanMosesEdciScoringSchemeType] | Unset = UNSET
    semantic_framework_references: list[DeMathplanMosesEdciSemanticFrameworkType] | Unset = UNSET
    title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    type_: DeMathplanMosesEdciCredentialTypeType | Unset = UNSET
    valid_from: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    valid_until: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    xsd_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        accreditation_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accreditation_references, Unset):
            accreditation_references = []
            for accreditation_references_item_data in self.accreditation_references:
                accreditation_references_item = accreditation_references_item_data.to_dict()
                accreditation_references.append(accreditation_references_item)

        agent_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agent_references, Unset):
            agent_references = []
            for agent_references_item_data in self.agent_references:
                agent_references_item = agent_references_item_data.to_dict()
                agent_references.append(agent_references_item)

        assessment_specification_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assessment_specification_references, Unset):
            assessment_specification_references = []
            for assessment_specification_references_item_data in self.assessment_specification_references:
                assessment_specification_references_item = assessment_specification_references_item_data.to_dict()
                assessment_specification_references.append(assessment_specification_references_item)

        attachment_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachment_list, Unset):
            attachment_list = []
            for attachment_list_item_data in self.attachment_list:
                attachment_list_item = attachment_list_item_data.to_dict()
                attachment_list.append(attachment_list_item)

        awarding_process_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.awarding_process_references, Unset):
            awarding_process_references = []
            for awarding_process_references_item_data in self.awarding_process_references:
                awarding_process_references_item = awarding_process_references_item_data.to_dict()
                awarding_process_references.append(awarding_process_references_item)

        child_credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_credentials, Unset):
            child_credentials = []
            for child_credentials_item_data in self.child_credentials:
                child_credentials_item = child_credentials_item_data.to_dict()
                child_credentials.append(child_credentials_item)

        credential_subject: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credential_subject, Unset):
            credential_subject = self.credential_subject.to_dict()

        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        display_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.display_parameters, Unset):
            display_parameters = self.display_parameters.to_dict()

        entitlement_specification_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entitlement_specification_references, Unset):
            entitlement_specification_references = []
            for entitlement_specification_references_item_data in self.entitlement_specification_references:
                entitlement_specification_references_item = entitlement_specification_references_item_data.to_dict()
                entitlement_specification_references.append(entitlement_specification_references_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        issued: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issued, Unset):
            issued = self.issued.to_dict()

        issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issuer, Unset):
            issuer = self.issuer.to_dict()

        learning_activity_specification_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.learning_activity_specification_references, Unset):
            learning_activity_specification_references = []
            for learning_activity_specification_references_item_data in self.learning_activity_specification_references:
                learning_activity_specification_references_item = (
                    learning_activity_specification_references_item_data.to_dict()
                )
                learning_activity_specification_references.append(learning_activity_specification_references_item)

        learning_opportunity_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.learning_opportunity_references, Unset):
            learning_opportunity_references = []
            for learning_opportunity_references_item_data in self.learning_opportunity_references:
                learning_opportunity_references_item = learning_opportunity_references_item_data.to_dict()
                learning_opportunity_references.append(learning_opportunity_references_item)

        learning_outcome_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.learning_outcome_references, Unset):
            learning_outcome_references = []
            for learning_outcome_references_item_data in self.learning_outcome_references:
                learning_outcome_references_item = learning_outcome_references_item_data.to_dict()
                learning_outcome_references.append(learning_outcome_references_item)

        learning_specification_references: dict[str, Any] | Unset = UNSET
        if not isinstance(self.learning_specification_references, Unset):
            learning_specification_references = self.learning_specification_references.to_dict()

        proof: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proof, Unset):
            proof = self.proof.to_dict()

        scoring_scheme_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scoring_scheme_references, Unset):
            scoring_scheme_references = []
            for scoring_scheme_references_item_data in self.scoring_scheme_references:
                scoring_scheme_references_item = scoring_scheme_references_item_data.to_dict()
                scoring_scheme_references.append(scoring_scheme_references_item)

        semantic_framework_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.semantic_framework_references, Unset):
            semantic_framework_references = []
            for semantic_framework_references_item_data in self.semantic_framework_references:
                semantic_framework_references_item = semantic_framework_references_item_data.to_dict()
                semantic_framework_references.append(semantic_framework_references_item)

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        valid_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.to_dict()

        valid_until: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valid_until, Unset):
            valid_until = self.valid_until.to_dict()

        xsd_version = self.xsd_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accreditation_references is not UNSET:
            field_dict["accreditationReferences"] = accreditation_references
        if agent_references is not UNSET:
            field_dict["agentReferences"] = agent_references
        if assessment_specification_references is not UNSET:
            field_dict["assessmentSpecificationReferences"] = assessment_specification_references
        if attachment_list is not UNSET:
            field_dict["attachmentList"] = attachment_list
        if awarding_process_references is not UNSET:
            field_dict["awardingProcessReferences"] = awarding_process_references
        if child_credentials is not UNSET:
            field_dict["childCredentials"] = child_credentials
        if credential_subject is not UNSET:
            field_dict["credentialSubject"] = credential_subject
        if description is not UNSET:
            field_dict["description"] = description
        if display_parameters is not UNSET:
            field_dict["displayParameters"] = display_parameters
        if entitlement_specification_references is not UNSET:
            field_dict["entitlementSpecificationReferences"] = entitlement_specification_references
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if issued is not UNSET:
            field_dict["issued"] = issued
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if learning_activity_specification_references is not UNSET:
            field_dict["learningActivitySpecificationReferences"] = learning_activity_specification_references
        if learning_opportunity_references is not UNSET:
            field_dict["learningOpportunityReferences"] = learning_opportunity_references
        if learning_outcome_references is not UNSET:
            field_dict["learningOutcomeReferences"] = learning_outcome_references
        if learning_specification_references is not UNSET:
            field_dict["learningSpecificationReferences"] = learning_specification_references
        if proof is not UNSET:
            field_dict["proof"] = proof
        if scoring_scheme_references is not UNSET:
            field_dict["scoringSchemeReferences"] = scoring_scheme_references
        if semantic_framework_references is not UNSET:
            field_dict["semanticFrameworkReferences"] = semantic_framework_references
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if xsd_version is not UNSET:
            field_dict["xsdVersion"] = xsd_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_accreditation_type import DeMathplanMosesEdciAccreditationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_assessment_specification_type import (
            DeMathplanMosesEdciAssessmentSpecificationType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_awarding_process_type import DeMathplanMosesEdciAwardingProcessType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_child_credentials_type import DeMathplanMosesEdciChildCredentialsType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_credential_type_type import DeMathplanMosesEdciCredentialTypeType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_display_parameters_type import DeMathplanMosesEdciDisplayParametersType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_entitlement_specification_type import (
            DeMathplanMosesEdciEntitlementSpecificationType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_europass_credential_type_proof import (
            DeMathplanMosesEdciEuropassCredentialTypeProof,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_generic_credential_subject_type import (
            DeMathplanMosesEdciGenericCredentialSubjectType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_learning_outcome_type import (
            DeMathplanMosesEdciGenericLearningOutcomeType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_id_reference_type import DeMathplanMosesEdciIdReferenceType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_learning_activity_specification_type import (
            DeMathplanMosesEdciLearningActivitySpecificationType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_learning_opportunity_type import DeMathplanMosesEdciLearningOpportunityType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_learning_specification_references_type import (
            DeMathplanMosesEdciLearningSpecificationReferencesType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_media_object_type import DeMathplanMosesEdciMediaObjectType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_organization_type import DeMathplanMosesEdciOrganizationType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_scoring_scheme_type import DeMathplanMosesEdciScoringSchemeType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_semantic_framework_type import DeMathplanMosesEdciSemanticFrameworkType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _accreditation_references = d.pop("accreditationReferences", UNSET)
        accreditation_references: list[DeMathplanMosesEdciAccreditationType] | Unset = UNSET
        if _accreditation_references is not UNSET:
            accreditation_references = []
            for accreditation_references_item_data in _accreditation_references:
                accreditation_references_item = DeMathplanMosesEdciAccreditationType.from_dict(
                    accreditation_references_item_data
                )

                accreditation_references.append(accreditation_references_item)

        _agent_references = d.pop("agentReferences", UNSET)
        agent_references: list[DeMathplanMosesEdciOrganizationType] | Unset = UNSET
        if _agent_references is not UNSET:
            agent_references = []
            for agent_references_item_data in _agent_references:
                agent_references_item = DeMathplanMosesEdciOrganizationType.from_dict(agent_references_item_data)

                agent_references.append(agent_references_item)

        _assessment_specification_references = d.pop("assessmentSpecificationReferences", UNSET)
        assessment_specification_references: list[DeMathplanMosesEdciAssessmentSpecificationType] | Unset = UNSET
        if _assessment_specification_references is not UNSET:
            assessment_specification_references = []
            for assessment_specification_references_item_data in _assessment_specification_references:
                assessment_specification_references_item = DeMathplanMosesEdciAssessmentSpecificationType.from_dict(
                    assessment_specification_references_item_data
                )

                assessment_specification_references.append(assessment_specification_references_item)

        _attachment_list = d.pop("attachmentList", UNSET)
        attachment_list: list[DeMathplanMosesEdciMediaObjectType] | Unset = UNSET
        if _attachment_list is not UNSET:
            attachment_list = []
            for attachment_list_item_data in _attachment_list:
                attachment_list_item = DeMathplanMosesEdciMediaObjectType.from_dict(attachment_list_item_data)

                attachment_list.append(attachment_list_item)

        _awarding_process_references = d.pop("awardingProcessReferences", UNSET)
        awarding_process_references: list[DeMathplanMosesEdciAwardingProcessType] | Unset = UNSET
        if _awarding_process_references is not UNSET:
            awarding_process_references = []
            for awarding_process_references_item_data in _awarding_process_references:
                awarding_process_references_item = DeMathplanMosesEdciAwardingProcessType.from_dict(
                    awarding_process_references_item_data
                )

                awarding_process_references.append(awarding_process_references_item)

        _child_credentials = d.pop("childCredentials", UNSET)
        child_credentials: list[DeMathplanMosesEdciChildCredentialsType] | Unset = UNSET
        if _child_credentials is not UNSET:
            child_credentials = []
            for child_credentials_item_data in _child_credentials:
                child_credentials_item = DeMathplanMosesEdciChildCredentialsType.from_dict(child_credentials_item_data)

                child_credentials.append(child_credentials_item)

        _credential_subject = d.pop("credentialSubject", UNSET)
        credential_subject: DeMathplanMosesEdciGenericCredentialSubjectType | Unset
        if isinstance(_credential_subject, Unset):
            credential_subject = UNSET
        else:
            credential_subject = DeMathplanMosesEdciGenericCredentialSubjectType.from_dict(_credential_subject)

        _description = d.pop("description", UNSET)
        description: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = DeMathplanMosesEdciTextType.from_dict(description_item_data)

                description.append(description_item)

        _display_parameters = d.pop("displayParameters", UNSET)
        display_parameters: DeMathplanMosesEdciDisplayParametersType | Unset
        if isinstance(_display_parameters, Unset):
            display_parameters = UNSET
        else:
            display_parameters = DeMathplanMosesEdciDisplayParametersType.from_dict(_display_parameters)

        _entitlement_specification_references = d.pop("entitlementSpecificationReferences", UNSET)
        entitlement_specification_references: list[DeMathplanMosesEdciEntitlementSpecificationType] | Unset = UNSET
        if _entitlement_specification_references is not UNSET:
            entitlement_specification_references = []
            for entitlement_specification_references_item_data in _entitlement_specification_references:
                entitlement_specification_references_item = DeMathplanMosesEdciEntitlementSpecificationType.from_dict(
                    entitlement_specification_references_item_data
                )

                entitlement_specification_references.append(entitlement_specification_references_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _issued = d.pop("issued", UNSET)
        issued: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_issued, Unset):
            issued = UNSET
        else:
            issued = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_issued)

        _issuer = d.pop("issuer", UNSET)
        issuer: DeMathplanMosesEdciIdReferenceType | Unset
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = DeMathplanMosesEdciIdReferenceType.from_dict(_issuer)

        _learning_activity_specification_references = d.pop("learningActivitySpecificationReferences", UNSET)
        learning_activity_specification_references: (
            list[DeMathplanMosesEdciLearningActivitySpecificationType] | Unset
        ) = UNSET
        if _learning_activity_specification_references is not UNSET:
            learning_activity_specification_references = []
            for learning_activity_specification_references_item_data in _learning_activity_specification_references:
                learning_activity_specification_references_item = (
                    DeMathplanMosesEdciLearningActivitySpecificationType.from_dict(
                        learning_activity_specification_references_item_data
                    )
                )

                learning_activity_specification_references.append(learning_activity_specification_references_item)

        _learning_opportunity_references = d.pop("learningOpportunityReferences", UNSET)
        learning_opportunity_references: list[DeMathplanMosesEdciLearningOpportunityType] | Unset = UNSET
        if _learning_opportunity_references is not UNSET:
            learning_opportunity_references = []
            for learning_opportunity_references_item_data in _learning_opportunity_references:
                learning_opportunity_references_item = DeMathplanMosesEdciLearningOpportunityType.from_dict(
                    learning_opportunity_references_item_data
                )

                learning_opportunity_references.append(learning_opportunity_references_item)

        _learning_outcome_references = d.pop("learningOutcomeReferences", UNSET)
        learning_outcome_references: list[DeMathplanMosesEdciGenericLearningOutcomeType] | Unset = UNSET
        if _learning_outcome_references is not UNSET:
            learning_outcome_references = []
            for learning_outcome_references_item_data in _learning_outcome_references:
                learning_outcome_references_item = DeMathplanMosesEdciGenericLearningOutcomeType.from_dict(
                    learning_outcome_references_item_data
                )

                learning_outcome_references.append(learning_outcome_references_item)

        _learning_specification_references = d.pop("learningSpecificationReferences", UNSET)
        learning_specification_references: DeMathplanMosesEdciLearningSpecificationReferencesType | Unset
        if isinstance(_learning_specification_references, Unset):
            learning_specification_references = UNSET
        else:
            learning_specification_references = DeMathplanMosesEdciLearningSpecificationReferencesType.from_dict(
                _learning_specification_references
            )

        _proof = d.pop("proof", UNSET)
        proof: DeMathplanMosesEdciEuropassCredentialTypeProof | Unset
        if isinstance(_proof, Unset):
            proof = UNSET
        else:
            proof = DeMathplanMosesEdciEuropassCredentialTypeProof.from_dict(_proof)

        _scoring_scheme_references = d.pop("scoringSchemeReferences", UNSET)
        scoring_scheme_references: list[DeMathplanMosesEdciScoringSchemeType] | Unset = UNSET
        if _scoring_scheme_references is not UNSET:
            scoring_scheme_references = []
            for scoring_scheme_references_item_data in _scoring_scheme_references:
                scoring_scheme_references_item = DeMathplanMosesEdciScoringSchemeType.from_dict(
                    scoring_scheme_references_item_data
                )

                scoring_scheme_references.append(scoring_scheme_references_item)

        _semantic_framework_references = d.pop("semanticFrameworkReferences", UNSET)
        semantic_framework_references: list[DeMathplanMosesEdciSemanticFrameworkType] | Unset = UNSET
        if _semantic_framework_references is not UNSET:
            semantic_framework_references = []
            for semantic_framework_references_item_data in _semantic_framework_references:
                semantic_framework_references_item = DeMathplanMosesEdciSemanticFrameworkType.from_dict(
                    semantic_framework_references_item_data
                )

                semantic_framework_references.append(semantic_framework_references_item)

        _title = d.pop("title", UNSET)
        title: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = DeMathplanMosesEdciTextType.from_dict(title_item_data)

                title.append(title_item)

        _type_ = d.pop("type", UNSET)
        type_: DeMathplanMosesEdciCredentialTypeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DeMathplanMosesEdciCredentialTypeType.from_dict(_type_)

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_valid_from)

        _valid_until = d.pop("validUntil", UNSET)
        valid_until: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_valid_until)

        xsd_version = d.pop("xsdVersion", UNSET)

        de_mathplan_moses_edci_europass_credential_type = cls(
            accreditation_references=accreditation_references,
            agent_references=agent_references,
            assessment_specification_references=assessment_specification_references,
            attachment_list=attachment_list,
            awarding_process_references=awarding_process_references,
            child_credentials=child_credentials,
            credential_subject=credential_subject,
            description=description,
            display_parameters=display_parameters,
            entitlement_specification_references=entitlement_specification_references,
            id=id,
            identifier=identifier,
            issued=issued,
            issuer=issuer,
            learning_activity_specification_references=learning_activity_specification_references,
            learning_opportunity_references=learning_opportunity_references,
            learning_outcome_references=learning_outcome_references,
            learning_specification_references=learning_specification_references,
            proof=proof,
            scoring_scheme_references=scoring_scheme_references,
            semantic_framework_references=semantic_framework_references,
            title=title,
            type_=type_,
            valid_from=valid_from,
            valid_until=valid_until,
            xsd_version=xsd_version,
        )

        de_mathplan_moses_edci_europass_credential_type.additional_properties = d
        return de_mathplan_moses_edci_europass_credential_type

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
