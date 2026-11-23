from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_open_api_components_schemas import CsSysRestOpenApiComponentsSchemas
    from ..models.cs_sys_rest_open_api_components_security_schemes import CsSysRestOpenApiComponentsSecuritySchemes


T = TypeVar("T", bound="CsSysRestOpenApiComponents")


@_attrs_define
class CsSysRestOpenApiComponents:
    """
    Attributes:
        schemas (CsSysRestOpenApiComponentsSchemas | Unset):
        security_schemes (CsSysRestOpenApiComponentsSecuritySchemes | Unset):
    """

    schemas: CsSysRestOpenApiComponentsSchemas | Unset = UNSET
    security_schemes: CsSysRestOpenApiComponentsSecuritySchemes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        schemas: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas.to_dict()

        security_schemes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.security_schemes, Unset):
            security_schemes = self.security_schemes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if security_schemes is not UNSET:
            field_dict["securitySchemes"] = security_schemes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_open_api_components_schemas import CsSysRestOpenApiComponentsSchemas  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_components_security_schemes import CsSysRestOpenApiComponentsSecuritySchemes  # noqa: PLC0415

        d = dict(src_dict)
        _schemas = d.pop("schemas", UNSET)
        schemas: CsSysRestOpenApiComponentsSchemas | Unset
        if isinstance(_schemas, Unset):
            schemas = UNSET
        else:
            schemas = CsSysRestOpenApiComponentsSchemas.from_dict(_schemas)

        _security_schemes = d.pop("securitySchemes", UNSET)
        security_schemes: CsSysRestOpenApiComponentsSecuritySchemes | Unset
        if isinstance(_security_schemes, Unset):
            security_schemes = UNSET
        else:
            security_schemes = CsSysRestOpenApiComponentsSecuritySchemes.from_dict(_security_schemes)

        cs_sys_rest_open_api_components = cls(
            schemas=schemas,
            security_schemes=security_schemes,
        )

        cs_sys_rest_open_api_components.additional_properties = d
        return cs_sys_rest_open_api_components

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
