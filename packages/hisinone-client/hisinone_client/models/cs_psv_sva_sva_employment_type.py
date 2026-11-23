from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsPsvSvaSvaEmploymentType")


@_attrs_define
class CsPsvSvaSvaEmploymentType:
    """
    Attributes:
        employment_type_id (int | Unset):
        pbv_art (str | Unset):
    """

    employment_type_id: int | Unset = UNSET
    pbv_art: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        employment_type_id = self.employment_type_id

        pbv_art = self.pbv_art

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if employment_type_id is not UNSET:
            field_dict["employmentTypeId"] = employment_type_id
        if pbv_art is not UNSET:
            field_dict["pbvArt"] = pbv_art

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        employment_type_id = d.pop("employmentTypeId", UNSET)

        pbv_art = d.pop("pbvArt", UNSET)

        cs_psv_sva_sva_employment_type = cls(
            employment_type_id=employment_type_id,
            pbv_art=pbv_art,
        )

        cs_psv_sva_sva_employment_type.additional_properties = d
        return cs_psv_sva_sva_employment_type

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
