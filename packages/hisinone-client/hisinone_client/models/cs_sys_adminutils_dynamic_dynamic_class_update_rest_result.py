from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_adminutils_dynamic_dynamic_class_rest import CsSysAdminutilsDynamicDynamicClassRest


T = TypeVar("T", bound="CsSysAdminutilsDynamicDynamicClassUpdateRestResult")


@_attrs_define
class CsSysAdminutilsDynamicDynamicClassUpdateRestResult:
    """
    Attributes:
        dynamic_class_rest_dto (CsSysAdminutilsDynamicDynamicClassRest | Unset):
        warnings (list[str] | Unset):
    """

    dynamic_class_rest_dto: CsSysAdminutilsDynamicDynamicClassRest | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        dynamic_class_rest_dto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_class_rest_dto, Unset):
            dynamic_class_rest_dto = self.dynamic_class_rest_dto.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dynamic_class_rest_dto is not UNSET:
            field_dict["dynamicClassRestDto"] = dynamic_class_rest_dto
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_adminutils_dynamic_dynamic_class_rest import CsSysAdminutilsDynamicDynamicClassRest  # noqa: PLC0415

        d = dict(src_dict)
        _dynamic_class_rest_dto = d.pop("dynamicClassRestDto", UNSET)
        dynamic_class_rest_dto: CsSysAdminutilsDynamicDynamicClassRest | Unset
        if isinstance(_dynamic_class_rest_dto, Unset):
            dynamic_class_rest_dto = UNSET
        else:
            dynamic_class_rest_dto = CsSysAdminutilsDynamicDynamicClassRest.from_dict(_dynamic_class_rest_dto)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        cs_sys_adminutils_dynamic_dynamic_class_update_rest_result = cls(
            dynamic_class_rest_dto=dynamic_class_rest_dto,
            warnings=warnings,
        )

        cs_sys_adminutils_dynamic_dynamic_class_update_rest_result.additional_properties = d
        return cs_sys_adminutils_dynamic_dynamic_class_update_rest_result

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
