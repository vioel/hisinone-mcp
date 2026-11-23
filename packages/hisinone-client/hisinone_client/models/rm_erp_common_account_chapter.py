from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_chapter_foreigntext import RmErpCommonAccountChapterForeigntext


T = TypeVar("T", bound="RmErpCommonAccountChapter")


@_attrs_define
class RmErpCommonAccountChapter:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountChapterForeigntext | Unset):
        ast_number (str | Unset):
        chapter (str | Unset):
        chapter_description_long (str | Unset):
        chapter_description_short (str | Unset):
        defaulttext (str | Unset):
        gg_number (str | Unset):
        h_indicator (str | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        indicator_ueber (str | Unset):
        is_changed (bool | Unset):
        kz_vhhf (str | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        payment_method_bay (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        tax_nominal_actual (str | Unset):
        tax_separated (str | Unset):
        tax_title (str | Unset):
        text (str | Unset):
        type_ (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
        vwg (int | Unset):
        year (str | Unset):
    """

    field_foreigntext: RmErpCommonAccountChapterForeigntext | Unset = UNSET
    ast_number: str | Unset = UNSET
    chapter: str | Unset = UNSET
    chapter_description_long: str | Unset = UNSET
    chapter_description_short: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    gg_number: str | Unset = UNSET
    h_indicator: str | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    indicator_ueber: str | Unset = UNSET
    is_changed: bool | Unset = UNSET
    kz_vhhf: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    payment_method_bay: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    tax_nominal_actual: str | Unset = UNSET
    tax_separated: str | Unset = UNSET
    tax_title: str | Unset = UNSET
    text: str | Unset = UNSET
    type_: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    vwg: int | Unset = UNSET
    year: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        ast_number = self.ast_number

        chapter = self.chapter

        chapter_description_long = self.chapter_description_long

        chapter_description_short = self.chapter_description_short

        defaulttext = self.defaulttext

        gg_number = self.gg_number

        h_indicator = self.h_indicator

        hiskey_id = self.hiskey_id

        id = self.id

        indicator_ueber = self.indicator_ueber

        is_changed = self.is_changed

        kz_vhhf = self.kz_vhhf

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        payment_method_bay = self.payment_method_bay

        shorttext = self.shorttext

        sortorder = self.sortorder

        tax_nominal_actual = self.tax_nominal_actual

        tax_separated = self.tax_separated

        tax_title = self.tax_title

        text = self.text

        type_ = self.type_

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        vwg = self.vwg

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if ast_number is not UNSET:
            field_dict["astNumber"] = ast_number
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if chapter_description_long is not UNSET:
            field_dict["chapterDescriptionLong"] = chapter_description_long
        if chapter_description_short is not UNSET:
            field_dict["chapterDescriptionShort"] = chapter_description_short
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if gg_number is not UNSET:
            field_dict["ggNumber"] = gg_number
        if h_indicator is not UNSET:
            field_dict["hIndicator"] = h_indicator
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if indicator_ueber is not UNSET:
            field_dict["indicatorUeber"] = indicator_ueber
        if is_changed is not UNSET:
            field_dict["isChanged"] = is_changed
        if kz_vhhf is not UNSET:
            field_dict["kzVhhf"] = kz_vhhf
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if payment_method_bay is not UNSET:
            field_dict["paymentMethodBay"] = payment_method_bay
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if tax_nominal_actual is not UNSET:
            field_dict["taxNominalActual"] = tax_nominal_actual
        if tax_separated is not UNSET:
            field_dict["taxSeparated"] = tax_separated
        if tax_title is not UNSET:
            field_dict["taxTitle"] = tax_title
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if vwg is not UNSET:
            field_dict["vwg"] = vwg
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_chapter_foreigntext import RmErpCommonAccountChapterForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountChapterForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountChapterForeigntext.from_dict(_field_foreigntext)

        ast_number = d.pop("astNumber", UNSET)

        chapter = d.pop("chapter", UNSET)

        chapter_description_long = d.pop("chapterDescriptionLong", UNSET)

        chapter_description_short = d.pop("chapterDescriptionShort", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        gg_number = d.pop("ggNumber", UNSET)

        h_indicator = d.pop("hIndicator", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        indicator_ueber = d.pop("indicatorUeber", UNSET)

        is_changed = d.pop("isChanged", UNSET)

        kz_vhhf = d.pop("kzVhhf", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        payment_method_bay = d.pop("paymentMethodBay", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        tax_nominal_actual = d.pop("taxNominalActual", UNSET)

        tax_separated = d.pop("taxSeparated", UNSET)

        tax_title = d.pop("taxTitle", UNSET)

        text = d.pop("text", UNSET)

        type_ = d.pop("type", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        vwg = d.pop("vwg", UNSET)

        year = d.pop("year", UNSET)

        rm_erp_common_account_chapter = cls(
            field_foreigntext=field_foreigntext,
            ast_number=ast_number,
            chapter=chapter,
            chapter_description_long=chapter_description_long,
            chapter_description_short=chapter_description_short,
            defaulttext=defaulttext,
            gg_number=gg_number,
            h_indicator=h_indicator,
            hiskey_id=hiskey_id,
            id=id,
            indicator_ueber=indicator_ueber,
            is_changed=is_changed,
            kz_vhhf=kz_vhhf,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            payment_method_bay=payment_method_bay,
            shorttext=shorttext,
            sortorder=sortorder,
            tax_nominal_actual=tax_nominal_actual,
            tax_separated=tax_separated,
            tax_title=tax_title,
            text=text,
            type_=type_,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
            vwg=vwg,
            year=year,
        )

        rm_erp_common_account_chapter.additional_properties = d
        return rm_erp_common_account_chapter

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
