from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_organization_to_import import (
        FsResPublicationUniversalImportOrganizationToImport,
    )
    from ..models.fs_res_publication_universal_import_personal_data import FsResPublicationUniversalImportPersonalData
    from ..models.fs_res_publication_universal_import_simple_person_identifier import (
        FsResPublicationUniversalImportSimplePersonIdentifier,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportCreatorToImport")


@_attrs_define
class FsResPublicationUniversalImportCreatorToImport:
    """
    Attributes:
        affiliations (list[FsResPublicationUniversalImportOrganizationToImport] | Unset):
        creatorname (str | Unset):
        firstname (str | Unset):
        nameprefix (str | Unset):
        namesuffix (str | Unset):
        person (FsResPublicationUniversalImportPersonalData | Unset):
        person_identifiers (list[FsResPublicationUniversalImportSimplePersonIdentifier] | Unset):
    """

    affiliations: list[FsResPublicationUniversalImportOrganizationToImport] | Unset = UNSET
    creatorname: str | Unset = UNSET
    firstname: str | Unset = UNSET
    nameprefix: str | Unset = UNSET
    namesuffix: str | Unset = UNSET
    person: FsResPublicationUniversalImportPersonalData | Unset = UNSET
    person_identifiers: list[FsResPublicationUniversalImportSimplePersonIdentifier] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        affiliations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.affiliations, Unset):
            affiliations = []
            for affiliations_item_data in self.affiliations:
                affiliations_item = affiliations_item_data.to_dict()
                affiliations.append(affiliations_item)

        creatorname = self.creatorname

        firstname = self.firstname

        nameprefix = self.nameprefix

        namesuffix = self.namesuffix

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        person_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.person_identifiers, Unset):
            person_identifiers = []
            for person_identifiers_item_data in self.person_identifiers:
                person_identifiers_item = person_identifiers_item_data.to_dict()
                person_identifiers.append(person_identifiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affiliations is not UNSET:
            field_dict["affiliations"] = affiliations
        if creatorname is not UNSET:
            field_dict["creatorname"] = creatorname
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if nameprefix is not UNSET:
            field_dict["nameprefix"] = nameprefix
        if namesuffix is not UNSET:
            field_dict["namesuffix"] = namesuffix
        if person is not UNSET:
            field_dict["person"] = person
        if person_identifiers is not UNSET:
            field_dict["personIdentifiers"] = person_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_organization_to_import import (
            FsResPublicationUniversalImportOrganizationToImport,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_personal_data import (
            FsResPublicationUniversalImportPersonalData,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_simple_person_identifier import (
            FsResPublicationUniversalImportSimplePersonIdentifier,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _affiliations = d.pop("affiliations", UNSET)
        affiliations: list[FsResPublicationUniversalImportOrganizationToImport] | Unset = UNSET
        if _affiliations is not UNSET:
            affiliations = []
            for affiliations_item_data in _affiliations:
                affiliations_item = FsResPublicationUniversalImportOrganizationToImport.from_dict(
                    affiliations_item_data
                )

                affiliations.append(affiliations_item)

        creatorname = d.pop("creatorname", UNSET)

        firstname = d.pop("firstname", UNSET)

        nameprefix = d.pop("nameprefix", UNSET)

        namesuffix = d.pop("namesuffix", UNSET)

        _person = d.pop("person", UNSET)
        person: FsResPublicationUniversalImportPersonalData | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = FsResPublicationUniversalImportPersonalData.from_dict(_person)

        _person_identifiers = d.pop("personIdentifiers", UNSET)
        person_identifiers: list[FsResPublicationUniversalImportSimplePersonIdentifier] | Unset = UNSET
        if _person_identifiers is not UNSET:
            person_identifiers = []
            for person_identifiers_item_data in _person_identifiers:
                person_identifiers_item = FsResPublicationUniversalImportSimplePersonIdentifier.from_dict(
                    person_identifiers_item_data
                )

                person_identifiers.append(person_identifiers_item)

        fs_res_publication_universal_import_creator_to_import = cls(
            affiliations=affiliations,
            creatorname=creatorname,
            firstname=firstname,
            nameprefix=nameprefix,
            namesuffix=namesuffix,
            person=person,
            person_identifiers=person_identifiers,
        )

        fs_res_publication_universal_import_creator_to_import.additional_properties = d
        return fs_res_publication_universal_import_creator_to_import

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
