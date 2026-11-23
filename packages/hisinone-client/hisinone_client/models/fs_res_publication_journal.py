from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_publication_global_identifier import FsResPublicationGlobalIdentifier
    from ..models.fs_res_publication_journal_foreigntext import FsResPublicationJournalForeigntext
    from ..models.fs_res_publication_publisher import FsResPublicationPublisher
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResPublicationJournal")


@_attrs_define
class FsResPublicationJournal:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResPublicationJournalForeigntext | Unset):
        defaulttext (str | Unset):
        global_identifiers (list[FsResPublicationGlobalIdentifier] | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        peer_reviewed (CsSysValueGenericValue | Unset):
        peer_reviewed_begin (int | Unset):
        publisher (FsResPublicationPublisher | Unset):
        shorttext (str | Unset):
        status (CsSysValueGenericValue | Unset):
        subtitle (str | Unset):
        uniquename (str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResPublicationJournalForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    global_identifiers: list[FsResPublicationGlobalIdentifier] | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    peer_reviewed: CsSysValueGenericValue | Unset = UNSET
    peer_reviewed_begin: int | Unset = UNSET
    publisher: FsResPublicationPublisher | Unset = UNSET
    shorttext: str | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    subtitle: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        global_identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_identifiers, Unset):
            global_identifiers = []
            for global_identifiers_item_data in self.global_identifiers:
                global_identifiers_item = global_identifiers_item_data.to_dict()
                global_identifiers.append(global_identifiers_item)

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

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
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if global_identifiers is not UNSET:
            field_dict["globalIdentifiers"] = global_identifiers
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
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
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_global_identifier import FsResPublicationGlobalIdentifier  # noqa: PLC0415
        from ..models.fs_res_publication_journal_foreigntext import FsResPublicationJournalForeigntext  # noqa: PLC0415
        from ..models.fs_res_publication_publisher import FsResPublicationPublisher  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationJournalForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationJournalForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        _global_identifiers = d.pop("globalIdentifiers", UNSET)
        global_identifiers: list[FsResPublicationGlobalIdentifier] | Unset = UNSET
        if _global_identifiers is not UNSET:
            global_identifiers = []
            for global_identifiers_item_data in _global_identifiers:
                global_identifiers_item = FsResPublicationGlobalIdentifier.from_dict(global_identifiers_item_data)

                global_identifiers.append(global_identifiers_item)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _peer_reviewed = d.pop("peerReviewed", UNSET)
        peer_reviewed: CsSysValueGenericValue | Unset
        if isinstance(_peer_reviewed, Unset):
            peer_reviewed = UNSET
        else:
            peer_reviewed = CsSysValueGenericValue.from_dict(_peer_reviewed)

        peer_reviewed_begin = d.pop("peerReviewedBegin", UNSET)

        _publisher = d.pop("publisher", UNSET)
        publisher: FsResPublicationPublisher | Unset
        if isinstance(_publisher, Unset):
            publisher = UNSET
        else:
            publisher = FsResPublicationPublisher.from_dict(_publisher)

        shorttext = d.pop("shorttext", UNSET)

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        subtitle = d.pop("subtitle", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        fs_res_publication_journal = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            global_identifiers=global_identifiers,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            peer_reviewed=peer_reviewed,
            peer_reviewed_begin=peer_reviewed_begin,
            publisher=publisher,
            shorttext=shorttext,
            status=status,
            subtitle=subtitle,
            uniquename=uniquename,
        )

        fs_res_publication_journal.additional_properties = d
        return fs_res_publication_journal

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
