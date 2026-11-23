from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_adminutils_dynamic_dynamic_attribute_rest import CsSysAdminutilsDynamicDynamicAttributeRest
    from ..models.cs_sys_dynamic_dynamic_class_type import CsSysDynamicDynamicClassType


T = TypeVar("T", bound="CsSysAdminutilsDynamicDynamicClassRest")


@_attrs_define
class CsSysAdminutilsDynamicDynamicClassRest:
    """
    Attributes:
        attributes (list[CsSysAdminutilsDynamicDynamicAttributeRest] | Unset):
        confsrc_id (int | Unset):
        dynamic_class_type (CsSysDynamicDynamicClassType | Unset):
        id (int | Unset):
        name (str | Unset):
        parent_dynamic_class_id (int | Unset):
    """

    attributes: list[CsSysAdminutilsDynamicDynamicAttributeRest] | Unset = UNSET
    confsrc_id: int | Unset = UNSET
    dynamic_class_type: CsSysDynamicDynamicClassType | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    parent_dynamic_class_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        confsrc_id = self.confsrc_id

        dynamic_class_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_class_type, Unset):
            dynamic_class_type = self.dynamic_class_type.to_dict()

        id = self.id

        name = self.name

        parent_dynamic_class_id = self.parent_dynamic_class_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if confsrc_id is not UNSET:
            field_dict["confsrcId"] = confsrc_id
        if dynamic_class_type is not UNSET:
            field_dict["dynamicClassType"] = dynamic_class_type
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_dynamic_class_id is not UNSET:
            field_dict["parentDynamicClassId"] = parent_dynamic_class_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_adminutils_dynamic_dynamic_attribute_rest import CsSysAdminutilsDynamicDynamicAttributeRest  # noqa: PLC0415
        from ..models.cs_sys_dynamic_dynamic_class_type import CsSysDynamicDynamicClassType  # noqa: PLC0415

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[CsSysAdminutilsDynamicDynamicAttributeRest] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = CsSysAdminutilsDynamicDynamicAttributeRest.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        confsrc_id = d.pop("confsrcId", UNSET)

        _dynamic_class_type = d.pop("dynamicClassType", UNSET)
        dynamic_class_type: CsSysDynamicDynamicClassType | Unset
        if isinstance(_dynamic_class_type, Unset):
            dynamic_class_type = UNSET
        else:
            dynamic_class_type = CsSysDynamicDynamicClassType.from_dict(_dynamic_class_type)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parent_dynamic_class_id = d.pop("parentDynamicClassId", UNSET)

        cs_sys_adminutils_dynamic_dynamic_class_rest = cls(
            attributes=attributes,
            confsrc_id=confsrc_id,
            dynamic_class_type=dynamic_class_type,
            id=id,
            name=name,
            parent_dynamic_class_id=parent_dynamic_class_id,
        )

        cs_sys_adminutils_dynamic_dynamic_class_rest.additional_properties = d
        return cs_sys_adminutils_dynamic_dynamic_class_rest

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
