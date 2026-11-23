from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_result_item_messages import (
        FsResPublicationUniversalImportResultItemMessages,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportResultItem")


@_attrs_define
class FsResPublicationUniversalImportResultItem:
    """
    Attributes:
        id (int | Unset):
        messages (FsResPublicationUniversalImportResultItemMessages | Unset):
        obj_guid (str | Unset):
    """

    id: int | Unset = UNSET
    messages: FsResPublicationUniversalImportResultItemMessages | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        messages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages.to_dict()

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if messages is not UNSET:
            field_dict["messages"] = messages
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_result_item_messages import (
            FsResPublicationUniversalImportResultItemMessages,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: FsResPublicationUniversalImportResultItemMessages | Unset
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = FsResPublicationUniversalImportResultItemMessages.from_dict(_messages)

        obj_guid = d.pop("objGuid", UNSET)

        fs_res_publication_universal_import_result_item = cls(
            id=id,
            messages=messages,
            obj_guid=obj_guid,
        )

        fs_res_publication_universal_import_result_item.additional_properties = d
        return fs_res_publication_universal_import_result_item

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
