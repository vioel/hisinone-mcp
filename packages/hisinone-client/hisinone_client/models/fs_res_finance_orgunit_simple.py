from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_e_address import CsPsvExternalOrganisationEAddress
    from ..models.cs_psv_external_organisation_postaddress import CsPsvExternalOrganisationPostaddress
    from ..models.fs_res_finance_orgunit_simple_foreigntext import FsResFinanceOrgunitSimpleForeigntext


T = TypeVar("T", bound="FsResFinanceOrgunitSimple")


@_attrs_define
class FsResFinanceOrgunitSimple:
    """
    Attributes:
        field_foreigntext (FsResFinanceOrgunitSimpleForeigntext | Unset):
        defaulttext (str | Unset):
        emails (list[CsPsvExternalOrganisationEAddress] | Unset):
        hiskey_id (int | Unset):
        hyperlinks (list[CsPsvExternalOrganisationEAddress] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        phones (list[CsPsvExternalOrganisationEAddress] | Unset):
        post_addresses (list[CsPsvExternalOrganisationPostaddress] | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
    """

    field_foreigntext: FsResFinanceOrgunitSimpleForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    emails: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    hyperlinks: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    phones: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
    post_addresses: list[CsPsvExternalOrganisationPostaddress] | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        hiskey_id = self.hiskey_id

        hyperlinks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hyperlinks, Unset):
            hyperlinks = []
            for hyperlinks_item_data in self.hyperlinks:
                hyperlinks_item = hyperlinks_item_data.to_dict()
                hyperlinks.append(hyperlinks_item)

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

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

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if emails is not UNSET:
            field_dict["emails"] = emails
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if hyperlinks is not UNSET:
            field_dict["hyperlinks"] = hyperlinks
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if phones is not UNSET:
            field_dict["phones"] = phones
        if post_addresses is not UNSET:
            field_dict["postAddresses"] = post_addresses
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_e_address import CsPsvExternalOrganisationEAddress  # noqa: PLC0415
        from ..models.cs_psv_external_organisation_postaddress import CsPsvExternalOrganisationPostaddress  # noqa: PLC0415
        from ..models.fs_res_finance_orgunit_simple_foreigntext import FsResFinanceOrgunitSimpleForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResFinanceOrgunitSimpleForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResFinanceOrgunitSimpleForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        _emails = d.pop("emails", UNSET)
        emails: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
        if _emails is not UNSET:
            emails = []
            for emails_item_data in _emails:
                emails_item = CsPsvExternalOrganisationEAddress.from_dict(emails_item_data)

                emails.append(emails_item)

        hiskey_id = d.pop("hiskeyId", UNSET)

        _hyperlinks = d.pop("hyperlinks", UNSET)
        hyperlinks: list[CsPsvExternalOrganisationEAddress] | Unset = UNSET
        if _hyperlinks is not UNSET:
            hyperlinks = []
            for hyperlinks_item_data in _hyperlinks:
                hyperlinks_item = CsPsvExternalOrganisationEAddress.from_dict(hyperlinks_item_data)

                hyperlinks.append(hyperlinks_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

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

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        fs_res_finance_orgunit_simple = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            emails=emails,
            hiskey_id=hiskey_id,
            hyperlinks=hyperlinks,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            phones=phones,
            post_addresses=post_addresses,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
        )

        fs_res_finance_orgunit_simple.additional_properties = d
        return fs_res_finance_orgunit_simple

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
