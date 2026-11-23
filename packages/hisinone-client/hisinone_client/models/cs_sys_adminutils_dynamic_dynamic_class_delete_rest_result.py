from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysAdminutilsDynamicDynamicClassDeleteRestResult")


@_attrs_define
class CsSysAdminutilsDynamicDynamicClassDeleteRestResult:
    """
    Attributes:
        is_deleted (bool | Unset):
        warnings (list[str] | Unset):
    """

    is_deleted: bool | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        is_deleted = self.is_deleted

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_deleted = d.pop("isDeleted", UNSET)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        cs_sys_adminutils_dynamic_dynamic_class_delete_rest_result = cls(
            is_deleted=is_deleted,
            warnings=warnings,
        )

        cs_sys_adminutils_dynamic_dynamic_class_delete_rest_result.additional_properties = d
        return cs_sys_adminutils_dynamic_dynamic_class_delete_rest_result

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
