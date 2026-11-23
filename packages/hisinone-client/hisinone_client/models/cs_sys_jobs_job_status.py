from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_jobs_job_handle import CsSysJobsJobHandle


T = TypeVar("T", bound="CsSysJobsJobStatus")


@_attrs_define
class CsSysJobsJobStatus:
    """
    Attributes:
        document_metadata_id (int | Unset):
        finished_at (int | Unset):
        handle (CsSysJobsJobHandle | Unset):
        job_key (str | Unset):
        job_name (str | Unset):
        notification_log_id (int | Unset):
        num_failed_items (int | Unset):
        num_successful_items (int | Unset):
        num_total_items (int | Unset):
        result_document_url (str | Unset):
        started_at (int | Unset):
        status (str | Unset):
        status_msg_key (str | Unset):
    """

    document_metadata_id: int | Unset = UNSET
    finished_at: int | Unset = UNSET
    handle: CsSysJobsJobHandle | Unset = UNSET
    job_key: str | Unset = UNSET
    job_name: str | Unset = UNSET
    notification_log_id: int | Unset = UNSET
    num_failed_items: int | Unset = UNSET
    num_successful_items: int | Unset = UNSET
    num_total_items: int | Unset = UNSET
    result_document_url: str | Unset = UNSET
    started_at: int | Unset = UNSET
    status: str | Unset = UNSET
    status_msg_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        document_metadata_id = self.document_metadata_id

        finished_at = self.finished_at

        handle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.handle, Unset):
            handle = self.handle.to_dict()

        job_key = self.job_key

        job_name = self.job_name

        notification_log_id = self.notification_log_id

        num_failed_items = self.num_failed_items

        num_successful_items = self.num_successful_items

        num_total_items = self.num_total_items

        result_document_url = self.result_document_url

        started_at = self.started_at

        status = self.status

        status_msg_key = self.status_msg_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_metadata_id is not UNSET:
            field_dict["documentMetadataId"] = document_metadata_id
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if handle is not UNSET:
            field_dict["handle"] = handle
        if job_key is not UNSET:
            field_dict["jobKey"] = job_key
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if notification_log_id is not UNSET:
            field_dict["notificationLogId"] = notification_log_id
        if num_failed_items is not UNSET:
            field_dict["numFailedItems"] = num_failed_items
        if num_successful_items is not UNSET:
            field_dict["numSuccessfulItems"] = num_successful_items
        if num_total_items is not UNSET:
            field_dict["numTotalItems"] = num_total_items
        if result_document_url is not UNSET:
            field_dict["resultDocumentUrl"] = result_document_url
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if status is not UNSET:
            field_dict["status"] = status
        if status_msg_key is not UNSET:
            field_dict["statusMsgKey"] = status_msg_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_jobs_job_handle import CsSysJobsJobHandle  # noqa: PLC0415

        d = dict(src_dict)
        document_metadata_id = d.pop("documentMetadataId", UNSET)

        finished_at = d.pop("finishedAt", UNSET)

        _handle = d.pop("handle", UNSET)
        handle: CsSysJobsJobHandle | Unset
        if isinstance(_handle, Unset):
            handle = UNSET
        else:
            handle = CsSysJobsJobHandle.from_dict(_handle)

        job_key = d.pop("jobKey", UNSET)

        job_name = d.pop("jobName", UNSET)

        notification_log_id = d.pop("notificationLogId", UNSET)

        num_failed_items = d.pop("numFailedItems", UNSET)

        num_successful_items = d.pop("numSuccessfulItems", UNSET)

        num_total_items = d.pop("numTotalItems", UNSET)

        result_document_url = d.pop("resultDocumentUrl", UNSET)

        started_at = d.pop("startedAt", UNSET)

        status = d.pop("status", UNSET)

        status_msg_key = d.pop("statusMsgKey", UNSET)

        cs_sys_jobs_job_status = cls(
            document_metadata_id=document_metadata_id,
            finished_at=finished_at,
            handle=handle,
            job_key=job_key,
            job_name=job_name,
            notification_log_id=notification_log_id,
            num_failed_items=num_failed_items,
            num_successful_items=num_successful_items,
            num_total_items=num_total_items,
            result_document_url=result_document_url,
            started_at=started_at,
            status=status,
            status_msg_key=status_msg_key,
        )

        cs_sys_jobs_job_status.additional_properties = d
        return cs_sys_jobs_job_status

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
