from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest")


@_attrs_define
class CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest:
    """
    Attributes:
        feedback_message_key (str | Unset):
        feedback_message_params (list[str] | Unset):
        icon (str | Unset):
        icon_message_key (str | Unset):
    """

    feedback_message_key: str | Unset = UNSET
    feedback_message_params: list[str] | Unset = UNSET
    icon: str | Unset = UNSET
    icon_message_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        feedback_message_key = self.feedback_message_key

        feedback_message_params: list[str] | Unset = UNSET
        if not isinstance(self.feedback_message_params, Unset):
            feedback_message_params = self.feedback_message_params

        icon = self.icon

        icon_message_key = self.icon_message_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feedback_message_key is not UNSET:
            field_dict["feedbackMessageKey"] = feedback_message_key
        if feedback_message_params is not UNSET:
            field_dict["feedbackMessageParams"] = feedback_message_params
        if icon is not UNSET:
            field_dict["icon"] = icon
        if icon_message_key is not UNSET:
            field_dict["iconMessageKey"] = icon_message_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feedback_message_key = d.pop("feedbackMessageKey", UNSET)

        feedback_message_params = cast(list[str], d.pop("feedbackMessageParams", UNSET))

        icon = d.pop("icon", UNSET)

        icon_message_key = d.pop("iconMessageKey", UNSET)

        cs_sys_upload_configuration_upload_field_validation_rest_controller_resource_feedback_rest = cls(
            feedback_message_key=feedback_message_key,
            feedback_message_params=feedback_message_params,
            icon=icon,
            icon_message_key=icon_message_key,
        )

        cs_sys_upload_configuration_upload_field_validation_rest_controller_resource_feedback_rest.additional_properties = d
        return cs_sys_upload_configuration_upload_field_validation_rest_controller_resource_feedback_rest

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
