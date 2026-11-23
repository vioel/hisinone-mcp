from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta_hisidentifier_hisidentifier_datatype_enum import MetaHisidentifierHisidentifierDatatypeEnum


T = TypeVar("T", bound="CsSysAdminutilsDynamicSimpleDynamicAttributeRest")


@_attrs_define
class CsSysAdminutilsDynamicSimpleDynamicAttributeRest:
    """
    Attributes:
        name (str | Unset):
        type_ (MetaHisidentifierHisidentifierDatatypeEnum | Unset):
    """

    name: str | Unset = UNSET
    type_: MetaHisidentifierHisidentifierDatatypeEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_hisidentifier_hisidentifier_datatype_enum import MetaHisidentifierHisidentifierDatatypeEnum  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: MetaHisidentifierHisidentifierDatatypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MetaHisidentifierHisidentifierDatatypeEnum.from_dict(_type_)

        cs_sys_adminutils_dynamic_simple_dynamic_attribute_rest = cls(
            name=name,
            type_=type_,
        )

        cs_sys_adminutils_dynamic_simple_dynamic_attribute_rest.additional_properties = d
        return cs_sys_adminutils_dynamic_simple_dynamic_attribute_rest

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
