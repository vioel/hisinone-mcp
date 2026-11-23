from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RmErpCommonProcessProcessTypeEnum")


@_attrs_define
class RmErpCommonProcessProcessTypeEnum:
    """
    Attributes:
        declaring_class (Any | Unset):
        document_relation (str | Unset):
        ident (str | Unset):
        workflow_relation (str | Unset):
    """

    declaring_class: Any | Unset = UNSET
    document_relation: str | Unset = UNSET
    ident: str | Unset = UNSET
    workflow_relation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        declaring_class = self.declaring_class

        document_relation = self.document_relation

        ident = self.ident

        workflow_relation = self.workflow_relation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if document_relation is not UNSET:
            field_dict["documentRelation"] = document_relation
        if ident is not UNSET:
            field_dict["ident"] = ident
        if workflow_relation is not UNSET:
            field_dict["workflowRelation"] = workflow_relation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declaring_class = d.pop("declaringClass", UNSET)

        document_relation = d.pop("documentRelation", UNSET)

        ident = d.pop("ident", UNSET)

        workflow_relation = d.pop("workflowRelation", UNSET)

        rm_erp_common_process_process_type_enum = cls(
            declaring_class=declaring_class,
            document_relation=document_relation,
            ident=ident,
            workflow_relation=workflow_relation,
        )

        rm_erp_common_process_process_type_enum.additional_properties = d
        return rm_erp_common_process_process_type_enum

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
