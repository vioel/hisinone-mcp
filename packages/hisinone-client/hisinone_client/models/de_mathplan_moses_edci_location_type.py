from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_address_type import DeMathplanMosesEdciAddressType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_location_type_spatial_code import DeMathplanMosesEdciLocationTypeSpatialCode
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType


T = TypeVar("T", bound="DeMathplanMosesEdciLocationType")


@_attrs_define
class DeMathplanMosesEdciLocationType:
    """
    Attributes:
        description (list[DeMathplanMosesEdciNoteType] | Unset):
        has_address (list[DeMathplanMosesEdciAddressType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        name (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        spatial_code (list[DeMathplanMosesEdciLocationTypeSpatialCode] | Unset):
    """

    description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    has_address: list[DeMathplanMosesEdciAddressType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    name: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    spatial_code: list[DeMathplanMosesEdciLocationTypeSpatialCode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        has_address: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.has_address, Unset):
            has_address = []
            for has_address_item_data in self.has_address:
                has_address_item = has_address_item_data.to_dict()
                has_address.append(has_address_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = []
            for name_item_data in self.name:
                name_item = name_item_data.to_dict()
                name.append(name_item)

        spatial_code: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.spatial_code, Unset):
            spatial_code = []
            for spatial_code_item_data in self.spatial_code:
                spatial_code_item = spatial_code_item_data.to_dict()
                spatial_code.append(spatial_code_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if has_address is not UNSET:
            field_dict["hasAddress"] = has_address
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if spatial_code is not UNSET:
            field_dict["spatialCode"] = spatial_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_address_type import DeMathplanMosesEdciAddressType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_location_type_spatial_code import (
            DeMathplanMosesEdciLocationTypeSpatialCode,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415

        d = dict(src_dict)
        _description = d.pop("description", UNSET)
        description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = DeMathplanMosesEdciNoteType.from_dict(description_item_data)

                description.append(description_item)

        _has_address = d.pop("hasAddress", UNSET)
        has_address: list[DeMathplanMosesEdciAddressType] | Unset = UNSET
        if _has_address is not UNSET:
            has_address = []
            for has_address_item_data in _has_address:
                has_address_item = DeMathplanMosesEdciAddressType.from_dict(has_address_item_data)

                has_address.append(has_address_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _name = d.pop("name", UNSET)
        name: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _name is not UNSET:
            name = []
            for name_item_data in _name:
                name_item = DeMathplanMosesEdciLanguageStringType.from_dict(name_item_data)

                name.append(name_item)

        _spatial_code = d.pop("spatialCode", UNSET)
        spatial_code: list[DeMathplanMosesEdciLocationTypeSpatialCode] | Unset = UNSET
        if _spatial_code is not UNSET:
            spatial_code = []
            for spatial_code_item_data in _spatial_code:
                spatial_code_item = DeMathplanMosesEdciLocationTypeSpatialCode.from_dict(spatial_code_item_data)

                spatial_code.append(spatial_code_item)

        de_mathplan_moses_edci_location_type = cls(
            description=description,
            has_address=has_address,
            id=id,
            identifier=identifier,
            name=name,
            spatial_code=spatial_code,
        )

        de_mathplan_moses_edci_location_type.additional_properties = d
        return de_mathplan_moses_edci_location_type

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
