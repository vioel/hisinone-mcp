from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_institute_erp_institute_foreigntext import RmErpCommonInstituteErpInstituteForeigntext
    from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue


T = TypeVar("T", bound="RmErpCommonInstituteErpInstitute")


@_attrs_define
class RmErpCommonInstituteErpInstitute:
    """
    Attributes:
        field_foreigntext (RmErpCommonInstituteErpInstituteForeigntext | Unset):
        bau_relevant (str | Unset):
        bes_relevant (str | Unset):
        building (str | Unset):
        city (str | Unset):
        cob_relevant (str | Unset):
        contact_person_inventory (str | Unset):
        contact_person_inventory_fax (str | Unset):
        contact_person_inventory_mail (str | Unset):
        contact_person_inventory_phone (str | Unset):
        contact_person_procurement (str | Unset):
        contact_person_procurement_fax (str | Unset):
        contact_person_procurement_mail (str | Unset):
        contact_person_procurement_phone (str | Unset):
        default_name (str | Unset):
        erp_country (RmErpCommonPersonErpCountryValue | Unset):
        id (int | Unset):
        institute_number (str | Unset):
        ivs_relevant (str | Unset):
        lock_version (int | Unset):
        long_name_one (str | Unset):
        long_name_two (str | Unset):
        lsf_relevant (str | Unset):
        mbs_relevant (str | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
        room (str | Unset):
        short_name (str | Unset):
        street (str | Unset):
        superordinate_institute_number (str | Unset):
        sva_relevant (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
        zip_ (str | Unset):
    """

    field_foreigntext: RmErpCommonInstituteErpInstituteForeigntext | Unset = UNSET
    bau_relevant: str | Unset = UNSET
    bes_relevant: str | Unset = UNSET
    building: str | Unset = UNSET
    city: str | Unset = UNSET
    cob_relevant: str | Unset = UNSET
    contact_person_inventory: str | Unset = UNSET
    contact_person_inventory_fax: str | Unset = UNSET
    contact_person_inventory_mail: str | Unset = UNSET
    contact_person_inventory_phone: str | Unset = UNSET
    contact_person_procurement: str | Unset = UNSET
    contact_person_procurement_fax: str | Unset = UNSET
    contact_person_procurement_mail: str | Unset = UNSET
    contact_person_procurement_phone: str | Unset = UNSET
    default_name: str | Unset = UNSET
    erp_country: RmErpCommonPersonErpCountryValue | Unset = UNSET
    id: int | Unset = UNSET
    institute_number: str | Unset = UNSET
    ivs_relevant: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    long_name_one: str | Unset = UNSET
    long_name_two: str | Unset = UNSET
    lsf_relevant: str | Unset = UNSET
    mbs_relevant: str | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    room: str | Unset = UNSET
    short_name: str | Unset = UNSET
    street: str | Unset = UNSET
    superordinate_institute_number: str | Unset = UNSET
    sva_relevant: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    zip_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        bau_relevant = self.bau_relevant

        bes_relevant = self.bes_relevant

        building = self.building

        city = self.city

        cob_relevant = self.cob_relevant

        contact_person_inventory = self.contact_person_inventory

        contact_person_inventory_fax = self.contact_person_inventory_fax

        contact_person_inventory_mail = self.contact_person_inventory_mail

        contact_person_inventory_phone = self.contact_person_inventory_phone

        contact_person_procurement = self.contact_person_procurement

        contact_person_procurement_fax = self.contact_person_procurement_fax

        contact_person_procurement_mail = self.contact_person_procurement_mail

        contact_person_procurement_phone = self.contact_person_procurement_phone

        default_name = self.default_name

        erp_country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.erp_country, Unset):
            erp_country = self.erp_country.to_dict()

        id = self.id

        institute_number = self.institute_number

        ivs_relevant = self.ivs_relevant

        lock_version = self.lock_version

        long_name_one = self.long_name_one

        long_name_two = self.long_name_two

        lsf_relevant = self.lsf_relevant

        mbs_relevant = self.mbs_relevant

        name = self.name

        obj_guid = self.obj_guid

        room = self.room

        short_name = self.short_name

        street = self.street

        superordinate_institute_number = self.superordinate_institute_number

        sva_relevant = self.sva_relevant

        valid_from = self.valid_from

        valid_to = self.valid_to

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if bau_relevant is not UNSET:
            field_dict["bauRelevant"] = bau_relevant
        if bes_relevant is not UNSET:
            field_dict["besRelevant"] = bes_relevant
        if building is not UNSET:
            field_dict["building"] = building
        if city is not UNSET:
            field_dict["city"] = city
        if cob_relevant is not UNSET:
            field_dict["cobRelevant"] = cob_relevant
        if contact_person_inventory is not UNSET:
            field_dict["contactPersonInventory"] = contact_person_inventory
        if contact_person_inventory_fax is not UNSET:
            field_dict["contactPersonInventoryFax"] = contact_person_inventory_fax
        if contact_person_inventory_mail is not UNSET:
            field_dict["contactPersonInventoryMail"] = contact_person_inventory_mail
        if contact_person_inventory_phone is not UNSET:
            field_dict["contactPersonInventoryPhone"] = contact_person_inventory_phone
        if contact_person_procurement is not UNSET:
            field_dict["contactPersonProcurement"] = contact_person_procurement
        if contact_person_procurement_fax is not UNSET:
            field_dict["contactPersonProcurementFax"] = contact_person_procurement_fax
        if contact_person_procurement_mail is not UNSET:
            field_dict["contactPersonProcurementMail"] = contact_person_procurement_mail
        if contact_person_procurement_phone is not UNSET:
            field_dict["contactPersonProcurementPhone"] = contact_person_procurement_phone
        if default_name is not UNSET:
            field_dict["defaultName"] = default_name
        if erp_country is not UNSET:
            field_dict["erpCountry"] = erp_country
        if id is not UNSET:
            field_dict["id"] = id
        if institute_number is not UNSET:
            field_dict["instituteNumber"] = institute_number
        if ivs_relevant is not UNSET:
            field_dict["ivsRelevant"] = ivs_relevant
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if long_name_one is not UNSET:
            field_dict["longNameOne"] = long_name_one
        if long_name_two is not UNSET:
            field_dict["longNameTwo"] = long_name_two
        if lsf_relevant is not UNSET:
            field_dict["lsfRelevant"] = lsf_relevant
        if mbs_relevant is not UNSET:
            field_dict["mbsRelevant"] = mbs_relevant
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if room is not UNSET:
            field_dict["room"] = room
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if street is not UNSET:
            field_dict["street"] = street
        if superordinate_institute_number is not UNSET:
            field_dict["superordinateInstituteNumber"] = superordinate_institute_number
        if sva_relevant is not UNSET:
            field_dict["svaRelevant"] = sva_relevant
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_institute_erp_institute_foreigntext import (
            RmErpCommonInstituteErpInstituteForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonInstituteErpInstituteForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonInstituteErpInstituteForeigntext.from_dict(_field_foreigntext)

        bau_relevant = d.pop("bauRelevant", UNSET)

        bes_relevant = d.pop("besRelevant", UNSET)

        building = d.pop("building", UNSET)

        city = d.pop("city", UNSET)

        cob_relevant = d.pop("cobRelevant", UNSET)

        contact_person_inventory = d.pop("contactPersonInventory", UNSET)

        contact_person_inventory_fax = d.pop("contactPersonInventoryFax", UNSET)

        contact_person_inventory_mail = d.pop("contactPersonInventoryMail", UNSET)

        contact_person_inventory_phone = d.pop("contactPersonInventoryPhone", UNSET)

        contact_person_procurement = d.pop("contactPersonProcurement", UNSET)

        contact_person_procurement_fax = d.pop("contactPersonProcurementFax", UNSET)

        contact_person_procurement_mail = d.pop("contactPersonProcurementMail", UNSET)

        contact_person_procurement_phone = d.pop("contactPersonProcurementPhone", UNSET)

        default_name = d.pop("defaultName", UNSET)

        _erp_country = d.pop("erpCountry", UNSET)
        erp_country: RmErpCommonPersonErpCountryValue | Unset
        if isinstance(_erp_country, Unset):
            erp_country = UNSET
        else:
            erp_country = RmErpCommonPersonErpCountryValue.from_dict(_erp_country)

        id = d.pop("id", UNSET)

        institute_number = d.pop("instituteNumber", UNSET)

        ivs_relevant = d.pop("ivsRelevant", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        long_name_one = d.pop("longNameOne", UNSET)

        long_name_two = d.pop("longNameTwo", UNSET)

        lsf_relevant = d.pop("lsfRelevant", UNSET)

        mbs_relevant = d.pop("mbsRelevant", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        room = d.pop("room", UNSET)

        short_name = d.pop("shortName", UNSET)

        street = d.pop("street", UNSET)

        superordinate_institute_number = d.pop("superordinateInstituteNumber", UNSET)

        sva_relevant = d.pop("svaRelevant", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        zip_ = d.pop("zip", UNSET)

        rm_erp_common_institute_erp_institute = cls(
            field_foreigntext=field_foreigntext,
            bau_relevant=bau_relevant,
            bes_relevant=bes_relevant,
            building=building,
            city=city,
            cob_relevant=cob_relevant,
            contact_person_inventory=contact_person_inventory,
            contact_person_inventory_fax=contact_person_inventory_fax,
            contact_person_inventory_mail=contact_person_inventory_mail,
            contact_person_inventory_phone=contact_person_inventory_phone,
            contact_person_procurement=contact_person_procurement,
            contact_person_procurement_fax=contact_person_procurement_fax,
            contact_person_procurement_mail=contact_person_procurement_mail,
            contact_person_procurement_phone=contact_person_procurement_phone,
            default_name=default_name,
            erp_country=erp_country,
            id=id,
            institute_number=institute_number,
            ivs_relevant=ivs_relevant,
            lock_version=lock_version,
            long_name_one=long_name_one,
            long_name_two=long_name_two,
            lsf_relevant=lsf_relevant,
            mbs_relevant=mbs_relevant,
            name=name,
            obj_guid=obj_guid,
            room=room,
            short_name=short_name,
            street=street,
            superordinate_institute_number=superordinate_institute_number,
            sva_relevant=sva_relevant,
            valid_from=valid_from,
            valid_to=valid_to,
            zip_=zip_,
        )

        rm_erp_common_institute_erp_institute.additional_properties = d
        return rm_erp_common_institute_erp_institute

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
