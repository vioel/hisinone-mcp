from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_jobapplication_job_application_form_config_category import (
        RmErpJobapplicationJobApplicationFormConfigCategory,
    )


T = TypeVar("T", bound="RmErpJobapplicationJobApplicationFormConfig")


@_attrs_define
class RmErpJobapplicationJobApplicationFormConfig:
    """
    Attributes:
        categories (list[RmErpJobapplicationJobApplicationFormConfigCategory] | Unset):
        send_confirmation_email (bool | Unset):
    """

    categories: list[RmErpJobapplicationJobApplicationFormConfigCategory] | Unset = UNSET
    send_confirmation_email: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        send_confirmation_email = self.send_confirmation_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if send_confirmation_email is not UNSET:
            field_dict["sendConfirmationEmail"] = send_confirmation_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_jobapplication_job_application_form_config_category import (
            RmErpJobapplicationJobApplicationFormConfigCategory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[RmErpJobapplicationJobApplicationFormConfigCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = RmErpJobapplicationJobApplicationFormConfigCategory.from_dict(categories_item_data)

                categories.append(categories_item)

        send_confirmation_email = d.pop("sendConfirmationEmail", UNSET)

        rm_erp_jobapplication_job_application_form_config = cls(
            categories=categories,
            send_confirmation_email=send_confirmation_email,
        )

        rm_erp_jobapplication_job_application_form_config.additional_properties = d
        return rm_erp_jobapplication_job_application_form_config

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
