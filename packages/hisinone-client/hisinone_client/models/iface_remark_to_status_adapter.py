from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iface_remark_on_exam import IfaceRemarkOnExam
    from ..models.iface_workstatus import IfaceWorkstatus


T = TypeVar("T", bound="IfaceRemarkToStatusAdapter")


@_attrs_define
class IfaceRemarkToStatusAdapter:
    """
    Attributes:
        associated_remark (IfaceRemarkOnExam | Unset):
        cancellation (bool | Unset):
        grade (float | Unset):
        id (int | Unset):
        input_remark (IfaceRemarkOnExam | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        workstatus (IfaceWorkstatus | Unset):
    """

    associated_remark: IfaceRemarkOnExam | Unset = UNSET
    cancellation: bool | Unset = UNSET
    grade: float | Unset = UNSET
    id: int | Unset = UNSET
    input_remark: IfaceRemarkOnExam | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    workstatus: IfaceWorkstatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        associated_remark: dict[str, Any] | Unset = UNSET
        if not isinstance(self.associated_remark, Unset):
            associated_remark = self.associated_remark.to_dict()

        cancellation = self.cancellation

        grade = self.grade

        id = self.id

        input_remark: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_remark, Unset):
            input_remark = self.input_remark.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        workstatus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workstatus, Unset):
            workstatus = self.workstatus.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associated_remark is not UNSET:
            field_dict["associatedRemark"] = associated_remark
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if grade is not UNSET:
            field_dict["grade"] = grade
        if id is not UNSET:
            field_dict["id"] = id
        if input_remark is not UNSET:
            field_dict["inputRemark"] = input_remark
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if workstatus is not UNSET:
            field_dict["workstatus"] = workstatus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iface_remark_on_exam import IfaceRemarkOnExam  # noqa: PLC0415
        from ..models.iface_workstatus import IfaceWorkstatus  # noqa: PLC0415

        d = dict(src_dict)
        _associated_remark = d.pop("associatedRemark", UNSET)
        associated_remark: IfaceRemarkOnExam | Unset
        if isinstance(_associated_remark, Unset):
            associated_remark = UNSET
        else:
            associated_remark = IfaceRemarkOnExam.from_dict(_associated_remark)

        cancellation = d.pop("cancellation", UNSET)

        grade = d.pop("grade", UNSET)

        id = d.pop("id", UNSET)

        _input_remark = d.pop("inputRemark", UNSET)
        input_remark: IfaceRemarkOnExam | Unset
        if isinstance(_input_remark, Unset):
            input_remark = UNSET
        else:
            input_remark = IfaceRemarkOnExam.from_dict(_input_remark)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _workstatus = d.pop("workstatus", UNSET)
        workstatus: IfaceWorkstatus | Unset
        if isinstance(_workstatus, Unset):
            workstatus = UNSET
        else:
            workstatus = IfaceWorkstatus.from_dict(_workstatus)

        iface_remark_to_status_adapter = cls(
            associated_remark=associated_remark,
            cancellation=cancellation,
            grade=grade,
            id=id,
            input_remark=input_remark,
            lock_version=lock_version,
            obj_guid=obj_guid,
            workstatus=workstatus,
        )

        iface_remark_to_status_adapter.additional_properties = d
        return iface_remark_to_status_adapter

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
