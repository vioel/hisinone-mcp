from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.cs_sys_upload_configuration_upload_field_validation_rest_controller_batch_feedback_request_rest_context_objects import (
        CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRestContextObjects,
    )


T = TypeVar("T", bound="CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest")


@_attrs_define
class CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRest:
    """
    Attributes:
        context_objects
            (CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRestContextObjects | Unset):
        javascript_context (str | Unset):
        resources (list[CsSysUploadConfigurationHisUploadFile] | Unset):
        upload_field_config_key (str | Unset):
    """

    context_objects: (
        CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRestContextObjects | Unset
    ) = UNSET
    javascript_context: str | Unset = UNSET
    resources: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
    upload_field_config_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        context_objects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context_objects, Unset):
            context_objects = self.context_objects.to_dict()

        javascript_context = self.javascript_context

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        upload_field_config_key = self.upload_field_config_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context_objects is not UNSET:
            field_dict["contextObjects"] = context_objects
        if javascript_context is not UNSET:
            field_dict["javascriptContext"] = javascript_context
        if resources is not UNSET:
            field_dict["resources"] = resources
        if upload_field_config_key is not UNSET:
            field_dict["uploadFieldConfigKey"] = upload_field_config_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.cs_sys_upload_configuration_upload_field_validation_rest_controller_batch_feedback_request_rest_context_objects import (
            CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRestContextObjects,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _context_objects = d.pop("contextObjects", UNSET)
        context_objects: (
            CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRestContextObjects | Unset
        )
        if isinstance(_context_objects, Unset):
            context_objects = UNSET
        else:
            context_objects = CsSysUploadConfigurationUploadFieldValidationRestControllerBatchFeedbackRequestRestContextObjects.from_dict(
                _context_objects
            )

        javascript_context = d.pop("javascriptContext", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = CsSysUploadConfigurationHisUploadFile.from_dict(resources_item_data)

                resources.append(resources_item)

        upload_field_config_key = d.pop("uploadFieldConfigKey", UNSET)

        cs_sys_upload_configuration_upload_field_validation_rest_controller_batch_feedback_request_rest = cls(
            context_objects=context_objects,
            javascript_context=javascript_context,
            resources=resources,
            upload_field_config_key=upload_field_config_key,
        )

        cs_sys_upload_configuration_upload_field_validation_rest_controller_batch_feedback_request_rest.additional_properties = d
        return cs_sys_upload_configuration_upload_field_validation_rest_controller_batch_feedback_request_rest

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
