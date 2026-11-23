from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_employee_employee import CsPsvEmployeeEmployee
    from ..models.cs_psv_employment_employment_foreigntext import CsPsvEmploymentEmploymentForeigntext
    from ..models.cs_psv_employment_employment_orgunit import CsPsvEmploymentEmploymentOrgunit
    from ..models.cs_psv_employment_employment_pay_grade import CsPsvEmploymentEmploymentPayGrade
    from ..models.cs_psv_personnelcost_financing import CsPsvPersonnelcostFinancing
    from ..models.cs_psv_workingtime_working_time import CsPsvWorkingtimeWorkingTime
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent


T = TypeVar("T", bound="CsPsvEmploymentEmployment")


@_attrs_define
class CsPsvEmploymentEmployment:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (CsPsvEmploymentEmploymentForeigntext | Unset):
        activity_type (CsSysValueGenericValue | Unset):
        employee (CsPsvEmployeeEmployee | Unset):
        employment_pay_grades (list[CsPsvEmploymentEmploymentPayGrade] | Unset):
        employment_type (CsSysValueGenericValue | Unset):
        extern (bool | Unset):
        graduation_type (CsSysValueGenericValue | Unset):
        id (int | Unset):
        joint_appointment (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        orgunits (list[CsPsvEmploymentEmploymentOrgunit] | Unset):
        parent_type (CsSysValueGenericValue | Unset):
        personnel_financings (list[CsPsvPersonnelcostFinancing] | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
        working_times (list[CsPsvWorkingtimeWorkingTime] | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: CsPsvEmploymentEmploymentForeigntext | Unset = UNSET
    activity_type: CsSysValueGenericValue | Unset = UNSET
    employee: CsPsvEmployeeEmployee | Unset = UNSET
    employment_pay_grades: list[CsPsvEmploymentEmploymentPayGrade] | Unset = UNSET
    employment_type: CsSysValueGenericValue | Unset = UNSET
    extern: bool | Unset = UNSET
    graduation_type: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    joint_appointment: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    orgunits: list[CsPsvEmploymentEmploymentOrgunit] | Unset = UNSET
    parent_type: CsSysValueGenericValue | Unset = UNSET
    personnel_financings: list[CsPsvPersonnelcostFinancing] | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    working_times: list[CsPsvWorkingtimeWorkingTime] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        activity_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activity_type, Unset):
            activity_type = self.activity_type.to_dict()

        employee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employee, Unset):
            employee = self.employee.to_dict()

        employment_pay_grades: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.employment_pay_grades, Unset):
            employment_pay_grades = []
            for employment_pay_grades_item_data in self.employment_pay_grades:
                employment_pay_grades_item = employment_pay_grades_item_data.to_dict()
                employment_pay_grades.append(employment_pay_grades_item)

        employment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employment_type, Unset):
            employment_type = self.employment_type.to_dict()

        extern = self.extern

        graduation_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.graduation_type, Unset):
            graduation_type = self.graduation_type.to_dict()

        id = self.id

        joint_appointment = self.joint_appointment

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        orgunits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orgunits, Unset):
            orgunits = []
            for orgunits_item_data in self.orgunits:
                orgunits_item = orgunits_item_data.to_dict()
                orgunits.append(orgunits_item)

        parent_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.to_dict()

        personnel_financings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.personnel_financings, Unset):
            personnel_financings = []
            for personnel_financings_item_data in self.personnel_financings:
                personnel_financings_item = personnel_financings_item_data.to_dict()
                personnel_financings.append(personnel_financings_item)

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

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        valid_from = self.valid_from

        valid_to = self.valid_to

        working_times: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.working_times, Unset):
            working_times = []
            for working_times_item_data in self.working_times:
                working_times_item = working_times_item_data.to_dict()
                working_times.append(working_times_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if activity_type is not UNSET:
            field_dict["activityType"] = activity_type
        if employee is not UNSET:
            field_dict["employee"] = employee
        if employment_pay_grades is not UNSET:
            field_dict["employmentPayGrades"] = employment_pay_grades
        if employment_type is not UNSET:
            field_dict["employmentType"] = employment_type
        if extern is not UNSET:
            field_dict["extern"] = extern
        if graduation_type is not UNSET:
            field_dict["graduationType"] = graduation_type
        if id is not UNSET:
            field_dict["id"] = id
        if joint_appointment is not UNSET:
            field_dict["jointAppointment"] = joint_appointment
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if orgunits is not UNSET:
            field_dict["orgunits"] = orgunits
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if personnel_financings is not UNSET:
            field_dict["personnelFinancings"] = personnel_financings
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if working_times is not UNSET:
            field_dict["workingTimes"] = working_times

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_employee_employee import CsPsvEmployeeEmployee  # noqa: PLC0415
        from ..models.cs_psv_employment_employment_foreigntext import CsPsvEmploymentEmploymentForeigntext  # noqa: PLC0415
        from ..models.cs_psv_employment_employment_orgunit import CsPsvEmploymentEmploymentOrgunit  # noqa: PLC0415
        from ..models.cs_psv_employment_employment_pay_grade import CsPsvEmploymentEmploymentPayGrade  # noqa: PLC0415
        from ..models.cs_psv_personnelcost_financing import CsPsvPersonnelcostFinancing  # noqa: PLC0415
        from ..models.cs_psv_workingtime_working_time import CsPsvWorkingtimeWorkingTime  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvEmploymentEmploymentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvEmploymentEmploymentForeigntext.from_dict(_field_foreigntext)

        _activity_type = d.pop("activityType", UNSET)
        activity_type: CsSysValueGenericValue | Unset
        if isinstance(_activity_type, Unset):
            activity_type = UNSET
        else:
            activity_type = CsSysValueGenericValue.from_dict(_activity_type)

        _employee = d.pop("employee", UNSET)
        employee: CsPsvEmployeeEmployee | Unset
        if isinstance(_employee, Unset):
            employee = UNSET
        else:
            employee = CsPsvEmployeeEmployee.from_dict(_employee)

        _employment_pay_grades = d.pop("employmentPayGrades", UNSET)
        employment_pay_grades: list[CsPsvEmploymentEmploymentPayGrade] | Unset = UNSET
        if _employment_pay_grades is not UNSET:
            employment_pay_grades = []
            for employment_pay_grades_item_data in _employment_pay_grades:
                employment_pay_grades_item = CsPsvEmploymentEmploymentPayGrade.from_dict(
                    employment_pay_grades_item_data
                )

                employment_pay_grades.append(employment_pay_grades_item)

        _employment_type = d.pop("employmentType", UNSET)
        employment_type: CsSysValueGenericValue | Unset
        if isinstance(_employment_type, Unset):
            employment_type = UNSET
        else:
            employment_type = CsSysValueGenericValue.from_dict(_employment_type)

        extern = d.pop("extern", UNSET)

        _graduation_type = d.pop("graduationType", UNSET)
        graduation_type: CsSysValueGenericValue | Unset
        if isinstance(_graduation_type, Unset):
            graduation_type = UNSET
        else:
            graduation_type = CsSysValueGenericValue.from_dict(_graduation_type)

        id = d.pop("id", UNSET)

        joint_appointment = d.pop("jointAppointment", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _orgunits = d.pop("orgunits", UNSET)
        orgunits: list[CsPsvEmploymentEmploymentOrgunit] | Unset = UNSET
        if _orgunits is not UNSET:
            orgunits = []
            for orgunits_item_data in _orgunits:
                orgunits_item = CsPsvEmploymentEmploymentOrgunit.from_dict(orgunits_item_data)

                orgunits.append(orgunits_item)

        _parent_type = d.pop("parentType", UNSET)
        parent_type: CsSysValueGenericValue | Unset
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = CsSysValueGenericValue.from_dict(_parent_type)

        _personnel_financings = d.pop("personnelFinancings", UNSET)
        personnel_financings: list[CsPsvPersonnelcostFinancing] | Unset = UNSET
        if _personnel_financings is not UNSET:
            personnel_financings = []
            for personnel_financings_item_data in _personnel_financings:
                personnel_financings_item = CsPsvPersonnelcostFinancing.from_dict(personnel_financings_item_data)

                personnel_financings.append(personnel_financings_item)

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

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        _working_times = d.pop("workingTimes", UNSET)
        working_times: list[CsPsvWorkingtimeWorkingTime] | Unset = UNSET
        if _working_times is not UNSET:
            working_times = []
            for working_times_item_data in _working_times:
                working_times_item = CsPsvWorkingtimeWorkingTime.from_dict(working_times_item_data)

                working_times.append(working_times_item)

        cs_psv_employment_employment = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            activity_type=activity_type,
            employee=employee,
            employment_pay_grades=employment_pay_grades,
            employment_type=employment_type,
            extern=extern,
            graduation_type=graduation_type,
            id=id,
            joint_appointment=joint_appointment,
            lock_version=lock_version,
            obj_guid=obj_guid,
            orgunits=orgunits,
            parent_type=parent_type,
            personnel_financings=personnel_financings,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            subject_areas=subject_areas,
            valid_from=valid_from,
            valid_to=valid_to,
            working_times=working_times,
        )

        cs_psv_employment_employment.additional_properties = d
        return cs_psv_employment_employment

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
