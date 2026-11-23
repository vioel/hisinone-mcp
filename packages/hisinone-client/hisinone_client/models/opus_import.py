from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opus_publication import OpusPublication


T = TypeVar("T", bound="OpusImport")


@_attrs_define
class OpusImport:
    """
    Attributes:
        publication_list (list[OpusPublication] | Unset):
    """

    publication_list: list[OpusPublication] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        publication_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publication_list, Unset):
            publication_list = []
            for publication_list_item_data in self.publication_list:
                publication_list_item = publication_list_item_data.to_dict()
                publication_list.append(publication_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if publication_list is not UNSET:
            field_dict["publicationList"] = publication_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opus_publication import OpusPublication  # noqa: PLC0415

        d = dict(src_dict)
        _publication_list = d.pop("publicationList", UNSET)
        publication_list: list[OpusPublication] | Unset = UNSET
        if _publication_list is not UNSET:
            publication_list = []
            for publication_list_item_data in _publication_list:
                publication_list_item = OpusPublication.from_dict(publication_list_item_data)

                publication_list.append(publication_list_item)

        opus_import = cls(
            publication_list=publication_list,
        )

        opus_import.additional_properties = d
        return opus_import

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
