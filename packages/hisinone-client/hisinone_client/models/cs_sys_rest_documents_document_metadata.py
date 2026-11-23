from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_rest_documents_document_metadata_foreigntext import (
        CsSysRestDocumentsDocumentMetadataForeigntext,
    )
    from ..models.cs_sys_rest_documents_mimedata import CsSysRestDocumentsMimedata
    from ..models.cs_sys_value_document_delete_policy_value import CsSysValueDocumentDeletePolicyValue
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.de_his_core_datatype_his_resource import DeHisCoreDatatypeHisResource


T = TypeVar("T", bound="CsSysRestDocumentsDocumentMetadata")


@_attrs_define
class CsSysRestDocumentsDocumentMetadata:
    """
    Attributes:
        field_foreigntext (CsSysRestDocumentsDocumentMetadataForeigntext | Unset):
        category (CsSysValueGenericValue | Unset):
        created_at (int | Unset):
        created_by (CsPsvPersonRest | Unset):
        doc_download_url (str | Unset):
        document_delete_policy_value (CsSysValueDocumentDeletePolicyValue | Unset):
        file_name (str | Unset):
        file_size_reduce_allowed (bool | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        mimedata (CsSysRestDocumentsMimedata | Unset):
        obj_guid (str | Unset):
        purpose (CsSysValueGenericValue | Unset):
        target (str | Unset):
        target_id (int | Unset):
        uploaded_resource (DeHisCoreDatatypeHisResource | Unset):
        visibility (CsSysValueGenericValue | Unset):
    """

    field_foreigntext: CsSysRestDocumentsDocumentMetadataForeigntext | Unset = UNSET
    category: CsSysValueGenericValue | Unset = UNSET
    created_at: int | Unset = UNSET
    created_by: CsPsvPersonRest | Unset = UNSET
    doc_download_url: str | Unset = UNSET
    document_delete_policy_value: CsSysValueDocumentDeletePolicyValue | Unset = UNSET
    file_name: str | Unset = UNSET
    file_size_reduce_allowed: bool | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    mimedata: CsSysRestDocumentsMimedata | Unset = UNSET
    obj_guid: str | Unset = UNSET
    purpose: CsSysValueGenericValue | Unset = UNSET
    target: str | Unset = UNSET
    target_id: int | Unset = UNSET
    uploaded_resource: DeHisCoreDatatypeHisResource | Unset = UNSET
    visibility: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        created_at = self.created_at

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        doc_download_url = self.doc_download_url

        document_delete_policy_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_delete_policy_value, Unset):
            document_delete_policy_value = self.document_delete_policy_value.to_dict()

        file_name = self.file_name

        file_size_reduce_allowed = self.file_size_reduce_allowed

        id = self.id

        lock_version = self.lock_version

        mimedata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mimedata, Unset):
            mimedata = self.mimedata.to_dict()

        obj_guid = self.obj_guid

        purpose: dict[str, Any] | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        target = self.target

        target_id = self.target_id

        uploaded_resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uploaded_resource, Unset):
            uploaded_resource = self.uploaded_resource.to_dict()

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if category is not UNSET:
            field_dict["category"] = category
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if doc_download_url is not UNSET:
            field_dict["docDownloadUrl"] = doc_download_url
        if document_delete_policy_value is not UNSET:
            field_dict["documentDeletePolicyValue"] = document_delete_policy_value
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size_reduce_allowed is not UNSET:
            field_dict["fileSizeReduceAllowed"] = file_size_reduce_allowed
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if mimedata is not UNSET:
            field_dict["mimedata"] = mimedata
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if target is not UNSET:
            field_dict["target"] = target
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if uploaded_resource is not UNSET:
            field_dict["uploadedResource"] = uploaded_resource
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_rest_documents_document_metadata_foreigntext import (
            CsSysRestDocumentsDocumentMetadataForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_sys_rest_documents_mimedata import CsSysRestDocumentsMimedata  # noqa: PLC0415
        from ..models.cs_sys_value_document_delete_policy_value import CsSysValueDocumentDeletePolicyValue  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.de_his_core_datatype_his_resource import DeHisCoreDatatypeHisResource  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsSysRestDocumentsDocumentMetadataForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsSysRestDocumentsDocumentMetadataForeigntext.from_dict(_field_foreigntext)

        _category = d.pop("category", UNSET)
        category: CsSysValueGenericValue | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CsSysValueGenericValue.from_dict(_category)

        created_at = d.pop("createdAt", UNSET)

        _created_by = d.pop("createdBy", UNSET)
        created_by: CsPsvPersonRest | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = CsPsvPersonRest.from_dict(_created_by)

        doc_download_url = d.pop("docDownloadUrl", UNSET)

        _document_delete_policy_value = d.pop("documentDeletePolicyValue", UNSET)
        document_delete_policy_value: CsSysValueDocumentDeletePolicyValue | Unset
        if isinstance(_document_delete_policy_value, Unset):
            document_delete_policy_value = UNSET
        else:
            document_delete_policy_value = CsSysValueDocumentDeletePolicyValue.from_dict(_document_delete_policy_value)

        file_name = d.pop("fileName", UNSET)

        file_size_reduce_allowed = d.pop("fileSizeReduceAllowed", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        _mimedata = d.pop("mimedata", UNSET)
        mimedata: CsSysRestDocumentsMimedata | Unset
        if isinstance(_mimedata, Unset):
            mimedata = UNSET
        else:
            mimedata = CsSysRestDocumentsMimedata.from_dict(_mimedata)

        obj_guid = d.pop("objGuid", UNSET)

        _purpose = d.pop("purpose", UNSET)
        purpose: CsSysValueGenericValue | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = CsSysValueGenericValue.from_dict(_purpose)

        target = d.pop("target", UNSET)

        target_id = d.pop("targetId", UNSET)

        _uploaded_resource = d.pop("uploadedResource", UNSET)
        uploaded_resource: DeHisCoreDatatypeHisResource | Unset
        if isinstance(_uploaded_resource, Unset):
            uploaded_resource = UNSET
        else:
            uploaded_resource = DeHisCoreDatatypeHisResource.from_dict(_uploaded_resource)

        _visibility = d.pop("visibility", UNSET)
        visibility: CsSysValueGenericValue | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = CsSysValueGenericValue.from_dict(_visibility)

        cs_sys_rest_documents_document_metadata = cls(
            field_foreigntext=field_foreigntext,
            category=category,
            created_at=created_at,
            created_by=created_by,
            doc_download_url=doc_download_url,
            document_delete_policy_value=document_delete_policy_value,
            file_name=file_name,
            file_size_reduce_allowed=file_size_reduce_allowed,
            id=id,
            lock_version=lock_version,
            mimedata=mimedata,
            obj_guid=obj_guid,
            purpose=purpose,
            target=target,
            target_id=target_id,
            uploaded_resource=uploaded_resource,
            visibility=visibility,
        )

        cs_sys_rest_documents_document_metadata.additional_properties = d
        return cs_sys_rest_documents_document_metadata

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
