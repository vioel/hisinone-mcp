from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType")


@_attrs_define
class DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType:
    """
    Attributes:
        declaring_class (Any | Unset):
        message_key (str | Unset):
        multi_value_type (bool | Unset):
        name (str | Unset):
        value_class (Any | Unset):
    """

    declaring_class: Any | Unset = UNSET
    message_key: str | Unset = UNSET
    multi_value_type: bool | Unset = UNSET
    name: str | Unset = UNSET
    value_class: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        declaring_class = self.declaring_class

        message_key = self.message_key

        multi_value_type = self.multi_value_type

        name = self.name

        value_class = self.value_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if message_key is not UNSET:
            field_dict["messageKey"] = message_key
        if multi_value_type is not UNSET:
            field_dict["multiValueType"] = multi_value_type
        if name is not UNSET:
            field_dict["name"] = name
        if value_class is not UNSET:
            field_dict["valueClass"] = value_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declaring_class = d.pop("declaringClass", UNSET)

        message_key = d.pop("messageKey", UNSET)

        multi_value_type = d.pop("multiValueType", UNSET)

        name = d.pop("name", UNSET)

        value_class = d.pop("valueClass", UNSET)

        de_his_appclient_jsf_cs_sys_job_configuration_settings_job_setting_type = cls(
            declaring_class=declaring_class,
            message_key=message_key,
            multi_value_type=multi_value_type,
            name=name,
            value_class=value_class,
        )

        de_his_appclient_jsf_cs_sys_job_configuration_settings_job_setting_type.additional_properties = d
        return de_his_appclient_jsf_cs_sys_job_configuration_settings_job_setting_type

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
