from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RmErpCommonWorkflowErpWorkflowHistoryItem")


@_attrs_define
class RmErpCommonWorkflowErpWorkflowHistoryItem:
    """
    Attributes:
        comment (str | Unset):
        edit_timestamp (int | Unset):
        executing_person_firstname (str | Unset):
        executing_person_surname (str | Unset):
        is_executed_by_system (bool | Unset):
        next_responsible_person_firstname (str | Unset):
        next_responsible_person_surname (str | Unset):
        processing_step_text (str | Unset):
        responsible_person_email (str | Unset):
    """

    comment: str | Unset = UNSET
    edit_timestamp: int | Unset = UNSET
    executing_person_firstname: str | Unset = UNSET
    executing_person_surname: str | Unset = UNSET
    is_executed_by_system: bool | Unset = UNSET
    next_responsible_person_firstname: str | Unset = UNSET
    next_responsible_person_surname: str | Unset = UNSET
    processing_step_text: str | Unset = UNSET
    responsible_person_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        edit_timestamp = self.edit_timestamp

        executing_person_firstname = self.executing_person_firstname

        executing_person_surname = self.executing_person_surname

        is_executed_by_system = self.is_executed_by_system

        next_responsible_person_firstname = self.next_responsible_person_firstname

        next_responsible_person_surname = self.next_responsible_person_surname

        processing_step_text = self.processing_step_text

        responsible_person_email = self.responsible_person_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if edit_timestamp is not UNSET:
            field_dict["editTimestamp"] = edit_timestamp
        if executing_person_firstname is not UNSET:
            field_dict["executingPersonFirstname"] = executing_person_firstname
        if executing_person_surname is not UNSET:
            field_dict["executingPersonSurname"] = executing_person_surname
        if is_executed_by_system is not UNSET:
            field_dict["isExecutedBySystem"] = is_executed_by_system
        if next_responsible_person_firstname is not UNSET:
            field_dict["nextResponsiblePersonFirstname"] = next_responsible_person_firstname
        if next_responsible_person_surname is not UNSET:
            field_dict["nextResponsiblePersonSurname"] = next_responsible_person_surname
        if processing_step_text is not UNSET:
            field_dict["processingStepText"] = processing_step_text
        if responsible_person_email is not UNSET:
            field_dict["responsiblePersonEmail"] = responsible_person_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        edit_timestamp = d.pop("editTimestamp", UNSET)

        executing_person_firstname = d.pop("executingPersonFirstname", UNSET)

        executing_person_surname = d.pop("executingPersonSurname", UNSET)

        is_executed_by_system = d.pop("isExecutedBySystem", UNSET)

        next_responsible_person_firstname = d.pop("nextResponsiblePersonFirstname", UNSET)

        next_responsible_person_surname = d.pop("nextResponsiblePersonSurname", UNSET)

        processing_step_text = d.pop("processingStepText", UNSET)

        responsible_person_email = d.pop("responsiblePersonEmail", UNSET)

        rm_erp_common_workflow_erp_workflow_history_item = cls(
            comment=comment,
            edit_timestamp=edit_timestamp,
            executing_person_firstname=executing_person_firstname,
            executing_person_surname=executing_person_surname,
            is_executed_by_system=is_executed_by_system,
            next_responsible_person_firstname=next_responsible_person_firstname,
            next_responsible_person_surname=next_responsible_person_surname,
            processing_step_text=processing_step_text,
            responsible_person_email=responsible_person_email,
        )

        rm_erp_common_workflow_erp_workflow_history_item.additional_properties = d
        return rm_erp_common_workflow_erp_workflow_history_item

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
