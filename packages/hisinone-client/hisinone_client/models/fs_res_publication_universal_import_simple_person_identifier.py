from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_simple_generic_value import (
        FsResPublicationUniversalImportSimpleGenericValue,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportSimplePersonIdentifier")


@_attrs_define
class FsResPublicationUniversalImportSimplePersonIdentifier:
    """
    Attributes:
        identifier (str | Unset):
        identifier_type (FsResPublicationUniversalImportSimpleGenericValue | Unset):
    """

    identifier: str | Unset = UNSET
    identifier_type: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        identifier_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_type, Unset):
            identifier_type = self.identifier_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_type is not UNSET:
            field_dict["identifierType"] = identifier_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_simple_generic_value import (
            FsResPublicationUniversalImportSimpleGenericValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        _identifier_type = d.pop("identifierType", UNSET)
        identifier_type: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_identifier_type, Unset):
            identifier_type = UNSET
        else:
            identifier_type = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_identifier_type)

        fs_res_publication_universal_import_simple_person_identifier = cls(
            identifier=identifier,
            identifier_type=identifier_type,
        )

        fs_res_publication_universal_import_simple_person_identifier.additional_properties = d
        return fs_res_publication_universal_import_simple_person_identifier

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
