from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeHisCoreDatatypeHisResource")


@_attrs_define
class DeHisCoreDatatypeHisResource:
    """
    Attributes:
        content (list[int] | Unset):
        content_type (str | Unset):
        document_metadata_category_id (int | Unset):
        name (str | Unset):
    """

    content: list[int] | Unset = UNSET
    content_type: str | Unset = UNSET
    document_metadata_category_id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        content: list[int] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content

        content_type = self.content_type

        document_metadata_category_id = self.document_metadata_category_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if document_metadata_category_id is not UNSET:
            field_dict["documentMetadataCategoryId"] = document_metadata_category_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = cast(list[int], d.pop("content", UNSET))

        content_type = d.pop("contentType", UNSET)

        document_metadata_category_id = d.pop("documentMetadataCategoryId", UNSET)

        name = d.pop("name", UNSET)

        de_his_core_datatype_his_resource = cls(
            content=content,
            content_type=content_type,
            document_metadata_category_id=document_metadata_category_id,
            name=name,
        )

        de_his_core_datatype_his_resource.additional_properties = d
        return de_his_core_datatype_his_resource

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
