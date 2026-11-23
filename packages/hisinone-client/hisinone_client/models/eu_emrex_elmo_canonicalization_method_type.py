from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="EuEmrexElmoCanonicalizationMethodType")


@_attrs_define
class EuEmrexElmoCanonicalizationMethodType:
    """
    Attributes:
        algorithm (str | Unset):
        content (list[JavaLangObject] | Unset):
    """

    algorithm: str | Unset = UNSET
    content: list[JavaLangObject] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm

        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        algorithm = d.pop("algorithm", UNSET)

        _content = d.pop("content", UNSET)
        content: list[JavaLangObject] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = JavaLangObject.from_dict(content_item_data)

                content.append(content_item)

        eu_emrex_elmo_canonicalization_method_type = cls(
            algorithm=algorithm,
            content=content,
        )

        eu_emrex_elmo_canonicalization_method_type.additional_properties = d
        return eu_emrex_elmo_canonicalization_method_type

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
