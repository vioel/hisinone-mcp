from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysUploadConfigurationHisUploadFile")


@_attrs_define
class CsSysUploadConfigurationHisUploadFile:
    """
    Attributes:
        archivable (bool | Unset):
        base64 (str | Unset):
        comment (str | Unset):
        config_key (str | Unset):
        content_type (str | Unset):
        created_at (int | Unset):
        document_metadata_category_id (int | Unset):
        download_url (str | Unset):
        expire_date (int | Unset):
        id (int | Unset):
        last_modified (str | Unset):
        name (str | Unset):
        sortorder (int | Unset):
        uuid (str | Unset):
    """

    archivable: bool | Unset = UNSET
    base64: str | Unset = UNSET
    comment: str | Unset = UNSET
    config_key: str | Unset = UNSET
    content_type: str | Unset = UNSET
    created_at: int | Unset = UNSET
    document_metadata_category_id: int | Unset = UNSET
    download_url: str | Unset = UNSET
    expire_date: int | Unset = UNSET
    id: int | Unset = UNSET
    last_modified: str | Unset = UNSET
    name: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        archivable = self.archivable

        base64 = self.base64

        comment = self.comment

        config_key = self.config_key

        content_type = self.content_type

        created_at = self.created_at

        document_metadata_category_id = self.document_metadata_category_id

        download_url = self.download_url

        expire_date = self.expire_date

        id = self.id

        last_modified = self.last_modified

        name = self.name

        sortorder = self.sortorder

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archivable is not UNSET:
            field_dict["archivable"] = archivable
        if base64 is not UNSET:
            field_dict["base64"] = base64
        if comment is not UNSET:
            field_dict["comment"] = comment
        if config_key is not UNSET:
            field_dict["configKey"] = config_key
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if document_metadata_category_id is not UNSET:
            field_dict["documentMetadataCategoryId"] = document_metadata_category_id
        if download_url is not UNSET:
            field_dict["downloadUrl"] = download_url
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date
        if id is not UNSET:
            field_dict["id"] = id
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if name is not UNSET:
            field_dict["name"] = name
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archivable = d.pop("archivable", UNSET)

        base64 = d.pop("base64", UNSET)

        comment = d.pop("comment", UNSET)

        config_key = d.pop("configKey", UNSET)

        content_type = d.pop("contentType", UNSET)

        created_at = d.pop("createdAt", UNSET)

        document_metadata_category_id = d.pop("documentMetadataCategoryId", UNSET)

        download_url = d.pop("downloadUrl", UNSET)

        expire_date = d.pop("expireDate", UNSET)

        id = d.pop("id", UNSET)

        last_modified = d.pop("lastModified", UNSET)

        name = d.pop("name", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        uuid = d.pop("uuid", UNSET)

        cs_sys_upload_configuration_his_upload_file = cls(
            archivable=archivable,
            base64=base64,
            comment=comment,
            config_key=config_key,
            content_type=content_type,
            created_at=created_at,
            document_metadata_category_id=document_metadata_category_id,
            download_url=download_url,
            expire_date=expire_date,
            id=id,
            last_modified=last_modified,
            name=name,
            sortorder=sortorder,
            uuid=uuid,
        )

        cs_sys_upload_configuration_his_upload_file.additional_properties = d
        return cs_sys_upload_configuration_his_upload_file

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
