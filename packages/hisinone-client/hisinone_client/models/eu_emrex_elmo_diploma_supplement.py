from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_diploma_supplement_section import EuEmrexElmoDiplomaSupplementSection
    from ..models.eu_emrex_elmo_signature_type import EuEmrexElmoSignatureType
    from ..models.java_lang_object import JavaLangObject
    from ..models.java_util_calendar import JavaUtilCalendar


T = TypeVar("T", bound="EuEmrexElmoDiplomaSupplement")


@_attrs_define
class EuEmrexElmoDiplomaSupplement:
    """
    Attributes:
        introduction (JavaLangObject | Unset):
        issue_date (JavaUtilCalendar | Unset):
        lang (str | Unset):
        section (list[EuEmrexElmoDiplomaSupplementSection] | Unset):
        signature (EuEmrexElmoSignatureType | Unset):
        version (str | Unset):
    """

    introduction: JavaLangObject | Unset = UNSET
    issue_date: JavaUtilCalendar | Unset = UNSET
    lang: str | Unset = UNSET
    section: list[EuEmrexElmoDiplomaSupplementSection] | Unset = UNSET
    signature: EuEmrexElmoSignatureType | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        introduction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.introduction, Unset):
            introduction = self.introduction.to_dict()

        issue_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.to_dict()

        lang = self.lang

        section: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.section, Unset):
            section = []
            for section_item_data in self.section:
                section_item = section_item_data.to_dict()
                section.append(section_item)

        signature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if introduction is not UNSET:
            field_dict["introduction"] = introduction
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if lang is not UNSET:
            field_dict["lang"] = lang
        if section is not UNSET:
            field_dict["section"] = section
        if signature is not UNSET:
            field_dict["signature"] = signature
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_diploma_supplement_section import EuEmrexElmoDiplomaSupplementSection  # noqa: PLC0415
        from ..models.eu_emrex_elmo_signature_type import EuEmrexElmoSignatureType  # noqa: PLC0415
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415
        from ..models.java_util_calendar import JavaUtilCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _introduction = d.pop("introduction", UNSET)
        introduction: JavaLangObject | Unset
        if isinstance(_introduction, Unset):
            introduction = UNSET
        else:
            introduction = JavaLangObject.from_dict(_introduction)

        _issue_date = d.pop("issueDate", UNSET)
        issue_date: JavaUtilCalendar | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = JavaUtilCalendar.from_dict(_issue_date)

        lang = d.pop("lang", UNSET)

        _section = d.pop("section", UNSET)
        section: list[EuEmrexElmoDiplomaSupplementSection] | Unset = UNSET
        if _section is not UNSET:
            section = []
            for section_item_data in _section:
                section_item = EuEmrexElmoDiplomaSupplementSection.from_dict(section_item_data)

                section.append(section_item)

        _signature = d.pop("signature", UNSET)
        signature: EuEmrexElmoSignatureType | Unset
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = EuEmrexElmoSignatureType.from_dict(_signature)

        version = d.pop("version", UNSET)

        eu_emrex_elmo_diploma_supplement = cls(
            introduction=introduction,
            issue_date=issue_date,
            lang=lang,
            section=section,
            signature=signature,
            version=version,
        )

        eu_emrex_elmo_diploma_supplement.additional_properties = d
        return eu_emrex_elmo_diploma_supplement

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
