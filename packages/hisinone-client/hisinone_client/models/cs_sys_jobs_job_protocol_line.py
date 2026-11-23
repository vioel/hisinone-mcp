from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_notification_notification_type import CsSysNotificationNotificationType


T = TypeVar("T", bound="CsSysJobsJobProtocolLine")


@_attrs_define
class CsSysJobsJobProtocolLine:
    """
    Attributes:
        created_at (int | Unset):
        message (str | Unset):
        type_ (CsSysNotificationNotificationType | Unset):
    """

    created_at: int | Unset = UNSET
    message: str | Unset = UNSET
    type_: CsSysNotificationNotificationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        message = self.message

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_notification_notification_type import CsSysNotificationNotificationType  # noqa: PLC0415

        d = dict(src_dict)
        created_at = d.pop("createdAt", UNSET)

        message = d.pop("message", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CsSysNotificationNotificationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CsSysNotificationNotificationType.from_dict(_type_)

        cs_sys_jobs_job_protocol_line = cls(
            created_at=created_at,
            message=message,
            type_=type_,
        )

        cs_sys_jobs_job_protocol_line.additional_properties = d
        return cs_sys_jobs_job_protocol_line

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
