from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_e_address import CsPsvExternalOrganisationEAddress
    from ..models.cs_psv_external_organisation_postaddress import CsPsvExternalOrganisationPostaddress
    from ..models.cs_psv_external_organisation_research_partner_simple_foreigntext import (
        CsPsvExternalOrganisationResearchPartnerSimpleForeigntext,
    )
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvExternalOrganisationResearchPartnerSimple")


@_attrs_define
class CsPsvExternalOrganisationResearchPartnerSimple:
    """
    Attributes:
        field_foreigntext (CsPsvExternalOrganisationResearchPartnerSimpleForeigntext | Unset):
        defaulttext (str | Unset):
        doctoral_cooperation_type_kdsf (CsSysValueGenericValue | Unset):
        emails (list[CsPsvExternalOrganisationEAddress] | Unset):
        funder_category_kdsf (CsSysValueGenericValue | Unset):
        hyperlinks (list[CsPsvExternalOrganisationEAddress] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        phones (list[CsPsvExternalOrganisationEAddress] | Unset):
        post_addresses (list[CsPsvExternalOrganisationPostaddress] | Unset):
    """

    field_foreigntext: CsPsvExternalOrganisationResearchPartnerSimpleForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    doctoral_cooperation_type_kdsf: CsSysValueGenericValue | Unset = UNSET
    emails: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
    funder_category_kdsf: CsSysValueGenericValue | Unset = UNSET
    hyperlinks: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    phones: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
    post_addresses: list[CsPsvExternalOrganisationPostaddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        doctoral_cooperation_type_kdsf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doctoral_cooperation_type_kdsf, Unset):
            doctoral_cooperation_type_kdsf = self.doctoral_cooperation_type_kdsf.to_dict()

        emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        funder_category_kdsf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funder_category_kdsf, Unset):
            funder_category_kdsf = self.funder_category_kdsf.to_dict()

        hyperlinks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hyperlinks, Unset):
            hyperlinks = []
            for hyperlinks_item_data in self.hyperlinks:
                hyperlinks_item = hyperlinks_item_data.to_dict()
                hyperlinks.append(hyperlinks_item)

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        phones: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        post_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_addresses, Unset):
            post_addresses = []
            for post_addresses_item_data in self.post_addresses:
                post_addresses_item = post_addresses_item_data.to_dict()
                post_addresses.append(post_addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if doctoral_cooperation_type_kdsf is not UNSET:
            field_dict["doctoralCooperationTypeKdsf"] = doctoral_cooperation_type_kdsf
        if emails is not UNSET:
            field_dict["emails"] = emails
        if funder_category_kdsf is not UNSET:
            field_dict["funderCategoryKdsf"] = funder_category_kdsf
        if hyperlinks is not UNSET:
            field_dict["hyperlinks"] = hyperlinks
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if phones is not UNSET:
            field_dict["phones"] = phones
        if post_addresses is not UNSET:
            field_dict["postAddresses"] = post_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_e_address import CsPsvExternalOrganisationEAddress  # noqa: PLC0415
        from ..models.cs_psv_external_organisation_postaddress import CsPsvExternalOrganisationPostaddress  # noqa: PLC0415
        from ..models.cs_psv_external_organisation_research_partner_simple_foreigntext import (
            CsPsvExternalOrganisationResearchPartnerSimpleForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvExternalOrganisationResearchPartnerSimpleForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvExternalOrganisationResearchPartnerSimpleForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        _doctoral_cooperation_type_kdsf = d.pop("doctoralCooperationTypeKdsf", UNSET)
        doctoral_cooperation_type_kdsf: CsSysValueGenericValue | Unset
        if isinstance(_doctoral_cooperation_type_kdsf, Unset):
            doctoral_cooperation_type_kdsf = UNSET
        else:
            doctoral_cooperation_type_kdsf = CsSysValueGenericValue.from_dict(_doctoral_cooperation_type_kdsf)

        _emails = d.pop("emails", UNSET)
        emails: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
        if _emails is not UNSET:
            emails = []
            for emails_item_data in _emails:
                emails_item = CsPsvExternalOrganisationEAddress.from_dict(emails_item_data)

                emails.append(emails_item)

        _funder_category_kdsf = d.pop("funderCategoryKdsf", UNSET)
        funder_category_kdsf: CsSysValueGenericValue | Unset
        if isinstance(_funder_category_kdsf, Unset):
            funder_category_kdsf = UNSET
        else:
            funder_category_kdsf = CsSysValueGenericValue.from_dict(_funder_category_kdsf)

        _hyperlinks = d.pop("hyperlinks", UNSET)
        hyperlinks: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
        if _hyperlinks is not UNSET:
            hyperlinks = []
            for hyperlinks_item_data in _hyperlinks:
                hyperlinks_item = CsPsvExternalOrganisationEAddress.from_dict(hyperlinks_item_data)

                hyperlinks.append(hyperlinks_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _phones = d.pop("phones", UNSET)
        phones: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
        if _phones is not UNSET:
            phones = []
            for phones_item_data in _phones:
                phones_item = CsPsvExternalOrganisationEAddress.from_dict(phones_item_data)

                phones.append(phones_item)

        _post_addresses = d.pop("postAddresses", UNSET)
        post_addresses: list[CsPsvExternalOrganisationPostaddress] | Unset = UNSET
        if _post_addresses is not UNSET:
            post_addresses = []
            for post_addresses_item_data in _post_addresses:
                post_addresses_item = CsPsvExternalOrganisationPostaddress.from_dict(post_addresses_item_data)

                post_addresses.append(post_addresses_item)

        cs_psv_external_organisation_research_partner_simple = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            doctoral_cooperation_type_kdsf=doctoral_cooperation_type_kdsf,
            emails=emails,
            funder_category_kdsf=funder_category_kdsf,
            hyperlinks=hyperlinks,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            phones=phones,
            post_addresses=post_addresses,
        )

        cs_psv_external_organisation_research_partner_simple.additional_properties = d
        return cs_psv_external_organisation_research_partner_simple

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
