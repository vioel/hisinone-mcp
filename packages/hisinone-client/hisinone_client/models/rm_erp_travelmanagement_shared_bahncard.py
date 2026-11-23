from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_travelmanagement_shared_bahncard_foreigntext import (
        RmErpTravelmanagementSharedBahncardForeigntext,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_bahncard_value import RmErpTravelmanagementSharedErpBahncardValue


T = TypeVar("T", bound="RmErpTravelmanagementSharedBahncard")


@_attrs_define
class RmErpTravelmanagementSharedBahncard:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementSharedBahncardForeigntext | Unset):
        bahncard_selected (RmErpTravelmanagementSharedErpBahncardValue | Unset):
        change_bahncard (RmErpCommonErpGenericValue | Unset):
        change_from_date (int | Unset):
        change_text (str | Unset):
        change_to_date (int | Unset):
        defaulttext (str | Unset):
        discount_first_bc (int | Unset):
        discount_second_bc (int | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        pgd_join_id (int | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_from_date_first_bc (int | Unset):
        valid_from_date_second_bc (int | Unset):
        valid_to (int | Unset):
        valid_to_date_first_bc (int | Unset):
        valid_to_date_second_bc (int | Unset):
    """

    field_foreigntext: RmErpTravelmanagementSharedBahncardForeigntext | Unset = UNSET
    bahncard_selected: RmErpTravelmanagementSharedErpBahncardValue | Unset = UNSET
    change_bahncard: RmErpCommonErpGenericValue | Unset = UNSET
    change_from_date: int | Unset = UNSET
    change_text: str | Unset = UNSET
    change_to_date: int | Unset = UNSET
    defaulttext: str | Unset = UNSET
    discount_first_bc: int | Unset = UNSET
    discount_second_bc: int | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    pgd_join_id: int | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_from_date_first_bc: int | Unset = UNSET
    valid_from_date_second_bc: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    valid_to_date_first_bc: int | Unset = UNSET
    valid_to_date_second_bc: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        bahncard_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bahncard_selected, Unset):
            bahncard_selected = self.bahncard_selected.to_dict()

        change_bahncard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_bahncard, Unset):
            change_bahncard = self.change_bahncard.to_dict()

        change_from_date = self.change_from_date

        change_text = self.change_text

        change_to_date = self.change_to_date

        defaulttext = self.defaulttext

        discount_first_bc = self.discount_first_bc

        discount_second_bc = self.discount_second_bc

        hiskey_id = self.hiskey_id

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        pgd_join_id = self.pgd_join_id

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_from_date_first_bc = self.valid_from_date_first_bc

        valid_from_date_second_bc = self.valid_from_date_second_bc

        valid_to = self.valid_to

        valid_to_date_first_bc = self.valid_to_date_first_bc

        valid_to_date_second_bc = self.valid_to_date_second_bc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if bahncard_selected is not UNSET:
            field_dict["bahncardSelected"] = bahncard_selected
        if change_bahncard is not UNSET:
            field_dict["changeBahncard"] = change_bahncard
        if change_from_date is not UNSET:
            field_dict["changeFromDate"] = change_from_date
        if change_text is not UNSET:
            field_dict["changeText"] = change_text
        if change_to_date is not UNSET:
            field_dict["changeToDate"] = change_to_date
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if discount_first_bc is not UNSET:
            field_dict["discountFirstBc"] = discount_first_bc
        if discount_second_bc is not UNSET:
            field_dict["discountSecondBc"] = discount_second_bc
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
        if pgd_join_id is not UNSET:
            field_dict["pgdJoinId"] = pgd_join_id
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
        if valid_from_date_first_bc is not UNSET:
            field_dict["validFromDateFirstBc"] = valid_from_date_first_bc
        if valid_from_date_second_bc is not UNSET:
            field_dict["validFromDateSecondBc"] = valid_from_date_second_bc
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if valid_to_date_first_bc is not UNSET:
            field_dict["validToDateFirstBc"] = valid_to_date_first_bc
        if valid_to_date_second_bc is not UNSET:
            field_dict["validToDateSecondBc"] = valid_to_date_second_bc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_travelmanagement_shared_bahncard_foreigntext import (
            RmErpTravelmanagementSharedBahncardForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_bahncard_value import (
            RmErpTravelmanagementSharedErpBahncardValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTravelmanagementSharedBahncardForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpTravelmanagementSharedBahncardForeigntext.from_dict(_field_foreigntext)

        _bahncard_selected = d.pop("bahncardSelected", UNSET)
        bahncard_selected: RmErpTravelmanagementSharedErpBahncardValue | Unset
        if isinstance(_bahncard_selected, Unset):
            bahncard_selected = UNSET
        else:
            bahncard_selected = RmErpTravelmanagementSharedErpBahncardValue.from_dict(_bahncard_selected)

        _change_bahncard = d.pop("changeBahncard", UNSET)
        change_bahncard: RmErpCommonErpGenericValue | Unset
        if isinstance(_change_bahncard, Unset):
            change_bahncard = UNSET
        else:
            change_bahncard = RmErpCommonErpGenericValue.from_dict(_change_bahncard)

        change_from_date = d.pop("changeFromDate", UNSET)

        change_text = d.pop("changeText", UNSET)

        change_to_date = d.pop("changeToDate", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        discount_first_bc = d.pop("discountFirstBc", UNSET)

        discount_second_bc = d.pop("discountSecondBc", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        pgd_join_id = d.pop("pgdJoinId", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_from_date_first_bc = d.pop("validFromDateFirstBc", UNSET)

        valid_from_date_second_bc = d.pop("validFromDateSecondBc", UNSET)

        valid_to = d.pop("validTo", UNSET)

        valid_to_date_first_bc = d.pop("validToDateFirstBc", UNSET)

        valid_to_date_second_bc = d.pop("validToDateSecondBc", UNSET)

        rm_erp_travelmanagement_shared_bahncard = cls(
            field_foreigntext=field_foreigntext,
            bahncard_selected=bahncard_selected,
            change_bahncard=change_bahncard,
            change_from_date=change_from_date,
            change_text=change_text,
            change_to_date=change_to_date,
            defaulttext=defaulttext,
            discount_first_bc=discount_first_bc,
            discount_second_bc=discount_second_bc,
            hiskey_id=hiskey_id,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            pgd_join_id=pgd_join_id,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_from_date_first_bc=valid_from_date_first_bc,
            valid_from_date_second_bc=valid_from_date_second_bc,
            valid_to=valid_to,
            valid_to_date_first_bc=valid_to_date_first_bc,
            valid_to_date_second_bc=valid_to_date_second_bc,
        )

        rm_erp_travelmanagement_shared_bahncard.additional_properties = d
        return rm_erp_travelmanagement_shared_bahncard

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
