from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_process_process_type_enum import RmErpCommonProcessProcessTypeEnum
    from ..models.rm_erp_common_workflow_erp_workflow_operation_step_foreigntext import (
        RmErpCommonWorkflowErpWorkflowOperationStepForeigntext,
    )


T = TypeVar("T", bound="RmErpCommonWorkflowErpWorkflowOperationStep")


@_attrs_define
class RmErpCommonWorkflowErpWorkflowOperationStep:
    """
    Attributes:
        field_foreigntext (RmErpCommonWorkflowErpWorkflowOperationStepForeigntext | Unset):
        comment (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        process_id (int | Unset):
        process_type (RmErpCommonProcessProcessTypeEnum | Unset):
        pseudonymized_next_responsible_person_id (str | Unset):
        pseudonymized_process_related_person_id (str | Unset):
        pseudonymized_step_id (str | Unset):
        use_case_ident (str | Unset):
    """

    field_foreigntext: RmErpCommonWorkflowErpWorkflowOperationStepForeigntext | Unset = UNSET
    comment: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    process_id: int | Unset = UNSET
    process_type: RmErpCommonProcessProcessTypeEnum | Unset = UNSET
    pseudonymized_next_responsible_person_id: str | Unset = UNSET
    pseudonymized_process_related_person_id: str | Unset = UNSET
    pseudonymized_step_id: str | Unset = UNSET
    use_case_ident: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        comment = self.comment

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        process_id = self.process_id

        process_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.process_type, Unset):
            process_type = self.process_type.to_dict()

        pseudonymized_next_responsible_person_id = self.pseudonymized_next_responsible_person_id

        pseudonymized_process_related_person_id = self.pseudonymized_process_related_person_id

        pseudonymized_step_id = self.pseudonymized_step_id

        use_case_ident = self.use_case_ident

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if comment is not UNSET:
            field_dict["comment"] = comment
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if process_id is not UNSET:
            field_dict["processId"] = process_id
        if process_type is not UNSET:
            field_dict["processType"] = process_type
        if pseudonymized_next_responsible_person_id is not UNSET:
            field_dict["pseudonymizedNextResponsiblePersonId"] = pseudonymized_next_responsible_person_id
        if pseudonymized_process_related_person_id is not UNSET:
            field_dict["pseudonymizedProcessRelatedPersonId"] = pseudonymized_process_related_person_id
        if pseudonymized_step_id is not UNSET:
            field_dict["pseudonymizedStepId"] = pseudonymized_step_id
        if use_case_ident is not UNSET:
            field_dict["useCaseIdent"] = use_case_ident

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_process_process_type_enum import RmErpCommonProcessProcessTypeEnum  # noqa: PLC0415
        from ..models.rm_erp_common_workflow_erp_workflow_operation_step_foreigntext import (
            RmErpCommonWorkflowErpWorkflowOperationStepForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonWorkflowErpWorkflowOperationStepForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonWorkflowErpWorkflowOperationStepForeigntext.from_dict(_field_foreigntext)

        comment = d.pop("comment", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        process_id = d.pop("processId", UNSET)

        _process_type = d.pop("processType", UNSET)
        process_type: RmErpCommonProcessProcessTypeEnum | Unset
        if isinstance(_process_type, Unset):
            process_type = UNSET
        else:
            process_type = RmErpCommonProcessProcessTypeEnum.from_dict(_process_type)

        pseudonymized_next_responsible_person_id = d.pop("pseudonymizedNextResponsiblePersonId", UNSET)

        pseudonymized_process_related_person_id = d.pop("pseudonymizedProcessRelatedPersonId", UNSET)

        pseudonymized_step_id = d.pop("pseudonymizedStepId", UNSET)

        use_case_ident = d.pop("useCaseIdent", UNSET)

        rm_erp_common_workflow_erp_workflow_operation_step = cls(
            field_foreigntext=field_foreigntext,
            comment=comment,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            process_id=process_id,
            process_type=process_type,
            pseudonymized_next_responsible_person_id=pseudonymized_next_responsible_person_id,
            pseudonymized_process_related_person_id=pseudonymized_process_related_person_id,
            pseudonymized_step_id=pseudonymized_step_id,
            use_case_ident=use_case_ident,
        )

        rm_erp_common_workflow_erp_workflow_operation_step.additional_properties = d
        return rm_erp_common_workflow_erp_workflow_operation_step

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
