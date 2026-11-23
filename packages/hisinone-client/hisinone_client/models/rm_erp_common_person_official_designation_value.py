from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_person_official_designation_value_foreigntext import (
        RmErpCommonPersonOfficialDesignationValueForeigntext,
    )


T = TypeVar("T", bound="RmErpCommonPersonOfficialDesignationValue")


@_attrs_define
class RmErpCommonPersonOfficialDesignationValue:
    """
    Attributes:
        field_foreigntext (RmErpCommonPersonOfficialDesignationValueForeigntext | Unset):
        committee_election (bool | Unset):
        country_designation (str | Unset):
        defaulttext (str | Unset):
        federal_designation (str | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: RmErpCommonPersonOfficialDesignationValueForeigntext | Unset = UNSET
    committee_election: bool | Unset = UNSET
    country_designation: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    federal_designation: str | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        committee_election = self.committee_election

        country_designation = self.country_designation

        defaulttext = self.defaulttext

        federal_designation = self.federal_designation

        hiskey_id = self.hiskey_id

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if committee_election is not UNSET:
            field_dict["committeeElection"] = committee_election
        if country_designation is not UNSET:
            field_dict["countryDesignation"] = country_designation
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if federal_designation is not UNSET:
            field_dict["federalDesignation"] = federal_designation
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_person_official_designation_value_foreigntext import (
            RmErpCommonPersonOfficialDesignationValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonPersonOfficialDesignationValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonPersonOfficialDesignationValueForeigntext.from_dict(_field_foreigntext)

        committee_election = d.pop("committeeElection", UNSET)

        country_designation = d.pop("countryDesignation", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        federal_designation = d.pop("federalDesignation", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        rm_erp_common_person_official_designation_value = cls(
            field_foreigntext=field_foreigntext,
            committee_election=committee_election,
            country_designation=country_designation,
            defaulttext=defaulttext,
            federal_designation=federal_designation,
            hiskey_id=hiskey_id,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        rm_erp_common_person_official_designation_value.additional_properties = d
        return rm_erp_common_person_official_designation_value

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
