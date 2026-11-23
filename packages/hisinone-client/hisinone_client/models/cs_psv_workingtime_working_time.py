from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_workingtime_working_time_foreigntext import CsPsvWorkingtimeWorkingTimeForeigntext


T = TypeVar("T", bound="CsPsvWorkingtimeWorkingTime")


@_attrs_define
class CsPsvWorkingtimeWorkingTime:
    """
    Attributes:
        field_foreigntext (CsPsvWorkingtimeWorkingTimeForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        tariff_working_hours_per_week (float | Unset):
        working_hours_in_percent (float | Unset):
    """

    field_foreigntext: CsPsvWorkingtimeWorkingTimeForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    tariff_working_hours_per_week: float | Unset = UNSET
    working_hours_in_percent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        tariff_working_hours_per_week = self.tariff_working_hours_per_week

        working_hours_in_percent = self.working_hours_in_percent

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
        if tariff_working_hours_per_week is not UNSET:
            field_dict["tariffWorkingHoursPerWeek"] = tariff_working_hours_per_week
        if working_hours_in_percent is not UNSET:
            field_dict["workingHoursInPercent"] = working_hours_in_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_workingtime_working_time_foreigntext import CsPsvWorkingtimeWorkingTimeForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvWorkingtimeWorkingTimeForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvWorkingtimeWorkingTimeForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        tariff_working_hours_per_week = d.pop("tariffWorkingHoursPerWeek", UNSET)

        working_hours_in_percent = d.pop("workingHoursInPercent", UNSET)

        cs_psv_workingtime_working_time = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            tariff_working_hours_per_week=tariff_working_hours_per_week,
            working_hours_in_percent=working_hours_in_percent,
        )

        cs_psv_workingtime_working_time.additional_properties = d
        return cs_psv_workingtime_working_time

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
