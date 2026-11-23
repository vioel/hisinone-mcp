from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_prize_nomination_nomination_foreigntext import FsResPrizeNominationNominationForeigntext
    from ..models.fs_res_prize_nomination_nomination_person import FsResPrizeNominationNominationPerson
    from ..models.fs_res_prize_nomination_prize import FsResPrizeNominationPrize
    from ..models.fs_res_project_project_obj import FsResProjectProjectObj
    from ..models.fs_res_publication_publication import FsResPublicationPublication
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent


T = TypeVar("T", bound="FsResPrizeNominationNomination")


@_attrs_define
class FsResPrizeNominationNomination:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResPrizeNominationNominationForeigntext | Unset):
        entry_date (int | Unset):
        full_name (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        name_addition (str | Unset):
        nominated_persons (list[FsResPrizeNominationNominationPerson] | Unset):
        nomination_year (int | Unset):
        obj_guid (str | Unset):
        prize (FsResPrizeNominationPrize | Unset):
        projects (list[FsResProjectProjectObj] | Unset):
        publications (list[FsResPublicationPublication] | Unset):
        range_ (CsSysValueGenericValue | Unset):
        research_areas (list[CsSysValueGenericValue] | Unset):
        research_areas_kdsf (list[CsSysValueGenericValue] | Unset):
        share_of_university (float | Unset):
        status (CsSysValueGenericValue | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
        total_endowment (float | Unset):
        total_number_person (int | Unset):
        type_ (CsSysValueGenericValue | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResPrizeNominationNominationForeigntext | Unset = UNSET
    entry_date: int | Unset = UNSET
    full_name: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    name_addition: str | Unset = UNSET
    nominated_persons: list[FsResPrizeNominationNominationPerson] | Unset = UNSET
    nomination_year: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    prize: FsResPrizeNominationPrize | Unset = UNSET
    projects: list[FsResProjectProjectObj] | Unset = UNSET
    publications: list[FsResPublicationPublication] | Unset = UNSET
    range_: CsSysValueGenericValue | Unset = UNSET
    research_areas: list[CsSysValueGenericValue] | Unset = UNSET
    research_areas_kdsf: list[CsSysValueGenericValue] | Unset = UNSET
    share_of_university: float | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    total_endowment: float | Unset = UNSET
    total_number_person: int | Unset = UNSET
    type_: CsSysValueGenericValue | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        entry_date = self.entry_date

        full_name = self.full_name

        id = self.id

        lock_version = self.lock_version

        name_addition = self.name_addition

        nominated_persons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nominated_persons, Unset):
            nominated_persons = []
            for nominated_persons_item_data in self.nominated_persons:
                nominated_persons_item = nominated_persons_item_data.to_dict()
                nominated_persons.append(nominated_persons_item)

        nomination_year = self.nomination_year

        obj_guid = self.obj_guid

        prize: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prize, Unset):
            prize = self.prize.to_dict()

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

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

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

        share_of_university = self.share_of_university

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        total_endowment = self.total_endowment

        total_number_person = self.total_number_person

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

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
        if entry_date is not UNSET:
            field_dict["entryDate"] = entry_date
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name_addition is not UNSET:
            field_dict["nameAddition"] = name_addition
        if nominated_persons is not UNSET:
            field_dict["nominatedPersons"] = nominated_persons
        if nomination_year is not UNSET:
            field_dict["nominationYear"] = nomination_year
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if prize is not UNSET:
            field_dict["prize"] = prize
        if projects is not UNSET:
            field_dict["projects"] = projects
        if publications is not UNSET:
            field_dict["publications"] = publications
        if range_ is not UNSET:
            field_dict["range"] = range_
        if research_areas is not UNSET:
            field_dict["researchAreas"] = research_areas
        if research_areas_kdsf is not UNSET:
            field_dict["researchAreasKdsf"] = research_areas_kdsf
        if share_of_university is not UNSET:
            field_dict["shareOfUniversity"] = share_of_university
        if status is not UNSET:
            field_dict["status"] = status
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas
        if total_endowment is not UNSET:
            field_dict["totalEndowment"] = total_endowment
        if total_number_person is not UNSET:
            field_dict["totalNumberPerson"] = total_number_person
        if type_ is not UNSET:
            field_dict["type"] = type_
        if visibility_value is not UNSET:
            field_dict["visibilityValue"] = visibility_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_nomination_foreigntext import FsResPrizeNominationNominationForeigntext  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_nomination_person import FsResPrizeNominationNominationPerson  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_prize import FsResPrizeNominationPrize  # noqa: PLC0415
        from ..models.fs_res_project_project_obj import FsResProjectProjectObj  # noqa: PLC0415
        from ..models.fs_res_publication_publication import FsResPublicationPublication  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPrizeNominationNominationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPrizeNominationNominationForeigntext.from_dict(_field_foreigntext)

        entry_date = d.pop("entryDate", UNSET)

        full_name = d.pop("fullName", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name_addition = d.pop("nameAddition", UNSET)

        _nominated_persons = d.pop("nominatedPersons", UNSET)
        nominated_persons: list[FsResPrizeNominationNominationPerson] | Unset = UNSET
        if _nominated_persons is not UNSET:
            nominated_persons = []
            for nominated_persons_item_data in _nominated_persons:
                nominated_persons_item = FsResPrizeNominationNominationPerson.from_dict(nominated_persons_item_data)

                nominated_persons.append(nominated_persons_item)

        nomination_year = d.pop("nominationYear", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _prize = d.pop("prize", UNSET)
        prize: FsResPrizeNominationPrize | Unset
        if isinstance(_prize, Unset):
            prize = UNSET
        else:
            prize = FsResPrizeNominationPrize.from_dict(_prize)

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

        _range_ = d.pop("range", UNSET)
        range_: CsSysValueGenericValue | Unset
        if isinstance(_range_, Unset):
            range_ = UNSET
        else:
            range_ = CsSysValueGenericValue.from_dict(_range_)

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

        share_of_university = d.pop("shareOfUniversity", UNSET)

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

        total_endowment = d.pop("totalEndowment", UNSET)

        total_number_person = d.pop("totalNumberPerson", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CsSysValueGenericValue | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CsSysValueGenericValue.from_dict(_type_)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        fs_res_prize_nomination_nomination = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            entry_date=entry_date,
            full_name=full_name,
            id=id,
            lock_version=lock_version,
            name_addition=name_addition,
            nominated_persons=nominated_persons,
            nomination_year=nomination_year,
            obj_guid=obj_guid,
            prize=prize,
            projects=projects,
            publications=publications,
            range_=range_,
            research_areas=research_areas,
            research_areas_kdsf=research_areas_kdsf,
            share_of_university=share_of_university,
            status=status,
            subject_areas=subject_areas,
            total_endowment=total_endowment,
            total_number_person=total_number_person,
            type_=type_,
            visibility_value=visibility_value,
        )

        fs_res_prize_nomination_nomination.additional_properties = d
        return fs_res_prize_nomination_nomination

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
