from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.impl_cs_sys_dynamic_dynamic_attribute import ImplCsSysDynamicDynamicAttribute
    from ..models.impl_cs_sys_dynamic_dynamic_class_foreigntext import ImplCsSysDynamicDynamicClassForeigntext


T = TypeVar("T", bound="ImplCsSysDynamicDynamicClass")


@_attrs_define
class ImplCsSysDynamicDynamicClass:
    """
    Attributes:
        field_foreigntext (ImplCsSysDynamicDynamicClassForeigntext | Unset):
        class_name (str | Unset):
        class_type (CsSysValueGenericValue | Unset):
        conf_source (CsSysValueGenericValue | Unset):
        dynamic_attributes (list[ImplCsSysDynamicDynamicAttribute] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ImplCsSysDynamicDynamicClassForeigntext | Unset = UNSET
    class_name: str | Unset = UNSET
    class_type: CsSysValueGenericValue | Unset = UNSET
    conf_source: CsSysValueGenericValue | Unset = UNSET
    dynamic_attributes: list[ImplCsSysDynamicDynamicAttribute] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        class_name = self.class_name

        class_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.class_type, Unset):
            class_type = self.class_type.to_dict()

        conf_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conf_source, Unset):
            conf_source = self.conf_source.to_dict()

        dynamic_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dynamic_attributes, Unset):
            dynamic_attributes = []
            for dynamic_attributes_item_data in self.dynamic_attributes:
                dynamic_attributes_item = dynamic_attributes_item_data.to_dict()
                dynamic_attributes.append(dynamic_attributes_item)

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if class_type is not UNSET:
            field_dict["classType"] = class_type
        if conf_source is not UNSET:
            field_dict["confSource"] = conf_source
        if dynamic_attributes is not UNSET:
            field_dict["dynamicAttributes"] = dynamic_attributes
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_attribute import ImplCsSysDynamicDynamicAttribute  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_class_foreigntext import ImplCsSysDynamicDynamicClassForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplCsSysDynamicDynamicClassForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplCsSysDynamicDynamicClassForeigntext.from_dict(_field_foreigntext)

        class_name = d.pop("className", UNSET)

        _class_type = d.pop("classType", UNSET)
        class_type: CsSysValueGenericValue | Unset
        if isinstance(_class_type, Unset):
            class_type = UNSET
        else:
            class_type = CsSysValueGenericValue.from_dict(_class_type)

        _conf_source = d.pop("confSource", UNSET)
        conf_source: CsSysValueGenericValue | Unset
        if isinstance(_conf_source, Unset):
            conf_source = UNSET
        else:
            conf_source = CsSysValueGenericValue.from_dict(_conf_source)

        _dynamic_attributes = d.pop("dynamicAttributes", UNSET)
        dynamic_attributes: list[ImplCsSysDynamicDynamicAttribute] | Unset = UNSET
        if _dynamic_attributes is not UNSET:
            dynamic_attributes = []
            for dynamic_attributes_item_data in _dynamic_attributes:
                dynamic_attributes_item = ImplCsSysDynamicDynamicAttribute.from_dict(dynamic_attributes_item_data)

                dynamic_attributes.append(dynamic_attributes_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        impl_cs_sys_dynamic_dynamic_class = cls(
            field_foreigntext=field_foreigntext,
            class_name=class_name,
            class_type=class_type,
            conf_source=conf_source,
            dynamic_attributes=dynamic_attributes,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        impl_cs_sys_dynamic_dynamic_class.additional_properties = d
        return impl_cs_sys_dynamic_dynamic_class

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
