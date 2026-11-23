from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_upload_field_request_context_object import (
        CsSysUploadConfigurationUploadFieldRequestContextObject,
    )


T = TypeVar("T", bound="CsSysUploadConfigurationUploadFieldRequest")


@_attrs_define
class CsSysUploadConfigurationUploadFieldRequest:
    """
    Attributes:
        config_key (str | Unset):
        context_object (CsSysUploadConfigurationUploadFieldRequestContextObject | Unset):
        javascript_context (str | Unset):
    """

    config_key: str | Unset = UNSET
    context_object: CsSysUploadConfigurationUploadFieldRequestContextObject | Unset = UNSET
    javascript_context: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_key = self.config_key

        context_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context_object, Unset):
            context_object = self.context_object.to_dict()

        javascript_context = self.javascript_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_key is not UNSET:
            field_dict["configKey"] = config_key
        if context_object is not UNSET:
            field_dict["contextObject"] = context_object
        if javascript_context is not UNSET:
            field_dict["javascriptContext"] = javascript_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_upload_field_request_context_object import (
            CsSysUploadConfigurationUploadFieldRequestContextObject,  # noqa: PLC0415
        )

        d = dict(src_dict)
        config_key = d.pop("configKey", UNSET)

        _context_object = d.pop("contextObject", UNSET)
        context_object: CsSysUploadConfigurationUploadFieldRequestContextObject | Unset
        if isinstance(_context_object, Unset):
            context_object = UNSET
        else:
            context_object = CsSysUploadConfigurationUploadFieldRequestContextObject.from_dict(_context_object)

        javascript_context = d.pop("javascriptContext", UNSET)

        cs_sys_upload_configuration_upload_field_request = cls(
            config_key=config_key,
            context_object=context_object,
            javascript_context=javascript_context,
        )

        cs_sys_upload_configuration_upload_field_request.additional_properties = d
        return cs_sys_upload_configuration_upload_field_request

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
