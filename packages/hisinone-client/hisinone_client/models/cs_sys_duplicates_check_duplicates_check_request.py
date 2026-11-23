from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_duplicates_check_duplicates_check_request_entity_attributes import (
        CsSysDuplicatesCheckDuplicatesCheckRequestEntityAttributes,
    )


T = TypeVar("T", bound="CsSysDuplicatesCheckDuplicatesCheckRequest")


@_attrs_define
class CsSysDuplicatesCheckDuplicatesCheckRequest:
    """
    Attributes:
        entity_attributes (CsSysDuplicatesCheckDuplicatesCheckRequestEntityAttributes | Unset):
        entity_config_uniquename (str | Unset):
    """

    entity_attributes: CsSysDuplicatesCheckDuplicatesCheckRequestEntityAttributes | Unset = UNSET
    entity_config_uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        entity_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_attributes, Unset):
            entity_attributes = self.entity_attributes.to_dict()

        entity_config_uniquename = self.entity_config_uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_attributes is not UNSET:
            field_dict["entityAttributes"] = entity_attributes
        if entity_config_uniquename is not UNSET:
            field_dict["entityConfigUniquename"] = entity_config_uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_duplicates_check_duplicates_check_request_entity_attributes import (
            CsSysDuplicatesCheckDuplicatesCheckRequestEntityAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _entity_attributes = d.pop("entityAttributes", UNSET)
        entity_attributes: CsSysDuplicatesCheckDuplicatesCheckRequestEntityAttributes | Unset
        if isinstance(_entity_attributes, Unset):
            entity_attributes = UNSET
        else:
            entity_attributes = CsSysDuplicatesCheckDuplicatesCheckRequestEntityAttributes.from_dict(_entity_attributes)

        entity_config_uniquename = d.pop("entityConfigUniquename", UNSET)

        cs_sys_duplicates_check_duplicates_check_request = cls(
            entity_attributes=entity_attributes,
            entity_config_uniquename=entity_config_uniquename,
        )

        cs_sys_duplicates_check_duplicates_check_request.additional_properties = d
        return cs_sys_duplicates_check_duplicates_check_request

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
