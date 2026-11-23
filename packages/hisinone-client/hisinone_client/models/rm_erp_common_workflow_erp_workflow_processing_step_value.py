from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_workflow_erp_workflow_forwarding_enum import (
        RmErpCommonWorkflowErpWorkflowForwardingEnum,
    )
    from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value_foreigntext import (
        RmErpCommonWorkflowErpWorkflowProcessingStepValueForeigntext,
    )


T = TypeVar("T", bound="RmErpCommonWorkflowErpWorkflowProcessingStepValue")


@_attrs_define
class RmErpCommonWorkflowErpWorkflowProcessingStepValue:
    """
    Attributes:
        field_foreigntext (RmErpCommonWorkflowErpWorkflowProcessingStepValueForeigntext | Unset):
        defaulttext (str | Unset):
        hiskey_id (str | Unset):
        is_selectable (bool | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        notification (int | Unset):
        obj_guid (str | Unset):
        passed (int | Unset):
        post_condition (RmErpCommonWorkflowErpWorkflowForwardingEnum | Unset):
        pseudonymized_pre_condition (list[str] | Unset):
        pseudonymized_step_id (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: RmErpCommonWorkflowErpWorkflowProcessingStepValueForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    is_selectable: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    notification: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    passed: int | Unset = UNSET
    post_condition: RmErpCommonWorkflowErpWorkflowForwardingEnum | Unset = UNSET
    pseudonymized_pre_condition: list[str] | Unset = UNSET
    pseudonymized_step_id: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        hiskey_id = self.hiskey_id

        is_selectable = self.is_selectable

        lock_version = self.lock_version

        longtext = self.longtext

        notification = self.notification

        obj_guid = self.obj_guid

        passed = self.passed

        post_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_condition, Unset):
            post_condition = self.post_condition.to_dict()

        pseudonymized_pre_condition: list[str] | Unset = UNSET
        if not isinstance(self.pseudonymized_pre_condition, Unset):
            pseudonymized_pre_condition = self.pseudonymized_pre_condition

        pseudonymized_step_id = self.pseudonymized_step_id

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if is_selectable is not UNSET:
            field_dict["isSelectable"] = is_selectable
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if notification is not UNSET:
            field_dict["notification"] = notification
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if passed is not UNSET:
            field_dict["passed"] = passed
        if post_condition is not UNSET:
            field_dict["postCondition"] = post_condition
        if pseudonymized_pre_condition is not UNSET:
            field_dict["pseudonymizedPreCondition"] = pseudonymized_pre_condition
        if pseudonymized_step_id is not UNSET:
            field_dict["pseudonymizedStepId"] = pseudonymized_step_id
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_workflow_erp_workflow_forwarding_enum import (
            RmErpCommonWorkflowErpWorkflowForwardingEnum,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_workflow_erp_workflow_processing_step_value_foreigntext import (
            RmErpCommonWorkflowErpWorkflowProcessingStepValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonWorkflowErpWorkflowProcessingStepValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonWorkflowErpWorkflowProcessingStepValueForeigntext.from_dict(
                _field_foreigntext
            )

        defaulttext = d.pop("defaulttext", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        is_selectable = d.pop("isSelectable", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        notification = d.pop("notification", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        passed = d.pop("passed", UNSET)

        _post_condition = d.pop("postCondition", UNSET)
        post_condition: RmErpCommonWorkflowErpWorkflowForwardingEnum | Unset
        if isinstance(_post_condition, Unset):
            post_condition = UNSET
        else:
            post_condition = RmErpCommonWorkflowErpWorkflowForwardingEnum.from_dict(_post_condition)

        pseudonymized_pre_condition = cast(list[str], d.pop("pseudonymizedPreCondition", UNSET))

        pseudonymized_step_id = d.pop("pseudonymizedStepId", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        rm_erp_common_workflow_erp_workflow_processing_step_value = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            hiskey_id=hiskey_id,
            is_selectable=is_selectable,
            lock_version=lock_version,
            longtext=longtext,
            notification=notification,
            obj_guid=obj_guid,
            passed=passed,
            post_condition=post_condition,
            pseudonymized_pre_condition=pseudonymized_pre_condition,
            pseudonymized_step_id=pseudonymized_step_id,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        rm_erp_common_workflow_erp_workflow_processing_step_value.additional_properties = d
        return rm_erp_common_workflow_erp_workflow_processing_step_value

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
