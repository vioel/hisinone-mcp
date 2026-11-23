from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CommonTermTypeValueTermcategory")


@_attrs_define
class CommonTermTypeValueTermcategory:
    """
    Attributes:
        declaring_class (Any | Unset):
        his_key (JavaLangObject | Unset):
    """

    declaring_class: Any | Unset = UNSET
    his_key: JavaLangObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        declaring_class = self.declaring_class

        his_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.his_key, Unset):
            his_key = self.his_key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if his_key is not UNSET:
            field_dict["hisKey"] = his_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        declaring_class = d.pop("declaringClass", UNSET)

        _his_key = d.pop("hisKey", UNSET)
        his_key: JavaLangObject | Unset
        if isinstance(_his_key, Unset):
            his_key = UNSET
        else:
            his_key = JavaLangObject.from_dict(_his_key)

        common_term_type_value_termcategory = cls(
            declaring_class=declaring_class,
            his_key=his_key,
        )

        common_term_type_value_termcategory.additional_properties = d
        return common_term_type_value_termcategory

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
