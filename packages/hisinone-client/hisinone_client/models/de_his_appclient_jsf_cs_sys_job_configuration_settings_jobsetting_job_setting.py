from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_meta_field_metadata_datatype import CsSysMetaFieldMetadataDatatype
    from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_job_setting_type import (
        DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType,
    )
    from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting_meta import (
        DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSettingMeta,
    )


T = TypeVar("T", bound="DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting")


@_attrs_define
class DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSetting:
    """
    Attributes:
        active (bool | Unset):
        applied_contexts (list[str] | Unset):
        available_datatypes (list[CsSysMetaFieldMetadataDatatype] | Unset):
        default_value (Any | Unset):
        extension_job_setting_validator (str | Unset):
        helptext (str | Unset):
        label (str | Unset):
        meta (DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSettingMeta | Unset):
        metadata_possibly_customized (bool | Unset):
        name (str | Unset):
        readonly (bool | Unset):
        required (bool | Unset):
        type_ (DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType | Unset):
        value (Any | Unset):
    """

    active: bool | Unset = UNSET
    applied_contexts: list[str] | Unset = UNSET
    available_datatypes: list[CsSysMetaFieldMetadataDatatype] | Unset = UNSET
    default_value: Any | Unset = UNSET
    extension_job_setting_validator: str | Unset = UNSET
    helptext: str | Unset = UNSET
    label: str | Unset = UNSET
    meta: DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSettingMeta | Unset = UNSET
    metadata_possibly_customized: bool | Unset = UNSET
    name: str | Unset = UNSET
    readonly: bool | Unset = UNSET
    required: bool | Unset = UNSET
    type_: DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType | Unset = UNSET
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        applied_contexts: list[str] | Unset = UNSET
        if not isinstance(self.applied_contexts, Unset):
            applied_contexts = self.applied_contexts

        available_datatypes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_datatypes, Unset):
            available_datatypes = []
            for available_datatypes_item_data in self.available_datatypes:
                available_datatypes_item = available_datatypes_item_data.to_dict()
                available_datatypes.append(available_datatypes_item)

        default_value = self.default_value

        extension_job_setting_validator = self.extension_job_setting_validator

        helptext = self.helptext

        label = self.label

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        metadata_possibly_customized = self.metadata_possibly_customized

        name = self.name

        readonly = self.readonly

        required = self.required

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if applied_contexts is not UNSET:
            field_dict["appliedContexts"] = applied_contexts
        if available_datatypes is not UNSET:
            field_dict["availableDatatypes"] = available_datatypes
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if extension_job_setting_validator is not UNSET:
            field_dict["extensionJobSettingValidator"] = extension_job_setting_validator
        if helptext is not UNSET:
            field_dict["helptext"] = helptext
        if label is not UNSET:
            field_dict["label"] = label
        if meta is not UNSET:
            field_dict["meta"] = meta
        if metadata_possibly_customized is not UNSET:
            field_dict["metadataPossiblyCustomized"] = metadata_possibly_customized
        if name is not UNSET:
            field_dict["name"] = name
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if required is not UNSET:
            field_dict["required"] = required
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_meta_field_metadata_datatype import CsSysMetaFieldMetadataDatatype  # noqa: PLC0415
        from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_job_setting_type import (
            DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType,  # noqa: PLC0415
        )
        from ..models.de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting_meta import (
            DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSettingMeta,  # noqa: PLC0415
        )

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        applied_contexts = cast(list[str], d.pop("appliedContexts", UNSET))

        _available_datatypes = d.pop("availableDatatypes", UNSET)
        available_datatypes: list[CsSysMetaFieldMetadataDatatype] | Unset = UNSET
        if _available_datatypes is not UNSET:
            available_datatypes = []
            for available_datatypes_item_data in _available_datatypes:
                available_datatypes_item = CsSysMetaFieldMetadataDatatype.from_dict(available_datatypes_item_data)

                available_datatypes.append(available_datatypes_item)

        default_value = d.pop("defaultValue", UNSET)

        extension_job_setting_validator = d.pop("extensionJobSettingValidator", UNSET)

        helptext = d.pop("helptext", UNSET)

        label = d.pop("label", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSettingMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DeHisAppclientJsfCsSysJobConfigurationSettingsJobsettingJobSettingMeta.from_dict(_meta)

        metadata_possibly_customized = d.pop("metadataPossiblyCustomized", UNSET)

        name = d.pop("name", UNSET)

        readonly = d.pop("readonly", UNSET)

        required = d.pop("required", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DeHisAppclientJsfCsSysJobConfigurationSettingsJobSettingType.from_dict(_type_)

        value = d.pop("value", UNSET)

        de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting = cls(
            active=active,
            applied_contexts=applied_contexts,
            available_datatypes=available_datatypes,
            default_value=default_value,
            extension_job_setting_validator=extension_job_setting_validator,
            helptext=helptext,
            label=label,
            meta=meta,
            metadata_possibly_customized=metadata_possibly_customized,
            name=name,
            readonly=readonly,
            required=required,
            type_=type_,
            value=value,
        )

        de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting.additional_properties = d
        return de_his_appclient_jsf_cs_sys_job_configuration_settings_jobsetting_job_setting

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
