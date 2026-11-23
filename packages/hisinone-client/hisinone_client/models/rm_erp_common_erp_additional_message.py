from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_additional_message_foreigntext import RmErpCommonErpAdditionalMessageForeigntext


T = TypeVar("T", bound="RmErpCommonErpAdditionalMessage")


@_attrs_define
class RmErpCommonErpAdditionalMessage:
    """
    Attributes:
        field_foreigntext (RmErpCommonErpAdditionalMessageForeigntext | Unset):
        dto (Any | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        message (str | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: RmErpCommonErpAdditionalMessageForeigntext | Unset = UNSET
    dto: Any | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    message: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        dto = self.dto

        id = self.id

        lock_version = self.lock_version

        message = self.message

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if dto is not UNSET:
            field_dict["dto"] = dto
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if message is not UNSET:
            field_dict["message"] = message
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_additional_message_foreigntext import RmErpCommonErpAdditionalMessageForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonErpAdditionalMessageForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonErpAdditionalMessageForeigntext.from_dict(_field_foreigntext)

        dto = d.pop("dto", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        message = d.pop("message", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        rm_erp_common_erp_additional_message = cls(
            field_foreigntext=field_foreigntext,
            dto=dto,
            id=id,
            lock_version=lock_version,
            message=message,
            obj_guid=obj_guid,
        )

        rm_erp_common_erp_additional_message.additional_properties = d
        return rm_erp_common_erp_additional_message

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
