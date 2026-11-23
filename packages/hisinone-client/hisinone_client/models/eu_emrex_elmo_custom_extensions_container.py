from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_custom_extensions_container_other_attributes import (
        EuEmrexElmoCustomExtensionsContainerOtherAttributes,
    )
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="EuEmrexElmoCustomExtensionsContainer")


@_attrs_define
class EuEmrexElmoCustomExtensionsContainer:
    """
    Attributes:
        any_ (list[JavaLangObject] | Unset):
        other_attributes (EuEmrexElmoCustomExtensionsContainerOtherAttributes | Unset):
    """

    any_: list[JavaLangObject] | Unset = UNSET
    other_attributes: EuEmrexElmoCustomExtensionsContainerOtherAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        any_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.any_, Unset):
            any_ = []
            for any_item_data in self.any_:
                any_item = any_item_data.to_dict()
                any_.append(any_item)

        other_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_attributes, Unset):
            other_attributes = self.other_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if any_ is not UNSET:
            field_dict["any"] = any_
        if other_attributes is not UNSET:
            field_dict["otherAttributes"] = other_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_custom_extensions_container_other_attributes import (
            EuEmrexElmoCustomExtensionsContainerOtherAttributes,  # noqa: PLC0415
        )
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        _any_ = d.pop("any", UNSET)
        any_: list[JavaLangObject] | Unset = UNSET
        if _any_ is not UNSET:
            any_ = []
            for any_item_data in _any_:
                any_item = JavaLangObject.from_dict(any_item_data)

                any_.append(any_item)

        _other_attributes = d.pop("otherAttributes", UNSET)
        other_attributes: EuEmrexElmoCustomExtensionsContainerOtherAttributes | Unset
        if isinstance(_other_attributes, Unset):
            other_attributes = UNSET
        else:
            other_attributes = EuEmrexElmoCustomExtensionsContainerOtherAttributes.from_dict(_other_attributes)

        eu_emrex_elmo_custom_extensions_container = cls(
            any_=any_,
            other_attributes=other_attributes,
        )

        eu_emrex_elmo_custom_extensions_container.additional_properties = d
        return eu_emrex_elmo_custom_extensions_container

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
