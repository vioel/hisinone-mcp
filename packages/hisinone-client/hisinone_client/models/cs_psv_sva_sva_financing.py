from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsPsvSvaSvaFinancing")


@_attrs_define
class CsPsvSvaSvaFinancing:
    """
    Attributes:
        pbv_id (int | Unset):
        pfi_art (str | Unset):
        pfi_bis (int | Unset):
        pfi_prozent (float | Unset):
        pfi_serial (int | Unset):
        pfi_von (int | Unset):
        poz_institut (str | Unset):
    """

    pbv_id: int | Unset = UNSET
    pfi_art: str | Unset = UNSET
    pfi_bis: int | Unset = UNSET
    pfi_prozent: float | Unset = UNSET
    pfi_serial: int | Unset = UNSET
    pfi_von: int | Unset = UNSET
    poz_institut: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        pbv_id = self.pbv_id

        pfi_art = self.pfi_art

        pfi_bis = self.pfi_bis

        pfi_prozent = self.pfi_prozent

        pfi_serial = self.pfi_serial

        pfi_von = self.pfi_von

        poz_institut = self.poz_institut

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pbv_id is not UNSET:
            field_dict["pbvId"] = pbv_id
        if pfi_art is not UNSET:
            field_dict["pfiArt"] = pfi_art
        if pfi_bis is not UNSET:
            field_dict["pfiBis"] = pfi_bis
        if pfi_prozent is not UNSET:
            field_dict["pfiProzent"] = pfi_prozent
        if pfi_serial is not UNSET:
            field_dict["pfiSerial"] = pfi_serial
        if pfi_von is not UNSET:
            field_dict["pfiVon"] = pfi_von
        if poz_institut is not UNSET:
            field_dict["pozInstitut"] = poz_institut

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pbv_id = d.pop("pbvId", UNSET)

        pfi_art = d.pop("pfiArt", UNSET)

        pfi_bis = d.pop("pfiBis", UNSET)

        pfi_prozent = d.pop("pfiProzent", UNSET)

        pfi_serial = d.pop("pfiSerial", UNSET)

        pfi_von = d.pop("pfiVon", UNSET)

        poz_institut = d.pop("pozInstitut", UNSET)

        cs_psv_sva_sva_financing = cls(
            pbv_id=pbv_id,
            pfi_art=pfi_art,
            pfi_bis=pfi_bis,
            pfi_prozent=pfi_prozent,
            pfi_serial=pfi_serial,
            pfi_von=pfi_von,
            poz_institut=poz_institut,
        )

        cs_psv_sva_sva_financing.additional_properties = d
        return cs_psv_sva_sva_financing

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
