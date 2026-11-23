from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_jobadvertisement_job_advertisement_contact_person import (
        RmErpJobadvertisementJobAdvertisementContactPerson,
    )
    from ..models.rm_erp_jobadvertisement_job_advertisement_foreigntext import (
        RmErpJobadvertisementJobAdvertisementForeigntext,
    )
    from ..models.rm_erp_jobadvertisement_job_advertisement_state import RmErpJobadvertisementJobAdvertisementState


T = TypeVar("T", bound="RmErpJobadvertisementJobAdvertisement")


@_attrs_define
class RmErpJobadvertisementJobAdvertisement:
    """
    Attributes:
        field_foreigntext (RmErpJobadvertisementJobAdvertisementForeigntext | Unset):
        description (str | Unset):
        first_contact_person (RmErpJobadvertisementJobAdvertisementContactPerson | Unset):
        id (int | Unset):
        internal_job_ad (bool | Unset):
        job_ad_state (list[RmErpJobadvertisementJobAdvertisementState] | Unset):
        job_advertisement_category (RmErpCommonErpGenericValue | Unset):
        job_advertisement_document_available (bool | Unset):
        job_join_id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        online_application_possible (bool | Unset):
        ref_number (str | Unset):
        sas_text_format (str | Unset):
        second_contact_person (RmErpJobadvertisementJobAdvertisementContactPerson | Unset):
        short_description (str | Unset):
        status (int | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: RmErpJobadvertisementJobAdvertisementForeigntext | Unset = UNSET
    description: str | Unset = UNSET
    first_contact_person: RmErpJobadvertisementJobAdvertisementContactPerson | Unset = UNSET
    id: int | Unset = UNSET
    internal_job_ad: bool | Unset = UNSET
    job_ad_state: list[RmErpJobadvertisementJobAdvertisementState] | Unset = UNSET
    job_advertisement_category: RmErpCommonErpGenericValue | Unset = UNSET
    job_advertisement_document_available: bool | Unset = UNSET
    job_join_id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    online_application_possible: bool | Unset = UNSET
    ref_number: str | Unset = UNSET
    sas_text_format: str | Unset = UNSET
    second_contact_person: RmErpJobadvertisementJobAdvertisementContactPerson | Unset = UNSET
    short_description: str | Unset = UNSET
    status: int | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        description = self.description

        first_contact_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_contact_person, Unset):
            first_contact_person = self.first_contact_person.to_dict()

        id = self.id

        internal_job_ad = self.internal_job_ad

        job_ad_state: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job_ad_state, Unset):
            job_ad_state = []
            for job_ad_state_item_data in self.job_ad_state:
                job_ad_state_item = job_ad_state_item_data.to_dict()
                job_ad_state.append(job_ad_state_item)

        job_advertisement_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_advertisement_category, Unset):
            job_advertisement_category = self.job_advertisement_category.to_dict()

        job_advertisement_document_available = self.job_advertisement_document_available

        job_join_id = self.job_join_id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        online_application_possible = self.online_application_possible

        ref_number = self.ref_number

        sas_text_format = self.sas_text_format

        second_contact_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.second_contact_person, Unset):
            second_contact_person = self.second_contact_person.to_dict()

        short_description = self.short_description

        status = self.status

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if description is not UNSET:
            field_dict["description"] = description
        if first_contact_person is not UNSET:
            field_dict["firstContactPerson"] = first_contact_person
        if id is not UNSET:
            field_dict["id"] = id
        if internal_job_ad is not UNSET:
            field_dict["internalJobAd"] = internal_job_ad
        if job_ad_state is not UNSET:
            field_dict["jobAdState"] = job_ad_state
        if job_advertisement_category is not UNSET:
            field_dict["jobAdvertisementCategory"] = job_advertisement_category
        if job_advertisement_document_available is not UNSET:
            field_dict["jobAdvertisementDocumentAvailable"] = job_advertisement_document_available
        if job_join_id is not UNSET:
            field_dict["jobJoinId"] = job_join_id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if online_application_possible is not UNSET:
            field_dict["onlineApplicationPossible"] = online_application_possible
        if ref_number is not UNSET:
            field_dict["refNumber"] = ref_number
        if sas_text_format is not UNSET:
            field_dict["sasTextFormat"] = sas_text_format
        if second_contact_person is not UNSET:
            field_dict["secondContactPerson"] = second_contact_person
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if status is not UNSET:
            field_dict["status"] = status
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_jobadvertisement_job_advertisement_contact_person import (
            RmErpJobadvertisementJobAdvertisementContactPerson,  # noqa: PLC0415
        )
        from ..models.rm_erp_jobadvertisement_job_advertisement_foreigntext import (
            RmErpJobadvertisementJobAdvertisementForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_jobadvertisement_job_advertisement_state import RmErpJobadvertisementJobAdvertisementState  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpJobadvertisementJobAdvertisementForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpJobadvertisementJobAdvertisementForeigntext.from_dict(_field_foreigntext)

        description = d.pop("description", UNSET)

        _first_contact_person = d.pop("firstContactPerson", UNSET)
        first_contact_person: RmErpJobadvertisementJobAdvertisementContactPerson | Unset
        if isinstance(_first_contact_person, Unset):
            first_contact_person = UNSET
        else:
            first_contact_person = RmErpJobadvertisementJobAdvertisementContactPerson.from_dict(_first_contact_person)

        id = d.pop("id", UNSET)

        internal_job_ad = d.pop("internalJobAd", UNSET)

        _job_ad_state = d.pop("jobAdState", UNSET)
        job_ad_state: list[RmErpJobadvertisementJobAdvertisementState] | Unset = UNSET
        if _job_ad_state is not UNSET:
            job_ad_state = []
            for job_ad_state_item_data in _job_ad_state:
                job_ad_state_item = RmErpJobadvertisementJobAdvertisementState.from_dict(job_ad_state_item_data)

                job_ad_state.append(job_ad_state_item)

        _job_advertisement_category = d.pop("jobAdvertisementCategory", UNSET)
        job_advertisement_category: RmErpCommonErpGenericValue | Unset
        if isinstance(_job_advertisement_category, Unset):
            job_advertisement_category = UNSET
        else:
            job_advertisement_category = RmErpCommonErpGenericValue.from_dict(_job_advertisement_category)

        job_advertisement_document_available = d.pop("jobAdvertisementDocumentAvailable", UNSET)

        job_join_id = d.pop("jobJoinId", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        online_application_possible = d.pop("onlineApplicationPossible", UNSET)

        ref_number = d.pop("refNumber", UNSET)

        sas_text_format = d.pop("sasTextFormat", UNSET)

        _second_contact_person = d.pop("secondContactPerson", UNSET)
        second_contact_person: RmErpJobadvertisementJobAdvertisementContactPerson | Unset
        if isinstance(_second_contact_person, Unset):
            second_contact_person = UNSET
        else:
            second_contact_person = RmErpJobadvertisementJobAdvertisementContactPerson.from_dict(_second_contact_person)

        short_description = d.pop("shortDescription", UNSET)

        status = d.pop("status", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        rm_erp_jobadvertisement_job_advertisement = cls(
            field_foreigntext=field_foreigntext,
            description=description,
            first_contact_person=first_contact_person,
            id=id,
            internal_job_ad=internal_job_ad,
            job_ad_state=job_ad_state,
            job_advertisement_category=job_advertisement_category,
            job_advertisement_document_available=job_advertisement_document_available,
            job_join_id=job_join_id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            online_application_possible=online_application_possible,
            ref_number=ref_number,
            sas_text_format=sas_text_format,
            second_contact_person=second_contact_person,
            short_description=short_description,
            status=status,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        rm_erp_jobadvertisement_job_advertisement.additional_properties = d
        return rm_erp_jobadvertisement_job_advertisement

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
