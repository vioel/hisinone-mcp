from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting import (
        DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting,
    )


T = TypeVar("T", bound="DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer")


@_attrs_define
class DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer:
    """
    Attributes:
        description (str | Unset):
        label (str | Unset):
        name (str | Unset):
        settings (list[DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting] | Unset):
    """

    description: str | Unset = UNSET
    label: str | Unset = UNSET
    name: str | Unset = UNSET
    settings: list[DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        label = self.label

        name = self.name

        settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = []
            for settings_item_data in self.settings:
                settings_item = settings_item_data.to_dict()
                settings.append(settings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting import (
            DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting,  # noqa: PLC0415
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: list[DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting] | Unset = UNSET
        if _settings is not UNSET:
            settings = []
            for settings_item_data in _settings:
                settings_item = DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting.from_dict(
                    settings_item_data
                )

                settings.append(settings_item)

        de_his_appclient_jsf_cs_sys_job_configuration_settings_container_job_settings_container = cls(
            description=description,
            label=label,
            name=name,
            settings=settings,
        )

        de_his_appclient_jsf_cs_sys_job_configuration_settings_container_job_settings_container.additional_properties = d
        return de_his_appclient_jsf_cs_sys_job_configuration_settings_container_job_settings_container

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
