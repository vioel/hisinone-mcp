from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.cs_sys_upload_configuration_upload_field_validation_rest_controller_feedback_request_rest_context_objects import (
        CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRestContextObjects,
    )


T = TypeVar("T", bound="CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRest")


@_attrs_define
class CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRest:
    """
    Attributes:
        context_objects (CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRestContextObjects |
            Unset):
        javascript_context (str | Unset):
        resource (CsSysUploadConfigurationHisUploadFile | Unset):
        upload_field_config_key (str | Unset):
    """

    context_objects: (
        CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRestContextObjects | Unset
    ) = UNSET
    javascript_context: str | Unset = UNSET
    resource: CsSysUploadConfigurationHisUploadFile | Unset = UNSET
    upload_field_config_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        context_objects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context_objects, Unset):
            context_objects = self.context_objects.to_dict()

        javascript_context = self.javascript_context

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        upload_field_config_key = self.upload_field_config_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_objects is not UNSET:
            field_dict["contextObjects"] = context_objects
        if javascript_context is not UNSET:
            field_dict["javascriptContext"] = javascript_context
        if resource is not UNSET:
            field_dict["resource"] = resource
        if upload_field_config_key is not UNSET:
            field_dict["uploadFieldConfigKey"] = upload_field_config_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.cs_sys_upload_configuration_upload_field_validation_rest_controller_feedback_request_rest_context_objects import (
            CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRestContextObjects,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _context_objects = d.pop("contextObjects", UNSET)
        context_objects: (
            CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRestContextObjects | Unset
        )
        if isinstance(_context_objects, Unset):
            context_objects = UNSET
        else:
            context_objects = (
                CsSysUploadConfigurationUploadFieldValidationRestControllerFeedbackRequestRestContextObjects.from_dict(
                    _context_objects
                )
            )

        javascript_context = d.pop("javascriptContext", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: CsSysUploadConfigurationHisUploadFile | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = CsSysUploadConfigurationHisUploadFile.from_dict(_resource)

        upload_field_config_key = d.pop("uploadFieldConfigKey", UNSET)

        cs_sys_upload_configuration_upload_field_validation_rest_controller_feedback_request_rest = cls(
            context_objects=context_objects,
            javascript_context=javascript_context,
            resource=resource,
            upload_field_config_key=upload_field_config_key,
        )

        cs_sys_upload_configuration_upload_field_validation_rest_controller_feedback_request_rest.additional_properties = d
        return cs_sys_upload_configuration_upload_field_validation_rest_controller_feedback_request_rest

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
