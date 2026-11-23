from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_groups_group_type import EuEmrexElmoGroupsGroupType


T = TypeVar("T", bound="EuEmrexElmoGroups")


@_attrs_define
class EuEmrexElmoGroups:
    """
    Attributes:
        group_type (list[EuEmrexElmoGroupsGroupType] | Unset):
    """

    group_type: list[EuEmrexElmoGroupsGroupType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        group_type: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_type, Unset):
            group_type = []
            for group_type_item_data in self.group_type:
                group_type_item = group_type_item_data.to_dict()
                group_type.append(group_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_type is not UNSET:
            field_dict["groupType"] = group_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_groups_group_type import EuEmrexElmoGroupsGroupType  # noqa: PLC0415

        d = dict(src_dict)
        _group_type = d.pop("groupType", UNSET)
        group_type: list[EuEmrexElmoGroupsGroupType] | Unset = UNSET
        if _group_type is not UNSET:
            group_type = []
            for group_type_item_data in _group_type:
                group_type_item = EuEmrexElmoGroupsGroupType.from_dict(group_type_item_data)

                group_type.append(group_type_item)

        eu_emrex_elmo_groups = cls(
            group_type=group_type,
        )

        eu_emrex_elmo_groups.additional_properties = d
        return eu_emrex_elmo_groups

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
