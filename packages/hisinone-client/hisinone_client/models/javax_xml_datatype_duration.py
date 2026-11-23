from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.javax_xml_namespace_q_name import JavaxXmlNamespaceQName


T = TypeVar("T", bound="JavaxXmlDatatypeDuration")


@_attrs_define
class JavaxXmlDatatypeDuration:
    """
    Attributes:
        days (int | Unset):
        hours (int | Unset):
        minutes (int | Unset):
        months (int | Unset):
        seconds (int | Unset):
        sign (int | Unset):
        x_ml_schema_type (JavaxXmlNamespaceQName | Unset):
        years (int | Unset):
    """

    days: int | Unset = UNSET
    hours: int | Unset = UNSET
    minutes: int | Unset = UNSET
    months: int | Unset = UNSET
    seconds: int | Unset = UNSET
    sign: int | Unset = UNSET
    x_ml_schema_type: JavaxXmlNamespaceQName | Unset = UNSET
    years: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        hours = self.hours

        minutes = self.minutes

        months = self.months

        seconds = self.seconds

        sign = self.sign

        x_ml_schema_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.x_ml_schema_type, Unset):
            x_ml_schema_type = self.x_ml_schema_type.to_dict()

        years = self.years

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if hours is not UNSET:
            field_dict["hours"] = hours
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if months is not UNSET:
            field_dict["months"] = months
        if seconds is not UNSET:
            field_dict["seconds"] = seconds
        if sign is not UNSET:
            field_dict["sign"] = sign
        if x_ml_schema_type is not UNSET:
            field_dict["xMLSchemaType"] = x_ml_schema_type
        if years is not UNSET:
            field_dict["years"] = years

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.javax_xml_namespace_q_name import JavaxXmlNamespaceQName  # noqa: PLC0415

        d = dict(src_dict)
        days = d.pop("days", UNSET)

        hours = d.pop("hours", UNSET)

        minutes = d.pop("minutes", UNSET)

        months = d.pop("months", UNSET)

        seconds = d.pop("seconds", UNSET)

        sign = d.pop("sign", UNSET)

        _x_ml_schema_type = d.pop("xMLSchemaType", UNSET)
        x_ml_schema_type: JavaxXmlNamespaceQName | Unset
        if isinstance(_x_ml_schema_type, Unset):
            x_ml_schema_type = UNSET
        else:
            x_ml_schema_type = JavaxXmlNamespaceQName.from_dict(_x_ml_schema_type)

        years = d.pop("years", UNSET)

        javax_xml_datatype_duration = cls(
            days=days,
            hours=hours,
            minutes=minutes,
            months=months,
            seconds=seconds,
            sign=sign,
            x_ml_schema_type=x_ml_schema_type,
            years=years,
        )

        javax_xml_datatype_duration.additional_properties = d
        return javax_xml_datatype_duration

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
