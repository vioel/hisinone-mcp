from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_open_api_parameter_schema import CsSysRestOpenApiParameterSchema


T = TypeVar("T", bound="CsSysRestOpenApiParameter")


@_attrs_define
class CsSysRestOpenApiParameter:
    """
    Attributes:
        in_ (str | Unset):
        name (str | Unset):
        required (bool | Unset):
        schema (CsSysRestOpenApiParameterSchema | Unset):
    """

    in_: str | Unset = UNSET
    name: str | Unset = UNSET
    required: bool | Unset = UNSET
    schema: CsSysRestOpenApiParameterSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        in_ = self.in_

        name = self.name

        required = self.required

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_ is not UNSET:
            field_dict["in"] = in_
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_open_api_parameter_schema import CsSysRestOpenApiParameterSchema  # noqa: PLC0415

        d = dict(src_dict)
        in_ = d.pop("in", UNSET)

        name = d.pop("name", UNSET)

        required = d.pop("required", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: CsSysRestOpenApiParameterSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = CsSysRestOpenApiParameterSchema.from_dict(_schema)

        cs_sys_rest_open_api_parameter = cls(
            in_=in_,
            name=name,
            required=required,
            schema=schema,
        )

        cs_sys_rest_open_api_parameter.additional_properties = d
        return cs_sys_rest_open_api_parameter

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
