from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_document_document import RmErpCommonDocumentDocument
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_financialoperating_payment_partner import RmErpCommonFinancialoperatingPaymentPartner
    from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute
    from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue
    from ..models.rm_erp_procurement_requisition_financing import RmErpProcurementRequisitionFinancing
    from ..models.rm_erp_procurement_requisition_foreigntext import RmErpProcurementRequisitionForeigntext


T = TypeVar("T", bound="RmErpProcurementRequisition")


@_attrs_define
class RmErpProcurementRequisition:
    """
    Attributes:
        field_foreigntext (RmErpProcurementRequisitionForeigntext | Unset):
        building (str | Unset):
        city (str | Unset):
        contact_person_inventory (str | Unset):
        contact_person_inventory_fax (str | Unset):
        contact_person_inventory_mail (str | Unset):
        contact_person_inventory_phone (str | Unset):
        contact_person_procurement (str | Unset):
        contact_person_procurement_fax (str | Unset):
        contact_person_procurement_mail (str | Unset):
        contact_person_procurement_phone (str | Unset):
        description (str | Unset):
        documents (list[RmErpCommonDocumentDocument] | Unset):
        erp_country (RmErpCommonPersonErpCountryValue | Unset):
        erp_institute (RmErpCommonInstituteErpInstitute | Unset):
        financial_operating_user_id (int | Unset):
        financial_operating_user_name (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
        payment_partner (RmErpCommonFinancialoperatingPaymentPartner | Unset):
        purpose (str | Unset):
        request_date (int | Unset):
        requisition_financing_list (list[RmErpProcurementRequisitionFinancing] | Unset):
        room_number (str | Unset):
        salutation (str | Unset):
        serialversionuid (int | Unset):
        split_mode (int | Unset):
        status (RmErpCommonErpGenericValue | Unset):
        street (str | Unset):
        subject (str | Unset):
        zip_ (str | Unset):
    """

    field_foreigntext: RmErpProcurementRequisitionForeigntext | Unset = UNSET
    building: str | Unset = UNSET
    city: str | Unset = UNSET
    contact_person_inventory: str | Unset = UNSET
    contact_person_inventory_fax: str | Unset = UNSET
    contact_person_inventory_mail: str | Unset = UNSET
    contact_person_inventory_phone: str | Unset = UNSET
    contact_person_procurement: str | Unset = UNSET
    contact_person_procurement_fax: str | Unset = UNSET
    contact_person_procurement_mail: str | Unset = UNSET
    contact_person_procurement_phone: str | Unset = UNSET
    description: str | Unset = UNSET
    documents: list[RmErpCommonDocumentDocument] | Unset = UNSET
    erp_country: RmErpCommonPersonErpCountryValue | Unset = UNSET
    erp_institute: RmErpCommonInstituteErpInstitute | Unset = UNSET
    financial_operating_user_id: int | Unset = UNSET
    financial_operating_user_name: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    payment_partner: RmErpCommonFinancialoperatingPaymentPartner | Unset = UNSET
    purpose: str | Unset = UNSET
    request_date: int | Unset = UNSET
    requisition_financing_list: list[RmErpProcurementRequisitionFinancing] | Unset = UNSET
    room_number: str | Unset = UNSET
    salutation: str | Unset = UNSET
    serialversionuid: int | Unset = UNSET
    split_mode: int | Unset = UNSET
    status: RmErpCommonErpGenericValue | Unset = UNSET
    street: str | Unset = UNSET
    subject: str | Unset = UNSET
    zip_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        building = self.building

        city = self.city

        contact_person_inventory = self.contact_person_inventory

        contact_person_inventory_fax = self.contact_person_inventory_fax

        contact_person_inventory_mail = self.contact_person_inventory_mail

        contact_person_inventory_phone = self.contact_person_inventory_phone

        contact_person_procurement = self.contact_person_procurement

        contact_person_procurement_fax = self.contact_person_procurement_fax

        contact_person_procurement_mail = self.contact_person_procurement_mail

        contact_person_procurement_phone = self.contact_person_procurement_phone

        description = self.description

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        erp_country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.erp_country, Unset):
            erp_country = self.erp_country.to_dict()

        erp_institute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.erp_institute, Unset):
            erp_institute = self.erp_institute.to_dict()

        financial_operating_user_id = self.financial_operating_user_id

        financial_operating_user_name = self.financial_operating_user_name

        id = self.id

        lock_version = self.lock_version

        name = self.name

        obj_guid = self.obj_guid

        payment_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment_partner, Unset):
            payment_partner = self.payment_partner.to_dict()

        purpose = self.purpose

        request_date = self.request_date

        requisition_financing_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requisition_financing_list, Unset):
            requisition_financing_list = []
            for requisition_financing_list_item_data in self.requisition_financing_list:
                requisition_financing_list_item = requisition_financing_list_item_data.to_dict()
                requisition_financing_list.append(requisition_financing_list_item)

        room_number = self.room_number

        salutation = self.salutation

        serialversionuid = self.serialversionuid

        split_mode = self.split_mode

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        street = self.street

        subject = self.subject

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if building is not UNSET:
            field_dict["building"] = building
        if city is not UNSET:
            field_dict["city"] = city
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
        if description is not UNSET:
            field_dict["description"] = description
        if documents is not UNSET:
            field_dict["documents"] = documents
        if erp_country is not UNSET:
            field_dict["erpCountry"] = erp_country
        if erp_institute is not UNSET:
            field_dict["erpInstitute"] = erp_institute
        if financial_operating_user_id is not UNSET:
            field_dict["financialOperatingUserId"] = financial_operating_user_id
        if financial_operating_user_name is not UNSET:
            field_dict["financialOperatingUserName"] = financial_operating_user_name
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if payment_partner is not UNSET:
            field_dict["paymentPartner"] = payment_partner
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if request_date is not UNSET:
            field_dict["requestDate"] = request_date
        if requisition_financing_list is not UNSET:
            field_dict["requisitionFinancingList"] = requisition_financing_list
        if room_number is not UNSET:
            field_dict["roomNumber"] = room_number
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if serialversionuid is not UNSET:
            field_dict["serialversionuid"] = serialversionuid
        if split_mode is not UNSET:
            field_dict["splitMode"] = split_mode
        if status is not UNSET:
            field_dict["status"] = status
        if street is not UNSET:
            field_dict["street"] = street
        if subject is not UNSET:
            field_dict["subject"] = subject
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_document_document import RmErpCommonDocumentDocument  # noqa: PLC0415
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_financialoperating_payment_partner import (
            RmErpCommonFinancialoperatingPaymentPartner,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute  # noqa: PLC0415
        from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue  # noqa: PLC0415
        from ..models.rm_erp_procurement_requisition_financing import RmErpProcurementRequisitionFinancing  # noqa: PLC0415
        from ..models.rm_erp_procurement_requisition_foreigntext import RmErpProcurementRequisitionForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpProcurementRequisitionForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpProcurementRequisitionForeigntext.from_dict(_field_foreigntext)

        building = d.pop("building", UNSET)

        city = d.pop("city", UNSET)

        contact_person_inventory = d.pop("contactPersonInventory", UNSET)

        contact_person_inventory_fax = d.pop("contactPersonInventoryFax", UNSET)

        contact_person_inventory_mail = d.pop("contactPersonInventoryMail", UNSET)

        contact_person_inventory_phone = d.pop("contactPersonInventoryPhone", UNSET)

        contact_person_procurement = d.pop("contactPersonProcurement", UNSET)

        contact_person_procurement_fax = d.pop("contactPersonProcurementFax", UNSET)

        contact_person_procurement_mail = d.pop("contactPersonProcurementMail", UNSET)

        contact_person_procurement_phone = d.pop("contactPersonProcurementPhone", UNSET)

        description = d.pop("description", UNSET)

        _documents = d.pop("documents", UNSET)
        documents: list[RmErpCommonDocumentDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RmErpCommonDocumentDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        _erp_country = d.pop("erpCountry", UNSET)
        erp_country: RmErpCommonPersonErpCountryValue | Unset
        if isinstance(_erp_country, Unset):
            erp_country = UNSET
        else:
            erp_country = RmErpCommonPersonErpCountryValue.from_dict(_erp_country)

        _erp_institute = d.pop("erpInstitute", UNSET)
        erp_institute: RmErpCommonInstituteErpInstitute | Unset
        if isinstance(_erp_institute, Unset):
            erp_institute = UNSET
        else:
            erp_institute = RmErpCommonInstituteErpInstitute.from_dict(_erp_institute)

        financial_operating_user_id = d.pop("financialOperatingUserId", UNSET)

        financial_operating_user_name = d.pop("financialOperatingUserName", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _payment_partner = d.pop("paymentPartner", UNSET)
        payment_partner: RmErpCommonFinancialoperatingPaymentPartner | Unset
        if isinstance(_payment_partner, Unset):
            payment_partner = UNSET
        else:
            payment_partner = RmErpCommonFinancialoperatingPaymentPartner.from_dict(_payment_partner)

        purpose = d.pop("purpose", UNSET)

        request_date = d.pop("requestDate", UNSET)

        _requisition_financing_list = d.pop("requisitionFinancingList", UNSET)
        requisition_financing_list: list[RmErpProcurementRequisitionFinancing] | Unset = UNSET
        if _requisition_financing_list is not UNSET:
            requisition_financing_list = []
            for requisition_financing_list_item_data in _requisition_financing_list:
                requisition_financing_list_item = RmErpProcurementRequisitionFinancing.from_dict(
                    requisition_financing_list_item_data
                )

                requisition_financing_list.append(requisition_financing_list_item)

        room_number = d.pop("roomNumber", UNSET)

        salutation = d.pop("salutation", UNSET)

        serialversionuid = d.pop("serialversionuid", UNSET)

        split_mode = d.pop("splitMode", UNSET)

        _status = d.pop("status", UNSET)
        status: RmErpCommonErpGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RmErpCommonErpGenericValue.from_dict(_status)

        street = d.pop("street", UNSET)

        subject = d.pop("subject", UNSET)

        zip_ = d.pop("zip", UNSET)

        rm_erp_procurement_requisition = cls(
            field_foreigntext=field_foreigntext,
            building=building,
            city=city,
            contact_person_inventory=contact_person_inventory,
            contact_person_inventory_fax=contact_person_inventory_fax,
            contact_person_inventory_mail=contact_person_inventory_mail,
            contact_person_inventory_phone=contact_person_inventory_phone,
            contact_person_procurement=contact_person_procurement,
            contact_person_procurement_fax=contact_person_procurement_fax,
            contact_person_procurement_mail=contact_person_procurement_mail,
            contact_person_procurement_phone=contact_person_procurement_phone,
            description=description,
            documents=documents,
            erp_country=erp_country,
            erp_institute=erp_institute,
            financial_operating_user_id=financial_operating_user_id,
            financial_operating_user_name=financial_operating_user_name,
            id=id,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
            payment_partner=payment_partner,
            purpose=purpose,
            request_date=request_date,
            requisition_financing_list=requisition_financing_list,
            room_number=room_number,
            salutation=salutation,
            serialversionuid=serialversionuid,
            split_mode=split_mode,
            status=status,
            street=street,
            subject=subject,
            zip_=zip_,
        )

        rm_erp_procurement_requisition.additional_properties = d
        return rm_erp_procurement_requisition

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
