from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_personnelcost_financing_foreigntext import CsPsvPersonnelcostFinancingForeigntext
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPersonnelcostFinancing")


@_attrs_define
class CsPsvPersonnelcostFinancing:
    """
    Attributes:
        field_foreigntext (CsPsvPersonnelcostFinancingForeigntext | Unset):
        budget_source_type (CsSysValueGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: CsPsvPersonnelcostFinancingForeigntext | Unset = UNSET
    budget_source_type: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        budget_source_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_source_type, Unset):
            budget_source_type = self.budget_source_type.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if budget_source_type is not UNSET:
            field_dict["budgetSourceType"] = budget_source_type
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_personnelcost_financing_foreigntext import CsPsvPersonnelcostFinancingForeigntext  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPersonnelcostFinancingForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPersonnelcostFinancingForeigntext.from_dict(_field_foreigntext)

        _budget_source_type = d.pop("budgetSourceType", UNSET)
        budget_source_type: CsSysValueGenericValue | Unset
        if isinstance(_budget_source_type, Unset):
            budget_source_type = UNSET
        else:
            budget_source_type = CsSysValueGenericValue.from_dict(_budget_source_type)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        cs_psv_personnelcost_financing = cls(
            field_foreigntext=field_foreigntext,
            budget_source_type=budget_source_type,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        cs_psv_personnelcost_financing.additional_properties = d
        return cs_psv_personnelcost_financing

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
