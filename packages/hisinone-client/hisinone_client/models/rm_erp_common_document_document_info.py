from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_document_document_category_value import RmErpCommonDocumentDocumentCategoryValue
    from ..models.rm_erp_common_document_document_info_foreigntext import RmErpCommonDocumentDocumentInfoForeigntext


T = TypeVar("T", bound="RmErpCommonDocumentDocumentInfo")


@_attrs_define
class RmErpCommonDocumentDocumentInfo:
    """
    Attributes:
        field_foreigntext (RmErpCommonDocumentDocumentInfoForeigntext | Unset):
        comment (str | Unset):
        document_category (RmErpCommonDocumentDocumentCategoryValue | Unset):
        filename (str | Unset):
        filesize (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        timestamp (int | Unset):
    """

    field_foreigntext: RmErpCommonDocumentDocumentInfoForeigntext | Unset = UNSET
    comment: str | Unset = UNSET
    document_category: RmErpCommonDocumentDocumentCategoryValue | Unset = UNSET
    filename: str | Unset = UNSET
    filesize: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        comment = self.comment

        document_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        filename = self.filename

        filesize = self.filesize

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if comment is not UNSET:
            field_dict["comment"] = comment
        if document_category is not UNSET:
            field_dict["documentCategory"] = document_category
        if filename is not UNSET:
            field_dict["filename"] = filename
        if filesize is not UNSET:
            field_dict["filesize"] = filesize
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_document_document_category_value import RmErpCommonDocumentDocumentCategoryValue  # noqa: PLC0415
        from ..models.rm_erp_common_document_document_info_foreigntext import RmErpCommonDocumentDocumentInfoForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonDocumentDocumentInfoForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonDocumentDocumentInfoForeigntext.from_dict(_field_foreigntext)

        comment = d.pop("comment", UNSET)

        _document_category = d.pop("documentCategory", UNSET)
        document_category: RmErpCommonDocumentDocumentCategoryValue | Unset
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = RmErpCommonDocumentDocumentCategoryValue.from_dict(_document_category)

        filename = d.pop("filename", UNSET)

        filesize = d.pop("filesize", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        rm_erp_common_document_document_info = cls(
            field_foreigntext=field_foreigntext,
            comment=comment,
            document_category=document_category,
            filename=filename,
            filesize=filesize,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            timestamp=timestamp,
        )

        rm_erp_common_document_document_info.additional_properties = d
        return rm_erp_common_document_document_info

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
