from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_academic_degree_value import CsPsvAcademicDegreeValue
    from ..models.cs_psv_address_rest import CsPsvAddressRest
    from ..models.cs_psv_psv_person_profile_extended_data import CsPsvPsvPersonProfileExtendedData
    from ..models.cs_psv_psv_person_profile_foreigntext import CsPsvPsvPersonProfileForeigntext
    from ..models.cs_psv_psv_person_profile_person_attributes import CsPsvPsvPersonProfilePersonAttributes
    from ..models.cs_psv_psv_profile_affiliation import CsPsvPsvProfileAffiliation
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPsvPersonProfile")


@_attrs_define
class CsPsvPsvPersonProfile:
    """
    Attributes:
        field_foreigntext (CsPsvPsvPersonProfileForeigntext | Unset):
        academicdegree (CsPsvAcademicDegreeValue | Unset):
        academicdegreesuffix (str | Unset):
        addresses (list[CsPsvAddressRest] | Unset):
        affiliations (list[CsPsvPsvProfileAffiliation] | Unset):
        allfirstnames (str | Unset):
        birthcity (str | Unset):
        birthdate (int | Unset):
        birthname (str | Unset):
        country (CsSysValueGenericValue | Unset):
        extended_data (CsPsvPsvPersonProfileExtendedData | Unset):
        firstname (str | Unset):
        gender (CsSysValueGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        nameprefix (str | Unset):
        namesuffix (str | Unset):
        obj_guid (str | Unset):
        person_attributes (CsPsvPsvPersonProfilePersonAttributes | Unset):
        person_complete_name (str | Unset):
        surname (str | Unset):
        title (CsSysValueGenericValue | Unset):
    """

    field_foreigntext: CsPsvPsvPersonProfileForeigntext | Unset = UNSET
    academicdegree: CsPsvAcademicDegreeValue | Unset = UNSET
    academicdegreesuffix: str | Unset = UNSET
    addresses: list[CsPsvAddressRest] | Unset = UNSET
    affiliations: list[CsPsvPsvProfileAffiliation] | Unset = UNSET
    allfirstnames: str | Unset = UNSET
    birthcity: str | Unset = UNSET
    birthdate: int | Unset = UNSET
    birthname: str | Unset = UNSET
    country: CsSysValueGenericValue | Unset = UNSET
    extended_data: CsPsvPsvPersonProfileExtendedData | Unset = UNSET
    firstname: str | Unset = UNSET
    gender: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    nameprefix: str | Unset = UNSET
    namesuffix: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person_attributes: CsPsvPsvPersonProfilePersonAttributes | Unset = UNSET
    person_complete_name: str | Unset = UNSET
    surname: str | Unset = UNSET
    title: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        academicdegree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.academicdegree, Unset):
            academicdegree = self.academicdegree.to_dict()

        academicdegreesuffix = self.academicdegreesuffix

        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        affiliations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.affiliations, Unset):
            affiliations = []
            for affiliations_item_data in self.affiliations:
                affiliations_item = affiliations_item_data.to_dict()
                affiliations.append(affiliations_item)

        allfirstnames = self.allfirstnames

        birthcity = self.birthcity

        birthdate = self.birthdate

        birthname = self.birthname

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        extended_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extended_data, Unset):
            extended_data = self.extended_data.to_dict()

        firstname = self.firstname

        gender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        id = self.id

        lock_version = self.lock_version

        nameprefix = self.nameprefix

        namesuffix = self.namesuffix

        obj_guid = self.obj_guid

        person_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person_attributes, Unset):
            person_attributes = self.person_attributes.to_dict()

        person_complete_name = self.person_complete_name

        surname = self.surname

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if academicdegree is not UNSET:
            field_dict["academicdegree"] = academicdegree
        if academicdegreesuffix is not UNSET:
            field_dict["academicdegreesuffix"] = academicdegreesuffix
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if affiliations is not UNSET:
            field_dict["affiliations"] = affiliations
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
        if extended_data is not UNSET:
            field_dict["extendedData"] = extended_data
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
        if person_attributes is not UNSET:
            field_dict["personAttributes"] = person_attributes
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
        from ..models.cs_psv_address_rest import CsPsvAddressRest  # noqa: PLC0415
        from ..models.cs_psv_psv_person_profile_extended_data import CsPsvPsvPersonProfileExtendedData  # noqa: PLC0415
        from ..models.cs_psv_psv_person_profile_foreigntext import CsPsvPsvPersonProfileForeigntext  # noqa: PLC0415
        from ..models.cs_psv_psv_person_profile_person_attributes import CsPsvPsvPersonProfilePersonAttributes  # noqa: PLC0415
        from ..models.cs_psv_psv_profile_affiliation import CsPsvPsvProfileAffiliation  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPsvPersonProfileForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPsvPersonProfileForeigntext.from_dict(_field_foreigntext)

        _academicdegree = d.pop("academicdegree", UNSET)
        academicdegree: CsPsvAcademicDegreeValue | Unset
        if isinstance(_academicdegree, Unset):
            academicdegree = UNSET
        else:
            academicdegree = CsPsvAcademicDegreeValue.from_dict(_academicdegree)

        academicdegreesuffix = d.pop("academicdegreesuffix", UNSET)

        _addresses = d.pop("addresses", UNSET)
        addresses: list[CsPsvAddressRest] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = CsPsvAddressRest.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        _affiliations = d.pop("affiliations", UNSET)
        affiliations: list[CsPsvPsvProfileAffiliation] | Unset = UNSET
        if _affiliations is not UNSET:
            affiliations = []
            for affiliations_item_data in _affiliations:
                affiliations_item = CsPsvPsvProfileAffiliation.from_dict(affiliations_item_data)

                affiliations.append(affiliations_item)

        allfirstnames = d.pop("allfirstnames", UNSET)

        birthcity = d.pop("birthcity", UNSET)

        birthdate = d.pop("birthdate", UNSET)

        birthname = d.pop("birthname", UNSET)

        _country = d.pop("country", UNSET)
        country: CsSysValueGenericValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = CsSysValueGenericValue.from_dict(_country)

        _extended_data = d.pop("extendedData", UNSET)
        extended_data: CsPsvPsvPersonProfileExtendedData | Unset
        if isinstance(_extended_data, Unset):
            extended_data = UNSET
        else:
            extended_data = CsPsvPsvPersonProfileExtendedData.from_dict(_extended_data)

        firstname = d.pop("firstname", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: CsSysValueGenericValue | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = CsSysValueGenericValue.from_dict(_gender)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        nameprefix = d.pop("nameprefix", UNSET)

        namesuffix = d.pop("namesuffix", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _person_attributes = d.pop("personAttributes", UNSET)
        person_attributes: CsPsvPsvPersonProfilePersonAttributes | Unset
        if isinstance(_person_attributes, Unset):
            person_attributes = UNSET
        else:
            person_attributes = CsPsvPsvPersonProfilePersonAttributes.from_dict(_person_attributes)

        person_complete_name = d.pop("personCompleteName", UNSET)

        surname = d.pop("surname", UNSET)

        _title = d.pop("title", UNSET)
        title: CsSysValueGenericValue | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = CsSysValueGenericValue.from_dict(_title)

        cs_psv_psv_person_profile = cls(
            field_foreigntext=field_foreigntext,
            academicdegree=academicdegree,
            academicdegreesuffix=academicdegreesuffix,
            addresses=addresses,
            affiliations=affiliations,
            allfirstnames=allfirstnames,
            birthcity=birthcity,
            birthdate=birthdate,
            birthname=birthname,
            country=country,
            extended_data=extended_data,
            firstname=firstname,
            gender=gender,
            id=id,
            lock_version=lock_version,
            nameprefix=nameprefix,
            namesuffix=namesuffix,
            obj_guid=obj_guid,
            person_attributes=person_attributes,
            person_complete_name=person_complete_name,
            surname=surname,
            title=title,
        )

        cs_psv_psv_person_profile.additional_properties = d
        return cs_psv_psv_person_profile

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
