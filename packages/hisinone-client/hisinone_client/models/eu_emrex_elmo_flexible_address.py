from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="EuEmrexElmoFlexibleAddress")


@_attrs_define
class EuEmrexElmoFlexibleAddress:
    """
    Attributes:
        address_line (list[str] | Unset):
        building_name (str | Unset):
        building_number (str | Unset):
        country (str | Unset):
        delivery_point_code (list[JavaLangObject] | Unset):
        floor (str | Unset):
        locality (str | Unset):
        post_office_box (str | Unset):
        postal_code (str | Unset):
        recipient_name (list[str] | Unset):
        region (str | Unset):
        street_name (str | Unset):
        unit (str | Unset):
    """

    address_line: list[str] | Unset = UNSET
    building_name: str | Unset = UNSET
    building_number: str | Unset = UNSET
    country: str | Unset = UNSET
    delivery_point_code: list[JavaLangObject] | Unset = UNSET
    floor: str | Unset = UNSET
    locality: str | Unset = UNSET
    post_office_box: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    recipient_name: list[str] | Unset = UNSET
    region: str | Unset = UNSET
    street_name: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        address_line: list[str] | Unset = UNSET
        if not isinstance(self.address_line, Unset):
            address_line = self.address_line

        building_name = self.building_name

        building_number = self.building_number

        country = self.country

        delivery_point_code: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.delivery_point_code, Unset):
            delivery_point_code = []
            for delivery_point_code_item_data in self.delivery_point_code:
                delivery_point_code_item = delivery_point_code_item_data.to_dict()
                delivery_point_code.append(delivery_point_code_item)

        floor = self.floor

        locality = self.locality

        post_office_box = self.post_office_box

        postal_code = self.postal_code

        recipient_name: list[str] | Unset = UNSET
        if not isinstance(self.recipient_name, Unset):
            recipient_name = self.recipient_name

        region = self.region

        street_name = self.street_name

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line is not UNSET:
            field_dict["addressLine"] = address_line
        if building_name is not UNSET:
            field_dict["buildingName"] = building_name
        if building_number is not UNSET:
            field_dict["buildingNumber"] = building_number
        if country is not UNSET:
            field_dict["country"] = country
        if delivery_point_code is not UNSET:
            field_dict["deliveryPointCode"] = delivery_point_code
        if floor is not UNSET:
            field_dict["floor"] = floor
        if locality is not UNSET:
            field_dict["locality"] = locality
        if post_office_box is not UNSET:
            field_dict["postOfficeBox"] = post_office_box
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if recipient_name is not UNSET:
            field_dict["recipientName"] = recipient_name
        if region is not UNSET:
            field_dict["region"] = region
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        address_line = cast(list[str], d.pop("addressLine", UNSET))

        building_name = d.pop("buildingName", UNSET)

        building_number = d.pop("buildingNumber", UNSET)

        country = d.pop("country", UNSET)

        _delivery_point_code = d.pop("deliveryPointCode", UNSET)
        delivery_point_code: list[JavaLangObject] | Unset = UNSET
        if _delivery_point_code is not UNSET:
            delivery_point_code = []
            for delivery_point_code_item_data in _delivery_point_code:
                delivery_point_code_item = JavaLangObject.from_dict(delivery_point_code_item_data)

                delivery_point_code.append(delivery_point_code_item)

        floor = d.pop("floor", UNSET)

        locality = d.pop("locality", UNSET)

        post_office_box = d.pop("postOfficeBox", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        recipient_name = cast(list[str], d.pop("recipientName", UNSET))

        region = d.pop("region", UNSET)

        street_name = d.pop("streetName", UNSET)

        unit = d.pop("unit", UNSET)

        eu_emrex_elmo_flexible_address = cls(
            address_line=address_line,
            building_name=building_name,
            building_number=building_number,
            country=country,
            delivery_point_code=delivery_point_code,
            floor=floor,
            locality=locality,
            post_office_box=post_office_box,
            postal_code=postal_code,
            recipient_name=recipient_name,
            region=region,
            street_name=street_name,
            unit=unit,
        )

        eu_emrex_elmo_flexible_address.additional_properties = d
        return eu_emrex_elmo_flexible_address

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
