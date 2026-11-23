from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CsSysRestOpenApiParameterSchema")


@_attrs_define
class CsSysRestOpenApiParameterSchema:
    additional_properties: dict[str, JavaLangObject] = _attrs_field(init=False, factory=dict[str, "JavaLangObject"])

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        cs_sys_rest_open_api_parameter_schema = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = JavaLangObject.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        cs_sys_rest_open_api_parameter_schema.additional_properties = additional_properties
        return cs_sys_rest_open_api_parameter_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> JavaLangObject:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: JavaLangObject) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
