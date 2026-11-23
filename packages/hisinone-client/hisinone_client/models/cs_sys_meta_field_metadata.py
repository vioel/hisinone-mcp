from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_meta_field_metadata_datatype import CsSysMetaFieldMetadataDatatype
    from ..models.cs_sys_meta_field_metadata_meta_infos import CsSysMetaFieldMetadataMetaInfos


T = TypeVar("T", bound="CsSysMetaFieldMetadata")


@_attrs_define
class CsSysMetaFieldMetadata:
    """
    Attributes:
        datatype (CsSysMetaFieldMetadataDatatype | Unset):
        default_value (str | Unset):
        empty (bool | Unset):
        empty_validation (bool | Unset):
        helptext_identifier (str | Unset):
        hidden (bool | Unset):
        identifier (str | Unset):
        labeltext_identifier (str | Unset):
        max_length (int | Unset):
        max_value_date (int | Unset):
        max_value_double (float | Unset):
        max_value_integer (int | Unset):
        meta_infos (list[CsSysMetaFieldMetadataMetaInfos] | Unset):
        min_length (int | Unset):
        min_value_date (int | Unset):
        min_value_double (float | Unset):
        min_value_integer (int | Unset):
        readonly (bool | Unset):
        regex_errortext_identifier (str | Unset):
        regex_pattern (str | Unset):
        required (bool | Unset):
        validation_method (str | Unset):
        validation_method_errortext_identifier (str | Unset):
    """

    datatype: CsSysMetaFieldMetadataDatatype | Unset = UNSET
    default_value: str | Unset = UNSET
    empty: bool | Unset = UNSET
    empty_validation: bool | Unset = UNSET
    helptext_identifier: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    labeltext_identifier: str | Unset = UNSET
    max_length: int | Unset = UNSET
    max_value_date: int | Unset = UNSET
    max_value_double: float | Unset = UNSET
    max_value_integer: int | Unset = UNSET
    meta_infos: list[CsSysMetaFieldMetadataMetaInfos] | Unset = UNSET
    min_length: int | Unset = UNSET
    min_value_date: int | Unset = UNSET
    min_value_double: float | Unset = UNSET
    min_value_integer: int | Unset = UNSET
    readonly: bool | Unset = UNSET
    regex_errortext_identifier: str | Unset = UNSET
    regex_pattern: str | Unset = UNSET
    required: bool | Unset = UNSET
    validation_method: str | Unset = UNSET
    validation_method_errortext_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        datatype: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datatype, Unset):
            datatype = self.datatype.to_dict()

        default_value = self.default_value

        empty = self.empty

        empty_validation = self.empty_validation

        helptext_identifier = self.helptext_identifier

        hidden = self.hidden

        identifier = self.identifier

        labeltext_identifier = self.labeltext_identifier

        max_length = self.max_length

        max_value_date = self.max_value_date

        max_value_double = self.max_value_double

        max_value_integer = self.max_value_integer

        meta_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.meta_infos, Unset):
            meta_infos = []
            for meta_infos_item_data in self.meta_infos:
                meta_infos_item = meta_infos_item_data.to_dict()
                meta_infos.append(meta_infos_item)

        min_length = self.min_length

        min_value_date = self.min_value_date

        min_value_double = self.min_value_double

        min_value_integer = self.min_value_integer

        readonly = self.readonly

        regex_errortext_identifier = self.regex_errortext_identifier

        regex_pattern = self.regex_pattern

        required = self.required

        validation_method = self.validation_method

        validation_method_errortext_identifier = self.validation_method_errortext_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datatype is not UNSET:
            field_dict["datatype"] = datatype
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if empty is not UNSET:
            field_dict["empty"] = empty
        if empty_validation is not UNSET:
            field_dict["emptyValidation"] = empty_validation
        if helptext_identifier is not UNSET:
            field_dict["helptextIdentifier"] = helptext_identifier
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if labeltext_identifier is not UNSET:
            field_dict["labeltextIdentifier"] = labeltext_identifier
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if max_value_date is not UNSET:
            field_dict["maxValueDate"] = max_value_date
        if max_value_double is not UNSET:
            field_dict["maxValueDouble"] = max_value_double
        if max_value_integer is not UNSET:
            field_dict["maxValueInteger"] = max_value_integer
        if meta_infos is not UNSET:
            field_dict["metaInfos"] = meta_infos
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if min_value_date is not UNSET:
            field_dict["minValueDate"] = min_value_date
        if min_value_double is not UNSET:
            field_dict["minValueDouble"] = min_value_double
        if min_value_integer is not UNSET:
            field_dict["minValueInteger"] = min_value_integer
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if regex_errortext_identifier is not UNSET:
            field_dict["regexErrortextIdentifier"] = regex_errortext_identifier
        if regex_pattern is not UNSET:
            field_dict["regexPattern"] = regex_pattern
        if required is not UNSET:
            field_dict["required"] = required
        if validation_method is not UNSET:
            field_dict["validationMethod"] = validation_method
        if validation_method_errortext_identifier is not UNSET:
            field_dict["validationMethodErrortextIdentifier"] = validation_method_errortext_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_meta_field_metadata_datatype import CsSysMetaFieldMetadataDatatype  # noqa: PLC0415
        from ..models.cs_sys_meta_field_metadata_meta_infos import CsSysMetaFieldMetadataMetaInfos  # noqa: PLC0415

        d = dict(src_dict)
        _datatype = d.pop("datatype", UNSET)
        datatype: CsSysMetaFieldMetadataDatatype | Unset
        if isinstance(_datatype, Unset):
            datatype = UNSET
        else:
            datatype = CsSysMetaFieldMetadataDatatype.from_dict(_datatype)

        default_value = d.pop("defaultValue", UNSET)

        empty = d.pop("empty", UNSET)

        empty_validation = d.pop("emptyValidation", UNSET)

        helptext_identifier = d.pop("helptextIdentifier", UNSET)

        hidden = d.pop("hidden", UNSET)

        identifier = d.pop("identifier", UNSET)

        labeltext_identifier = d.pop("labeltextIdentifier", UNSET)

        max_length = d.pop("maxLength", UNSET)

        max_value_date = d.pop("maxValueDate", UNSET)

        max_value_double = d.pop("maxValueDouble", UNSET)

        max_value_integer = d.pop("maxValueInteger", UNSET)

        _meta_infos = d.pop("metaInfos", UNSET)
        meta_infos: list[CsSysMetaFieldMetadataMetaInfos] | Unset = UNSET
        if _meta_infos is not UNSET:
            meta_infos = []
            for meta_infos_item_data in _meta_infos:
                meta_infos_item = CsSysMetaFieldMetadataMetaInfos.from_dict(meta_infos_item_data)

                meta_infos.append(meta_infos_item)

        min_length = d.pop("minLength", UNSET)

        min_value_date = d.pop("minValueDate", UNSET)

        min_value_double = d.pop("minValueDouble", UNSET)

        min_value_integer = d.pop("minValueInteger", UNSET)

        readonly = d.pop("readonly", UNSET)

        regex_errortext_identifier = d.pop("regexErrortextIdentifier", UNSET)

        regex_pattern = d.pop("regexPattern", UNSET)

        required = d.pop("required", UNSET)

        validation_method = d.pop("validationMethod", UNSET)

        validation_method_errortext_identifier = d.pop("validationMethodErrortextIdentifier", UNSET)

        cs_sys_meta_field_metadata = cls(
            datatype=datatype,
            default_value=default_value,
            empty=empty,
            empty_validation=empty_validation,
            helptext_identifier=helptext_identifier,
            hidden=hidden,
            identifier=identifier,
            labeltext_identifier=labeltext_identifier,
            max_length=max_length,
            max_value_date=max_value_date,
            max_value_double=max_value_double,
            max_value_integer=max_value_integer,
            meta_infos=meta_infos,
            min_length=min_length,
            min_value_date=min_value_date,
            min_value_double=min_value_double,
            min_value_integer=min_value_integer,
            readonly=readonly,
            regex_errortext_identifier=regex_errortext_identifier,
            regex_pattern=regex_pattern,
            required=required,
            validation_method=validation_method,
            validation_method_errortext_identifier=validation_method_errortext_identifier,
        )

        cs_sys_meta_field_metadata.additional_properties = d
        return cs_sys_meta_field_metadata

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
