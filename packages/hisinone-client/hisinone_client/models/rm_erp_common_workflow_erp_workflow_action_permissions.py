from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RmErpCommonWorkflowErpWorkflowActionPermissions")


@_attrs_define
class RmErpCommonWorkflowErpWorkflowActionPermissions:
    """
    Attributes:
        delete_workflow_permission (bool | Unset):
        edit_workflow_permission (bool | Unset):
    """

    delete_workflow_permission: bool | Unset = UNSET
    edit_workflow_permission: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        delete_workflow_permission = self.delete_workflow_permission

        edit_workflow_permission = self.edit_workflow_permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_workflow_permission is not UNSET:
            field_dict["deleteWorkflowPermission"] = delete_workflow_permission
        if edit_workflow_permission is not UNSET:
            field_dict["editWorkflowPermission"] = edit_workflow_permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delete_workflow_permission = d.pop("deleteWorkflowPermission", UNSET)

        edit_workflow_permission = d.pop("editWorkflowPermission", UNSET)

        rm_erp_common_workflow_erp_workflow_action_permissions = cls(
            delete_workflow_permission=delete_workflow_permission,
            edit_workflow_permission=edit_workflow_permission,
        )

        rm_erp_common_workflow_erp_workflow_action_permissions.additional_properties = d
        return rm_erp_common_workflow_erp_workflow_action_permissions

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
