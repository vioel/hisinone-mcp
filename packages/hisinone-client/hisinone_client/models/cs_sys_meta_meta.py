from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_meta_field_metadata import CsSysMetaFieldMetadata


T = TypeVar("T", bound="CsSysMetaMeta")


@_attrs_define
class CsSysMetaMeta:
    """
    Attributes:
        identifier (str | Unset):
        mandatory (CsSysMetaFieldMetadata | Unset):
        remark (str | Unset):
        standard (CsSysMetaFieldMetadata | Unset):
    """

    identifier: str | Unset = UNSET
    mandatory: CsSysMetaFieldMetadata | Unset = UNSET
    remark: str | Unset = UNSET
    standard: CsSysMetaFieldMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        mandatory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mandatory, Unset):
            mandatory = self.mandatory.to_dict()

        remark = self.remark

        standard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.standard, Unset):
            standard = self.standard.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if remark is not UNSET:
            field_dict["remark"] = remark
        if standard is not UNSET:
            field_dict["standard"] = standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_meta_field_metadata import CsSysMetaFieldMetadata  # noqa: PLC0415

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        _mandatory = d.pop("mandatory", UNSET)
        mandatory: CsSysMetaFieldMetadata | Unset
        if isinstance(_mandatory, Unset):
            mandatory = UNSET
        else:
            mandatory = CsSysMetaFieldMetadata.from_dict(_mandatory)

        remark = d.pop("remark", UNSET)

        _standard = d.pop("standard", UNSET)
        standard: CsSysMetaFieldMetadata | Unset
        if isinstance(_standard, Unset):
            standard = UNSET
        else:
            standard = CsSysMetaFieldMetadata.from_dict(_standard)

        cs_sys_meta_meta = cls(
            identifier=identifier,
            mandatory=mandatory,
            remark=remark,
            standard=standard,
        )

        cs_sys_meta_meta.additional_properties = d
        return cs_sys_meta_meta

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
