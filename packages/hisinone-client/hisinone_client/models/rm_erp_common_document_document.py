from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_document_document_category_value import RmErpCommonDocumentDocumentCategoryValue
    from ..models.rm_erp_common_document_document_foreigntext import RmErpCommonDocumentDocumentForeigntext
    from ..models.rm_erp_common_filemanagement_storage_location_enum import RmErpCommonFilemanagementStorageLocationEnum
    from ..models.rm_erp_common_person_person_basic_data import RmErpCommonPersonPersonBasicData


T = TypeVar("T", bound="RmErpCommonDocumentDocument")


@_attrs_define
class RmErpCommonDocumentDocument:
    """
    Attributes:
        field_foreigntext (RmErpCommonDocumentDocumentForeigntext | Unset):
        comment (str | Unset):
        dms_join_id (str | Unset):
        document_category (RmErpCommonDocumentDocumentCategoryValue | Unset):
        file (list[int] | Unset):
        filename (str | Unset):
        filesize (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person (RmErpCommonPersonPersonBasicData | Unset):
        storage_location (RmErpCommonFilemanagementStorageLocationEnum | Unset):
        timestamp (int | Unset):
    """

    field_foreigntext: RmErpCommonDocumentDocumentForeigntext | Unset = UNSET
    comment: str | Unset = UNSET
    dms_join_id: str | Unset = UNSET
    document_category: RmErpCommonDocumentDocumentCategoryValue | Unset = UNSET
    file: list[int] | Unset = UNSET
    filename: str | Unset = UNSET
    filesize: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person: RmErpCommonPersonPersonBasicData | Unset = UNSET
    storage_location: RmErpCommonFilemanagementStorageLocationEnum | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        comment = self.comment

        dms_join_id = self.dms_join_id

        document_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        file: list[int] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file

        filename = self.filename

        filesize = self.filesize

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        storage_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storage_location, Unset):
            storage_location = self.storage_location.to_dict()

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if comment is not UNSET:
            field_dict["comment"] = comment
        if dms_join_id is not UNSET:
            field_dict["dmsJoinId"] = dms_join_id
        if document_category is not UNSET:
            field_dict["documentCategory"] = document_category
        if file is not UNSET:
            field_dict["file"] = file
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
        if person is not UNSET:
            field_dict["person"] = person
        if storage_location is not UNSET:
            field_dict["storageLocation"] = storage_location
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_document_document_category_value import RmErpCommonDocumentDocumentCategoryValue  # noqa: PLC0415
        from ..models.rm_erp_common_document_document_foreigntext import RmErpCommonDocumentDocumentForeigntext  # noqa: PLC0415
        from ..models.rm_erp_common_filemanagement_storage_location_enum import (
            RmErpCommonFilemanagementStorageLocationEnum,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_person_person_basic_data import RmErpCommonPersonPersonBasicData  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonDocumentDocumentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonDocumentDocumentForeigntext.from_dict(_field_foreigntext)

        comment = d.pop("comment", UNSET)

        dms_join_id = d.pop("dmsJoinId", UNSET)

        _document_category = d.pop("documentCategory", UNSET)
        document_category: RmErpCommonDocumentDocumentCategoryValue | Unset
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = RmErpCommonDocumentDocumentCategoryValue.from_dict(_document_category)

        file = cast(list[int], d.pop("file", UNSET))

        filename = d.pop("filename", UNSET)

        filesize = d.pop("filesize", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _person = d.pop("person", UNSET)
        person: RmErpCommonPersonPersonBasicData | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = RmErpCommonPersonPersonBasicData.from_dict(_person)

        _storage_location = d.pop("storageLocation", UNSET)
        storage_location: RmErpCommonFilemanagementStorageLocationEnum | Unset
        if isinstance(_storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = RmErpCommonFilemanagementStorageLocationEnum.from_dict(_storage_location)

        timestamp = d.pop("timestamp", UNSET)

        rm_erp_common_document_document = cls(
            field_foreigntext=field_foreigntext,
            comment=comment,
            dms_join_id=dms_join_id,
            document_category=document_category,
            file=file,
            filename=filename,
            filesize=filesize,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person=person,
            storage_location=storage_location,
            timestamp=timestamp,
        )

        rm_erp_common_document_document.additional_properties = d
        return rm_erp_common_document_document

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
