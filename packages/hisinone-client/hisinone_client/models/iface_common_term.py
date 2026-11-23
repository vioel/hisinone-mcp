from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_term_type_value import CsSysValueTermTypeValue


T = TypeVar("T", bound="IfaceCommonTerm")


@_attrs_define
class IfaceCommonTerm:
    """
    Attributes:
        defaulttext (str | Unset):
        id (str | Unset):
        longtext (str | Unset):
        shorttext (str | Unset):
        term_as_integer (int | Unset):
        term_type (CsSysValueTermTypeValue | Unset):
        term_type_category (int | Unset):
        term_type_id (int | Unset):
        term_type_number (int | Unset):
        text (str | Unset):
        year (int | Unset):
    """

    defaulttext: str | Unset = UNSET
    id: str | Unset = UNSET
    longtext: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    term_as_integer: int | Unset = UNSET
    term_type: CsSysValueTermTypeValue | Unset = UNSET
    term_type_category: int | Unset = UNSET
    term_type_id: int | Unset = UNSET
    term_type_number: int | Unset = UNSET
    text: str | Unset = UNSET
    year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defaulttext = self.defaulttext

        id = self.id

        longtext = self.longtext

        shorttext = self.shorttext

        term_as_integer = self.term_as_integer

        term_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.term_type, Unset):
            term_type = self.term_type.to_dict()

        term_type_category = self.term_type_category

        term_type_id = self.term_type_id

        term_type_number = self.term_type_number

        text = self.text

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if term_as_integer is not UNSET:
            field_dict["termAsInteger"] = term_as_integer
        if term_type is not UNSET:
            field_dict["termType"] = term_type
        if term_type_category is not UNSET:
            field_dict["termTypeCategory"] = term_type_category
        if term_type_id is not UNSET:
            field_dict["termTypeId"] = term_type_id
        if term_type_number is not UNSET:
            field_dict["termTypeNumber"] = term_type_number
        if text is not UNSET:
            field_dict["text"] = text
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_term_type_value import CsSysValueTermTypeValue  # noqa: PLC0415

        d = dict(src_dict)
        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        longtext = d.pop("longtext", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        term_as_integer = d.pop("termAsInteger", UNSET)

        _term_type = d.pop("termType", UNSET)
        term_type: CsSysValueTermTypeValue | Unset
        if isinstance(_term_type, Unset):
            term_type = UNSET
        else:
            term_type = CsSysValueTermTypeValue.from_dict(_term_type)

        term_type_category = d.pop("termTypeCategory", UNSET)

        term_type_id = d.pop("termTypeId", UNSET)

        term_type_number = d.pop("termTypeNumber", UNSET)

        text = d.pop("text", UNSET)

        year = d.pop("year", UNSET)

        iface_common_term = cls(
            defaulttext=defaulttext,
            id=id,
            longtext=longtext,
            shorttext=shorttext,
            term_as_integer=term_as_integer,
            term_type=term_type,
            term_type_category=term_type_category,
            term_type_id=term_type_id,
            term_type_number=term_type_number,
            text=text,
            year=year,
        )

        iface_common_term.additional_properties = d
        return iface_common_term

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
