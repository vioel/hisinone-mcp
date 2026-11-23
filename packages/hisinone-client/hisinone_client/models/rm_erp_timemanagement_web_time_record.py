from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_timemanagement_web_time_record_foreigntext import RmErpTimemanagementWebTimeRecordForeigntext
    from ..models.rm_erp_timemanagement_web_time_record_type_enum import RmErpTimemanagementWebTimeRecordTypeEnum


T = TypeVar("T", bound="RmErpTimemanagementWebTimeRecord")


@_attrs_define
class RmErpTimemanagementWebTimeRecord:
    """
    Attributes:
        field_foreigntext (RmErpTimemanagementWebTimeRecordForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        record_type (RmErpTimemanagementWebTimeRecordTypeEnum | Unset):
        timestamp (int | Unset):
    """

    field_foreigntext: RmErpTimemanagementWebTimeRecordForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    record_type: RmErpTimemanagementWebTimeRecordTypeEnum | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        record_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.record_type, Unset):
            record_type = self.record_type.to_dict()

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if record_type is not UNSET:
            field_dict["recordType"] = record_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_timemanagement_web_time_record_foreigntext import (
            RmErpTimemanagementWebTimeRecordForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_timemanagement_web_time_record_type_enum import RmErpTimemanagementWebTimeRecordTypeEnum  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTimemanagementWebTimeRecordForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpTimemanagementWebTimeRecordForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _record_type = d.pop("recordType", UNSET)
        record_type: RmErpTimemanagementWebTimeRecordTypeEnum | Unset
        if isinstance(_record_type, Unset):
            record_type = UNSET
        else:
            record_type = RmErpTimemanagementWebTimeRecordTypeEnum.from_dict(_record_type)

        timestamp = d.pop("timestamp", UNSET)

        rm_erp_timemanagement_web_time_record = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            record_type=record_type,
            timestamp=timestamp,
        )

        rm_erp_timemanagement_web_time_record.additional_properties = d
        return rm_erp_timemanagement_web_time_record

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
