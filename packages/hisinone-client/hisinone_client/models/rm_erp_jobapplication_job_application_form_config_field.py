from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_jobapplication_job_application_form_config_field_min_file import (
        RmErpJobapplicationJobApplicationFormConfigFieldMinFile,
    )


T = TypeVar("T", bound="RmErpJobapplicationJobApplicationFormConfigField")


@_attrs_define
class RmErpJobapplicationJobApplicationFormConfigField:
    """
    Attributes:
        active (str | Unset):
        allowed_file_extensions (list[str] | Unset):
        mandatory (str | Unset):
        max_file_size (str | Unset):
        max_files (str | Unset):
        min_files (list[RmErpJobapplicationJobApplicationFormConfigFieldMinFile] | Unset):
        ref (str | Unset):
    """

    active: str | Unset = UNSET
    allowed_file_extensions: list[str] | Unset = UNSET
    mandatory: str | Unset = UNSET
    max_file_size: str | Unset = UNSET
    max_files: str | Unset = UNSET
    min_files: list[RmErpJobapplicationJobApplicationFormConfigFieldMinFile] | Unset = UNSET
    ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        allowed_file_extensions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_file_extensions, Unset):
            allowed_file_extensions = self.allowed_file_extensions

        mandatory = self.mandatory

        max_file_size = self.max_file_size

        max_files = self.max_files

        min_files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.min_files, Unset):
            min_files = []
            for min_files_item_data in self.min_files:
                min_files_item = min_files_item_data.to_dict()
                min_files.append(min_files_item)

        ref = self.ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if allowed_file_extensions is not UNSET:
            field_dict["allowedFileExtensions"] = allowed_file_extensions
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if max_file_size is not UNSET:
            field_dict["maxFileSize"] = max_file_size
        if max_files is not UNSET:
            field_dict["maxFiles"] = max_files
        if min_files is not UNSET:
            field_dict["minFiles"] = min_files
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_jobapplication_job_application_form_config_field_min_file import (
            RmErpJobapplicationJobApplicationFormConfigFieldMinFile,  # noqa: PLC0415
        )

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        allowed_file_extensions = cast(list[str], d.pop("allowedFileExtensions", UNSET))

        mandatory = d.pop("mandatory", UNSET)

        max_file_size = d.pop("maxFileSize", UNSET)

        max_files = d.pop("maxFiles", UNSET)

        _min_files = d.pop("minFiles", UNSET)
        min_files: list[RmErpJobapplicationJobApplicationFormConfigFieldMinFile] | Unset = UNSET
        if _min_files is not UNSET:
            min_files = []
            for min_files_item_data in _min_files:
                min_files_item = RmErpJobapplicationJobApplicationFormConfigFieldMinFile.from_dict(min_files_item_data)

                min_files.append(min_files_item)

        ref = d.pop("ref", UNSET)

        rm_erp_jobapplication_job_application_form_config_field = cls(
            active=active,
            allowed_file_extensions=allowed_file_extensions,
            mandatory=mandatory,
            max_file_size=max_file_size,
            max_files=max_files,
            min_files=min_files,
            ref=ref,
        )

        rm_erp_jobapplication_job_application_form_config_field.additional_properties = d
        return rm_erp_jobapplication_job_application_form_config_field

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
