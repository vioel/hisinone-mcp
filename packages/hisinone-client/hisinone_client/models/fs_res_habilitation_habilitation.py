from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_habilitation_habilitation_foreigntext import FsResHabilitationHabilitationForeigntext
    from ..models.fs_res_habilitation_habilitation_person import FsResHabilitationHabilitationPerson
    from ..models.fs_res_project_project_obj import FsResProjectProjectObj
    from ..models.fs_res_publication_publication import FsResPublicationPublication
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResHabilitationHabilitation")


@_attrs_define
class FsResHabilitationHabilitation:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResHabilitationHabilitationForeigntext | Unset):
        admission_date (int | Unset):
        certificate_date (int | Unset):
        docents (list[FsResHabilitationHabilitationPerson] | Unset):
        doctoral (CsPsvPersonRest | Unset):
        doctoral_orgunit_obj (CsSysValueGenericValue | Unset):
        end_habilitation_phase (int | Unset):
        habilitation_type (CsSysValueGenericValue | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        orgunit_obj (CsSysValueGenericValue | Unset):
        projects (list[FsResProjectProjectObj] | Unset):
        publications (list[FsResPublicationPublication] | Unset):
        registration_date (int | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        start_habilitation_phase (int | Unset):
        status (CsSysValueGenericValue | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        title (str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResHabilitationHabilitationForeigntext | Unset = UNSET
    admission_date: int | Unset = UNSET
    certificate_date: int | Unset = UNSET
    docents: list[FsResHabilitationHabilitationPerson] | Unset = UNSET
    doctoral: CsPsvPersonRest | Unset = UNSET
    doctoral_orgunit_obj: CsSysValueGenericValue | Unset = UNSET
    end_habilitation_phase: int | Unset = UNSET
    habilitation_type: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    orgunit_obj: CsSysValueGenericValue | Unset = UNSET
    projects: list[FsResProjectProjectObj] | Unset = UNSET
    publications: list[FsResPublicationPublication] | Unset = UNSET
    registration_date: int | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    start_habilitation_phase: int | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        admission_date = self.admission_date

        certificate_date = self.certificate_date

        docents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.docents, Unset):
            docents = []
            for docents_item_data in self.docents:
                docents_item = docents_item_data.to_dict()
                docents.append(docents_item)

        doctoral: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doctoral, Unset):
            doctoral = self.doctoral.to_dict()

        doctoral_orgunit_obj: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doctoral_orgunit_obj, Unset):
            doctoral_orgunit_obj = self.doctoral_orgunit_obj.to_dict()

        end_habilitation_phase = self.end_habilitation_phase

        habilitation_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.habilitation_type, Unset):
            habilitation_type = self.habilitation_type.to_dict()

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        orgunit_obj: dict[str, Any] | Unset = UNSET
        if not isinstance(self.orgunit_obj, Unset):
            orgunit_obj = self.orgunit_obj.to_dict()

        projects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = []
            for projects_item_data in self.projects:
                projects_item = projects_item_data.to_dict()
                projects.append(projects_item)

        publications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publications, Unset):
            publications = []
            for publications_item_data in self.publications:
                publications_item = publications_item_data.to_dict()
                publications.append(publications_item)

        registration_date = self.registration_date

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

        start_habilitation_phase = self.start_habilitation_phase

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if admission_date is not UNSET:
            field_dict["admissionDate"] = admission_date
        if certificate_date is not UNSET:
            field_dict["certificateDate"] = certificate_date
        if docents is not UNSET:
            field_dict["docents"] = docents
        if doctoral is not UNSET:
            field_dict["doctoral"] = doctoral
        if doctoral_orgunit_obj is not UNSET:
            field_dict["doctoralOrgunitObj"] = doctoral_orgunit_obj
        if end_habilitation_phase is not UNSET:
            field_dict["endHabilitationPhase"] = end_habilitation_phase
        if habilitation_type is not UNSET:
            field_dict["habilitationType"] = habilitation_type
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if orgunit_obj is not UNSET:
            field_dict["orgunitObj"] = orgunit_obj
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publications is not UNSET:
            field_dict["publications"] = publications
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if start_habilitation_phase is not UNSET:
            field_dict["startHabilitationPhase"] = start_habilitation_phase
        if status is not UNSET:
            field_dict["status"] = status
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_habilitation_habilitation_foreigntext import FsResHabilitationHabilitationForeigntext  # noqa: PLC0415
        from ..models.fs_res_habilitation_habilitation_person import FsResHabilitationHabilitationPerson  # noqa: PLC0415
        from ..models.fs_res_project_project_obj import FsResProjectProjectObj  # noqa: PLC0415
        from ..models.fs_res_publication_publication import FsResPublicationPublication  # noqa: PLC0415
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
        field_foreigntext: FsResHabilitationHabilitationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResHabilitationHabilitationForeigntext.from_dict(_field_foreigntext)

        admission_date = d.pop("admissionDate", UNSET)

        certificate_date = d.pop("certificateDate", UNSET)

        _docents = d.pop("docents", UNSET)
        docents: list[FsResHabilitationHabilitationPerson] | Unset = UNSET
        if _docents is not UNSET:
            docents = []
            for docents_item_data in _docents:
                docents_item = FsResHabilitationHabilitationPerson.from_dict(docents_item_data)

                docents.append(docents_item)

        _doctoral = d.pop("doctoral", UNSET)
        doctoral: CsPsvPersonRest | Unset
        if isinstance(_doctoral, Unset):
            doctoral = UNSET
        else:
            doctoral = CsPsvPersonRest.from_dict(_doctoral)

        _doctoral_orgunit_obj = d.pop("doctoralOrgunitObj", UNSET)
        doctoral_orgunit_obj: CsSysValueGenericValue | Unset
        if isinstance(_doctoral_orgunit_obj, Unset):
            doctoral_orgunit_obj = UNSET
        else:
            doctoral_orgunit_obj = CsSysValueGenericValue.from_dict(_doctoral_orgunit_obj)

        end_habilitation_phase = d.pop("endHabilitationPhase", UNSET)

        _habilitation_type = d.pop("habilitationType", UNSET)
        habilitation_type: CsSysValueGenericValue | Unset
        if isinstance(_habilitation_type, Unset):
            habilitation_type = UNSET
        else:
            habilitation_type = CsSysValueGenericValue.from_dict(_habilitation_type)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _orgunit_obj = d.pop("orgunitObj", UNSET)
        orgunit_obj: CsSysValueGenericValue | Unset
        if isinstance(_orgunit_obj, Unset):
            orgunit_obj = UNSET
        else:
            orgunit_obj = CsSysValueGenericValue.from_dict(_orgunit_obj)

        _projects = d.pop("projects", UNSET)
        projects: list[FsResProjectProjectObj] | Unset = UNSET
        if _projects is not UNSET:
            projects = []
            for projects_item_data in _projects:
                projects_item = FsResProjectProjectObj.from_dict(projects_item_data)

                projects.append(projects_item)

        _publications = d.pop("publications", UNSET)
        publications: list[FsResPublicationPublication] | Unset = UNSET
        if _publications is not UNSET:
            publications = []
            for publications_item_data in _publications:
                publications_item = FsResPublicationPublication.from_dict(publications_item_data)

                publications.append(publications_item)

        registration_date = d.pop("registrationDate", UNSET)

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

        start_habilitation_phase = d.pop("startHabilitationPhase", UNSET)

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

        fs_res_habilitation_habilitation = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            admission_date=admission_date,
            certificate_date=certificate_date,
            docents=docents,
            doctoral=doctoral,
            doctoral_orgunit_obj=doctoral_orgunit_obj,
            end_habilitation_phase=end_habilitation_phase,
            habilitation_type=habilitation_type,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            orgunit_obj=orgunit_obj,
            projects=projects,
            publications=publications,
            registration_date=registration_date,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            start_habilitation_phase=start_habilitation_phase,
            status=status,
            subject_areas=subject_areas,
            title=title,
        )

        fs_res_habilitation_habilitation.additional_properties = d
        return fs_res_habilitation_habilitation

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
