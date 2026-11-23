from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_demo_his_my_dynamic_demo_data_upload_files import (
        CsSysUploadConfigurationDemoHisMyDynamicDemoDataUploadFiles,
    )


T = TypeVar("T", bound="CsSysUploadConfigurationDemoHisMyDynamicDemoData")


@_attrs_define
class CsSysUploadConfigurationDemoHisMyDynamicDemoData:
    """
    Attributes:
        additional_data (str | Unset):
        upload_files (CsSysUploadConfigurationDemoHisMyDynamicDemoDataUploadFiles | Unset):
    """

    additional_data: str | Unset = UNSET
    upload_files: CsSysUploadConfigurationDemoHisMyDynamicDemoDataUploadFiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_data = self.additional_data

        upload_files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upload_files, Unset):
            upload_files = self.upload_files.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_data is not UNSET:
            field_dict["additionalData"] = additional_data
        if upload_files is not UNSET:
            field_dict["uploadFiles"] = upload_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_demo_his_my_dynamic_demo_data_upload_files import (
            CsSysUploadConfigurationDemoHisMyDynamicDemoDataUploadFiles,  # noqa: PLC0415
        )

        d = dict(src_dict)
        additional_data = d.pop("additionalData", UNSET)

        _upload_files = d.pop("uploadFiles", UNSET)
        upload_files: CsSysUploadConfigurationDemoHisMyDynamicDemoDataUploadFiles | Unset
        if isinstance(_upload_files, Unset):
            upload_files = UNSET
        else:
            upload_files = CsSysUploadConfigurationDemoHisMyDynamicDemoDataUploadFiles.from_dict(_upload_files)

        cs_sys_upload_configuration_demo_his_my_dynamic_demo_data = cls(
            additional_data=additional_data,
            upload_files=upload_files,
        )

        cs_sys_upload_configuration_demo_his_my_dynamic_demo_data.additional_properties = d
        return cs_sys_upload_configuration_demo_his_my_dynamic_demo_data

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
