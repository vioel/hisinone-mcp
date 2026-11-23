from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsPsvSvaSvaWorkingTime")


@_attrs_define
class CsPsvSvaSvaWorkingTime:
    """
    Attributes:
        paz_bis (int | Unset):
        paz_serial (int | Unset):
        paz_tz_proz (float | Unset):
        paz_von (int | Unset):
        pbv_id (int | Unset):
    """

    paz_bis: int | Unset = UNSET
    paz_serial: int | Unset = UNSET
    paz_tz_proz: float | Unset = UNSET
    paz_von: int | Unset = UNSET
    pbv_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        paz_bis = self.paz_bis

        paz_serial = self.paz_serial

        paz_tz_proz = self.paz_tz_proz

        paz_von = self.paz_von

        pbv_id = self.pbv_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paz_bis is not UNSET:
            field_dict["pazBis"] = paz_bis
        if paz_serial is not UNSET:
            field_dict["pazSerial"] = paz_serial
        if paz_tz_proz is not UNSET:
            field_dict["pazTzProz"] = paz_tz_proz
        if paz_von is not UNSET:
            field_dict["pazVon"] = paz_von
        if pbv_id is not UNSET:
            field_dict["pbvId"] = pbv_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paz_bis = d.pop("pazBis", UNSET)

        paz_serial = d.pop("pazSerial", UNSET)

        paz_tz_proz = d.pop("pazTzProz", UNSET)

        paz_von = d.pop("pazVon", UNSET)

        pbv_id = d.pop("pbvId", UNSET)

        cs_psv_sva_sva_working_time = cls(
            paz_bis=paz_bis,
            paz_serial=paz_serial,
            paz_tz_proz=paz_tz_proz,
            paz_von=paz_von,
            pbv_id=pbv_id,
        )

        cs_psv_sva_sva_working_time.additional_properties = d
        return cs_psv_sva_sva_working_time

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
