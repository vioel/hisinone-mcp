from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_document_document import RmErpCommonDocumentDocument
    from ..models.rm_erp_jobapplication_job_application_content import RmErpJobapplicationJobApplicationContent
    from ..models.rm_erp_jobapplication_job_application_data_and_documents_foreigntext import (
        RmErpJobapplicationJobApplicationDataAndDocumentsForeigntext,
    )


T = TypeVar("T", bound="RmErpJobapplicationJobApplicationDataAndDocuments")


@_attrs_define
class RmErpJobapplicationJobApplicationDataAndDocuments:
    """
    Attributes:
        field_foreigntext (RmErpJobapplicationJobApplicationDataAndDocumentsForeigntext | Unset):
        application (RmErpJobapplicationJobApplicationContent | Unset):
        documents (list[RmErpCommonDocumentDocument] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        privacy_policy_accepted (bool | Unset):
    """

    field_foreigntext: RmErpJobapplicationJobApplicationDataAndDocumentsForeigntext | Unset = UNSET
    application: RmErpJobapplicationJobApplicationContent | Unset = UNSET
    documents: list[RmErpCommonDocumentDocument] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    privacy_policy_accepted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        privacy_policy_accepted = self.privacy_policy_accepted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if application is not UNSET:
            field_dict["application"] = application
        if documents is not UNSET:
            field_dict["documents"] = documents
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if privacy_policy_accepted is not UNSET:
            field_dict["privacyPolicyAccepted"] = privacy_policy_accepted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_document_document import RmErpCommonDocumentDocument  # noqa: PLC0415
        from ..models.rm_erp_jobapplication_job_application_content import RmErpJobapplicationJobApplicationContent  # noqa: PLC0415
        from ..models.rm_erp_jobapplication_job_application_data_and_documents_foreigntext import (
            RmErpJobapplicationJobApplicationDataAndDocumentsForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpJobapplicationJobApplicationDataAndDocumentsForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpJobapplicationJobApplicationDataAndDocumentsForeigntext.from_dict(
                _field_foreigntext
            )

        _application = d.pop("application", UNSET)
        application: RmErpJobapplicationJobApplicationContent | Unset
        if isinstance(_application, Unset):
            application = UNSET
        else:
            application = RmErpJobapplicationJobApplicationContent.from_dict(_application)

        _documents = d.pop("documents", UNSET)
        documents: list[RmErpCommonDocumentDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RmErpCommonDocumentDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        privacy_policy_accepted = d.pop("privacyPolicyAccepted", UNSET)

        rm_erp_jobapplication_job_application_data_and_documents = cls(
            field_foreigntext=field_foreigntext,
            application=application,
            documents=documents,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            privacy_policy_accepted=privacy_policy_accepted,
        )

        rm_erp_jobapplication_job_application_data_and_documents.additional_properties = d
        return rm_erp_jobapplication_job_application_data_and_documents

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
