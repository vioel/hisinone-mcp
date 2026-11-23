from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_jobs_job_handle import CsSysJobsJobHandle
    from ..models.cs_sys_jobs_job_protocol_line import CsSysJobsJobProtocolLine


T = TypeVar("T", bound="CsSysJobsJobProtocolChunk")


@_attrs_define
class CsSysJobsJobProtocolChunk:
    """
    Attributes:
        end_pos (int | Unset):
        handle (CsSysJobsJobHandle | Unset):
        lines (list[CsSysJobsJobProtocolLine] | Unset):
        start_pos (int | Unset):
    """

    end_pos: int | Unset = UNSET
    handle: CsSysJobsJobHandle | Unset = UNSET
    lines: list[CsSysJobsJobProtocolLine] | Unset = UNSET
    start_pos: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        end_pos = self.end_pos

        handle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.handle, Unset):
            handle = self.handle.to_dict()

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        start_pos = self.start_pos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_pos is not UNSET:
            field_dict["endPos"] = end_pos
        if handle is not UNSET:
            field_dict["handle"] = handle
        if lines is not UNSET:
            field_dict["lines"] = lines
        if start_pos is not UNSET:
            field_dict["startPos"] = start_pos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_jobs_job_handle import CsSysJobsJobHandle  # noqa: PLC0415
        from ..models.cs_sys_jobs_job_protocol_line import CsSysJobsJobProtocolLine  # noqa: PLC0415

        d = dict(src_dict)
        end_pos = d.pop("endPos", UNSET)

        _handle = d.pop("handle", UNSET)
        handle: CsSysJobsJobHandle | Unset
        if isinstance(_handle, Unset):
            handle = UNSET
        else:
            handle = CsSysJobsJobHandle.from_dict(_handle)

        _lines = d.pop("lines", UNSET)
        lines: list[CsSysJobsJobProtocolLine] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = CsSysJobsJobProtocolLine.from_dict(lines_item_data)

                lines.append(lines_item)

        start_pos = d.pop("startPos", UNSET)

        cs_sys_jobs_job_protocol_chunk = cls(
            end_pos=end_pos,
            handle=handle,
            lines=lines,
            start_pos=start_pos,
        )

        cs_sys_jobs_job_protocol_chunk.additional_properties = d
        return cs_sys_jobs_job_protocol_chunk

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
