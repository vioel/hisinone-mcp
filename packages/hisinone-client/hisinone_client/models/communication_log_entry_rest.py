from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.communication_log_entry_rest_additional_attributes import (
        CommunicationLogEntryRestAdditionalAttributes,
    )


T = TypeVar("T", bound="CommunicationLogEntryRest")


@_attrs_define
class CommunicationLogEntryRest:
    """
    Attributes:
        additional_attributes (CommunicationLogEntryRestAdditionalAttributes | Unset):
        created_at (int | Unset):
        deletable (bool | Unset):
        domain_ids (list[int] | Unset):
        editable (bool | Unset):
        id (int | Unset):
        recipient_id (int | Unset):
        recipient_name (str | Unset):
        recipient_type (int | Unset):
        sender_id (int | Unset):
        sender_name (str | Unset):
        sender_type (int | Unset):
        subtype (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
    """

    additional_attributes: CommunicationLogEntryRestAdditionalAttributes | Unset = UNSET
    created_at: int | Unset = UNSET
    deletable: bool | Unset = UNSET
    domain_ids: list[int] | Unset = UNSET
    editable: bool | Unset = UNSET
    id: int | Unset = UNSET
    recipient_id: int | Unset = UNSET
    recipient_name: str | Unset = UNSET
    recipient_type: int | Unset = UNSET
    sender_id: int | Unset = UNSET
    sender_name: str | Unset = UNSET
    sender_type: int | Unset = UNSET
    subtype: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_attributes, Unset):
            additional_attributes = self.additional_attributes.to_dict()

        created_at = self.created_at

        deletable = self.deletable

        domain_ids: list[int] | Unset = UNSET
        if not isinstance(self.domain_ids, Unset):
            domain_ids = self.domain_ids

        editable = self.editable

        id = self.id

        recipient_id = self.recipient_id

        recipient_name = self.recipient_name

        recipient_type = self.recipient_type

        sender_id = self.sender_id

        sender_name = self.sender_name

        sender_type = self.sender_type

        subtype = self.subtype

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_attributes is not UNSET:
            field_dict["additionalAttributes"] = additional_attributes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if domain_ids is not UNSET:
            field_dict["domainIds"] = domain_ids
        if editable is not UNSET:
            field_dict["editable"] = editable
        if id is not UNSET:
            field_dict["id"] = id
        if recipient_id is not UNSET:
            field_dict["recipientId"] = recipient_id
        if recipient_name is not UNSET:
            field_dict["recipientName"] = recipient_name
        if recipient_type is not UNSET:
            field_dict["recipientType"] = recipient_type
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if sender_type is not UNSET:
            field_dict["senderType"] = sender_type
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.communication_log_entry_rest_additional_attributes import (
            CommunicationLogEntryRestAdditionalAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _additional_attributes = d.pop("additionalAttributes", UNSET)
        additional_attributes: CommunicationLogEntryRestAdditionalAttributes | Unset
        if isinstance(_additional_attributes, Unset):
            additional_attributes = UNSET
        else:
            additional_attributes = CommunicationLogEntryRestAdditionalAttributes.from_dict(_additional_attributes)

        created_at = d.pop("createdAt", UNSET)

        deletable = d.pop("deletable", UNSET)

        domain_ids = cast(list[int], d.pop("domainIds", UNSET))

        editable = d.pop("editable", UNSET)

        id = d.pop("id", UNSET)

        recipient_id = d.pop("recipientId", UNSET)

        recipient_name = d.pop("recipientName", UNSET)

        recipient_type = d.pop("recipientType", UNSET)

        sender_id = d.pop("senderId", UNSET)

        sender_name = d.pop("senderName", UNSET)

        sender_type = d.pop("senderType", UNSET)

        subtype = d.pop("subtype", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        communication_log_entry_rest = cls(
            additional_attributes=additional_attributes,
            created_at=created_at,
            deletable=deletable,
            domain_ids=domain_ids,
            editable=editable,
            id=id,
            recipient_id=recipient_id,
            recipient_name=recipient_name,
            recipient_type=recipient_type,
            sender_id=sender_id,
            sender_name=sender_name,
            sender_type=sender_type,
            subtype=subtype,
            title=title,
            type_=type_,
        )

        communication_log_entry_rest.additional_properties = d
        return communication_log_entry_rest

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
