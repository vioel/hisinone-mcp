from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_address_type import DeMathplanMosesEdciAddressType
    from ..models.de_mathplan_moses_edci_interactive_web_resource_type import (
        DeMathplanMosesEdciInteractiveWebResourceType,
    )
    from ..models.de_mathplan_moses_edci_m_box_type import DeMathplanMosesEdciMBoxType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_phone_type import DeMathplanMosesEdciPhoneType


T = TypeVar("T", bound="DeMathplanMosesEdciContactPointType")


@_attrs_define
class DeMathplanMosesEdciContactPointType:
    """
    Attributes:
        address (list[DeMathplanMosesEdciAddressType] | Unset):
        description (list[DeMathplanMosesEdciNoteType] | Unset):
        mail_box (list[DeMathplanMosesEdciMBoxType] | Unset):
        note (list[DeMathplanMosesEdciNoteType] | Unset):
        phone (list[DeMathplanMosesEdciPhoneType] | Unset):
        wallet (list[str] | Unset):
        webresource (list[DeMathplanMosesEdciInteractiveWebResourceType] | Unset):
    """

    address: list[DeMathplanMosesEdciAddressType] | Unset = UNSET
    description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    mail_box: list[DeMathplanMosesEdciMBoxType] | Unset = UNSET
    note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    phone: list[DeMathplanMosesEdciPhoneType] | Unset = UNSET
    wallet: list[str] | Unset = UNSET
    webresource: list[DeMathplanMosesEdciInteractiveWebResourceType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        address: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = []
            for address_item_data in self.address:
                address_item = address_item_data.to_dict()
                address.append(address_item)

        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        mail_box: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mail_box, Unset):
            mail_box = []
            for mail_box_item_data in self.mail_box:
                mail_box_item = mail_box_item_data.to_dict()
                mail_box.append(mail_box_item)

        note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.note, Unset):
            note = []
            for note_item_data in self.note:
                note_item = note_item_data.to_dict()
                note.append(note_item)

        phone: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phone, Unset):
            phone = []
            for phone_item_data in self.phone:
                phone_item = phone_item_data.to_dict()
                phone.append(phone_item)

        wallet: list[str] | Unset = UNSET
        if not isinstance(self.wallet, Unset):
            wallet = self.wallet

        webresource: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.webresource, Unset):
            webresource = []
            for webresource_item_data in self.webresource:
                webresource_item = webresource_item_data.to_dict()
                webresource.append(webresource_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if description is not UNSET:
            field_dict["description"] = description
        if mail_box is not UNSET:
            field_dict["mailBox"] = mail_box
        if note is not UNSET:
            field_dict["note"] = note
        if phone is not UNSET:
            field_dict["phone"] = phone
        if wallet is not UNSET:
            field_dict["wallet"] = wallet
        if webresource is not UNSET:
            field_dict["webresource"] = webresource

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_address_type import DeMathplanMosesEdciAddressType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_interactive_web_resource_type import (
            DeMathplanMosesEdciInteractiveWebResourceType,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_m_box_type import DeMathplanMosesEdciMBoxType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_phone_type import DeMathplanMosesEdciPhoneType  # noqa: PLC0415

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: list[DeMathplanMosesEdciAddressType] | Unset = UNSET
        if _address is not UNSET:
            address = []
            for address_item_data in _address:
                address_item = DeMathplanMosesEdciAddressType.from_dict(address_item_data)

                address.append(address_item)

        _description = d.pop("description", UNSET)
        description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = DeMathplanMosesEdciNoteType.from_dict(description_item_data)

                description.append(description_item)

        _mail_box = d.pop("mailBox", UNSET)
        mail_box: list[DeMathplanMosesEdciMBoxType] | Unset = UNSET
        if _mail_box is not UNSET:
            mail_box = []
            for mail_box_item_data in _mail_box:
                mail_box_item = DeMathplanMosesEdciMBoxType.from_dict(mail_box_item_data)

                mail_box.append(mail_box_item)

        _note = d.pop("note", UNSET)
        note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _note is not UNSET:
            note = []
            for note_item_data in _note:
                note_item = DeMathplanMosesEdciNoteType.from_dict(note_item_data)

                note.append(note_item)

        _phone = d.pop("phone", UNSET)
        phone: list[DeMathplanMosesEdciPhoneType] | Unset = UNSET
        if _phone is not UNSET:
            phone = []
            for phone_item_data in _phone:
                phone_item = DeMathplanMosesEdciPhoneType.from_dict(phone_item_data)

                phone.append(phone_item)

        wallet = cast(list[str], d.pop("wallet", UNSET))

        _webresource = d.pop("webresource", UNSET)
        webresource: list[DeMathplanMosesEdciInteractiveWebResourceType] | Unset = UNSET
        if _webresource is not UNSET:
            webresource = []
            for webresource_item_data in _webresource:
                webresource_item = DeMathplanMosesEdciInteractiveWebResourceType.from_dict(webresource_item_data)

                webresource.append(webresource_item)

        de_mathplan_moses_edci_contact_point_type = cls(
            address=address,
            description=description,
            mail_box=mail_box,
            note=note,
            phone=phone,
            wallet=wallet,
            webresource=webresource,
        )

        de_mathplan_moses_edci_contact_point_type.additional_properties = d
        return de_mathplan_moses_edci_contact_point_type

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
