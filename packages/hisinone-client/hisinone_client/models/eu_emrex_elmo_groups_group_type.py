from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_groups_group_type_group import EuEmrexElmoGroupsGroupTypeGroup
    from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang


T = TypeVar("T", bound="EuEmrexElmoGroupsGroupType")


@_attrs_define
class EuEmrexElmoGroupsGroupType:
    """
    Attributes:
        group (list[EuEmrexElmoGroupsGroupTypeGroup] | Unset):
        id (str | Unset):
        title (EuEmrexElmoTokenWithOptionalLang | Unset):
    """

    group: list[EuEmrexElmoGroupsGroupTypeGroup] | Unset = UNSET
    id: str | Unset = UNSET
    title: EuEmrexElmoTokenWithOptionalLang | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        group: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = []
            for group_item_data in self.group:
                group_item = group_item_data.to_dict()
                group.append(group_item)

        id = self.id

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_groups_group_type_group import EuEmrexElmoGroupsGroupTypeGroup  # noqa: PLC0415
        from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang  # noqa: PLC0415

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: list[EuEmrexElmoGroupsGroupTypeGroup] | Unset = UNSET
        if _group is not UNSET:
            group = []
            for group_item_data in _group:
                group_item = EuEmrexElmoGroupsGroupTypeGroup.from_dict(group_item_data)

                group.append(group_item)

        id = d.pop("id", UNSET)

        _title = d.pop("title", UNSET)
        title: EuEmrexElmoTokenWithOptionalLang | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = EuEmrexElmoTokenWithOptionalLang.from_dict(_title)

        eu_emrex_elmo_groups_group_type = cls(
            group=group,
            id=id,
            title=title,
        )

        eu_emrex_elmo_groups_group_type.additional_properties = d
        return eu_emrex_elmo_groups_group_type

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
