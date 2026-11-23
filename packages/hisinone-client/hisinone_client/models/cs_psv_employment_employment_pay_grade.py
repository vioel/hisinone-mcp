from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_employment_employment_pay_grade_foreigntext import CsPsvEmploymentEmploymentPayGradeForeigntext
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvEmploymentEmploymentPayGrade")


@_attrs_define
class CsPsvEmploymentEmploymentPayGrade:
    """
    Attributes:
        field_foreigntext (CsPsvEmploymentEmploymentPayGradeForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        pay_grade (CsSysValueGenericValue | Unset):
    """

    field_foreigntext: CsPsvEmploymentEmploymentPayGradeForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    pay_grade: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        pay_grade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pay_grade, Unset):
            pay_grade = self.pay_grade.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if pay_grade is not UNSET:
            field_dict["payGrade"] = pay_grade

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_employment_employment_pay_grade_foreigntext import (
            CsPsvEmploymentEmploymentPayGradeForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvEmploymentEmploymentPayGradeForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvEmploymentEmploymentPayGradeForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _pay_grade = d.pop("payGrade", UNSET)
        pay_grade: CsSysValueGenericValue | Unset
        if isinstance(_pay_grade, Unset):
            pay_grade = UNSET
        else:
            pay_grade = CsSysValueGenericValue.from_dict(_pay_grade)

        cs_psv_employment_employment_pay_grade = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            pay_grade=pay_grade,
        )

        cs_psv_employment_employment_pay_grade.additional_properties = d
        return cs_psv_employment_employment_pay_grade

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
