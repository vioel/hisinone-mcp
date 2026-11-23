from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="MetaHisidentifierHisidentifierDatatypeEnum")


@_attrs_define
class MetaHisidentifierHisidentifierDatatypeEnum:
    """
    Attributes:
        datatype_restriction_available (bool | Unset):
        date_restriction_available (bool | Unset):
        declaring_class (Any | Unset):
        double_restriction_available (bool | Unset):
        integer_restriction_available (bool | Unset):
        key (JavaLangObject | Unset):
        length_restriction_available (bool | Unset):
        regex_pattern_restriction_available (bool | Unset):
    """

    datatype_restriction_available: bool | Unset = UNSET
    date_restriction_available: bool | Unset = UNSET
    declaring_class: Any | Unset = UNSET
    double_restriction_available: bool | Unset = UNSET
    integer_restriction_available: bool | Unset = UNSET
    key: JavaLangObject | Unset = UNSET
    length_restriction_available: bool | Unset = UNSET
    regex_pattern_restriction_available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        datatype_restriction_available = self.datatype_restriction_available

        date_restriction_available = self.date_restriction_available

        declaring_class = self.declaring_class

        double_restriction_available = self.double_restriction_available

        integer_restriction_available = self.integer_restriction_available

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        length_restriction_available = self.length_restriction_available

        regex_pattern_restriction_available = self.regex_pattern_restriction_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datatype_restriction_available is not UNSET:
            field_dict["datatypeRestrictionAvailable"] = datatype_restriction_available
        if date_restriction_available is not UNSET:
            field_dict["dateRestrictionAvailable"] = date_restriction_available
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if double_restriction_available is not UNSET:
            field_dict["doubleRestrictionAvailable"] = double_restriction_available
        if integer_restriction_available is not UNSET:
            field_dict["integerRestrictionAvailable"] = integer_restriction_available
        if key is not UNSET:
            field_dict["key"] = key
        if length_restriction_available is not UNSET:
            field_dict["lengthRestrictionAvailable"] = length_restriction_available
        if regex_pattern_restriction_available is not UNSET:
            field_dict["regexPatternRestrictionAvailable"] = regex_pattern_restriction_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        datatype_restriction_available = d.pop("datatypeRestrictionAvailable", UNSET)

        date_restriction_available = d.pop("dateRestrictionAvailable", UNSET)

        declaring_class = d.pop("declaringClass", UNSET)

        double_restriction_available = d.pop("doubleRestrictionAvailable", UNSET)

        integer_restriction_available = d.pop("integerRestrictionAvailable", UNSET)

        _key = d.pop("key", UNSET)
        key: JavaLangObject | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = JavaLangObject.from_dict(_key)

        length_restriction_available = d.pop("lengthRestrictionAvailable", UNSET)

        regex_pattern_restriction_available = d.pop("regexPatternRestrictionAvailable", UNSET)

        meta_hisidentifier_hisidentifier_datatype_enum = cls(
            datatype_restriction_available=datatype_restriction_available,
            date_restriction_available=date_restriction_available,
            declaring_class=declaring_class,
            double_restriction_available=double_restriction_available,
            integer_restriction_available=integer_restriction_available,
            key=key,
            length_restriction_available=length_restriction_available,
            regex_pattern_restriction_available=regex_pattern_restriction_available,
        )

        meta_hisidentifier_hisidentifier_datatype_enum.additional_properties = d
        return meta_hisidentifier_hisidentifier_datatype_enum

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
