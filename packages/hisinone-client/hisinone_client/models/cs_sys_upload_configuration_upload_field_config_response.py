from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysUploadConfigurationUploadFieldConfigResponse")


@_attrs_define
class CsSysUploadConfigurationUploadFieldConfigResponse:
    """
    Attributes:
        allow_comment (bool | Unset):
        allowed_content_types (list[str] | Unset):
        allowed_extensions (list[str] | Unset):
        config_key (str | Unset):
        css (str | Unset):
        document_metadata_category_ids (list[int] | Unset):
        file_limit (int | Unset):
        helptext_above (str | Unset):
        helptext_below (str | Unset):
        helptext_icon (str | Unset):
        label (str | Unset):
        multiple_upload (bool | Unset):
        readonly (bool | Unset):
        required (bool | Unset):
        show_category_if_unique (bool | Unset):
        size_limit (int | Unset):
    """

    allow_comment: bool | Unset = UNSET
    allowed_content_types: list[str] | Unset = UNSET
    allowed_extensions: list[str] | Unset = UNSET
    config_key: str | Unset = UNSET
    css: str | Unset = UNSET
    document_metadata_category_ids: list[int] | Unset = UNSET
    file_limit: int | Unset = UNSET
    helptext_above: str | Unset = UNSET
    helptext_below: str | Unset = UNSET
    helptext_icon: str | Unset = UNSET
    label: str | Unset = UNSET
    multiple_upload: bool | Unset = UNSET
    readonly: bool | Unset = UNSET
    required: bool | Unset = UNSET
    show_category_if_unique: bool | Unset = UNSET
    size_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        allow_comment = self.allow_comment

        allowed_content_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_content_types, Unset):
            allowed_content_types = self.allowed_content_types

        allowed_extensions: list[str] | Unset = UNSET
        if not isinstance(self.allowed_extensions, Unset):
            allowed_extensions = self.allowed_extensions

        config_key = self.config_key

        css = self.css

        document_metadata_category_ids: list[int] | Unset = UNSET
        if not isinstance(self.document_metadata_category_ids, Unset):
            document_metadata_category_ids = self.document_metadata_category_ids

        file_limit = self.file_limit

        helptext_above = self.helptext_above

        helptext_below = self.helptext_below

        helptext_icon = self.helptext_icon

        label = self.label

        multiple_upload = self.multiple_upload

        readonly = self.readonly

        required = self.required

        show_category_if_unique = self.show_category_if_unique

        size_limit = self.size_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_comment is not UNSET:
            field_dict["allowComment"] = allow_comment
        if allowed_content_types is not UNSET:
            field_dict["allowedContentTypes"] = allowed_content_types
        if allowed_extensions is not UNSET:
            field_dict["allowedExtensions"] = allowed_extensions
        if config_key is not UNSET:
            field_dict["configKey"] = config_key
        if css is not UNSET:
            field_dict["css"] = css
        if document_metadata_category_ids is not UNSET:
            field_dict["documentMetadataCategoryIds"] = document_metadata_category_ids
        if file_limit is not UNSET:
            field_dict["fileLimit"] = file_limit
        if helptext_above is not UNSET:
            field_dict["helptextAbove"] = helptext_above
        if helptext_below is not UNSET:
            field_dict["helptextBelow"] = helptext_below
        if helptext_icon is not UNSET:
            field_dict["helptextIcon"] = helptext_icon
        if label is not UNSET:
            field_dict["label"] = label
        if multiple_upload is not UNSET:
            field_dict["multipleUpload"] = multiple_upload
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if required is not UNSET:
            field_dict["required"] = required
        if show_category_if_unique is not UNSET:
            field_dict["showCategoryIfUnique"] = show_category_if_unique
        if size_limit is not UNSET:
            field_dict["sizeLimit"] = size_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_comment = d.pop("allowComment", UNSET)

        allowed_content_types = cast(list[str], d.pop("allowedContentTypes", UNSET))

        allowed_extensions = cast(list[str], d.pop("allowedExtensions", UNSET))

        config_key = d.pop("configKey", UNSET)

        css = d.pop("css", UNSET)

        document_metadata_category_ids = cast(list[int], d.pop("documentMetadataCategoryIds", UNSET))

        file_limit = d.pop("fileLimit", UNSET)

        helptext_above = d.pop("helptextAbove", UNSET)

        helptext_below = d.pop("helptextBelow", UNSET)

        helptext_icon = d.pop("helptextIcon", UNSET)

        label = d.pop("label", UNSET)

        multiple_upload = d.pop("multipleUpload", UNSET)

        readonly = d.pop("readonly", UNSET)

        required = d.pop("required", UNSET)

        show_category_if_unique = d.pop("showCategoryIfUnique", UNSET)

        size_limit = d.pop("sizeLimit", UNSET)

        cs_sys_upload_configuration_upload_field_config_response = cls(
            allow_comment=allow_comment,
            allowed_content_types=allowed_content_types,
            allowed_extensions=allowed_extensions,
            config_key=config_key,
            css=css,
            document_metadata_category_ids=document_metadata_category_ids,
            file_limit=file_limit,
            helptext_above=helptext_above,
            helptext_below=helptext_below,
            helptext_icon=helptext_icon,
            label=label,
            multiple_upload=multiple_upload,
            readonly=readonly,
            required=required,
            show_category_if_unique=show_category_if_unique,
            size_limit=size_limit,
        )

        cs_sys_upload_configuration_upload_field_config_response.additional_properties = d
        return cs_sys_upload_configuration_upload_field_config_response

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
