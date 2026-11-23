from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_document_document_info import RmErpCommonDocumentDocumentInfo
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_person_educational_attainment_value import RmErpCommonPersonEducationalAttainmentValue
    from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue
    from ..models.rm_erp_common_person_marital_status_value import RmErpCommonPersonMaritalStatusValue
    from ..models.rm_erp_common_person_official_designation_value import RmErpCommonPersonOfficialDesignationValue
    from ..models.rm_erp_employment_employment_part_time_type_value import RmErpEmploymentEmploymentPartTimeTypeValue
    from ..models.rm_erp_jobapplication_job_application_content_foreigntext import (
        RmErpJobapplicationJobApplicationContentForeigntext,
    )


T = TypeVar("T", bound="RmErpJobapplicationJobApplicationContent")


@_attrs_define
class RmErpJobapplicationJobApplicationContent:
    """
    Attributes:
        field_foreigntext (RmErpJobapplicationJobApplicationContentForeigntext | Unset):
        academic_degree (RmErpCommonErpGenericValue | Unset):
        additional_name (str | Unset):
        address_supplement (str | Unset):
        application_date (int | Unset):
        birth_date (int | Unset):
        city (str | Unset):
        country (RmErpCommonPersonErpCountryValue | Unset):
        disability (bool | Unset):
        disability_in_percent (int | Unset):
        documents (list[RmErpCommonDocumentDocumentInfo] | Unset):
        earliest_commencement_date (int | Unset):
        educational_attainment (RmErpCommonPersonEducationalAttainmentValue | Unset):
        emailaddress (str | Unset):
        final_grade (float | Unset):
        firstname (str | Unset):
        gender (RmErpCommonErpGenericValue | Unset):
        id (int | Unset):
        information_source (RmErpCommonErpGenericValue | Unset):
        internal_application (bool | Unset):
        job_advertisement_id (int | Unset):
        lock_version (int | Unset):
        marital_status (RmErpCommonPersonMaritalStatusValue | Unset):
        mobile_number (str | Unset):
        nationality (RmErpCommonPersonErpCountryValue | Unset):
        obj_guid (str | Unset):
        official_designation (RmErpCommonPersonOfficialDesignationValue | Unset):
        part_time_scope (float | Unset):
        part_time_type (RmErpEmploymentEmploymentPartTimeTypeValue | Unset):
        parttime (bool | Unset):
        phone_number (str | Unset):
        postcode (str | Unset):
        salary_requirements (float | Unset):
        street (str | Unset):
        surname (str | Unset):
        title (RmErpCommonErpGenericValue | Unset):
        unemployed (bool | Unset):
    """

    field_foreigntext: RmErpJobapplicationJobApplicationContentForeigntext | Unset = UNSET
    academic_degree: RmErpCommonErpGenericValue | Unset = UNSET
    additional_name: str | Unset = UNSET
    address_supplement: str | Unset = UNSET
    application_date: int | Unset = UNSET
    birth_date: int | Unset = UNSET
    city: str | Unset = UNSET
    country: RmErpCommonPersonErpCountryValue | Unset = UNSET
    disability: bool | Unset = UNSET
    disability_in_percent: int | Unset = UNSET
    documents: list[RmErpCommonDocumentDocumentInfo] | Unset = UNSET
    earliest_commencement_date: int | Unset = UNSET
    educational_attainment: RmErpCommonPersonEducationalAttainmentValue | Unset = UNSET
    emailaddress: str | Unset = UNSET
    final_grade: float | Unset = UNSET
    firstname: str | Unset = UNSET
    gender: RmErpCommonErpGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    information_source: RmErpCommonErpGenericValue | Unset = UNSET
    internal_application: bool | Unset = UNSET
    job_advertisement_id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    marital_status: RmErpCommonPersonMaritalStatusValue | Unset = UNSET
    mobile_number: str | Unset = UNSET
    nationality: RmErpCommonPersonErpCountryValue | Unset = UNSET
    obj_guid: str | Unset = UNSET
    official_designation: RmErpCommonPersonOfficialDesignationValue | Unset = UNSET
    part_time_scope: float | Unset = UNSET
    part_time_type: RmErpEmploymentEmploymentPartTimeTypeValue | Unset = UNSET
    parttime: bool | Unset = UNSET
    phone_number: str | Unset = UNSET
    postcode: str | Unset = UNSET
    salary_requirements: float | Unset = UNSET
    street: str | Unset = UNSET
    surname: str | Unset = UNSET
    title: RmErpCommonErpGenericValue | Unset = UNSET
    unemployed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        academic_degree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.academic_degree, Unset):
            academic_degree = self.academic_degree.to_dict()

        additional_name = self.additional_name

        address_supplement = self.address_supplement

        application_date = self.application_date

        birth_date = self.birth_date

        city = self.city

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        disability = self.disability

        disability_in_percent = self.disability_in_percent

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        earliest_commencement_date = self.earliest_commencement_date

        educational_attainment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.educational_attainment, Unset):
            educational_attainment = self.educational_attainment.to_dict()

        emailaddress = self.emailaddress

        final_grade = self.final_grade

        firstname = self.firstname

        gender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        id = self.id

        information_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.information_source, Unset):
            information_source = self.information_source.to_dict()

        internal_application = self.internal_application

        job_advertisement_id = self.job_advertisement_id

        lock_version = self.lock_version

        marital_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marital_status, Unset):
            marital_status = self.marital_status.to_dict()

        mobile_number = self.mobile_number

        nationality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nationality, Unset):
            nationality = self.nationality.to_dict()

        obj_guid = self.obj_guid

        official_designation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.official_designation, Unset):
            official_designation = self.official_designation.to_dict()

        part_time_scope = self.part_time_scope

        part_time_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_time_type, Unset):
            part_time_type = self.part_time_type.to_dict()

        parttime = self.parttime

        phone_number = self.phone_number

        postcode = self.postcode

        salary_requirements = self.salary_requirements

        street = self.street

        surname = self.surname

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        unemployed = self.unemployed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if academic_degree is not UNSET:
            field_dict["academicDegree"] = academic_degree
        if additional_name is not UNSET:
            field_dict["additionalName"] = additional_name
        if address_supplement is not UNSET:
            field_dict["addressSupplement"] = address_supplement
        if application_date is not UNSET:
            field_dict["applicationDate"] = application_date
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if disability is not UNSET:
            field_dict["disability"] = disability
        if disability_in_percent is not UNSET:
            field_dict["disabilityInPercent"] = disability_in_percent
        if documents is not UNSET:
            field_dict["documents"] = documents
        if earliest_commencement_date is not UNSET:
            field_dict["earliestCommencementDate"] = earliest_commencement_date
        if educational_attainment is not UNSET:
            field_dict["educationalAttainment"] = educational_attainment
        if emailaddress is not UNSET:
            field_dict["emailaddress"] = emailaddress
        if final_grade is not UNSET:
            field_dict["finalGrade"] = final_grade
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if gender is not UNSET:
            field_dict["gender"] = gender
        if id is not UNSET:
            field_dict["id"] = id
        if information_source is not UNSET:
            field_dict["informationSource"] = information_source
        if internal_application is not UNSET:
            field_dict["internalApplication"] = internal_application
        if job_advertisement_id is not UNSET:
            field_dict["jobAdvertisementId"] = job_advertisement_id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if marital_status is not UNSET:
            field_dict["maritalStatus"] = marital_status
        if mobile_number is not UNSET:
            field_dict["mobileNumber"] = mobile_number
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if official_designation is not UNSET:
            field_dict["officialDesignation"] = official_designation
        if part_time_scope is not UNSET:
            field_dict["partTimeScope"] = part_time_scope
        if part_time_type is not UNSET:
            field_dict["partTimeType"] = part_time_type
        if parttime is not UNSET:
            field_dict["parttime"] = parttime
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if salary_requirements is not UNSET:
            field_dict["salaryRequirements"] = salary_requirements
        if street is not UNSET:
            field_dict["street"] = street
        if surname is not UNSET:
            field_dict["surname"] = surname
        if title is not UNSET:
            field_dict["title"] = title
        if unemployed is not UNSET:
            field_dict["unemployed"] = unemployed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_document_document_info import RmErpCommonDocumentDocumentInfo  # noqa: PLC0415
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_educational_attainment_value import (
            RmErpCommonPersonEducationalAttainmentValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_marital_status_value import RmErpCommonPersonMaritalStatusValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_official_designation_value import RmErpCommonPersonOfficialDesignationValue  # noqa: PLC0415
        from ..models.rm_erp_employment_employment_part_time_type_value import (
            RmErpEmploymentEmploymentPartTimeTypeValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_jobapplication_job_application_content_foreigntext import (
            RmErpJobapplicationJobApplicationContentForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpJobapplicationJobApplicationContentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpJobapplicationJobApplicationContentForeigntext.from_dict(_field_foreigntext)

        _academic_degree = d.pop("academicDegree", UNSET)
        academic_degree: RmErpCommonErpGenericValue | Unset
        if isinstance(_academic_degree, Unset):
            academic_degree = UNSET
        else:
            academic_degree = RmErpCommonErpGenericValue.from_dict(_academic_degree)

        additional_name = d.pop("additionalName", UNSET)

        address_supplement = d.pop("addressSupplement", UNSET)

        application_date = d.pop("applicationDate", UNSET)

        birth_date = d.pop("birthDate", UNSET)

        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: RmErpCommonPersonErpCountryValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = RmErpCommonPersonErpCountryValue.from_dict(_country)

        disability = d.pop("disability", UNSET)

        disability_in_percent = d.pop("disabilityInPercent", UNSET)

        _documents = d.pop("documents", UNSET)
        documents: list[RmErpCommonDocumentDocumentInfo] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RmErpCommonDocumentDocumentInfo.from_dict(documents_item_data)

                documents.append(documents_item)

        earliest_commencement_date = d.pop("earliestCommencementDate", UNSET)

        _educational_attainment = d.pop("educationalAttainment", UNSET)
        educational_attainment: RmErpCommonPersonEducationalAttainmentValue | Unset
        if isinstance(_educational_attainment, Unset):
            educational_attainment = UNSET
        else:
            educational_attainment = RmErpCommonPersonEducationalAttainmentValue.from_dict(_educational_attainment)

        emailaddress = d.pop("emailaddress", UNSET)

        final_grade = d.pop("finalGrade", UNSET)

        firstname = d.pop("firstname", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: RmErpCommonErpGenericValue | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = RmErpCommonErpGenericValue.from_dict(_gender)

        id = d.pop("id", UNSET)

        _information_source = d.pop("informationSource", UNSET)
        information_source: RmErpCommonErpGenericValue | Unset
        if isinstance(_information_source, Unset):
            information_source = UNSET
        else:
            information_source = RmErpCommonErpGenericValue.from_dict(_information_source)

        internal_application = d.pop("internalApplication", UNSET)

        job_advertisement_id = d.pop("jobAdvertisementId", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        _marital_status = d.pop("maritalStatus", UNSET)
        marital_status: RmErpCommonPersonMaritalStatusValue | Unset
        if isinstance(_marital_status, Unset):
            marital_status = UNSET
        else:
            marital_status = RmErpCommonPersonMaritalStatusValue.from_dict(_marital_status)

        mobile_number = d.pop("mobileNumber", UNSET)

        _nationality = d.pop("nationality", UNSET)
        nationality: RmErpCommonPersonErpCountryValue | Unset
        if isinstance(_nationality, Unset):
            nationality = UNSET
        else:
            nationality = RmErpCommonPersonErpCountryValue.from_dict(_nationality)

        obj_guid = d.pop("objGuid", UNSET)

        _official_designation = d.pop("officialDesignation", UNSET)
        official_designation: RmErpCommonPersonOfficialDesignationValue | Unset
        if isinstance(_official_designation, Unset):
            official_designation = UNSET
        else:
            official_designation = RmErpCommonPersonOfficialDesignationValue.from_dict(_official_designation)

        part_time_scope = d.pop("partTimeScope", UNSET)

        _part_time_type = d.pop("partTimeType", UNSET)
        part_time_type: RmErpEmploymentEmploymentPartTimeTypeValue | Unset
        if isinstance(_part_time_type, Unset):
            part_time_type = UNSET
        else:
            part_time_type = RmErpEmploymentEmploymentPartTimeTypeValue.from_dict(_part_time_type)

        parttime = d.pop("parttime", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        postcode = d.pop("postcode", UNSET)

        salary_requirements = d.pop("salaryRequirements", UNSET)

        street = d.pop("street", UNSET)

        surname = d.pop("surname", UNSET)

        _title = d.pop("title", UNSET)
        title: RmErpCommonErpGenericValue | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = RmErpCommonErpGenericValue.from_dict(_title)

        unemployed = d.pop("unemployed", UNSET)

        rm_erp_jobapplication_job_application_content = cls(
            field_foreigntext=field_foreigntext,
            academic_degree=academic_degree,
            additional_name=additional_name,
            address_supplement=address_supplement,
            application_date=application_date,
            birth_date=birth_date,
            city=city,
            country=country,
            disability=disability,
            disability_in_percent=disability_in_percent,
            documents=documents,
            earliest_commencement_date=earliest_commencement_date,
            educational_attainment=educational_attainment,
            emailaddress=emailaddress,
            final_grade=final_grade,
            firstname=firstname,
            gender=gender,
            id=id,
            information_source=information_source,
            internal_application=internal_application,
            job_advertisement_id=job_advertisement_id,
            lock_version=lock_version,
            marital_status=marital_status,
            mobile_number=mobile_number,
            nationality=nationality,
            obj_guid=obj_guid,
            official_designation=official_designation,
            part_time_scope=part_time_scope,
            part_time_type=part_time_type,
            parttime=parttime,
            phone_number=phone_number,
            postcode=postcode,
            salary_requirements=salary_requirements,
            street=street,
            surname=surname,
            title=title,
            unemployed=unemployed,
        )

        rm_erp_jobapplication_job_application_content.additional_properties = d
        return rm_erp_jobapplication_job_application_content

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
