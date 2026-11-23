from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opus_identifier import OpusIdentifier


T = TypeVar("T", bound="OpusAuthor")


@_attrs_define
class OpusAuthor:
    """
    Attributes:
        first_name (str | Unset):
        identifiers (list[OpusIdentifier] | Unset):
        last_name (str | Unset):
        person_role_type (str | Unset):
    """

    first_name: str | Unset = UNSET
    identifiers: list[OpusIdentifier] | Unset = UNSET
    last_name: str | Unset = UNSET
    person_role_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        last_name = self.last_name

        person_role_type = self.person_role_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if person_role_type is not UNSET:
            field_dict["personRoleType"] = person_role_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opus_identifier import OpusIdentifier  # noqa: PLC0415

        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: list[OpusIdentifier] | Unset = UNSET
        if _identifiers is not UNSET:
            identifiers = []
            for identifiers_item_data in _identifiers:
                identifiers_item = OpusIdentifier.from_dict(identifiers_item_data)

                identifiers.append(identifiers_item)

        last_name = d.pop("lastName", UNSET)

        person_role_type = d.pop("personRoleType", UNSET)

        opus_author = cls(
            first_name=first_name,
            identifiers=identifiers,
            last_name=last_name,
            person_role_type=person_role_type,
        )

        opus_author.additional_properties = d
        return opus_author

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
