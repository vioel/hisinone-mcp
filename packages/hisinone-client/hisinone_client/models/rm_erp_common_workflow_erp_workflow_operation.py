from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_workflow_erp_workflow_person_data import RmErpCommonWorkflowErpWorkflowPersonData
    from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value import (
        RmErpCommonWorkflowErpWorkflowProcessingStepValue,
    )


T = TypeVar("T", bound="RmErpCommonWorkflowErpWorkflowOperation")


@_attrs_define
class RmErpCommonWorkflowErpWorkflowOperation:
    """
    Attributes:
        erp_workflow_person_data_dtos (list[RmErpCommonWorkflowErpWorkflowPersonData] | Unset):
        erp_workflow_processing_step_value_dtos (list[RmErpCommonWorkflowErpWorkflowProcessingStepValue] | Unset):
        pseudonymized_preallocated_person_id (str | Unset):
    """

    erp_workflow_person_data_dtos: list[RmErpCommonWorkflowErpWorkflowPersonData] | Unset = UNSET
    erp_workflow_processing_step_value_dtos: list[RmErpCommonWorkflowErpWorkflowProcessingStepValue] | Unset = UNSET
    pseudonymized_preallocated_person_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        erp_workflow_person_data_dtos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.erp_workflow_person_data_dtos, Unset):
            erp_workflow_person_data_dtos = []
            for erp_workflow_person_data_dtos_item_data in self.erp_workflow_person_data_dtos:
                erp_workflow_person_data_dtos_item = erp_workflow_person_data_dtos_item_data.to_dict()
                erp_workflow_person_data_dtos.append(erp_workflow_person_data_dtos_item)

        erp_workflow_processing_step_value_dtos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.erp_workflow_processing_step_value_dtos, Unset):
            erp_workflow_processing_step_value_dtos = []
            for erp_workflow_processing_step_value_dtos_item_data in self.erp_workflow_processing_step_value_dtos:
                erp_workflow_processing_step_value_dtos_item = (
                    erp_workflow_processing_step_value_dtos_item_data.to_dict()
                )
                erp_workflow_processing_step_value_dtos.append(erp_workflow_processing_step_value_dtos_item)

        pseudonymized_preallocated_person_id = self.pseudonymized_preallocated_person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if erp_workflow_person_data_dtos is not UNSET:
            field_dict["erpWorkflowPersonDataDtos"] = erp_workflow_person_data_dtos
        if erp_workflow_processing_step_value_dtos is not UNSET:
            field_dict["erpWorkflowProcessingStepValueDtos"] = erp_workflow_processing_step_value_dtos
        if pseudonymized_preallocated_person_id is not UNSET:
            field_dict["pseudonymizedPreallocatedPersonId"] = pseudonymized_preallocated_person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_workflow_erp_workflow_person_data import RmErpCommonWorkflowErpWorkflowPersonData  # noqa: PLC0415
        from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value import (
            RmErpCommonWorkflowErpWorkflowProcessingStepValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _erp_workflow_person_data_dtos = d.pop("erpWorkflowPersonDataDtos", UNSET)
        erp_workflow_person_data_dtos: list[RmErpCommonWorkflowErpWorkflowPersonData] | Unset = UNSET
        if _erp_workflow_person_data_dtos is not UNSET:
            erp_workflow_person_data_dtos = []
            for erp_workflow_person_data_dtos_item_data in _erp_workflow_person_data_dtos:
                erp_workflow_person_data_dtos_item = RmErpCommonWorkflowErpWorkflowPersonData.from_dict(
                    erp_workflow_person_data_dtos_item_data
                )

                erp_workflow_person_data_dtos.append(erp_workflow_person_data_dtos_item)

        _erp_workflow_processing_step_value_dtos = d.pop("erpWorkflowProcessingStepValueDtos", UNSET)
        erp_workflow_processing_step_value_dtos: list[RmErpCommonWorkflowErpWorkflowProcessingStepValue] | Unset = UNSET
        if _erp_workflow_processing_step_value_dtos is not UNSET:
            erp_workflow_processing_step_value_dtos = []
            for erp_workflow_processing_step_value_dtos_item_data in _erp_workflow_processing_step_value_dtos:
                erp_workflow_processing_step_value_dtos_item = (
                    RmErpCommonWorkflowErpWorkflowProcessingStepValue.from_dict(
                        erp_workflow_processing_step_value_dtos_item_data
                    )
                )

                erp_workflow_processing_step_value_dtos.append(erp_workflow_processing_step_value_dtos_item)

        pseudonymized_preallocated_person_id = d.pop("pseudonymizedPreallocatedPersonId", UNSET)

        rm_erp_common_workflow_erp_workflow_operation = cls(
            erp_workflow_person_data_dtos=erp_workflow_person_data_dtos,
            erp_workflow_processing_step_value_dtos=erp_workflow_processing_step_value_dtos,
            pseudonymized_preallocated_person_id=pseudonymized_preallocated_person_id,
        )

        rm_erp_common_workflow_erp_workflow_operation.additional_properties = d
        return rm_erp_common_workflow_erp_workflow_operation

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
