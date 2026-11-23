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
    from ..models.fs_res_publication_universal_import_simple_global_identifier import (
        FsResPublicationUniversalImportSimpleGlobalIdentifier,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportOrganizationToImport")


@_attrs_define
class FsResPublicationUniversalImportOrganizationToImport:
    """
    Attributes:
        city (str | Unset):
        country (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        defaulttext (str | Unset):
        identifiers (list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset):
        orgunit_id (int | Unset):
        research_partner_id (int | Unset):
    """

    city: str | Unset = UNSET
    country: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    defaulttext: str | Unset = UNSET
    identifiers: list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset = UNSET
    orgunit_id: int | Unset = UNSET
    research_partner_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        defaulttext = self.defaulttext

        identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        orgunit_id = self.orgunit_id

        research_partner_id = self.research_partner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if orgunit_id is not UNSET:
            field_dict["orgunitId"] = orgunit_id
        if research_partner_id is not UNSET:
            field_dict["researchPartnerId"] = research_partner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_simple_generic_value import (
            FsResPublicationUniversalImportSimpleGenericValue,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_simple_global_identifier import (
            FsResPublicationUniversalImportSimpleGlobalIdentifier,  # noqa: PLC0415
        )

        d = dict(src_dict)
        city = d.pop("city", UNSET)

        _country = d.pop("country", UNSET)
        country: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_country)

        defaulttext = d.pop("defaulttext", UNSET)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset = UNSET
        if _identifiers is not UNSET:
            identifiers = []
            for identifiers_item_data in _identifiers:
                identifiers_item = FsResPublicationUniversalImportSimpleGlobalIdentifier.from_dict(
                    identifiers_item_data
                )

                identifiers.append(identifiers_item)

        orgunit_id = d.pop("orgunitId", UNSET)

        research_partner_id = d.pop("researchPartnerId", UNSET)

        fs_res_publication_universal_import_organization_to_import = cls(
            city=city,
            country=country,
            defaulttext=defaulttext,
            identifiers=identifiers,
            orgunit_id=orgunit_id,
            research_partner_id=research_partner_id,
        )

        fs_res_publication_universal_import_organization_to_import.additional_properties = d
        return fs_res_publication_universal_import_organization_to_import

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
