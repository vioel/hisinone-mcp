from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_research_partner_simple import (
        CsPsvExternalOrganisationResearchPartnerSimple,
    )
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_publication_journal import FsResPublicationJournal
    from ..models.fs_res_research_activity_research_activity_foreigntext import (
        FsResResearchActivityResearchActivityForeigntext,
    )
    from ..models.fs_res_research_activity_research_activity_type_value import (
        FsResResearchActivityResearchActivityTypeValue,
    )
    from ..models.fs_res_research_relationship_research_relationship import (
        FsResResearchRelationshipResearchRelationship,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResResearchActivityResearchActivity")


@_attrs_define
class FsResResearchActivityResearchActivity:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResResearchActivityResearchActivityForeigntext | Unset):
        client_orgunit (CsSysValueGenericValue | Unset):
        client_research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        commentary (str | Unset):
        contribution_type (CsSysValueGenericValue | Unset):
        date_from (int | Unset):
        date_of_assessment (int | Unset):
        date_to (int | Unset):
        description (str | Unset):
        funding_line (str | Unset):
        group_name (str | Unset):
        id (int | Unset):
        journal (FsResPublicationJournal | Unset):
        language (ImplFsResLanguageValue | Unset):
        location (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        orgunit (CsSysValueGenericValue | Unset):
        own_role (str | Unset):
        person (CsPsvPersonRest | Unset):
        position (CsSysValueGenericValue | Unset):
        research_activity_type_value (FsResResearchActivityResearchActivityTypeValue | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        research_relationship (FsResResearchRelationshipResearchRelationship | Unset):
        serialversionuid (int | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        successful_foundation (CsSysValueGenericValue | Unset):
        title (str | Unset):
        url (str | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResResearchActivityResearchActivityForeigntext | Unset = UNSET
    client_orgunit: CsSysValueGenericValue | Unset = UNSET
    client_research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    commentary: str | Unset = UNSET
    contribution_type: CsSysValueGenericValue | Unset = UNSET
    date_from: int | Unset = UNSET
    date_of_assessment: int | Unset = UNSET
    date_to: int | Unset = UNSET
    description: str | Unset = UNSET
    funding_line: str | Unset = UNSET
    group_name: str | Unset = UNSET
    id: int | Unset = UNSET
    journal: FsResPublicationJournal | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    location: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    orgunit: CsSysValueGenericValue | Unset = UNSET
    own_role: str | Unset = UNSET
    person: CsPsvPersonRest | Unset = UNSET
    position: CsSysValueGenericValue | Unset = UNSET
    research_activity_type_value: FsResResearchActivityResearchActivityTypeValue | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    research_relationship: FsResResearchRelationshipResearchRelationship | Unset = UNSET
    serialversionuid: int | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    successful_foundation: CsSysValueGenericValue | Unset = UNSET
    title: str | Unset = UNSET
    url: str | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        client_orgunit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_orgunit, Unset):
            client_orgunit = self.client_orgunit.to_dict()

        client_research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_research_partner, Unset):
            client_research_partner = self.client_research_partner.to_dict()

        commentary = self.commentary

        contribution_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contribution_type, Unset):
            contribution_type = self.contribution_type.to_dict()

        date_from = self.date_from

        date_of_assessment = self.date_of_assessment

        date_to = self.date_to

        description = self.description

        funding_line = self.funding_line

        group_name = self.group_name

        id = self.id

        journal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.journal, Unset):
            journal = self.journal.to_dict()

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        location = self.location

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        orgunit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.orgunit, Unset):
            orgunit = self.orgunit.to_dict()

        own_role = self.own_role

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        research_activity_type_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_activity_type_value, Unset):
            research_activity_type_value = self.research_activity_type_value.to_dict()

        research_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_areas, Unset):
            research_areas = []
            for research_areas_item_data in self.research_areas:
                research_areas_item = research_areas_item_data.to_dict()
                research_areas.append(research_areas_item)

        research_areas_kdsf: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_areas_kdsf, Unset):
            research_areas_kdsf = []
            for research_areas_kdsf_item_data in self.research_areas_kdsf:
                research_areas_kdsf_item = research_areas_kdsf_item_data.to_dict()
                research_areas_kdsf.append(research_areas_kdsf_item)

        research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_partner, Unset):
            research_partner = self.research_partner.to_dict()

        research_relationship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_relationship, Unset):
            research_relationship = self.research_relationship.to_dict()

        serialversionuid = self.serialversionuid

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        successful_foundation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.successful_foundation, Unset):
            successful_foundation = self.successful_foundation.to_dict()

        title = self.title

        url = self.url

        visibility_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_value, Unset):
            visibility_value = self.visibility_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if client_orgunit is not UNSET:
            field_dict["clientOrgunit"] = client_orgunit
        if client_research_partner is not UNSET:
            field_dict["clientResearchPartner"] = client_research_partner
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if contribution_type is not UNSET:
            field_dict["contributionType"] = contribution_type
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_of_assessment is not UNSET:
            field_dict["dateOfAssessment"] = date_of_assessment
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if description is not UNSET:
            field_dict["description"] = description
        if funding_line is not UNSET:
            field_dict["fundingLine"] = funding_line
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if id is not UNSET:
            field_dict["id"] = id
        if journal is not UNSET:
            field_dict["journal"] = journal
        if language is not UNSET:
            field_dict["language"] = language
        if location is not UNSET:
            field_dict["location"] = location
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if orgunit is not UNSET:
            field_dict["orgunit"] = orgunit
        if own_role is not UNSET:
            field_dict["ownRole"] = own_role
        if person is not UNSET:
            field_dict["person"] = person
        if position is not UNSET:
            field_dict["position"] = position
        if research_activity_type_value is not UNSET:
            field_dict["researchActivityTypeValue"] = research_activity_type_value
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner
        if research_relationship is not UNSET:
            field_dict["researchRelationship"] = research_relationship
        if serialversionuid is not UNSET:
            field_dict["serialversionuid"] = serialversionuid
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if successful_foundation is not UNSET:
            field_dict["successfulFoundation"] = successful_foundation
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if visibility_value is not UNSET:
            field_dict["visibilityValue"] = visibility_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_journal import FsResPublicationJournal  # noqa: PLC0415
        from ..models.fs_res_research_activity_research_activity_foreigntext import (
            FsResResearchActivityResearchActivityForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_research_activity_research_activity_type_value import (
            FsResResearchActivityResearchActivityTypeValue,  # noqa: PLC0415
        )
        from ..models.fs_res_research_relationship_research_relationship import (
            FsResResearchRelationshipResearchRelationship,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResResearchActivityResearchActivityForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResResearchActivityResearchActivityForeigntext.from_dict(_field_foreigntext)

        _client_orgunit = d.pop("clientOrgunit", UNSET)
        client_orgunit: CsSysValueGenericValue | Unset
        if isinstance(_client_orgunit, Unset):
            client_orgunit = UNSET
        else:
            client_orgunit = CsSysValueGenericValue.from_dict(_client_orgunit)

        _client_research_partner = d.pop("clientResearchPartner", UNSET)
        client_research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_client_research_partner, Unset):
            client_research_partner = UNSET
        else:
            client_research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_client_research_partner)

        commentary = d.pop("commentary", UNSET)

        _contribution_type = d.pop("contributionType", UNSET)
        contribution_type: CsSysValueGenericValue | Unset
        if isinstance(_contribution_type, Unset):
            contribution_type = UNSET
        else:
            contribution_type = CsSysValueGenericValue.from_dict(_contribution_type)

        date_from = d.pop("dateFrom", UNSET)

        date_of_assessment = d.pop("dateOfAssessment", UNSET)

        date_to = d.pop("dateTo", UNSET)

        description = d.pop("description", UNSET)

        funding_line = d.pop("fundingLine", UNSET)

        group_name = d.pop("groupName", UNSET)

        id = d.pop("id", UNSET)

        _journal = d.pop("journal", UNSET)
        journal: FsResPublicationJournal | Unset
        if isinstance(_journal, Unset):
            journal = UNSET
        else:
            journal = FsResPublicationJournal.from_dict(_journal)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        location = d.pop("location", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _orgunit = d.pop("orgunit", UNSET)
        orgunit: CsSysValueGenericValue | Unset
        if isinstance(_orgunit, Unset):
            orgunit = UNSET
        else:
            orgunit = CsSysValueGenericValue.from_dict(_orgunit)

        own_role = d.pop("ownRole", UNSET)

        _person = d.pop("person", UNSET)
        person: CsPsvPersonRest | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CsPsvPersonRest.from_dict(_person)

        _position = d.pop("position", UNSET)
        position: CsSysValueGenericValue | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = CsSysValueGenericValue.from_dict(_position)

        _research_activity_type_value = d.pop("researchActivityTypeValue", UNSET)
        research_activity_type_value: FsResResearchActivityResearchActivityTypeValue | Unset
        if isinstance(_research_activity_type_value, Unset):
            research_activity_type_value = UNSET
        else:
            research_activity_type_value = FsResResearchActivityResearchActivityTypeValue.from_dict(
                _research_activity_type_value
            )

        _research_areas = d.pop("researchAreas", UNSET)
        research_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _research_areas is not UNSET:
            research_areas = []
            for research_areas_item_data in _research_areas:
                research_areas_item = CsSysValueGenericValue.from_dict(research_areas_item_data)

                research_areas.append(research_areas_item)

        _research_areas_kdsf = d.pop("researchAreasKdsf", UNSET)
        research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
        if _research_areas_kdsf is not UNSET:
            research_areas_kdsf = []
            for research_areas_kdsf_item_data in _research_areas_kdsf:
                research_areas_kdsf_item = CsSysValueGenericValue.from_dict(research_areas_kdsf_item_data)

                research_areas_kdsf.append(research_areas_kdsf_item)

        _research_partner = d.pop("researchPartner", UNSET)
        research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_research_partner, Unset):
            research_partner = UNSET
        else:
            research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_research_partner)

        _research_relationship = d.pop("researchRelationship", UNSET)
        research_relationship: FsResResearchRelationshipResearchRelationship | Unset
        if isinstance(_research_relationship, Unset):
            research_relationship = UNSET
        else:
            research_relationship = FsResResearchRelationshipResearchRelationship.from_dict(_research_relationship)

        serialversionuid = d.pop("serialversionuid", UNSET)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        _successful_foundation = d.pop("successfulFoundation", UNSET)
        successful_foundation: CsSysValueGenericValue | Unset
        if isinstance(_successful_foundation, Unset):
            successful_foundation = UNSET
        else:
            successful_foundation = CsSysValueGenericValue.from_dict(_successful_foundation)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        fs_res_research_activity_research_activity = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            client_orgunit=client_orgunit,
            client_research_partner=client_research_partner,
            commentary=commentary,
            contribution_type=contribution_type,
            date_from=date_from,
            date_of_assessment=date_of_assessment,
            date_to=date_to,
            description=description,
            funding_line=funding_line,
            group_name=group_name,
            id=id,
            journal=journal,
            language=language,
            location=location,
            lock_version=lock_version,
            obj_guid=obj_guid,
            orgunit=orgunit,
            own_role=own_role,
            person=person,
            position=position,
            research_activity_type_value=research_activity_type_value,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            research_partner=research_partner,
            research_relationship=research_relationship,
            serialversionuid=serialversionuid,
            subject_areas=subject_areas,
            successful_foundation=successful_foundation,
            title=title,
            url=url,
            visibility_value=visibility_value,
        )

        fs_res_research_activity_research_activity.additional_properties = d
        return fs_res_research_activity_research_activity

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
