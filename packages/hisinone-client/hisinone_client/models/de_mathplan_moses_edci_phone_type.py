from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeMathplanMosesEdciPhoneType")


@_attrs_define
class DeMathplanMosesEdciPhoneType:
    """
    Attributes:
        area_dialing (str | Unset):
        country_dialing (str | Unset):
        dial_number (str | Unset):
        phone_number (str | Unset):
    """

    area_dialing: str | Unset = UNSET
    country_dialing: str | Unset = UNSET
    dial_number: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        area_dialing = self.area_dialing

        country_dialing = self.country_dialing

        dial_number = self.dial_number

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area_dialing is not UNSET:
            field_dict["areaDialing"] = area_dialing
        if country_dialing is not UNSET:
            field_dict["countryDialing"] = country_dialing
        if dial_number is not UNSET:
            field_dict["dialNumber"] = dial_number
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area_dialing = d.pop("areaDialing", UNSET)

        country_dialing = d.pop("countryDialing", UNSET)

        dial_number = d.pop("dialNumber", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        de_mathplan_moses_edci_phone_type = cls(
            area_dialing=area_dialing,
            country_dialing=country_dialing,
            dial_number=dial_number,
            phone_number=phone_number,
        )

        de_mathplan_moses_edci_phone_type.additional_properties = d
        return de_mathplan_moses_edci_phone_type

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
