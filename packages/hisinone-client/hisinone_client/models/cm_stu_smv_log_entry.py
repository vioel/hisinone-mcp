from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CmStuSmvLogEntry")


@_attrs_define
class CmStuSmvLogEntry:
    """
    Example:
        {'entryTimestamp': '2020-10-13T09:22:44', 'entry': 'Ein Protokolleintrag.', 'fileName':
            'TSMV0001_HS_Header_HSTOKV.xml', 'recordIdentifier': '12345'}

    Attributes:
        action (str | Unset):
        entry (str | Unset):
        entry_timestamp (int | Unset):
        file_name (str | Unset):
        group_id (str | Unset):
        log_level (str | Unset):
        record_identifier (str | Unset):
    """

    action: str | Unset = UNSET
    entry: str | Unset = UNSET
    entry_timestamp: int | Unset = UNSET
    file_name: str | Unset = UNSET
    group_id: str | Unset = UNSET
    log_level: str | Unset = UNSET
    record_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        entry = self.entry

        entry_timestamp = self.entry_timestamp

        file_name = self.file_name

        group_id = self.group_id

        log_level = self.log_level

        record_identifier = self.record_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if entry is not UNSET:
            field_dict["entry"] = entry
        if entry_timestamp is not UNSET:
            field_dict["entryTimestamp"] = entry_timestamp
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if log_level is not UNSET:
            field_dict["logLevel"] = log_level
        if record_identifier is not UNSET:
            field_dict["recordIdentifier"] = record_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        entry = d.pop("entry", UNSET)

        entry_timestamp = d.pop("entryTimestamp", UNSET)

        file_name = d.pop("fileName", UNSET)

        group_id = d.pop("groupId", UNSET)

        log_level = d.pop("logLevel", UNSET)

        record_identifier = d.pop("recordIdentifier", UNSET)

        cm_stu_smv_log_entry = cls(
            action=action,
            entry=entry,
            entry_timestamp=entry_timestamp,
            file_name=file_name,
            group_id=group_id,
            log_level=log_level,
            record_identifier=record_identifier,
        )

        cm_stu_smv_log_entry.additional_properties = d
        return cm_stu_smv_log_entry

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
