from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract
    from ..models.fs_res_patent_patent_foreigntext_type_0 import FsResPatentPatentForeigntextType0
    from ..models.fs_res_patent_patent_inventor import FsResPatentPatentInventor
    from ..models.fs_res_patent_patent_listviews_type_0 import FsResPatentPatentListviewsType0
    from ..models.fs_res_patent_patent_orgunit import FsResPatentPatentOrgunit
    from ..models.fs_res_project_project_obj import FsResProjectProjectObj
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResPatentPatent")


@_attrs_define
class FsResPatentPatent:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | None | Unset):
        field_foreigntext (FsResPatentPatentForeigntextType0 | None | Unset):
        commentary (None | str | Unset):
        country (CsSysValueGenericValue | Unset):
        documents (list[CsSysUploadConfigurationHisUploadFile] | Unset):
        grant_date (int | Unset):
        id (int | Unset):
        inventors (list[FsResPatentPatentInventor] | Unset):
        language (ImplFsResLanguageValue | Unset):
        listviews (FsResPatentPatentListviewsType0 | None | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organizations (list[FsResPatentPatentOrgunit] | Unset):
        patent_number (str | Unset):
        priority_patent (FsResPatentPatent | None | Unset):
        projects (list[FsResProjectProjectObj] | None | Unset):
        publication_number (str | Unset):
        registration_date (int | Unset):
        registration_type (CsSysValueGenericValue | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        research_contracts (list[FsResFinanceResearchContract] | None | Unset):
        status (CsSysValueGenericValue | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        title (str | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | None | Unset = UNSET
    field_foreigntext: FsResPatentPatentForeigntextType0 | None | Unset = UNSET
    commentary: None | str | Unset = UNSET
    country: CsSysValueGenericValue | Unset = UNSET
    documents: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
    grant_date: int | Unset = UNSET
    id: int | Unset = UNSET
    inventors: list[FsResPatentPatentInventor] | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    listviews: FsResPatentPatentListviewsType0 | None | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organizations: list[FsResPatentPatentOrgunit] | Unset = UNSET
    patent_number: str | Unset = UNSET
    priority_patent: FsResPatentPatent | None | Unset = UNSET
    projects: list[FsResProjectProjectObj] | None | Unset = UNSET
    publication_number: str | Unset = UNSET
    registration_date: int | Unset = UNSET
    registration_type: CsSysValueGenericValue | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    research_contracts: list[FsResFinanceResearchContract] | None | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    title: str | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_res_patent_patent_foreigntext_type_0 import FsResPatentPatentForeigntextType0  # noqa: PLC0415
        from ..models.fs_res_patent_patent_listviews_type_0 import FsResPatentPatentListviewsType0  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        field_dynamic_component: dict[str, Any] | None | Unset
        if isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        elif isinstance(self.field_dynamic_component, ImplCsSysDynamicDynamicComponent):
            field_dynamic_component = self.field_dynamic_component.to_dict()
        else:
            field_dynamic_component = self.field_dynamic_component

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResPatentPatentForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        commentary: None | str | Unset
        if isinstance(self.commentary, Unset):
            commentary = UNSET
        else:
            commentary = self.commentary

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        grant_date = self.grant_date

        id = self.id

        inventors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventors, Unset):
            inventors = []
            for inventors_item_data in self.inventors:
                inventors_item = inventors_item_data.to_dict()
                inventors.append(inventors_item)

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        listviews: dict[str, Any] | None | Unset
        if isinstance(self.listviews, Unset):
            listviews = UNSET
        elif isinstance(self.listviews, FsResPatentPatentListviewsType0):
            listviews = self.listviews.to_dict()
        else:
            listviews = self.listviews

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        patent_number = self.patent_number

        priority_patent: dict[str, Any] | None | Unset
        if isinstance(self.priority_patent, Unset):
            priority_patent = UNSET
        elif isinstance(self.priority_patent, FsResPatentPatent):
            priority_patent = self.priority_patent.to_dict()
        else:
            priority_patent = self.priority_patent

        projects: list[dict[str, Any]] | None | Unset
        if isinstance(self.projects, Unset):
            projects = UNSET
        elif isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        publication_number = self.publication_number

        registration_date = self.registration_date

        registration_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_type, Unset):
            registration_type = self.registration_type.to_dict()

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

        research_contracts: list[dict[str, Any]] | None | Unset
        if isinstance(self.research_contracts, Unset):
            research_contracts = UNSET
        elif isinstance(self.research_contracts, list):
            research_contracts = []
            for research_contracts_type_0_item_data in self.research_contracts:
                research_contracts_type_0_item = research_contracts_type_0_item_data.to_dict()
                research_contracts.append(research_contracts_type_0_item)

        else:
            research_contracts = self.research_contracts

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        title = self.title

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
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if country is not UNSET:
            field_dict["country"] = country
        if documents is not UNSET:
            field_dict["documents"] = documents
        if grant_date is not UNSET:
            field_dict["grantDate"] = grant_date
        if id is not UNSET:
            field_dict["id"] = id
        if inventors is not UNSET:
            field_dict["inventors"] = inventors
        if language is not UNSET:
            field_dict["language"] = language
        if listviews is not UNSET:
            field_dict["listviews"] = listviews
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if patent_number is not UNSET:
            field_dict["patentNumber"] = patent_number
        if priority_patent is not UNSET:
            field_dict["priorityPatent"] = priority_patent
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publication_number is not UNSET:
            field_dict["publicationNumber"] = publication_number
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if registration_type is not UNSET:
            field_dict["registrationType"] = registration_type
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if research_contracts is not UNSET:
            field_dict["researchContracts"] = research_contracts
        if status is not UNSET:
            field_dict["status"] = status
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if title is not UNSET:
            field_dict["title"] = title
        if visibility_value is not UNSET:
            field_dict["visibilityValue"] = visibility_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract  # noqa: PLC0415
        from ..models.fs_res_patent_patent_foreigntext_type_0 import FsResPatentPatentForeigntextType0  # noqa: PLC0415
        from ..models.fs_res_patent_patent_inventor import FsResPatentPatentInventor  # noqa: PLC0415
        from ..models.fs_res_patent_patent_listviews_type_0 import FsResPatentPatentListviewsType0  # noqa: PLC0415
        from ..models.fs_res_patent_patent_orgunit import FsResPatentPatentOrgunit  # noqa: PLC0415
        from ..models.fs_res_project_project_obj import FsResProjectProjectObj  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_field_dynamic_component(data: object) -> ImplCsSysDynamicDynamicComponent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_dynamic_component_type_0 = ImplCsSysDynamicDynamicComponent.from_dict(cast(dict[str, Any], data))

            return field_dynamic_component_type_0

        field_dynamic_component = _parse_field_dynamic_component(d.pop("_dynamicComponent", UNSET))

        def _parse_field_foreigntext(data: object) -> FsResPatentPatentForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResPatentPatentForeigntextType0.from_dict(cast(dict[str, Any], data))

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        def _parse_commentary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commentary = _parse_commentary(d.pop("commentary", UNSET))

        _country = d.pop("country", UNSET)
        country: CsSysValueGenericValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = CsSysValueGenericValue.from_dict(_country)

        _documents = d.pop("documents", UNSET)
        documents: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = CsSysUploadConfigurationHisUploadFile.from_dict(documents_item_data)

                documents.append(documents_item)

        grant_date = d.pop("grantDate", UNSET)

        id = d.pop("id", UNSET)

        _inventors = d.pop("inventors", UNSET)
        inventors: list[FsResPatentPatentInventor] | Unset = UNSET
        if _inventors is not UNSET:
            inventors = []
            for inventors_item_data in _inventors:
                inventors_item = FsResPatentPatentInventor.from_dict(inventors_item_data)

                inventors.append(inventors_item)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        def _parse_listviews(data: object) -> FsResPatentPatentListviewsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            listviews_type_0 = FsResPatentPatentListviewsType0.from_dict(cast(dict[str, Any], data))

            return listviews_type_0

        listviews = _parse_listviews(d.pop("listviews", UNSET))

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[FsResPatentPatentOrgunit] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = FsResPatentPatentOrgunit.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        patent_number = d.pop("patentNumber", UNSET)

        def _parse_priority_patent(data: object) -> FsResPatentPatent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            priority_patent_type_0 = FsResPatentPatent.from_dict(cast(dict[str, Any], data))

            return priority_patent_type_0

        priority_patent = _parse_priority_patent(d.pop("priorityPatent", UNSET))

        def _parse_projects(data: object) -> list[FsResProjectProjectObj] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            projects_type_0: list[FsResProjectProjectObj] = []
            _projects_type_0 = cast(list[dict[str, Any]], data)
            for projects_type_0_item_data in _projects_type_0:
                projects_type_0_item = FsResProjectProjectObj.from_dict(projects_type_0_item_data)

                projects_type_0.append(projects_type_0_item)

            return projects_type_0

        projects = _parse_projects(d.pop("projects", UNSET))

        publication_number = d.pop("publicationNumber", UNSET)

        registration_date = d.pop("registrationDate", UNSET)

        _registration_type = d.pop("registrationType", UNSET)
        registration_type: CsSysValueGenericValue | Unset
        if isinstance(_registration_type, Unset):
            registration_type = UNSET
        else:
            registration_type = CsSysValueGenericValue.from_dict(_registration_type)

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

        def _parse_research_contracts(data: object) -> list[FsResFinanceResearchContract] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            research_contracts_type_0: list[FsResFinanceResearchContract] = []
            _research_contracts_type_0 = cast(list[dict[str, Any]], data)
            for research_contracts_type_0_item_data in _research_contracts_type_0:
                research_contracts_type_0_item = FsResFinanceResearchContract.from_dict(
                    research_contracts_type_0_item_data
                )

                research_contracts_type_0.append(research_contracts_type_0_item)

            return research_contracts_type_0

        research_contracts = _parse_research_contracts(d.pop("researchContracts", UNSET))

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        title = d.pop("title", UNSET)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        fs_res_patent_patent = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            commentary=commentary,
            country=country,
            documents=documents,
            grant_date=grant_date,
            id=id,
            inventors=inventors,
            language=language,
            listviews=listviews,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organizations=organizations,
            patent_number=patent_number,
            priority_patent=priority_patent,
            projects=projects,
            publication_number=publication_number,
            registration_date=registration_date,
            registration_type=registration_type,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            research_contracts=research_contracts,
            status=status,
            subject_areas=subject_areas,
            title=title,
            visibility_value=visibility_value,
        )

        fs_res_patent_patent.additional_properties = d
        return fs_res_patent_patent

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
