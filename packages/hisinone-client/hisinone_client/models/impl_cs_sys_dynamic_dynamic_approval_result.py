from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.impl_cs_sys_dynamic_dynamic_approval_result_foreigntext import (
        ImplCsSysDynamicDynamicApprovalResultForeigntext,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_object import ImplCsSysDynamicDynamicObject


T = TypeVar("T", bound="ImplCsSysDynamicDynamicApprovalResult")


@_attrs_define
class ImplCsSysDynamicDynamicApprovalResult:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicDynamicApprovalResultForeigntext | Unset):
        approval_status (CsSysValueGenericValue | Unset):
        dynamic_object (ImplCsSysDynamicDynamicObject | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person (CsPsvPersonRest | Unset):
        remark (str | Unset):
        right_level (int | Unset):
        rule_identifier (str | Unset):
    """

    field_foreigntext: ImplCsSysDynamicDynamicApprovalResultForeigntext | Unset = UNSET
    approval_status: CsSysValueGenericValue | Unset = UNSET
    dynamic_object: ImplCsSysDynamicDynamicObject | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person: CsPsvPersonRest | Unset = UNSET
    remark: str | Unset = UNSET
    right_level: int | Unset = UNSET
    rule_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        approval_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.approval_status, Unset):
            approval_status = self.approval_status.to_dict()

        dynamic_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_object, Unset):
            dynamic_object = self.dynamic_object.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        remark = self.remark

        right_level = self.right_level

        rule_identifier = self.rule_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if approval_status is not UNSET:
            field_dict["approvalStatus"] = approval_status
        if dynamic_object is not UNSET:
            field_dict["dynamicObject"] = dynamic_object
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person is not UNSET:
            field_dict["person"] = person
        if remark is not UNSET:
            field_dict["remark"] = remark
        if right_level is not UNSET:
            field_dict["rightLevel"] = right_level
        if rule_identifier is not UNSET:
            field_dict["ruleIdentifier"] = rule_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_approval_result_foreigntext import (
            ImplCsSysDynamicDynamicApprovalResultForeigntext,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_dynamic_object import ImplCsSysDynamicDynamicObject  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicDynamicApprovalResultForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicDynamicApprovalResultForeigntext.from_dict(_field_foreigntext)

        _approval_status = d.pop("approvalStatus", UNSET)
        approval_status: CsSysValueGenericValue | Unset
        if isinstance(_approval_status, Unset):
            approval_status = UNSET
        else:
            approval_status = CsSysValueGenericValue.from_dict(_approval_status)

        _dynamic_object = d.pop("dynamicObject", UNSET)
        dynamic_object: ImplCsSysDynamicDynamicObject | Unset
        if isinstance(_dynamic_object, Unset):
            dynamic_object = UNSET
        else:
            dynamic_object = ImplCsSysDynamicDynamicObject.from_dict(_dynamic_object)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _person = d.pop("person", UNSET)
        person: CsPsvPersonRest | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CsPsvPersonRest.from_dict(_person)

        remark = d.pop("remark", UNSET)

        right_level = d.pop("rightLevel", UNSET)

        rule_identifier = d.pop("ruleIdentifier", UNSET)

        impl_cs_sys_dynamic_dynamic_approval_result = cls(
            field_foreigntext=field_foreigntext,
            approval_status=approval_status,
            dynamic_object=dynamic_object,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person=person,
            remark=remark,
            right_level=right_level,
            rule_identifier=rule_identifier,
        )

        impl_cs_sys_dynamic_dynamic_approval_result.additional_properties = d
        return impl_cs_sys_dynamic_dynamic_approval_result

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
