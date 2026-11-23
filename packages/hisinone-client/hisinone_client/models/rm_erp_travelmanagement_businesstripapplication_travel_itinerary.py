from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_travelmanagement_businesstripapplication_travel_itinerary_foreigntext import (
        RmErpTravelmanagementBusinesstripapplicationTravelItineraryForeigntext,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_arrival_value import RmErpTravelmanagementSharedErpArrivalValue
    from ..models.rm_erp_travelmanagement_shared_erp_return_trip_value import (
        RmErpTravelmanagementSharedErpReturnTripValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_transportation_value import (
        RmErpTravelmanagementSharedErpTransportationValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_travel_zone_value import (
        RmErpTravelmanagementSharedErpTravelZoneValue,
    )


T = TypeVar("T", bound="RmErpTravelmanagementBusinesstripapplicationTravelItinerary")


@_attrs_define
class RmErpTravelmanagementBusinesstripapplicationTravelItinerary:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementBusinesstripapplicationTravelItineraryForeigntext | Unset):
        arrival_selected (RmErpTravelmanagementSharedErpArrivalValue | Unset):
        compensation_amount (float | Unset):
        destination (str | Unset):
        distance (int | Unset):
        emissions (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        origin (str | Unset):
        reason (str | Unset):
        return_trip_selected (RmErpTravelmanagementSharedErpReturnTripValue | Unset):
        transportation_selected (RmErpTravelmanagementSharedErpTransportationValue | Unset):
        travel_zone_selected (RmErpTravelmanagementSharedErpTravelZoneValue | Unset):
        trip_begin_date (int | Unset):
        trip_end_date (int | Unset):
    """

    field_foreigntext: RmErpTravelmanagementBusinesstripapplicationTravelItineraryForeigntext | Unset = UNSET
    arrival_selected: RmErpTravelmanagementSharedErpArrivalValue | Unset = UNSET
    compensation_amount: float | Unset = UNSET
    destination: str | Unset = UNSET
    distance: int | Unset = UNSET
    emissions: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    origin: str | Unset = UNSET
    reason: str | Unset = UNSET
    return_trip_selected: RmErpTravelmanagementSharedErpReturnTripValue | Unset = UNSET
    transportation_selected: RmErpTravelmanagementSharedErpTransportationValue | Unset = UNSET
    travel_zone_selected: RmErpTravelmanagementSharedErpTravelZoneValue | Unset = UNSET
    trip_begin_date: int | Unset = UNSET
    trip_end_date: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        arrival_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arrival_selected, Unset):
            arrival_selected = self.arrival_selected.to_dict()

        compensation_amount = self.compensation_amount

        destination = self.destination

        distance = self.distance

        emissions = self.emissions

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        origin = self.origin

        reason = self.reason

        return_trip_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_trip_selected, Unset):
            return_trip_selected = self.return_trip_selected.to_dict()

        transportation_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_selected, Unset):
            transportation_selected = self.transportation_selected.to_dict()

        travel_zone_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.travel_zone_selected, Unset):
            travel_zone_selected = self.travel_zone_selected.to_dict()

        trip_begin_date = self.trip_begin_date

        trip_end_date = self.trip_end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if arrival_selected is not UNSET:
            field_dict["arrivalSelected"] = arrival_selected
        if compensation_amount is not UNSET:
            field_dict["compensationAmount"] = compensation_amount
        if destination is not UNSET:
            field_dict["destination"] = destination
        if distance is not UNSET:
            field_dict["distance"] = distance
        if emissions is not UNSET:
            field_dict["emissions"] = emissions
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if origin is not UNSET:
            field_dict["origin"] = origin
        if reason is not UNSET:
            field_dict["reason"] = reason
        if return_trip_selected is not UNSET:
            field_dict["returnTripSelected"] = return_trip_selected
        if transportation_selected is not UNSET:
            field_dict["transportationSelected"] = transportation_selected
        if travel_zone_selected is not UNSET:
            field_dict["travelZoneSelected"] = travel_zone_selected
        if trip_begin_date is not UNSET:
            field_dict["tripBeginDate"] = trip_begin_date
        if trip_end_date is not UNSET:
            field_dict["tripEndDate"] = trip_end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_travelmanagement_businesstripapplication_travel_itinerary_foreigntext import (
            RmErpTravelmanagementBusinesstripapplicationTravelItineraryForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_arrival_value import RmErpTravelmanagementSharedErpArrivalValue  # noqa: PLC0415
        from ..models.rm_erp_travelmanagement_shared_erp_return_trip_value import (
            RmErpTravelmanagementSharedErpReturnTripValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_transportation_value import (
            RmErpTravelmanagementSharedErpTransportationValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_travel_zone_value import (
            RmErpTravelmanagementSharedErpTravelZoneValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTravelmanagementBusinesstripapplicationTravelItineraryForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpTravelmanagementBusinesstripapplicationTravelItineraryForeigntext.from_dict(
                _field_foreigntext
            )

        _arrival_selected = d.pop("arrivalSelected", UNSET)
        arrival_selected: RmErpTravelmanagementSharedErpArrivalValue | Unset
        if isinstance(_arrival_selected, Unset):
            arrival_selected = UNSET
        else:
            arrival_selected = RmErpTravelmanagementSharedErpArrivalValue.from_dict(_arrival_selected)

        compensation_amount = d.pop("compensationAmount", UNSET)

        destination = d.pop("destination", UNSET)

        distance = d.pop("distance", UNSET)

        emissions = d.pop("emissions", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        origin = d.pop("origin", UNSET)

        reason = d.pop("reason", UNSET)

        _return_trip_selected = d.pop("returnTripSelected", UNSET)
        return_trip_selected: RmErpTravelmanagementSharedErpReturnTripValue | Unset
        if isinstance(_return_trip_selected, Unset):
            return_trip_selected = UNSET
        else:
            return_trip_selected = RmErpTravelmanagementSharedErpReturnTripValue.from_dict(_return_trip_selected)

        _transportation_selected = d.pop("transportationSelected", UNSET)
        transportation_selected: RmErpTravelmanagementSharedErpTransportationValue | Unset
        if isinstance(_transportation_selected, Unset):
            transportation_selected = UNSET
        else:
            transportation_selected = RmErpTravelmanagementSharedErpTransportationValue.from_dict(
                _transportation_selected
            )

        _travel_zone_selected = d.pop("travelZoneSelected", UNSET)
        travel_zone_selected: RmErpTravelmanagementSharedErpTravelZoneValue | Unset
        if isinstance(_travel_zone_selected, Unset):
            travel_zone_selected = UNSET
        else:
            travel_zone_selected = RmErpTravelmanagementSharedErpTravelZoneValue.from_dict(_travel_zone_selected)

        trip_begin_date = d.pop("tripBeginDate", UNSET)

        trip_end_date = d.pop("tripEndDate", UNSET)

        rm_erp_travelmanagement_businesstripapplication_travel_itinerary = cls(
            field_foreigntext=field_foreigntext,
            arrival_selected=arrival_selected,
            compensation_amount=compensation_amount,
            destination=destination,
            distance=distance,
            emissions=emissions,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            origin=origin,
            reason=reason,
            return_trip_selected=return_trip_selected,
            transportation_selected=transportation_selected,
            travel_zone_selected=travel_zone_selected,
            trip_begin_date=trip_begin_date,
            trip_end_date=trip_end_date,
        )

        rm_erp_travelmanagement_businesstripapplication_travel_itinerary.additional_properties = d
        return rm_erp_travelmanagement_businesstripapplication_travel_itinerary

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
