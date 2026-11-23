from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_doctoral_structured_doctoral_course_program_foreigntext import (
        FsResDoctoralStructuredDoctoralCourseProgramForeigntext,
    )
    from ..models.fs_res_doctoral_structured_doctoral_course_program_orgunit import (
        FsResDoctoralStructuredDoctoralCourseProgramOrgunit,
    )
    from ..models.fs_res_doctoral_structured_doctoral_course_program_person import (
        FsResDoctoralStructuredDoctoralCourseProgramPerson,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResDoctoralStructuredDoctoralCourseProgram")


@_attrs_define
class FsResDoctoralStructuredDoctoralCourseProgram:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResDoctoralStructuredDoctoralCourseProgramForeigntext | Unset):
        course_of_study (CsSysValueGenericValue | Unset):
        description (str | Unset):
        doctoral_position_available (CsSysValueGenericValue | Unset):
        financing_type (CsSysValueGenericValue | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organizations (list[FsResDoctoralStructuredDoctoralCourseProgramOrgunit] | Unset):
        persons (list[FsResDoctoralStructuredDoctoralCourseProgramPerson] | Unset):
        program_end (int | Unset):
        program_start (int | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        scholarship_available (CsSysValueGenericValue | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        title (str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResDoctoralStructuredDoctoralCourseProgramForeigntext | Unset = UNSET
    course_of_study: CsSysValueGenericValue | Unset = UNSET
    description: str | Unset = UNSET
    doctoral_position_available: CsSysValueGenericValue | Unset = UNSET
    financing_type: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organizations: list[FsResDoctoralStructuredDoctoralCourseProgramOrgunit] | Unset = UNSET
    persons: list[FsResDoctoralStructuredDoctoralCourseProgramPerson] | Unset = UNSET
    program_end: int | Unset = UNSET
    program_start: int | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    scholarship_available: CsSysValueGenericValue | Unset = UNSET
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

        course_of_study: dict[str, Any] | Unset = UNSET
        if not isinstance(self.course_of_study, Unset):
            course_of_study = self.course_of_study.to_dict()

        description = self.description

        doctoral_position_available: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doctoral_position_available, Unset):
            doctoral_position_available = self.doctoral_position_available.to_dict()

        financing_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.financing_type, Unset):
            financing_type = self.financing_type.to_dict()

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        persons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        program_end = self.program_end

        program_start = self.program_start

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

        scholarship_available: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scholarship_available, Unset):
            scholarship_available = self.scholarship_available.to_dict()

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
        if course_of_study is not UNSET:
            field_dict["courseOfStudy"] = course_of_study
        if description is not UNSET:
            field_dict["description"] = description
        if doctoral_position_available is not UNSET:
            field_dict["doctoralPositionAvailable"] = doctoral_position_available
        if financing_type is not UNSET:
            field_dict["financingType"] = financing_type
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if persons is not UNSET:
            field_dict["persons"] = persons
        if program_end is not UNSET:
            field_dict["programEnd"] = program_end
        if program_start is not UNSET:
            field_dict["programStart"] = program_start
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if scholarship_available is not UNSET:
            field_dict["scholarshipAvailable"] = scholarship_available
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_doctoral_structured_doctoral_course_program_foreigntext import (
            FsResDoctoralStructuredDoctoralCourseProgramForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_doctoral_structured_doctoral_course_program_orgunit import (
            FsResDoctoralStructuredDoctoralCourseProgramOrgunit,  # noqa: PLC0415
        )
        from ..models.fs_res_doctoral_structured_doctoral_course_program_person import (
            FsResDoctoralStructuredDoctoralCourseProgramPerson,  # noqa: PLC0415
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
        field_foreigntext: FsResDoctoralStructuredDoctoralCourseProgramForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResDoctoralStructuredDoctoralCourseProgramForeigntext.from_dict(_field_foreigntext)

        _course_of_study = d.pop("courseOfStudy", UNSET)
        course_of_study: CsSysValueGenericValue | Unset
        if isinstance(_course_of_study, Unset):
            course_of_study = UNSET
        else:
            course_of_study = CsSysValueGenericValue.from_dict(_course_of_study)

        description = d.pop("description", UNSET)

        _doctoral_position_available = d.pop("doctoralPositionAvailable", UNSET)
        doctoral_position_available: CsSysValueGenericValue | Unset
        if isinstance(_doctoral_position_available, Unset):
            doctoral_position_available = UNSET
        else:
            doctoral_position_available = CsSysValueGenericValue.from_dict(_doctoral_position_available)

        _financing_type = d.pop("financingType", UNSET)
        financing_type: CsSysValueGenericValue | Unset
        if isinstance(_financing_type, Unset):
            financing_type = UNSET
        else:
            financing_type = CsSysValueGenericValue.from_dict(_financing_type)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[FsResDoctoralStructuredDoctoralCourseProgramOrgunit] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = FsResDoctoralStructuredDoctoralCourseProgramOrgunit.from_dict(
                    organizations_item_data
                )

                organizations.append(organizations_item)

        _persons = d.pop("persons", UNSET)
        persons: list[FsResDoctoralStructuredDoctoralCourseProgramPerson] | Unset = UNSET
        if _persons is not UNSET:
            persons = []
            for persons_item_data in _persons:
                persons_item = FsResDoctoralStructuredDoctoralCourseProgramPerson.from_dict(persons_item_data)

                persons.append(persons_item)

        program_end = d.pop("programEnd", UNSET)

        program_start = d.pop("programStart", UNSET)

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

        _scholarship_available = d.pop("scholarshipAvailable", UNSET)
        scholarship_available: CsSysValueGenericValue | Unset
        if isinstance(_scholarship_available, Unset):
            scholarship_available = UNSET
        else:
            scholarship_available = CsSysValueGenericValue.from_dict(_scholarship_available)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        title = d.pop("title", UNSET)

        fs_res_doctoral_structured_doctoral_course_program = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            course_of_study=course_of_study,
            description=description,
            doctoral_position_available=doctoral_position_available,
            financing_type=financing_type,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organizations=organizations,
            persons=persons,
            program_end=program_end,
            program_start=program_start,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            scholarship_available=scholarship_available,
            subject_areas=subject_areas,
            title=title,
        )

        fs_res_doctoral_structured_doctoral_course_program.additional_properties = d
        return fs_res_doctoral_structured_doctoral_course_program

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
