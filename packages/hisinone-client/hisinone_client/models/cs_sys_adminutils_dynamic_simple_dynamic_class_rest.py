from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_adminutils_dynamic_simple_dynamic_attribute_rest import (
        CsSysAdminutilsDynamicSimpleDynamicAttributeRest,
    )
    from ..models.cs_sys_dynamic_dynamic_class_type import CsSysDynamicDynamicClassType


T = TypeVar("T", bound="CsSysAdminutilsDynamicSimpleDynamicClassRest")


@_attrs_define
class CsSysAdminutilsDynamicSimpleDynamicClassRest:
    """
    Attributes:
        attributes (list[CsSysAdminutilsDynamicSimpleDynamicAttributeRest] | Unset):
        id (int | Unset):
        name (str | Unset):
        type_ (CsSysDynamicDynamicClassType | Unset):
    """

    attributes: list[CsSysAdminutilsDynamicSimpleDynamicAttributeRest] | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: CsSysDynamicDynamicClassType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        id = self.id

        name = self.name

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_adminutils_dynamic_simple_dynamic_attribute_rest import (
            CsSysAdminutilsDynamicSimpleDynamicAttributeRest,  # noqa: PLC0415
        )
        from ..models.cs_sys_dynamic_dynamic_class_type import CsSysDynamicDynamicClassType  # noqa: PLC0415

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[CsSysAdminutilsDynamicSimpleDynamicAttributeRest] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = CsSysAdminutilsDynamicSimpleDynamicAttributeRest.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CsSysDynamicDynamicClassType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CsSysDynamicDynamicClassType.from_dict(_type_)

        cs_sys_adminutils_dynamic_simple_dynamic_class_rest = cls(
            attributes=attributes,
            id=id,
            name=name,
            type_=type_,
        )

        cs_sys_adminutils_dynamic_simple_dynamic_class_rest.additional_properties = d
        return cs_sys_adminutils_dynamic_simple_dynamic_class_rest

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
