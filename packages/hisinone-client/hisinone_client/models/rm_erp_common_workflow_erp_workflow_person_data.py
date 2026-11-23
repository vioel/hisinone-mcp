from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value import (
        RmErpCommonWorkflowErpWorkflowProcessingStepValue,
    )


T = TypeVar("T", bound="RmErpCommonWorkflowErpWorkflowPersonData")


@_attrs_define
class RmErpCommonWorkflowErpWorkflowPersonData:
    """
    Attributes:
        available_processing_steps (list[RmErpCommonWorkflowErpWorkflowProcessingStepValue] | Unset):
        firstname (str | Unset):
        name_addition (str | Unset):
        pseudonymized_person_id (str | Unset):
        salutation (RmErpCommonErpGenericValue | Unset):
        surname (str | Unset):
    """

    available_processing_steps: list[RmErpCommonWorkflowErpWorkflowProcessingStepValue] | Unset = UNSET
    firstname: str | Unset = UNSET
    name_addition: str | Unset = UNSET
    pseudonymized_person_id: str | Unset = UNSET
    salutation: RmErpCommonErpGenericValue | Unset = UNSET
    surname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        available_processing_steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_processing_steps, Unset):
            available_processing_steps = []
            for available_processing_steps_item_data in self.available_processing_steps:
                available_processing_steps_item = available_processing_steps_item_data.to_dict()
                available_processing_steps.append(available_processing_steps_item)

        firstname = self.firstname

        name_addition = self.name_addition

        pseudonymized_person_id = self.pseudonymized_person_id

        salutation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.to_dict()

        surname = self.surname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_processing_steps is not UNSET:
            field_dict["availableProcessingSteps"] = available_processing_steps
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if name_addition is not UNSET:
            field_dict["nameAddition"] = name_addition
        if pseudonymized_person_id is not UNSET:
            field_dict["pseudonymizedPersonId"] = pseudonymized_person_id
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if surname is not UNSET:
            field_dict["surname"] = surname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value import (
            RmErpCommonWorkflowErpWorkflowProcessingStepValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _available_processing_steps = d.pop("availableProcessingSteps", UNSET)
        available_processing_steps: list[RmErpCommonWorkflowErpWorkflowProcessingStepValue] | Unset = UNSET
        if _available_processing_steps is not UNSET:
            available_processing_steps = []
            for available_processing_steps_item_data in _available_processing_steps:
                available_processing_steps_item = RmErpCommonWorkflowErpWorkflowProcessingStepValue.from_dict(
                    available_processing_steps_item_data
                )

                available_processing_steps.append(available_processing_steps_item)

        firstname = d.pop("firstname", UNSET)

        name_addition = d.pop("nameAddition", UNSET)

        pseudonymized_person_id = d.pop("pseudonymizedPersonId", UNSET)

        _salutation = d.pop("salutation", UNSET)
        salutation: RmErpCommonErpGenericValue | Unset
        if isinstance(_salutation, Unset):
            salutation = UNSET
        else:
            salutation = RmErpCommonErpGenericValue.from_dict(_salutation)

        surname = d.pop("surname", UNSET)

        rm_erp_common_workflow_erp_workflow_person_data = cls(
            available_processing_steps=available_processing_steps,
            firstname=firstname,
            name_addition=name_addition,
            pseudonymized_person_id=pseudonymized_person_id,
            salutation=salutation,
            surname=surname,
        )

        rm_erp_common_workflow_erp_workflow_person_data.additional_properties = d
        return rm_erp_common_workflow_erp_workflow_person_data

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
