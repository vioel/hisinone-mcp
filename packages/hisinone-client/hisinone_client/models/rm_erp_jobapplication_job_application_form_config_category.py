from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_jobapplication_job_application_form_config_field import (
        RmErpJobapplicationJobApplicationFormConfigField,
    )


T = TypeVar("T", bound="RmErpJobapplicationJobApplicationFormConfigCategory")


@_attrs_define
class RmErpJobapplicationJobApplicationFormConfigCategory:
    """
    Attributes:
        active (str | Unset):
        fields (list[RmErpJobapplicationJobApplicationFormConfigField] | Unset):
        id (str | Unset):
    """

    active: str | Unset = UNSET
    fields: list[RmErpJobapplicationJobApplicationFormConfigField] | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_jobapplication_job_application_form_config_field import (
            RmErpJobapplicationJobApplicationFormConfigField,  # noqa: PLC0415
        )

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[RmErpJobapplicationJobApplicationFormConfigField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = RmErpJobapplicationJobApplicationFormConfigField.from_dict(fields_item_data)

                fields.append(fields_item)

        id = d.pop("id", UNSET)

        rm_erp_jobapplication_job_application_form_config_category = cls(
            active=active,
            fields=fields,
            id=id,
        )

        rm_erp_jobapplication_job_application_form_config_category.additional_properties = d
        return rm_erp_jobapplication_job_application_form_config_category

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
