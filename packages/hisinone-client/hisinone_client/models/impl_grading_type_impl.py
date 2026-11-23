from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iface_grade_to_status_adapter import IfaceGradeToStatusAdapter
    from ..models.iface_grading_type_conversion_adapter import IfaceGradingTypeConversionAdapter
    from ..models.iface_grading_type_country_adapter import IfaceGradingTypeCountryAdapter
    from ..models.iface_grading_type_purpose import IfaceGradingTypePurpose
    from ..models.iface_grading_type_text_adapter import IfaceGradingTypeTextAdapter
    from ..models.iface_remark_to_status_adapter import IfaceRemarkToStatusAdapter
    from ..models.iface_rounding_method import IfaceRoundingMethod
    from ..models.impl_grading_type_impl_foreigntext import ImplGradingTypeImplForeigntext


T = TypeVar("T", bound="ImplGradingTypeImpl")


@_attrs_define
class ImplGradingTypeImpl:
    """
    Attributes:
        field_foreigntext (ImplGradingTypeImplForeigntext | Unset):
        allowed_values (str | Unset):
        allowed_values_as_list (list[float] | Unset):
        country (list[IfaceGradingTypeCountryAdapter] | Unset):
        credits_threshold (float | Unset):
        defaulttext (str | Unset):
        grade_status (list[IfaceGradeToStatusAdapter] | Unset):
        grading_type_conversion (list[IfaceGradingTypeConversionAdapter] | Unset):
        grading_type_purpose (IfaceGradingTypePurpose | Unset):
        grading_type_texts (list[IfaceGradingTypeTextAdapter] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        lower_limit (float | Unset):
        obj_guid (str | Unset):
        regular_expression (str | Unset):
        remarks (list[IfaceRemarkToStatusAdapter] | Unset):
        rounding_method (IfaceRoundingMethod | Unset):
        rounding_position (int | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        type_of_grading (int | Unset):
        uniquename (str | Unset):
        upper_limit (float | Unset):
    """

    field_foreigntext: ImplGradingTypeImplForeigntext | Unset = UNSET
    allowed_values: str | Unset = UNSET
    allowed_values_as_list: list[float] | Unset = UNSET
    country: list[IfaceGradingTypeCountryAdapter] | Unset = UNSET
    credits_threshold: float | Unset = UNSET
    defaulttext: str | Unset = UNSET
    grade_status: list[IfaceGradeToStatusAdapter] | Unset = UNSET
    grading_type_conversion: list[IfaceGradingTypeConversionAdapter] | Unset = UNSET
    grading_type_purpose: IfaceGradingTypePurpose | Unset = UNSET
    grading_type_texts: list[IfaceGradingTypeTextAdapter] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    lower_limit: float | Unset = UNSET
    obj_guid: str | Unset = UNSET
    regular_expression: str | Unset = UNSET
    remarks: list[IfaceRemarkToStatusAdapter] | Unset = UNSET
    rounding_method: IfaceRoundingMethod | Unset = UNSET
    rounding_position: int | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    type_of_grading: int | Unset = UNSET
    uniquename: str | Unset = UNSET
    upper_limit: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        allowed_values = self.allowed_values

        allowed_values_as_list: list[float] | Unset = UNSET
        if not isinstance(self.allowed_values_as_list, Unset):
            allowed_values_as_list = self.allowed_values_as_list

        country: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = []
            for country_item_data in self.country:
                country_item = country_item_data.to_dict()
                country.append(country_item)

        credits_threshold = self.credits_threshold

        defaulttext = self.defaulttext

        grade_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grade_status, Unset):
            grade_status = []
            for grade_status_item_data in self.grade_status:
                grade_status_item = grade_status_item_data.to_dict()
                grade_status.append(grade_status_item)

        grading_type_conversion: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grading_type_conversion, Unset):
            grading_type_conversion = []
            for grading_type_conversion_item_data in self.grading_type_conversion:
                grading_type_conversion_item = grading_type_conversion_item_data.to_dict()
                grading_type_conversion.append(grading_type_conversion_item)

        grading_type_purpose: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grading_type_purpose, Unset):
            grading_type_purpose = self.grading_type_purpose.to_dict()

        grading_type_texts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grading_type_texts, Unset):
            grading_type_texts = []
            for grading_type_texts_item_data in self.grading_type_texts:
                grading_type_texts_item = grading_type_texts_item_data.to_dict()
                grading_type_texts.append(grading_type_texts_item)

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        lower_limit = self.lower_limit

        obj_guid = self.obj_guid

        regular_expression = self.regular_expression

        remarks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remarks, Unset):
            remarks = []
            for remarks_item_data in self.remarks:
                remarks_item = remarks_item_data.to_dict()
                remarks.append(remarks_item)

        rounding_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rounding_method, Unset):
            rounding_method = self.rounding_method.to_dict()

        rounding_position = self.rounding_position

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        type_of_grading = self.type_of_grading

        uniquename = self.uniquename

        upper_limit = self.upper_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
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
        if text is not UNSET:
            field_dict["text"] = text
        if type_of_grading is not UNSET:
            field_dict["typeOfGrading"] = type_of_grading
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if upper_limit is not UNSET:
            field_dict["upperLimit"] = upper_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iface_grade_to_status_adapter import IfaceGradeToStatusAdapter  # noqa: PLC0415
        from ..models.iface_grading_type_conversion_adapter import IfaceGradingTypeConversionAdapter  # noqa: PLC0415
        from ..models.iface_grading_type_country_adapter import IfaceGradingTypeCountryAdapter  # noqa: PLC0415
        from ..models.iface_grading_type_purpose import IfaceGradingTypePurpose  # noqa: PLC0415
        from ..models.iface_grading_type_text_adapter import IfaceGradingTypeTextAdapter  # noqa: PLC0415
        from ..models.iface_remark_to_status_adapter import IfaceRemarkToStatusAdapter  # noqa: PLC0415
        from ..models.iface_rounding_method import IfaceRoundingMethod  # noqa: PLC0415
        from ..models.impl_grading_type_impl_foreigntext import ImplGradingTypeImplForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplGradingTypeImplForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplGradingTypeImplForeigntext.from_dict(_field_foreigntext)

        allowed_values = d.pop("allowedValues", UNSET)

        allowed_values_as_list = cast(list[float], d.pop("allowedValuesAsList", UNSET))

        _country = d.pop("country", UNSET)
        country: list[IfaceGradingTypeCountryAdapter] | Unset = UNSET
        if _country is not UNSET:
            country = []
            for country_item_data in _country:
                country_item = IfaceGradingTypeCountryAdapter.from_dict(country_item_data)

                country.append(country_item)

        credits_threshold = d.pop("creditsThreshold", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        _grade_status = d.pop("gradeStatus", UNSET)
        grade_status: list[IfaceGradeToStatusAdapter] | Unset = UNSET
        if _grade_status is not UNSET:
            grade_status = []
            for grade_status_item_data in _grade_status:
                grade_status_item = IfaceGradeToStatusAdapter.from_dict(grade_status_item_data)

                grade_status.append(grade_status_item)

        _grading_type_conversion = d.pop("gradingTypeConversion", UNSET)
        grading_type_conversion: list[IfaceGradingTypeConversionAdapter] | Unset = UNSET
        if _grading_type_conversion is not UNSET:
            grading_type_conversion = []
            for grading_type_conversion_item_data in _grading_type_conversion:
                grading_type_conversion_item = IfaceGradingTypeConversionAdapter.from_dict(
                    grading_type_conversion_item_data
                )

                grading_type_conversion.append(grading_type_conversion_item)

        _grading_type_purpose = d.pop("gradingTypePurpose", UNSET)
        grading_type_purpose: IfaceGradingTypePurpose | Unset
        if isinstance(_grading_type_purpose, Unset):
            grading_type_purpose = UNSET
        else:
            grading_type_purpose = IfaceGradingTypePurpose.from_dict(_grading_type_purpose)

        _grading_type_texts = d.pop("gradingTypeTexts", UNSET)
        grading_type_texts: list[IfaceGradingTypeTextAdapter] | Unset = UNSET
        if _grading_type_texts is not UNSET:
            grading_type_texts = []
            for grading_type_texts_item_data in _grading_type_texts:
                grading_type_texts_item = IfaceGradingTypeTextAdapter.from_dict(grading_type_texts_item_data)

                grading_type_texts.append(grading_type_texts_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        lower_limit = d.pop("lowerLimit", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        regular_expression = d.pop("regularExpression", UNSET)

        _remarks = d.pop("remarks", UNSET)
        remarks: list[IfaceRemarkToStatusAdapter] | Unset = UNSET
        if _remarks is not UNSET:
            remarks = []
            for remarks_item_data in _remarks:
                remarks_item = IfaceRemarkToStatusAdapter.from_dict(remarks_item_data)

                remarks.append(remarks_item)

        _rounding_method = d.pop("roundingMethod", UNSET)
        rounding_method: IfaceRoundingMethod | Unset
        if isinstance(_rounding_method, Unset):
            rounding_method = UNSET
        else:
            rounding_method = IfaceRoundingMethod.from_dict(_rounding_method)

        rounding_position = d.pop("roundingPosition", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        type_of_grading = d.pop("typeOfGrading", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        upper_limit = d.pop("upperLimit", UNSET)

        impl_grading_type_impl = cls(
            field_foreigntext=field_foreigntext,
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
            text=text,
            type_of_grading=type_of_grading,
            uniquename=uniquename,
            upper_limit=upper_limit,
        )

        impl_grading_type_impl.additional_properties = d
        return impl_grading_type_impl

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
