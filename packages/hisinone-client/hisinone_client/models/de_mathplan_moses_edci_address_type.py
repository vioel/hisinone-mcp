from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_address_type_country import DeMathplanMosesEdciAddressTypeCountry
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType


T = TypeVar("T", bound="DeMathplanMosesEdciAddressType")


@_attrs_define
class DeMathplanMosesEdciAddressType:
    """
    Attributes:
        country (DeMathplanMosesEdciAddressTypeCountry | Unset):
        full_address (list[DeMathplanMosesEdciNoteType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
    """

    country: DeMathplanMosesEdciAddressTypeCountry | Unset = UNSET
    full_address: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        full_address: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.full_address, Unset):
            full_address = []
            for full_address_item_data in self.full_address:
                full_address_item = full_address_item_data.to_dict()
                full_address.append(full_address_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if full_address is not UNSET:
            field_dict["fullAddress"] = full_address
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_address_type_country import DeMathplanMosesEdciAddressTypeCountry  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415

        d = dict(src_dict)
        _country = d.pop("country", UNSET)
        country: DeMathplanMosesEdciAddressTypeCountry | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = DeMathplanMosesEdciAddressTypeCountry.from_dict(_country)

        _full_address = d.pop("fullAddress", UNSET)
        full_address: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _full_address is not UNSET:
            full_address = []
            for full_address_item_data in _full_address:
                full_address_item = DeMathplanMosesEdciNoteType.from_dict(full_address_item_data)

                full_address.append(full_address_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        de_mathplan_moses_edci_address_type = cls(
            country=country,
            full_address=full_address,
            id=id,
            identifier=identifier,
        )

        de_mathplan_moses_edci_address_type.additional_properties = d
        return de_mathplan_moses_edci_address_type

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
