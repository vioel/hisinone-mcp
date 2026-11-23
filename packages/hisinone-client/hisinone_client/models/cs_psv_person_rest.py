from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_academic_degree_value import CsPsvAcademicDegreeValue
    from ..models.cs_psv_person_rest_foreigntext_type_0 import CsPsvPersonRestForeigntextType0
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPersonRest")


@_attrs_define
class CsPsvPersonRest:
    """
    Attributes:
        field_foreigntext (CsPsvPersonRestForeigntextType0 | None | Unset):
        academicdegree (CsPsvAcademicDegreeValue | None | Unset):
        academicdegreesuffix (None | str | Unset):
        allfirstnames (None | str | Unset):
        birthcity (None | str | Unset):
        birthdate (int | None | Unset):
        birthname (None | str | Unset):
        country (CsSysValueGenericValue | None | Unset):
        firstname (str | Unset):
        gender (CsSysValueGenericValue | None | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        nameprefix (None | str | Unset):
        namesuffix (None | str | Unset):
        obj_guid (None | str | Unset):
        person_complete_name (None | str | Unset):
        surname (str | Unset):
        title (CsSysValueGenericValue | None | Unset):
    """

    field_foreigntext: CsPsvPersonRestForeigntextType0 | None | Unset = UNSET
    academicdegree: CsPsvAcademicDegreeValue | None | Unset = UNSET
    academicdegreesuffix: None | str | Unset = UNSET
    allfirstnames: None | str | Unset = UNSET
    birthcity: None | str | Unset = UNSET
    birthdate: int | None | Unset = UNSET
    birthname: None | str | Unset = UNSET
    country: CsSysValueGenericValue | None | Unset = UNSET
    firstname: str | Unset = UNSET
    gender: CsSysValueGenericValue | None | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    nameprefix: None | str | Unset = UNSET
    namesuffix: None | str | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    person_complete_name: None | str | Unset = UNSET
    surname: str | Unset = UNSET
    title: CsSysValueGenericValue | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.cs_psv_academic_degree_value import CsPsvAcademicDegreeValue  # noqa: PLC0415
        from ..models.cs_psv_person_rest_foreigntext_type_0 import CsPsvPersonRestForeigntextType0  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, CsPsvPersonRestForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        academicdegree: dict[str, Any] | None | Unset
        if isinstance(self.academicdegree, Unset):
            academicdegree = UNSET
        elif isinstance(self.academicdegree, CsPsvAcademicDegreeValue):
            academicdegree = self.academicdegree.to_dict()
        else:
            academicdegree = self.academicdegree

        academicdegreesuffix: None | str | Unset
        if isinstance(self.academicdegreesuffix, Unset):
            academicdegreesuffix = UNSET
        else:
            academicdegreesuffix = self.academicdegreesuffix

        allfirstnames: None | str | Unset
        if isinstance(self.allfirstnames, Unset):
            allfirstnames = UNSET
        else:
            allfirstnames = self.allfirstnames

        birthcity: None | str | Unset
        if isinstance(self.birthcity, Unset):
            birthcity = UNSET
        else:
            birthcity = self.birthcity

        birthdate: int | None | Unset
        if isinstance(self.birthdate, Unset):
            birthdate = UNSET
        else:
            birthdate = self.birthdate

        birthname: None | str | Unset
        if isinstance(self.birthname, Unset):
            birthname = UNSET
        else:
            birthname = self.birthname

        country: dict[str, Any] | None | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        elif isinstance(self.country, CsSysValueGenericValue):
            country = self.country.to_dict()
        else:
            country = self.country

        firstname = self.firstname

        gender: dict[str, Any] | None | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        elif isinstance(self.gender, CsSysValueGenericValue):
            gender = self.gender.to_dict()
        else:
            gender = self.gender

        id = self.id

        lock_version = self.lock_version

        nameprefix: None | str | Unset
        if isinstance(self.nameprefix, Unset):
            nameprefix = UNSET
        else:
            nameprefix = self.nameprefix

        namesuffix: None | str | Unset
        if isinstance(self.namesuffix, Unset):
            namesuffix = UNSET
        else:
            namesuffix = self.namesuffix

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        person_complete_name: None | str | Unset
        if isinstance(self.person_complete_name, Unset):
            person_complete_name = UNSET
        else:
            person_complete_name = self.person_complete_name

        surname = self.surname

        title: dict[str, Any] | None | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        elif isinstance(self.title, CsSysValueGenericValue):
            title = self.title.to_dict()
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if academicdegree is not UNSET:
            field_dict["academicdegree"] = academicdegree
        if academicdegreesuffix is not UNSET:
            field_dict["academicdegreesuffix"] = academicdegreesuffix
        if allfirstnames is not UNSET:
            field_dict["allfirstnames"] = allfirstnames
        if birthcity is not UNSET:
            field_dict["birthcity"] = birthcity
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if birthname is not UNSET:
            field_dict["birthname"] = birthname
        if country is not UNSET:
            field_dict["country"] = country
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if gender is not UNSET:
            field_dict["gender"] = gender
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if nameprefix is not UNSET:
            field_dict["nameprefix"] = nameprefix
        if namesuffix is not UNSET:
            field_dict["namesuffix"] = namesuffix
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person_complete_name is not UNSET:
            field_dict["personCompleteName"] = person_complete_name
        if surname is not UNSET:
            field_dict["surname"] = surname
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_academic_degree_value import CsPsvAcademicDegreeValue  # noqa: PLC0415
        from ..models.cs_psv_person_rest_foreigntext_type_0 import CsPsvPersonRestForeigntextType0  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_field_foreigntext(data: object) -> CsPsvPersonRestForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = CsPsvPersonRestForeigntextType0.from_dict(cast(dict[str, Any], data))

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        def _parse_academicdegree(data: object) -> CsPsvAcademicDegreeValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            academicdegree_type_0 = CsPsvAcademicDegreeValue.from_dict(cast(dict[str, Any], data))

            return academicdegree_type_0

        academicdegree = _parse_academicdegree(d.pop("academicdegree", UNSET))

        def _parse_academicdegreesuffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academicdegreesuffix = _parse_academicdegreesuffix(d.pop("academicdegreesuffix", UNSET))

        def _parse_allfirstnames(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        allfirstnames = _parse_allfirstnames(d.pop("allfirstnames", UNSET))

        def _parse_birthcity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        birthcity = _parse_birthcity(d.pop("birthcity", UNSET))

        def _parse_birthdate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        birthdate = _parse_birthdate(d.pop("birthdate", UNSET))

        def _parse_birthname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        birthname = _parse_birthname(d.pop("birthname", UNSET))

        def _parse_country(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            country_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return country_type_0

        country = _parse_country(d.pop("country", UNSET))

        firstname = d.pop("firstname", UNSET)

        def _parse_gender(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            gender_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return gender_type_0

        gender = _parse_gender(d.pop("gender", UNSET))

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_nameprefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nameprefix = _parse_nameprefix(d.pop("nameprefix", UNSET))

        def _parse_namesuffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namesuffix = _parse_namesuffix(d.pop("namesuffix", UNSET))

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        def _parse_person_complete_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        person_complete_name = _parse_person_complete_name(d.pop("personCompleteName", UNSET))

        surname = d.pop("surname", UNSET)

        def _parse_title(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            title_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return title_type_0

        title = _parse_title(d.pop("title", UNSET))

        cs_psv_person_rest = cls(
            field_foreigntext=field_foreigntext,
            academicdegree=academicdegree,
            academicdegreesuffix=academicdegreesuffix,
            allfirstnames=allfirstnames,
            birthcity=birthcity,
            birthdate=birthdate,
            birthname=birthname,
            country=country,
            firstname=firstname,
            gender=gender,
            id=id,
            lock_version=lock_version,
            nameprefix=nameprefix,
            namesuffix=namesuffix,
            obj_guid=obj_guid,
            person_complete_name=person_complete_name,
            surname=surname,
            title=title,
        )

        cs_psv_person_rest.additional_properties = d
        return cs_psv_person_rest

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
