from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_publication_publication_document_metadata_foreigntext import (
        FsResPublicationPublicationDocumentMetadataForeigntext,
    )


T = TypeVar("T", bound="FsResPublicationPublicationDocumentMetadata")


@_attrs_define
class FsResPublicationPublicationDocumentMetadata:
    """
    Attributes:
        field_foreigntext (FsResPublicationPublicationDocumentMetadataForeigntext | Unset):
        access (CsSysValueGenericValue | Unset):
        access_after_embargo_date (CsSysValueGenericValue | Unset):
        documents (list[CsSysUploadConfigurationHisUploadFile] | Unset):
        embargo_date (int | Unset):
        id (int | Unset):
        license_ (CsSysValueGenericValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        title (str | Unset):
    """

    field_foreigntext: FsResPublicationPublicationDocumentMetadataForeigntext | Unset = UNSET
    access: CsSysValueGenericValue | Unset = UNSET
    access_after_embargo_date: CsSysValueGenericValue | Unset = UNSET
    documents: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
    embargo_date: int | Unset = UNSET
    id: int | Unset = UNSET
    license_: CsSysValueGenericValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        access_after_embargo_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access_after_embargo_date, Unset):
            access_after_embargo_date = self.access_after_embargo_date.to_dict()

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        embargo_date = self.embargo_date

        id = self.id

        license_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if access is not UNSET:
            field_dict["access"] = access
        if access_after_embargo_date is not UNSET:
            field_dict["accessAfterEmbargoDate"] = access_after_embargo_date
        if documents is not UNSET:
            field_dict["documents"] = documents
        if embargo_date is not UNSET:
            field_dict["embargoDate"] = embargo_date
        if id is not UNSET:
            field_dict["id"] = id
        if license_ is not UNSET:
            field_dict["license"] = license_
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_upload_configuration_his_upload_file import CsSysUploadConfigurationHisUploadFile  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_publication_document_metadata_foreigntext import (
            FsResPublicationPublicationDocumentMetadataForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationPublicationDocumentMetadataForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationPublicationDocumentMetadataForeigntext.from_dict(_field_foreigntext)

        _access = d.pop("access", UNSET)
        access: CsSysValueGenericValue | Unset
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = CsSysValueGenericValue.from_dict(_access)

        _access_after_embargo_date = d.pop("accessAfterEmbargoDate", UNSET)
        access_after_embargo_date: CsSysValueGenericValue | Unset
        if isinstance(_access_after_embargo_date, Unset):
            access_after_embargo_date = UNSET
        else:
            access_after_embargo_date = CsSysValueGenericValue.from_dict(_access_after_embargo_date)

        _documents = d.pop("documents", UNSET)
        documents: list[CsSysUploadConfigurationHisUploadFile] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = CsSysUploadConfigurationHisUploadFile.from_dict(documents_item_data)

                documents.append(documents_item)

        embargo_date = d.pop("embargoDate", UNSET)

        id = d.pop("id", UNSET)

        _license_ = d.pop("license", UNSET)
        license_: CsSysValueGenericValue | Unset
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = CsSysValueGenericValue.from_dict(_license_)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        title = d.pop("title", UNSET)

        fs_res_publication_publication_document_metadata = cls(
            field_foreigntext=field_foreigntext,
            access=access,
            access_after_embargo_date=access_after_embargo_date,
            documents=documents,
            embargo_date=embargo_date,
            id=id,
            license_=license_,
            lock_version=lock_version,
            obj_guid=obj_guid,
            title=title,
        )

        fs_res_publication_publication_document_metadata.additional_properties = d
        return fs_res_publication_publication_document_metadata

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
