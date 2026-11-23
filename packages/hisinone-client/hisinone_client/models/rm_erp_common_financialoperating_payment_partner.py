from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_financialoperating_payment_partner_foreigntext import (
        RmErpCommonFinancialoperatingPaymentPartnerForeigntext,
    )


T = TypeVar("T", bound="RmErpCommonFinancialoperatingPaymentPartner")


@_attrs_define
class RmErpCommonFinancialoperatingPaymentPartner:
    """
    Attributes:
        field_foreigntext (RmErpCommonFinancialoperatingPaymentPartnerForeigntext | Unset):
        bank_account_number (str | Unset):
        bank_city (str | Unset):
        bank_code (str | Unset):
        bank_name (str | Unset):
        bic (str | Unset):
        branch_office (str | Unset):
        city (str | Unset):
        contact_fax (str | Unset):
        contact_mail (str | Unset):
        contact_name (str | Unset):
        contact_phone (str | Unset):
        customer_number (str | Unset):
        department (str | Unset):
        iban (str | Unset):
        id (int | Unset):
        key (str | Unset):
        lock_version (int | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
        street (str | Unset):
        zip_ (str | Unset):
    """

    field_foreigntext: RmErpCommonFinancialoperatingPaymentPartnerForeigntext | Unset = UNSET
    bank_account_number: str | Unset = UNSET
    bank_city: str | Unset = UNSET
    bank_code: str | Unset = UNSET
    bank_name: str | Unset = UNSET
    bic: str | Unset = UNSET
    branch_office: str | Unset = UNSET
    city: str | Unset = UNSET
    contact_fax: str | Unset = UNSET
    contact_mail: str | Unset = UNSET
    contact_name: str | Unset = UNSET
    contact_phone: str | Unset = UNSET
    customer_number: str | Unset = UNSET
    department: str | Unset = UNSET
    iban: str | Unset = UNSET
    id: int | Unset = UNSET
    key: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    street: str | Unset = UNSET
    zip_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        bank_account_number = self.bank_account_number

        bank_city = self.bank_city

        bank_code = self.bank_code

        bank_name = self.bank_name

        bic = self.bic

        branch_office = self.branch_office

        city = self.city

        contact_fax = self.contact_fax

        contact_mail = self.contact_mail

        contact_name = self.contact_name

        contact_phone = self.contact_phone

        customer_number = self.customer_number

        department = self.department

        iban = self.iban

        id = self.id

        key = self.key

        lock_version = self.lock_version

        name = self.name

        obj_guid = self.obj_guid

        street = self.street

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if bank_account_number is not UNSET:
            field_dict["bankAccountNumber"] = bank_account_number
        if bank_city is not UNSET:
            field_dict["bankCity"] = bank_city
        if bank_code is not UNSET:
            field_dict["bankCode"] = bank_code
        if bank_name is not UNSET:
            field_dict["bankName"] = bank_name
        if bic is not UNSET:
            field_dict["bic"] = bic
        if branch_office is not UNSET:
            field_dict["branchOffice"] = branch_office
        if city is not UNSET:
            field_dict["city"] = city
        if contact_fax is not UNSET:
            field_dict["contactFax"] = contact_fax
        if contact_mail is not UNSET:
            field_dict["contactMail"] = contact_mail
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone
        if customer_number is not UNSET:
            field_dict["customerNumber"] = customer_number
        if department is not UNSET:
            field_dict["department"] = department
        if iban is not UNSET:
            field_dict["iban"] = iban
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if street is not UNSET:
            field_dict["street"] = street
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_financialoperating_payment_partner_foreigntext import (
            RmErpCommonFinancialoperatingPaymentPartnerForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonFinancialoperatingPaymentPartnerForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonFinancialoperatingPaymentPartnerForeigntext.from_dict(_field_foreigntext)

        bank_account_number = d.pop("bankAccountNumber", UNSET)

        bank_city = d.pop("bankCity", UNSET)

        bank_code = d.pop("bankCode", UNSET)

        bank_name = d.pop("bankName", UNSET)

        bic = d.pop("bic", UNSET)

        branch_office = d.pop("branchOffice", UNSET)

        city = d.pop("city", UNSET)

        contact_fax = d.pop("contactFax", UNSET)

        contact_mail = d.pop("contactMail", UNSET)

        contact_name = d.pop("contactName", UNSET)

        contact_phone = d.pop("contactPhone", UNSET)

        customer_number = d.pop("customerNumber", UNSET)

        department = d.pop("department", UNSET)

        iban = d.pop("iban", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        street = d.pop("street", UNSET)

        zip_ = d.pop("zip", UNSET)

        rm_erp_common_financialoperating_payment_partner = cls(
            field_foreigntext=field_foreigntext,
            bank_account_number=bank_account_number,
            bank_city=bank_city,
            bank_code=bank_code,
            bank_name=bank_name,
            bic=bic,
            branch_office=branch_office,
            city=city,
            contact_fax=contact_fax,
            contact_mail=contact_mail,
            contact_name=contact_name,
            contact_phone=contact_phone,
            customer_number=customer_number,
            department=department,
            iban=iban,
            id=id,
            key=key,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
            street=street,
            zip_=zip_,
        )

        rm_erp_common_financialoperating_payment_partner.additional_properties = d
        return rm_erp_common_financialoperating_payment_partner

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
