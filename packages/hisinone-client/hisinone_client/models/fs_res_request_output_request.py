from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_request_output_request_foreigntext import FsResRequestOutputRequestForeigntext


T = TypeVar("T", bound="FsResRequestOutputRequest")


@_attrs_define
class FsResRequestOutputRequest:
    """
    Attributes:
        field_foreigntext (FsResRequestOutputRequestForeigntext | Unset):
        execution_time (int | Unset):
        executor (CsPsvPersonRest | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        output_media (CsSysValueGenericValue | Unset):
        recipient (CsPsvPersonRest | Unset):
        report_id (int | Unset):
        request_time (int | Unset):
        requester (CsPsvPersonRest | Unset):
    """

    field_foreigntext: FsResRequestOutputRequestForeigntext | Unset = UNSET
    execution_time: int | Unset = UNSET
    executor: CsPsvPersonRest | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    output_media: CsSysValueGenericValue | Unset = UNSET
    recipient: CsPsvPersonRest | Unset = UNSET
    report_id: int | Unset = UNSET
    request_time: int | Unset = UNSET
    requester: CsPsvPersonRest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        execution_time = self.execution_time

        executor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executor, Unset):
            executor = self.executor.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        output_media: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_media, Unset):
            output_media = self.output_media.to_dict()

        recipient: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        report_id = self.report_id

        request_time = self.request_time

        requester: dict[str, Any] | Unset = UNSET
        if not isinstance(self.requester, Unset):
            requester = self.requester.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if execution_time is not UNSET:
            field_dict["executionTime"] = execution_time
        if executor is not UNSET:
            field_dict["executor"] = executor
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if output_media is not UNSET:
            field_dict["outputMedia"] = output_media
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if request_time is not UNSET:
            field_dict["requestTime"] = request_time
        if requester is not UNSET:
            field_dict["requester"] = requester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_request_output_request_foreigntext import FsResRequestOutputRequestForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResRequestOutputRequestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResRequestOutputRequestForeigntext.from_dict(_field_foreigntext)

        execution_time = d.pop("executionTime", UNSET)

        _executor = d.pop("executor", UNSET)
        executor: CsPsvPersonRest | Unset
        if isinstance(_executor, Unset):
            executor = UNSET
        else:
            executor = CsPsvPersonRest.from_dict(_executor)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _output_media = d.pop("outputMedia", UNSET)
        output_media: CsSysValueGenericValue | Unset
        if isinstance(_output_media, Unset):
            output_media = UNSET
        else:
            output_media = CsSysValueGenericValue.from_dict(_output_media)

        _recipient = d.pop("recipient", UNSET)
        recipient: CsPsvPersonRest | Unset
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = CsPsvPersonRest.from_dict(_recipient)

        report_id = d.pop("reportId", UNSET)

        request_time = d.pop("requestTime", UNSET)

        _requester = d.pop("requester", UNSET)
        requester: CsPsvPersonRest | Unset
        if isinstance(_requester, Unset):
            requester = UNSET
        else:
            requester = CsPsvPersonRest.from_dict(_requester)

        fs_res_request_output_request = cls(
            field_foreigntext=field_foreigntext,
            execution_time=execution_time,
            executor=executor,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            output_media=output_media,
            recipient=recipient,
            report_id=report_id,
            request_time=request_time,
            requester=requester,
        )

        fs_res_request_output_request.additional_properties = d
        return fs_res_request_output_request

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
