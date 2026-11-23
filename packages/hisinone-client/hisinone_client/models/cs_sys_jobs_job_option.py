from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_container_job_settings_container import (
        DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer,
    )


T = TypeVar("T", bound="CsSysJobsJobOption")


@_attrs_define
class CsSysJobsJobOption:
    """
    Attributes:
        default_job_settings (list[DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer] |
            Unset):
        force_show_config (bool | Unset):
        job_configuration (str | Unset):
        key (str | Unset):
        name (str | Unset):
        quickstarter_icon (str | Unset):
        sortorder (int | Unset):
    """

    default_job_settings: list[DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer] | Unset = (
        UNSET
    )
    force_show_config: bool | Unset = UNSET
    job_configuration: str | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    quickstarter_icon: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        default_job_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_job_settings, Unset):
            default_job_settings = []
            for default_job_settings_item_data in self.default_job_settings:
                default_job_settings_item = default_job_settings_item_data.to_dict()
                default_job_settings.append(default_job_settings_item)

        force_show_config = self.force_show_config

        job_configuration = self.job_configuration

        key = self.key

        name = self.name

        quickstarter_icon = self.quickstarter_icon

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_job_settings is not UNSET:
            field_dict["defaultJobSettings"] = default_job_settings
        if force_show_config is not UNSET:
            field_dict["forceShowConfig"] = force_show_config
        if job_configuration is not UNSET:
            field_dict["jobConfiguration"] = job_configuration
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if quickstarter_icon is not UNSET:
            field_dict["quickstarterIcon"] = quickstarter_icon
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_container_job_settings_container import (
            DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _default_job_settings = d.pop("defaultJobSettings", UNSET)
        default_job_settings: (
            list[DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer] | Unset
        ) = UNSET
        if _default_job_settings is not UNSET:
            default_job_settings = []
            for default_job_settings_item_data in _default_job_settings:
                default_job_settings_item = (
                    DeHisAppclientJsfCsSysJobConfigurationSettingsContainerJobSettingsContainer.from_dict(
                        default_job_settings_item_data
                    )
                )

                default_job_settings.append(default_job_settings_item)

        force_show_config = d.pop("forceShowConfig", UNSET)

        job_configuration = d.pop("jobConfiguration", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        quickstarter_icon = d.pop("quickstarterIcon", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        cs_sys_jobs_job_option = cls(
            default_job_settings=default_job_settings,
            force_show_config=force_show_config,
            job_configuration=job_configuration,
            key=key,
            name=name,
            quickstarter_icon=quickstarter_icon,
            sortorder=sortorder,
        )

        cs_sys_jobs_job_option.additional_properties = d
        return cs_sys_jobs_job_option

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
