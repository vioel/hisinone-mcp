from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iface_grading_type_purpose import IfaceGradingTypePurpose
    from ..models.iface_rounding_method import IfaceRoundingMethod


T = TypeVar("T", bound="IfaceGradingType")


@_attrs_define
class IfaceGradingType:
    """
    Attributes:
        allowed_values (str | Unset):
        allowed_values_as_list (list[float] | Unset):
        country (list[Any] | Unset):
        credits_threshold (float | Unset):
        defaulttext (str | Unset):
        grade_status (list[Any] | Unset):
        grading_type_conversion (list[Any] | Unset):
        grading_type_purpose (IfaceGradingTypePurpose | Unset):
        grading_type_texts (list[Any] | Unset):
        id (int | Unset):
        identifier (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        lower_limit (float | Unset):
        obj_guid (str | Unset):
        regular_expression (str | Unset):
        remarks (list[Any] | Unset):
        rounding_method (IfaceRoundingMethod | Unset):
        rounding_position (int | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        type_of_grading (int | Unset):
        uniquename (str | Unset):
        upper_limit (float | Unset):
    """

    allowed_values: str | Unset = UNSET
    allowed_values_as_list: list[float] | Unset = UNSET
    country: list[Any] | Unset = UNSET
    credits_threshold: float | Unset = UNSET
    defaulttext: str | Unset = UNSET
    grade_status: list[Any] | Unset = UNSET
    grading_type_conversion: list[Any] | Unset = UNSET
    grading_type_purpose: IfaceGradingTypePurpose | Unset = UNSET
    grading_type_texts: list[Any] | Unset = UNSET
    id: int | Unset = UNSET
    identifier: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    lower_limit: float | Unset = UNSET
    obj_guid: str | Unset = UNSET
    regular_expression: str | Unset = UNSET
    remarks: list[Any] | Unset = UNSET
    rounding_method: IfaceRoundingMethod | Unset = UNSET
    rounding_position: int | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    type_of_grading: int | Unset = UNSET
    uniquename: str | Unset = UNSET
    upper_limit: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        allowed_values = self.allowed_values

        allowed_values_as_list: list[float] | Unset = UNSET
        if not isinstance(self.allowed_values_as_list, Unset):
            allowed_values_as_list = self.allowed_values_as_list

        country: list[Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country

        credits_threshold = self.credits_threshold

        defaulttext = self.defaulttext

        grade_status: list[Any] | Unset = UNSET
        if not isinstance(self.grade_status, Unset):
            grade_status = self.grade_status

        grading_type_conversion: list[Any] | Unset = UNSET
        if not isinstance(self.grading_type_conversion, Unset):
            grading_type_conversion = self.grading_type_conversion

        grading_type_purpose: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grading_type_purpose, Unset):
            grading_type_purpose = self.grading_type_purpose.to_dict()

        grading_type_texts: list[Any] | Unset = UNSET
        if not isinstance(self.grading_type_texts, Unset):
            grading_type_texts = self.grading_type_texts

        id = self.id

        identifier = self.identifier

        lock_version = self.lock_version

        longtext = self.longtext

        lower_limit = self.lower_limit

        obj_guid = self.obj_guid

        regular_expression = self.regular_expression

        remarks: list[Any] | Unset = UNSET
        if not isinstance(self.remarks, Unset):
            remarks = self.remarks

        rounding_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rounding_method, Unset):
            rounding_method = self.rounding_method.to_dict()

        rounding_position = self.rounding_position

        shorttext = self.shorttext

        sortorder = self.sortorder

        type_of_grading = self.type_of_grading

        uniquename = self.uniquename

        upper_limit = self.upper_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if allowed_values_as_list is not UNSET:
            field_dict["allowedValuesAsList"] = allowed_values_as_list
        if country is not UNSET:
            field_dict["country"] = country
        if credits_threshold is not UNSET:
            field_dict["creditsThreshold"] = credits_threshold
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if grade_status is not UNSET:
            field_dict["gradeStatus"] = grade_status
        if grading_type_conversion is not UNSET:
            field_dict["gradingTypeConversion"] = grading_type_conversion
        if grading_type_purpose is not UNSET:
            field_dict["gradingTypePurpose"] = grading_type_purpose
        if grading_type_texts is not UNSET:
            field_dict["gradingTypeTexts"] = grading_type_texts
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if lower_limit is not UNSET:
            field_dict["lowerLimit"] = lower_limit
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if regular_expression is not UNSET:
            field_dict["regularExpression"] = regular_expression
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if rounding_method is not UNSET:
            field_dict["roundingMethod"] = rounding_method
        if rounding_position is not UNSET:
            field_dict["roundingPosition"] = rounding_position
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if type_of_grading is not UNSET:
            field_dict["typeOfGrading"] = type_of_grading
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if upper_limit is not UNSET:
            field_dict["upperLimit"] = upper_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iface_grading_type_purpose import IfaceGradingTypePurpose  # noqa: PLC0415
        from ..models.iface_rounding_method import IfaceRoundingMethod  # noqa: PLC0415

        d = dict(src_dict)
        allowed_values = d.pop("allowedValues", UNSET)

        allowed_values_as_list = cast(list[float], d.pop("allowedValuesAsList", UNSET))

        country = cast(list[Any], d.pop("country", UNSET))

        credits_threshold = d.pop("creditsThreshold", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        grade_status = cast(list[Any], d.pop("gradeStatus", UNSET))

        grading_type_conversion = cast(list[Any], d.pop("gradingTypeConversion", UNSET))

        _grading_type_purpose = d.pop("gradingTypePurpose", UNSET)
        grading_type_purpose: IfaceGradingTypePurpose | Unset
        if isinstance(_grading_type_purpose, Unset):
            grading_type_purpose = UNSET
        else:
            grading_type_purpose = IfaceGradingTypePurpose.from_dict(_grading_type_purpose)

        grading_type_texts = cast(list[Any], d.pop("gradingTypeTexts", UNSET))

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        lower_limit = d.pop("lowerLimit", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        regular_expression = d.pop("regularExpression", UNSET)

        remarks = cast(list[Any], d.pop("remarks", UNSET))

        _rounding_method = d.pop("roundingMethod", UNSET)
        rounding_method: IfaceRoundingMethod | Unset
        if isinstance(_rounding_method, Unset):
            rounding_method = UNSET
        else:
            rounding_method = IfaceRoundingMethod.from_dict(_rounding_method)

        rounding_position = d.pop("roundingPosition", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        type_of_grading = d.pop("typeOfGrading", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        upper_limit = d.pop("upperLimit", UNSET)

        iface_grading_type = cls(
            allowed_values=allowed_values,
            allowed_values_as_list=allowed_values_as_list,
            country=country,
            credits_threshold=credits_threshold,
            defaulttext=defaulttext,
            grade_status=grade_status,
            grading_type_conversion=grading_type_conversion,
            grading_type_purpose=grading_type_purpose,
            grading_type_texts=grading_type_texts,
            id=id,
            identifier=identifier,
            lock_version=lock_version,
            longtext=longtext,
            lower_limit=lower_limit,
            obj_guid=obj_guid,
            regular_expression=regular_expression,
            remarks=remarks,
            rounding_method=rounding_method,
            rounding_position=rounding_position,
            shorttext=shorttext,
            sortorder=sortorder,
            type_of_grading=type_of_grading,
            uniquename=uniquename,
            upper_limit=upper_limit,
        )

        iface_grading_type.additional_properties = d
        return iface_grading_type

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
