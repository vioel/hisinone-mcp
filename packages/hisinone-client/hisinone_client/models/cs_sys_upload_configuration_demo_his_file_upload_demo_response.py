from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile


T = TypeVar("T", bound="CsSysUploadConfigurationDemoHisFileUploadDemoResponse")


@_attrs_define
class CsSysUploadConfigurationDemoHisFileUploadDemoResponse:
    """
    Attributes:
        additional_form_data (str | Unset):
        uploaded_files (list[CsSysUploadConfigurationHisUploadFile] | Unset):
    """

    additional_form_data: str | Unset = UNSET
    uploaded_files: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_form_data = self.additional_form_data

        uploaded_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.uploaded_files, Unset):
            uploaded_files = []
            for uploaded_files_item_data in self.uploaded_files:
                uploaded_files_item = uploaded_files_item_data.to_dict()
                uploaded_files.append(uploaded_files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_form_data is not UNSET:
            field_dict["additionalFormData"] = additional_form_data
        if uploaded_files is not UNSET:
            field_dict["uploadedFiles"] = uploaded_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415

        d = dict(src_dict)
        additional_form_data = d.pop("additionalFormData", UNSET)

        _uploaded_files = d.pop("uploadedFiles", UNSET)
        uploaded_files: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
        if _uploaded_files is not UNSET:
            uploaded_files = []
            for uploaded_files_item_data in _uploaded_files:
                uploaded_files_item = CsSysUploadConfigurationHisUploadFile.from_dict(uploaded_files_item_data)

                uploaded_files.append(uploaded_files_item)

        cs_sys_upload_configuration_demo_his_file_upload_demo_response = cls(
            additional_form_data=additional_form_data,
            uploaded_files=uploaded_files,
        )

        cs_sys_upload_configuration_demo_his_file_upload_demo_response.additional_properties = d
        return cs_sys_upload_configuration_demo_his_file_upload_demo_response

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
