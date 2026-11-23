from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_math_big_integer import JavaMathBigInteger
    from ..models.javax_xml_namespace_q_name import JavaxXmlNamespaceQName


T = TypeVar("T", bound="JavaxXmlDatatypeXMLGregorianCalendar")


@_attrs_define
class JavaxXmlDatatypeXMLGregorianCalendar:
    """
    Attributes:
        day (int | Unset):
        eon (JavaMathBigInteger | Unset):
        eon_and_year (JavaMathBigInteger | Unset):
        fractional_second (float | Unset):
        hour (int | Unset):
        millisecond (int | Unset):
        minute (int | Unset):
        month (int | Unset):
        second (int | Unset):
        timezone (int | Unset):
        valid (bool | Unset):
        x_ml_schema_type (JavaxXmlNamespaceQName | Unset):
        year (int | Unset):
    """

    day: int | Unset = UNSET
    eon: JavaMathBigInteger | Unset = UNSET
    eon_and_year: JavaMathBigInteger | Unset = UNSET
    fractional_second: float | Unset = UNSET
    hour: int | Unset = UNSET
    millisecond: int | Unset = UNSET
    minute: int | Unset = UNSET
    month: int | Unset = UNSET
    second: int | Unset = UNSET
    timezone: int | Unset = UNSET
    valid: bool | Unset = UNSET
    x_ml_schema_type: JavaxXmlNamespaceQName | Unset = UNSET
    year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        eon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eon, Unset):
            eon = self.eon.to_dict()

        eon_and_year: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eon_and_year, Unset):
            eon_and_year = self.eon_and_year.to_dict()

        fractional_second = self.fractional_second

        hour = self.hour

        millisecond = self.millisecond

        minute = self.minute

        month = self.month

        second = self.second

        timezone = self.timezone

        valid = self.valid

        x_ml_schema_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.x_ml_schema_type, Unset):
            x_ml_schema_type = self.x_ml_schema_type.to_dict()

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if eon is not UNSET:
            field_dict["eon"] = eon
        if eon_and_year is not UNSET:
            field_dict["eonAndYear"] = eon_and_year
        if fractional_second is not UNSET:
            field_dict["fractionalSecond"] = fractional_second
        if hour is not UNSET:
            field_dict["hour"] = hour
        if millisecond is not UNSET:
            field_dict["millisecond"] = millisecond
        if minute is not UNSET:
            field_dict["minute"] = minute
        if month is not UNSET:
            field_dict["month"] = month
        if second is not UNSET:
            field_dict["second"] = second
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if valid is not UNSET:
            field_dict["valid"] = valid
        if x_ml_schema_type is not UNSET:
            field_dict["xMLSchemaType"] = x_ml_schema_type
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_math_big_integer import JavaMathBigInteger  # noqa: PLC0415
        from ..models.javax_xml_namespace_q_name import JavaxXmlNamespaceQName  # noqa: PLC0415

        d = dict(src_dict)
        day = d.pop("day", UNSET)

        _eon = d.pop("eon", UNSET)
        eon: JavaMathBigInteger | Unset
        if isinstance(_eon, Unset):
            eon = UNSET
        else:
            eon = JavaMathBigInteger.from_dict(_eon)

        _eon_and_year = d.pop("eonAndYear", UNSET)
        eon_and_year: JavaMathBigInteger | Unset
        if isinstance(_eon_and_year, Unset):
            eon_and_year = UNSET
        else:
            eon_and_year = JavaMathBigInteger.from_dict(_eon_and_year)

        fractional_second = d.pop("fractionalSecond", UNSET)

        hour = d.pop("hour", UNSET)

        millisecond = d.pop("millisecond", UNSET)

        minute = d.pop("minute", UNSET)

        month = d.pop("month", UNSET)

        second = d.pop("second", UNSET)

        timezone = d.pop("timezone", UNSET)

        valid = d.pop("valid", UNSET)

        _x_ml_schema_type = d.pop("xMLSchemaType", UNSET)
        x_ml_schema_type: JavaxXmlNamespaceQName | Unset
        if isinstance(_x_ml_schema_type, Unset):
            x_ml_schema_type = UNSET
        else:
            x_ml_schema_type = JavaxXmlNamespaceQName.from_dict(_x_ml_schema_type)

        year = d.pop("year", UNSET)

        javax_xml_datatype_xml_gregorian_calendar = cls(
            day=day,
            eon=eon,
            eon_and_year=eon_and_year,
            fractional_second=fractional_second,
            hour=hour,
            millisecond=millisecond,
            minute=minute,
            month=month,
            second=second,
            timezone=timezone,
            valid=valid,
            x_ml_schema_type=x_ml_schema_type,
            year=year,
        )

        javax_xml_datatype_xml_gregorian_calendar.additional_properties = d
        return javax_xml_datatype_xml_gregorian_calendar

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
