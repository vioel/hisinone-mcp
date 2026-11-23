from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile


T = TypeVar("T", bound="CsSysTestUploadTestRestControllerUploadTestRest")


@_attrs_define
class CsSysTestUploadTestRestControllerUploadTestRest:
    """
    Attributes:
        file_list (list[CsSysUploadConfigurationHisUploadFile] | Unset):
        other_data (str | Unset):
        single_file (CsSysUploadConfigurationHisUploadFile | Unset):
    """

    file_list: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
    other_data: str | Unset = UNSET
    single_file: CsSysUploadConfigurationHisUploadFile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        file_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_list, Unset):
            file_list = []
            for file_list_item_data in self.file_list:
                file_list_item = file_list_item_data.to_dict()
                file_list.append(file_list_item)

        other_data = self.other_data

        single_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.single_file, Unset):
            single_file = self.single_file.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_list is not UNSET:
            field_dict["fileList"] = file_list
        if other_data is not UNSET:
            field_dict["otherData"] = other_data
        if single_file is not UNSET:
            field_dict["singleFile"] = single_file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415

        d = dict(src_dict)
        _file_list = d.pop("fileList", UNSET)
        file_list: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
        if _file_list is not UNSET:
            file_list = []
            for file_list_item_data in _file_list:
                file_list_item = CsSysUploadConfigurationHisUploadFile.from_dict(file_list_item_data)

                file_list.append(file_list_item)

        other_data = d.pop("otherData", UNSET)

        _single_file = d.pop("singleFile", UNSET)
        single_file: CsSysUploadConfigurationHisUploadFile | Unset
        if isinstance(_single_file, Unset):
            single_file = UNSET
        else:
            single_file = CsSysUploadConfigurationHisUploadFile.from_dict(_single_file)

        cs_sys_test_upload_test_rest_controller_upload_test_rest = cls(
            file_list=file_list,
            other_data=other_data,
            single_file=single_file,
        )

        cs_sys_test_upload_test_rest_controller_upload_test_rest.additional_properties = d
        return cs_sys_test_upload_test_rest_controller_upload_test_rest

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
