from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationRecordUpdateRest")


@_attrs_define
class ConversationRecordUpdateRest:
    """
    Attributes:
        domain_ids (list[int] | Unset):
        id (int | Unset):
        text (str | Unset):
        title (str | Unset):
    """

    domain_ids: list[int] | Unset = UNSET
    id: int | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        domain_ids: list[int] | Unset = UNSET
        if not isinstance(self.domain_ids, Unset):
            domain_ids = self.domain_ids

        id = self.id

        text = self.text

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_ids is not UNSET:
            field_dict["domainIds"] = domain_ids
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_ids = cast(list[int], d.pop("domainIds", UNSET))

        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        conversation_record_update_rest = cls(
            domain_ids=domain_ids,
            id=id,
            text=text,
            title=title,
        )

        conversation_record_update_rest.additional_properties = d
        return conversation_record_update_rest

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
