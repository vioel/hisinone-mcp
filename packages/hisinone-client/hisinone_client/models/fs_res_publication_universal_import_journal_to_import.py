from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_publisher_to_import import (
        FsResPublicationUniversalImportPublisherToImport,
    )
    from ..models.fs_res_publication_universal_import_simple_generic_value import (
        FsResPublicationUniversalImportSimpleGenericValue,
    )
    from ..models.fs_res_publication_universal_import_simple_global_identifier import (
        FsResPublicationUniversalImportSimpleGlobalIdentifier,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportJournalToImport")


@_attrs_define
class FsResPublicationUniversalImportJournalToImport:
    """
    Attributes:
        defaulttext (str | Unset):
        global_identifiers (list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset):
        language (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        obj_guid (str | Unset):
        peer_reviewed (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        peer_reviewed_begin (str | Unset):
        publisher (FsResPublicationUniversalImportPublisherToImport | Unset):
        shorttext (str | Unset):
        status (FsResPublicationUniversalImportSimpleGenericValue | Unset):
        subtitle (str | Unset):
        uniquename (str | Unset):
    """

    defaulttext: str | Unset = UNSET
    global_identifiers: list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset = UNSET
    language: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    obj_guid: str | Unset = UNSET
    peer_reviewed: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    peer_reviewed_begin: str | Unset = UNSET
    publisher: FsResPublicationUniversalImportPublisherToImport | Unset = UNSET
    shorttext: str | Unset = UNSET
    status: FsResPublicationUniversalImportSimpleGenericValue | Unset = UNSET
    subtitle: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defaulttext = self.defaulttext

        global_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_identifiers, Unset):
            global_identifiers = []
            for global_identifiers_item_data in self.global_identifiers:
                global_identifiers_item = global_identifiers_item_data.to_dict()
                global_identifiers.append(global_identifiers_item)

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        obj_guid = self.obj_guid

        peer_reviewed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.peer_reviewed, Unset):
            peer_reviewed = self.peer_reviewed.to_dict()

        peer_reviewed_begin = self.peer_reviewed_begin

        publisher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher.to_dict()

        shorttext = self.shorttext

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        subtitle = self.subtitle

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if global_identifiers is not UNSET:
            field_dict["globalIdentifiers"] = global_identifiers
        if language is not UNSET:
            field_dict["language"] = language
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if peer_reviewed is not UNSET:
            field_dict["peerReviewed"] = peer_reviewed
        if peer_reviewed_begin is not UNSET:
            field_dict["peerReviewedBegin"] = peer_reviewed_begin
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if status is not UNSET:
            field_dict["status"] = status
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_publisher_to_import import (
            FsResPublicationUniversalImportPublisherToImport,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_simple_generic_value import (
            FsResPublicationUniversalImportSimpleGenericValue,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_simple_global_identifier import (
            FsResPublicationUniversalImportSimpleGlobalIdentifier,  # noqa: PLC0415
        )

        d = dict(src_dict)
        defaulttext = d.pop("defaulttext", UNSET)

        _global_identifiers = d.pop("globalIdentifiers", UNSET)
        global_identifiers: list[FsResPublicationUniversalImportSimpleGlobalIdentifier] | Unset = UNSET
        if _global_identifiers is not UNSET:
            global_identifiers = []
            for global_identifiers_item_data in _global_identifiers:
                global_identifiers_item = FsResPublicationUniversalImportSimpleGlobalIdentifier.from_dict(
                    global_identifiers_item_data
                )

                global_identifiers.append(global_identifiers_item)

        _language = d.pop("language", UNSET)
        language: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_language)

        obj_guid = d.pop("objGuid", UNSET)

        _peer_reviewed = d.pop("peerReviewed", UNSET)
        peer_reviewed: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_peer_reviewed, Unset):
            peer_reviewed = UNSET
        else:
            peer_reviewed = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_peer_reviewed)

        peer_reviewed_begin = d.pop("peerReviewedBegin", UNSET)

        _publisher = d.pop("publisher", UNSET)
        publisher: FsResPublicationUniversalImportPublisherToImport | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = FsResPublicationUniversalImportPublisherToImport.from_dict(_publisher)

        shorttext = d.pop("shorttext", UNSET)

        _status = d.pop("status", UNSET)
        status: FsResPublicationUniversalImportSimpleGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FsResPublicationUniversalImportSimpleGenericValue.from_dict(_status)

        subtitle = d.pop("subtitle", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        fs_res_publication_universal_import_journal_to_import = cls(
            defaulttext=defaulttext,
            global_identifiers=global_identifiers,
            language=language,
            obj_guid=obj_guid,
            peer_reviewed=peer_reviewed,
            peer_reviewed_begin=peer_reviewed_begin,
            publisher=publisher,
            shorttext=shorttext,
            status=status,
            subtitle=subtitle,
            uniquename=uniquename,
        )

        fs_res_publication_universal_import_journal_to_import.additional_properties = d
        return fs_res_publication_universal_import_journal_to_import

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
