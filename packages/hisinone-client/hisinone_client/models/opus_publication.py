from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opus_author import OpusAuthor
    from ..models.opus_date import OpusDate
    from ..models.opus_files import OpusFiles
    from ..models.opus_identifier import OpusIdentifier
    from ..models.opus_keywords import OpusKeywords
    from ..models.opus_notes import OpusNotes
    from ..models.opus_title import OpusTitle


T = TypeVar("T", bound="OpusPublication")


@_attrs_define
class OpusPublication:
    """
    Attributes:
        abstracts (list[OpusTitle] | Unset):
        article_number (str | Unset):
        belongs_to_bibliography (bool | Unset):
        dates (list[OpusDate] | Unset):
        edition (str | Unset):
        files (list[OpusFiles] | Unset):
        his_id (int | Unset):
        identifiers (list[OpusIdentifier] | Unset):
        issue (str | Unset):
        keywords (list[OpusKeywords] | Unset):
        language (str | Unset):
        notes (list[OpusNotes] | Unset):
        page_first (str | Unset):
        page_last (str | Unset):
        page_number (str | Unset):
        persons (list[OpusAuthor] | Unset):
        publisher_name (str | Unset):
        publisher_place (str | Unset):
        titles (list[OpusTitle] | Unset):
        titles_main (list[OpusTitle] | Unset):
        type_ (str | Unset):
        volume (str | Unset):
    """

    abstracts: list[OpusTitle] | Unset = UNSET
    article_number: str | Unset = UNSET
    belongs_to_bibliography: bool | Unset = UNSET
    dates: list[OpusDate] | Unset = UNSET
    edition: str | Unset = UNSET
    files: list[OpusFiles] | Unset = UNSET
    his_id: int | Unset = UNSET
    identifiers: list[OpusIdentifier] | Unset = UNSET
    issue: str | Unset = UNSET
    keywords: list[OpusKeywords] | Unset = UNSET
    language: str | Unset = UNSET
    notes: list[OpusNotes] | Unset = UNSET
    page_first: str | Unset = UNSET
    page_last: str | Unset = UNSET
    page_number: str | Unset = UNSET
    persons: list[OpusAuthor] | Unset = UNSET
    publisher_name: str | Unset = UNSET
    publisher_place: str | Unset = UNSET
    titles: list[OpusTitle] | Unset = UNSET
    titles_main: list[OpusTitle] | Unset = UNSET
    type_: str | Unset = UNSET
    volume: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        abstracts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.abstracts, Unset):
            abstracts = []
            for abstracts_item_data in self.abstracts:
                abstracts_item = abstracts_item_data.to_dict()
                abstracts.append(abstracts_item)

        article_number = self.article_number

        belongs_to_bibliography = self.belongs_to_bibliography

        dates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.to_dict()
                dates.append(dates_item)

        edition = self.edition

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        his_id = self.his_id

        identifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()
                identifiers.append(identifiers_item)

        issue = self.issue

        keywords: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = []
            for keywords_item_data in self.keywords:
                keywords_item = keywords_item_data.to_dict()
                keywords.append(keywords_item)

        language = self.language

        notes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)

        page_first = self.page_first

        page_last = self.page_last

        page_number = self.page_number

        persons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.persons, Unset):
            persons = []
            for persons_item_data in self.persons:
                persons_item = persons_item_data.to_dict()
                persons.append(persons_item)

        publisher_name = self.publisher_name

        publisher_place = self.publisher_place

        titles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.titles, Unset):
            titles = []
            for titles_item_data in self.titles:
                titles_item = titles_item_data.to_dict()
                titles.append(titles_item)

        titles_main: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.titles_main, Unset):
            titles_main = []
            for titles_main_item_data in self.titles_main:
                titles_main_item = titles_main_item_data.to_dict()
                titles_main.append(titles_main_item)

        type_ = self.type_

        volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abstracts is not UNSET:
            field_dict["abstracts"] = abstracts
        if article_number is not UNSET:
            field_dict["articleNumber"] = article_number
        if belongs_to_bibliography is not UNSET:
            field_dict["belongsToBibliography"] = belongs_to_bibliography
        if dates is not UNSET:
            field_dict["dates"] = dates
        if edition is not UNSET:
            field_dict["edition"] = edition
        if files is not UNSET:
            field_dict["files"] = files
        if his_id is not UNSET:
            field_dict["hisId"] = his_id
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if issue is not UNSET:
            field_dict["issue"] = issue
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if language is not UNSET:
            field_dict["language"] = language
        if notes is not UNSET:
            field_dict["notes"] = notes
        if page_first is not UNSET:
            field_dict["pageFirst"] = page_first
        if page_last is not UNSET:
            field_dict["pageLast"] = page_last
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if persons is not UNSET:
            field_dict["persons"] = persons
        if publisher_name is not UNSET:
            field_dict["publisherName"] = publisher_name
        if publisher_place is not UNSET:
            field_dict["publisherPlace"] = publisher_place
        if titles is not UNSET:
            field_dict["titles"] = titles
        if titles_main is not UNSET:
            field_dict["titlesMain"] = titles_main
        if type_ is not UNSET:
            field_dict["type"] = type_
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opus_author import OpusAuthor  # noqa: PLC0415
        from ..models.opus_date import OpusDate  # noqa: PLC0415
        from ..models.opus_files import OpusFiles  # noqa: PLC0415
        from ..models.opus_identifier import OpusIdentifier  # noqa: PLC0415
        from ..models.opus_keywords import OpusKeywords  # noqa: PLC0415
        from ..models.opus_notes import OpusNotes  # noqa: PLC0415
        from ..models.opus_title import OpusTitle  # noqa: PLC0415

        d = dict(src_dict)
        _abstracts = d.pop("abstracts", UNSET)
        abstracts: list[OpusTitle] | Unset = UNSET
        if _abstracts is not UNSET:
            abstracts = []
            for abstracts_item_data in _abstracts:
                abstracts_item = OpusTitle.from_dict(abstracts_item_data)

                abstracts.append(abstracts_item)

        article_number = d.pop("articleNumber", UNSET)

        belongs_to_bibliography = d.pop("belongsToBibliography", UNSET)

        _dates = d.pop("dates", UNSET)
        dates: list[OpusDate] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = OpusDate.from_dict(dates_item_data)

                dates.append(dates_item)

        edition = d.pop("edition", UNSET)

        _files = d.pop("files", UNSET)
        files: list[OpusFiles] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = OpusFiles.from_dict(files_item_data)

                files.append(files_item)

        his_id = d.pop("hisId", UNSET)

        _identifiers = d.pop("identifiers", UNSET)
        identifiers: list[OpusIdentifier] | Unset = UNSET
        if _identifiers is not UNSET:
            identifiers = []
            for identifiers_item_data in _identifiers:
                identifiers_item = OpusIdentifier.from_dict(identifiers_item_data)

                identifiers.append(identifiers_item)

        issue = d.pop("issue", UNSET)

        _keywords = d.pop("keywords", UNSET)
        keywords: list[OpusKeywords] | Unset = UNSET
        if _keywords is not UNSET:
            keywords = []
            for keywords_item_data in _keywords:
                keywords_item = OpusKeywords.from_dict(keywords_item_data)

                keywords.append(keywords_item)

        language = d.pop("language", UNSET)

        _notes = d.pop("notes", UNSET)
        notes: list[OpusNotes] | Unset = UNSET
        if _notes is not UNSET:
            notes = []
            for notes_item_data in _notes:
                notes_item = OpusNotes.from_dict(notes_item_data)

                notes.append(notes_item)

        page_first = d.pop("pageFirst", UNSET)

        page_last = d.pop("pageLast", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        _persons = d.pop("persons", UNSET)
        persons: list[OpusAuthor] | Unset = UNSET
        if _persons is not UNSET:
            persons = []
            for persons_item_data in _persons:
                persons_item = OpusAuthor.from_dict(persons_item_data)

                persons.append(persons_item)

        publisher_name = d.pop("publisherName", UNSET)

        publisher_place = d.pop("publisherPlace", UNSET)

        _titles = d.pop("titles", UNSET)
        titles: list[OpusTitle] | Unset = UNSET
        if _titles is not UNSET:
            titles = []
            for titles_item_data in _titles:
                titles_item = OpusTitle.from_dict(titles_item_data)

                titles.append(titles_item)

        _titles_main = d.pop("titlesMain", UNSET)
        titles_main: list[OpusTitle] | Unset = UNSET
        if _titles_main is not UNSET:
            titles_main = []
            for titles_main_item_data in _titles_main:
                titles_main_item = OpusTitle.from_dict(titles_main_item_data)

                titles_main.append(titles_main_item)

        type_ = d.pop("type", UNSET)

        volume = d.pop("volume", UNSET)

        opus_publication = cls(
            abstracts=abstracts,
            article_number=article_number,
            belongs_to_bibliography=belongs_to_bibliography,
            dates=dates,
            edition=edition,
            files=files,
            his_id=his_id,
            identifiers=identifiers,
            issue=issue,
            keywords=keywords,
            language=language,
            notes=notes,
            page_first=page_first,
            page_last=page_last,
            page_number=page_number,
            persons=persons,
            publisher_name=publisher_name,
            publisher_place=publisher_place,
            titles=titles,
            titles_main=titles_main,
            type_=type_,
            volume=volume,
        )

        opus_publication.additional_properties = d
        return opus_publication

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
