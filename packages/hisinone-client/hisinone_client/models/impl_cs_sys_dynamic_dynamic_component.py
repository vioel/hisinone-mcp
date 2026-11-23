from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_dynamic_conditions import ImplCsSysDynamicConditions
    from ..models.impl_cs_sys_dynamic_simple_dynamic_component import ImplCsSysDynamicSimpleDynamicComponent
    from ..models.impl_cs_sys_dynamic_simple_dynamic_object import ImplCsSysDynamicSimpleDynamicObject


T = TypeVar("T", bound="ImplCsSysDynamicDynamicComponent")


@_attrs_define
class ImplCsSysDynamicDynamicComponent:
    """
    Attributes:
        conditions (ImplCsSysDynamicConditions | Unset):
        dynamic_objects (list[ImplCsSysDynamicSimpleDynamicObject] | Unset):
        gui_component (ImplCsSysDynamicSimpleDynamicComponent | Unset):
    """

    conditions: ImplCsSysDynamicConditions | Unset = UNSET
    dynamic_objects: list[ImplCsSysDynamicSimpleDynamicObject] | Unset = UNSET
    gui_component: ImplCsSysDynamicSimpleDynamicComponent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        dynamic_objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dynamic_objects, Unset):
            dynamic_objects = []
            for dynamic_objects_item_data in self.dynamic_objects:
                dynamic_objects_item = dynamic_objects_item_data.to_dict()
                dynamic_objects.append(dynamic_objects_item)

        gui_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gui_component, Unset):
            gui_component = self.gui_component.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if dynamic_objects is not UNSET:
            field_dict["dynamicObjects"] = dynamic_objects
        if gui_component is not UNSET:
            field_dict["guiComponent"] = gui_component

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_dynamic_conditions import ImplCsSysDynamicConditions  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_simple_dynamic_component import ImplCsSysDynamicSimpleDynamicComponent  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_simple_dynamic_object import ImplCsSysDynamicSimpleDynamicObject  # noqa: PLC0415

        d = dict(src_dict)
        _conditions = d.pop("conditions", UNSET)
        conditions: ImplCsSysDynamicConditions | Unset
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = ImplCsSysDynamicConditions.from_dict(_conditions)

        _dynamic_objects = d.pop("dynamicObjects", UNSET)
        dynamic_objects: list[ImplCsSysDynamicSimpleDynamicObject] | Unset = UNSET
        if _dynamic_objects is not UNSET:
            dynamic_objects = []
            for dynamic_objects_item_data in _dynamic_objects:
                dynamic_objects_item = ImplCsSysDynamicSimpleDynamicObject.from_dict(dynamic_objects_item_data)

                dynamic_objects.append(dynamic_objects_item)

        _gui_component = d.pop("guiComponent", UNSET)
        gui_component: ImplCsSysDynamicSimpleDynamicComponent | Unset
        if isinstance(_gui_component, Unset):
            gui_component = UNSET
        else:
            gui_component = ImplCsSysDynamicSimpleDynamicComponent.from_dict(_gui_component)

        impl_cs_sys_dynamic_dynamic_component = cls(
            conditions=conditions,
            dynamic_objects=dynamic_objects,
            gui_component=gui_component,
        )

        impl_cs_sys_dynamic_dynamic_component.additional_properties = d
        return impl_cs_sys_dynamic_dynamic_component

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
