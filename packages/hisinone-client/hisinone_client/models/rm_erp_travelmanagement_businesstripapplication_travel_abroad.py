from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_travelmanagement_businesstripapplication_travel_abroad_foreigntext import (
        RmErpTravelmanagementBusinesstripapplicationTravelAbroadForeigntext,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_foreign_country_value import (
        RmErpTravelmanagementSharedErpForeignCountryValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_transportation_value import (
        RmErpTravelmanagementSharedErpTransportationValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_travel_day_value import (
        RmErpTravelmanagementSharedErpTravelDayValue,
    )


T = TypeVar("T", bound="RmErpTravelmanagementBusinesstripapplicationTravelAbroad")


@_attrs_define
class RmErpTravelmanagementBusinesstripapplicationTravelAbroad:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementBusinesstripapplicationTravelAbroadForeigntext | Unset):
        destination_from (str | Unset):
        destination_to (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        note (str | Unset):
        obj_guid (str | Unset):
        transportation_selected (RmErpTravelmanagementSharedErpTransportationValue | Unset):
        travel_day_selected (RmErpTravelmanagementSharedErpTravelDayValue | Unset):
        travel_itinerary_from_selected (RmErpTravelmanagementSharedErpForeignCountryValue | Unset):
        travel_itinerary_to_selected (RmErpTravelmanagementSharedErpForeignCountryValue | Unset):
        trip_begin_date (int | Unset):
        trip_end_date (int | Unset):
    """

    field_foreigntext: RmErpTravelmanagementBusinesstripapplicationTravelAbroadForeigntext | Unset = UNSET
    destination_from: str | Unset = UNSET
    destination_to: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    note: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    transportation_selected: RmErpTravelmanagementSharedErpTransportationValue | Unset = UNSET
    travel_day_selected: RmErpTravelmanagementSharedErpTravelDayValue | Unset = UNSET
    travel_itinerary_from_selected: RmErpTravelmanagementSharedErpForeignCountryValue | Unset = UNSET
    travel_itinerary_to_selected: RmErpTravelmanagementSharedErpForeignCountryValue | Unset = UNSET
    trip_begin_date: int | Unset = UNSET
    trip_end_date: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        destination_from = self.destination_from

        destination_to = self.destination_to

        id = self.id

        lock_version = self.lock_version

        note = self.note

        obj_guid = self.obj_guid

        transportation_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_selected, Unset):
            transportation_selected = self.transportation_selected.to_dict()

        travel_day_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.travel_day_selected, Unset):
            travel_day_selected = self.travel_day_selected.to_dict()

        travel_itinerary_from_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.travel_itinerary_from_selected, Unset):
            travel_itinerary_from_selected = self.travel_itinerary_from_selected.to_dict()

        travel_itinerary_to_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.travel_itinerary_to_selected, Unset):
            travel_itinerary_to_selected = self.travel_itinerary_to_selected.to_dict()

        trip_begin_date = self.trip_begin_date

        trip_end_date = self.trip_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if destination_from is not UNSET:
            field_dict["destinationFrom"] = destination_from
        if destination_to is not UNSET:
            field_dict["destinationTo"] = destination_to
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if note is not UNSET:
            field_dict["note"] = note
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if transportation_selected is not UNSET:
            field_dict["transportationSelected"] = transportation_selected
        if travel_day_selected is not UNSET:
            field_dict["travelDaySelected"] = travel_day_selected
        if travel_itinerary_from_selected is not UNSET:
            field_dict["travelItineraryFromSelected"] = travel_itinerary_from_selected
        if travel_itinerary_to_selected is not UNSET:
            field_dict["travelItineraryToSelected"] = travel_itinerary_to_selected
        if trip_begin_date is not UNSET:
            field_dict["tripBeginDate"] = trip_begin_date
        if trip_end_date is not UNSET:
            field_dict["tripEndDate"] = trip_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_travelmanagement_businesstripapplication_travel_abroad_foreigntext import (
            RmErpTravelmanagementBusinesstripapplicationTravelAbroadForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_foreign_country_value import (
            RmErpTravelmanagementSharedErpForeignCountryValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_transportation_value import (
            RmErpTravelmanagementSharedErpTransportationValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_travel_day_value import (
            RmErpTravelmanagementSharedErpTravelDayValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTravelmanagementBusinesstripapplicationTravelAbroadForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpTravelmanagementBusinesstripapplicationTravelAbroadForeigntext.from_dict(
                _field_foreigntext
            )

        destination_from = d.pop("destinationFrom", UNSET)

        destination_to = d.pop("destinationTo", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        note = d.pop("note", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _transportation_selected = d.pop("transportationSelected", UNSET)
        transportation_selected: RmErpTravelmanagementSharedErpTransportationValue | Unset
        if isinstance(_transportation_selected, Unset):
            transportation_selected = UNSET
        else:
            transportation_selected = RmErpTravelmanagementSharedErpTransportationValue.from_dict(
                _transportation_selected
            )

        _travel_day_selected = d.pop("travelDaySelected", UNSET)
        travel_day_selected: RmErpTravelmanagementSharedErpTravelDayValue | Unset
        if isinstance(_travel_day_selected, Unset):
            travel_day_selected = UNSET
        else:
            travel_day_selected = RmErpTravelmanagementSharedErpTravelDayValue.from_dict(_travel_day_selected)

        _travel_itinerary_from_selected = d.pop("travelItineraryFromSelected", UNSET)
        travel_itinerary_from_selected: RmErpTravelmanagementSharedErpForeignCountryValue | Unset
        if isinstance(_travel_itinerary_from_selected, Unset):
            travel_itinerary_from_selected = UNSET
        else:
            travel_itinerary_from_selected = RmErpTravelmanagementSharedErpForeignCountryValue.from_dict(
                _travel_itinerary_from_selected
            )

        _travel_itinerary_to_selected = d.pop("travelItineraryToSelected", UNSET)
        travel_itinerary_to_selected: RmErpTravelmanagementSharedErpForeignCountryValue | Unset
        if isinstance(_travel_itinerary_to_selected, Unset):
            travel_itinerary_to_selected = UNSET
        else:
            travel_itinerary_to_selected = RmErpTravelmanagementSharedErpForeignCountryValue.from_dict(
                _travel_itinerary_to_selected
            )

        trip_begin_date = d.pop("tripBeginDate", UNSET)

        trip_end_date = d.pop("tripEndDate", UNSET)

        rm_erp_travelmanagement_businesstripapplication_travel_abroad = cls(
            field_foreigntext=field_foreigntext,
            destination_from=destination_from,
            destination_to=destination_to,
            id=id,
            lock_version=lock_version,
            note=note,
            obj_guid=obj_guid,
            transportation_selected=transportation_selected,
            travel_day_selected=travel_day_selected,
            travel_itinerary_from_selected=travel_itinerary_from_selected,
            travel_itinerary_to_selected=travel_itinerary_to_selected,
            trip_begin_date=trip_begin_date,
            trip_end_date=trip_end_date,
        )

        rm_erp_travelmanagement_businesstripapplication_travel_abroad.additional_properties = d
        return rm_erp_travelmanagement_businesstripapplication_travel_abroad

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
