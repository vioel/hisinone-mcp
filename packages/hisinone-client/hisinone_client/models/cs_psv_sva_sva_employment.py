from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsPsvSvaSvaEmployment")


@_attrs_define
class CsPsvSvaSvaEmployment:
    """
    Attributes:
        pbv_activity_type (str | Unset):
        pbv_art (str | Unset):
        pbv_befr (int | Unset):
        pbv_bis (int | Unset):
        pbv_id (int | Unset):
        pbv_nr (int | Unset):
        pbv_qualifizierungsverfahren (str | Unset):
        pbv_type (str | Unset):
        pbv_von (int | Unset):
        pgd_familyname (str | Unset):
        pgd_firstname (str | Unset):
        pgd_gender (str | Unset):
        pgd_id (int | Unset):
    """

    pbv_activity_type: str | Unset = UNSET
    pbv_art: str | Unset = UNSET
    pbv_befr: int | Unset = UNSET
    pbv_bis: int | Unset = UNSET
    pbv_id: int | Unset = UNSET
    pbv_nr: int | Unset = UNSET
    pbv_qualifizierungsverfahren: str | Unset = UNSET
    pbv_type: str | Unset = UNSET
    pbv_von: int | Unset = UNSET
    pgd_familyname: str | Unset = UNSET
    pgd_firstname: str | Unset = UNSET
    pgd_gender: str | Unset = UNSET
    pgd_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        pbv_activity_type = self.pbv_activity_type

        pbv_art = self.pbv_art

        pbv_befr = self.pbv_befr

        pbv_bis = self.pbv_bis

        pbv_id = self.pbv_id

        pbv_nr = self.pbv_nr

        pbv_qualifizierungsverfahren = self.pbv_qualifizierungsverfahren

        pbv_type = self.pbv_type

        pbv_von = self.pbv_von

        pgd_familyname = self.pgd_familyname

        pgd_firstname = self.pgd_firstname

        pgd_gender = self.pgd_gender

        pgd_id = self.pgd_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pbv_activity_type is not UNSET:
            field_dict["pbvActivityType"] = pbv_activity_type
        if pbv_art is not UNSET:
            field_dict["pbvArt"] = pbv_art
        if pbv_befr is not UNSET:
            field_dict["pbvBefr"] = pbv_befr
        if pbv_bis is not UNSET:
            field_dict["pbvBis"] = pbv_bis
        if pbv_id is not UNSET:
            field_dict["pbvId"] = pbv_id
        if pbv_nr is not UNSET:
            field_dict["pbvNr"] = pbv_nr
        if pbv_qualifizierungsverfahren is not UNSET:
            field_dict["pbvQualifizierungsverfahren"] = pbv_qualifizierungsverfahren
        if pbv_type is not UNSET:
            field_dict["pbvType"] = pbv_type
        if pbv_von is not UNSET:
            field_dict["pbvVon"] = pbv_von
        if pgd_familyname is not UNSET:
            field_dict["pgdFamilyname"] = pgd_familyname
        if pgd_firstname is not UNSET:
            field_dict["pgdFirstname"] = pgd_firstname
        if pgd_gender is not UNSET:
            field_dict["pgdGender"] = pgd_gender
        if pgd_id is not UNSET:
            field_dict["pgdId"] = pgd_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pbv_activity_type = d.pop("pbvActivityType", UNSET)

        pbv_art = d.pop("pbvArt", UNSET)

        pbv_befr = d.pop("pbvBefr", UNSET)

        pbv_bis = d.pop("pbvBis", UNSET)

        pbv_id = d.pop("pbvId", UNSET)

        pbv_nr = d.pop("pbvNr", UNSET)

        pbv_qualifizierungsverfahren = d.pop("pbvQualifizierungsverfahren", UNSET)

        pbv_type = d.pop("pbvType", UNSET)

        pbv_von = d.pop("pbvVon", UNSET)

        pgd_familyname = d.pop("pgdFamilyname", UNSET)

        pgd_firstname = d.pop("pgdFirstname", UNSET)

        pgd_gender = d.pop("pgdGender", UNSET)

        pgd_id = d.pop("pgdId", UNSET)

        cs_psv_sva_sva_employment = cls(
            pbv_activity_type=pbv_activity_type,
            pbv_art=pbv_art,
            pbv_befr=pbv_befr,
            pbv_bis=pbv_bis,
            pbv_id=pbv_id,
            pbv_nr=pbv_nr,
            pbv_qualifizierungsverfahren=pbv_qualifizierungsverfahren,
            pbv_type=pbv_type,
            pbv_von=pbv_von,
            pgd_familyname=pgd_familyname,
            pgd_firstname=pgd_firstname,
            pgd_gender=pgd_gender,
            pgd_id=pgd_id,
        )

        cs_psv_sva_sva_employment.additional_properties = d
        return cs_psv_sva_sva_employment

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
