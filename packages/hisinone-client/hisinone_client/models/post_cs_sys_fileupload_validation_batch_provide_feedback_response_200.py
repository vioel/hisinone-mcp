from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_upload_field_validation_rest_controller_resource_feedback_rest import (
        CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest,
    )


T = TypeVar("T", bound="PostCsSysFileuploadValidationBatchProvideFeedbackResponse200")


@_attrs_define
class PostCsSysFileuploadValidationBatchProvideFeedbackResponse200:
    additional_properties: dict[
        str, list[CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest]
    ] = _attrs_field(
        init=False,
        factory=dict[str, "list[CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest]"],
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            _additional_property_json: list[dict[str, Any]] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                _additional_property_json.append(additional_property_item)
            field_dict[prop_name] = _additional_property_json

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_upload_field_validation_rest_controller_resource_feedback_rest import (
            CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest,  # noqa: PLC0415
        )

        d = dict(src_dict)
        post_cs_sys_fileupload_validation_batch_provide_feedback_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property: list[
                CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest
            ] = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = (
                    CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest.from_dict(
                        additional_property_item_data
                    )
                )

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        post_cs_sys_fileupload_validation_batch_provide_feedback_response_200.additional_properties = (
            additional_properties
        )
        return post_cs_sys_fileupload_validation_batch_provide_feedback_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> list[CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: list[CsSysUploadConfigurationUploadFieldValidationRestControllerResourceFeedbackRest]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
