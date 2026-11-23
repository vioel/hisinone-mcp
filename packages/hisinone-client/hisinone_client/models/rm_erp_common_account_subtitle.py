from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_subtitle_foreigntext import RmErpCommonAccountSubtitleForeigntext


T = TypeVar("T", bound="RmErpCommonAccountSubtitle")


@_attrs_define
class RmErpCommonAccountSubtitle:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountSubtitleForeigntext | Unset):
        akts (float | Unset):
        ausz (float | Unset):
        chapter (str | Unset):
        cover_ring_hierarchy_level_one (str | Unset):
        cover_ring_hierarchy_level_two (str | Unset):
        cover_ring_kor (str | Unset):
        defaulttext (str | Unset):
        dtgr (int | Unset):
        ein (float | Unset):
        fest (float | Unset):
        financial_stat (str | Unset):
        hhans (float | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        indicator_ueber (str | Unset):
        is_changed (bool | Unset):
        korr_indicator (str | Unset):
        lock (float | Unset):
        lock_indicator (str | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        mwpf (str | Unset):
        o_number (str | Unset):
        obj_guid (str | Unset):
        remains (float | Unset):
        shorttext (str | Unset):
        soll (float | Unset):
        soll_kontr (str | Unset):
        sortorder (int | Unset):
        subtitle (str | Unset):
        subtitle_description (str | Unset):
        text (str | Unset):
        title (str | Unset):
        title_kor (str | Unset):
        type_ (str | Unset):
        undertitle_kor (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
        verfkor (float | Unset):
        vojs (float | Unset):
        vwg (int | Unset):
        year (str | Unset):
        zvert (float | Unset):
    """

    field_foreigntext: RmErpCommonAccountSubtitleForeigntext | Unset = UNSET
    akts: float | Unset = UNSET
    ausz: float | Unset = UNSET
    chapter: str | Unset = UNSET
    cover_ring_hierarchy_level_one: str | Unset = UNSET
    cover_ring_hierarchy_level_two: str | Unset = UNSET
    cover_ring_kor: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    dtgr: int | Unset = UNSET
    ein: float | Unset = UNSET
    fest: float | Unset = UNSET
    financial_stat: str | Unset = UNSET
    hhans: float | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    indicator_ueber: str | Unset = UNSET
    is_changed: bool | Unset = UNSET
    korr_indicator: str | Unset = UNSET
    lock: float | Unset = UNSET
    lock_indicator: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    mwpf: str | Unset = UNSET
    o_number: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    remains: float | Unset = UNSET
    shorttext: str | Unset = UNSET
    soll: float | Unset = UNSET
    soll_kontr: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    subtitle: str | Unset = UNSET
    subtitle_description: str | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    title_kor: str | Unset = UNSET
    type_: str | Unset = UNSET
    undertitle_kor: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    verfkor: float | Unset = UNSET
    vojs: float | Unset = UNSET
    vwg: int | Unset = UNSET
    year: str | Unset = UNSET
    zvert: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        akts = self.akts

        ausz = self.ausz

        chapter = self.chapter

        cover_ring_hierarchy_level_one = self.cover_ring_hierarchy_level_one

        cover_ring_hierarchy_level_two = self.cover_ring_hierarchy_level_two

        cover_ring_kor = self.cover_ring_kor

        defaulttext = self.defaulttext

        dtgr = self.dtgr

        ein = self.ein

        fest = self.fest

        financial_stat = self.financial_stat

        hhans = self.hhans

        hiskey_id = self.hiskey_id

        id = self.id

        indicator_ueber = self.indicator_ueber

        is_changed = self.is_changed

        korr_indicator = self.korr_indicator

        lock = self.lock

        lock_indicator = self.lock_indicator

        lock_version = self.lock_version

        longtext = self.longtext

        mwpf = self.mwpf

        o_number = self.o_number

        obj_guid = self.obj_guid

        remains = self.remains

        shorttext = self.shorttext

        soll = self.soll

        soll_kontr = self.soll_kontr

        sortorder = self.sortorder

        subtitle = self.subtitle

        subtitle_description = self.subtitle_description

        text = self.text

        title = self.title

        title_kor = self.title_kor

        type_ = self.type_

        undertitle_kor = self.undertitle_kor

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        verfkor = self.verfkor

        vojs = self.vojs

        vwg = self.vwg

        year = self.year

        zvert = self.zvert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if akts is not UNSET:
            field_dict["akts"] = akts
        if ausz is not UNSET:
            field_dict["ausz"] = ausz
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if cover_ring_hierarchy_level_one is not UNSET:
            field_dict["coverRingHierarchyLevelOne"] = cover_ring_hierarchy_level_one
        if cover_ring_hierarchy_level_two is not UNSET:
            field_dict["coverRingHierarchyLevelTwo"] = cover_ring_hierarchy_level_two
        if cover_ring_kor is not UNSET:
            field_dict["coverRingKor"] = cover_ring_kor
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if dtgr is not UNSET:
            field_dict["dtgr"] = dtgr
        if ein is not UNSET:
            field_dict["ein"] = ein
        if fest is not UNSET:
            field_dict["fest"] = fest
        if financial_stat is not UNSET:
            field_dict["financialStat"] = financial_stat
        if hhans is not UNSET:
            field_dict["hhans"] = hhans
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if indicator_ueber is not UNSET:
            field_dict["indicatorUeber"] = indicator_ueber
        if is_changed is not UNSET:
            field_dict["isChanged"] = is_changed
        if korr_indicator is not UNSET:
            field_dict["korrIndicator"] = korr_indicator
        if lock is not UNSET:
            field_dict["lock"] = lock
        if lock_indicator is not UNSET:
            field_dict["lockIndicator"] = lock_indicator
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if mwpf is not UNSET:
            field_dict["mwpf"] = mwpf
        if o_number is not UNSET:
            field_dict["oNumber"] = o_number
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if remains is not UNSET:
            field_dict["remains"] = remains
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if soll is not UNSET:
            field_dict["soll"] = soll
        if soll_kontr is not UNSET:
            field_dict["sollKontr"] = soll_kontr
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if subtitle_description is not UNSET:
            field_dict["subtitleDescription"] = subtitle_description
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if title_kor is not UNSET:
            field_dict["titleKor"] = title_kor
        if type_ is not UNSET:
            field_dict["type"] = type_
        if undertitle_kor is not UNSET:
            field_dict["undertitleKor"] = undertitle_kor
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if verfkor is not UNSET:
            field_dict["verfkor"] = verfkor
        if vojs is not UNSET:
            field_dict["vojs"] = vojs
        if vwg is not UNSET:
            field_dict["vwg"] = vwg
        if year is not UNSET:
            field_dict["year"] = year
        if zvert is not UNSET:
            field_dict["zvert"] = zvert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_subtitle_foreigntext import RmErpCommonAccountSubtitleForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountSubtitleForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountSubtitleForeigntext.from_dict(_field_foreigntext)

        akts = d.pop("akts", UNSET)

        ausz = d.pop("ausz", UNSET)

        chapter = d.pop("chapter", UNSET)

        cover_ring_hierarchy_level_one = d.pop("coverRingHierarchyLevelOne", UNSET)

        cover_ring_hierarchy_level_two = d.pop("coverRingHierarchyLevelTwo", UNSET)

        cover_ring_kor = d.pop("coverRingKor", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        dtgr = d.pop("dtgr", UNSET)

        ein = d.pop("ein", UNSET)

        fest = d.pop("fest", UNSET)

        financial_stat = d.pop("financialStat", UNSET)

        hhans = d.pop("hhans", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        indicator_ueber = d.pop("indicatorUeber", UNSET)

        is_changed = d.pop("isChanged", UNSET)

        korr_indicator = d.pop("korrIndicator", UNSET)

        lock = d.pop("lock", UNSET)

        lock_indicator = d.pop("lockIndicator", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        mwpf = d.pop("mwpf", UNSET)

        o_number = d.pop("oNumber", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        remains = d.pop("remains", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        soll = d.pop("soll", UNSET)

        soll_kontr = d.pop("sollKontr", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        subtitle_description = d.pop("subtitleDescription", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        title_kor = d.pop("titleKor", UNSET)

        type_ = d.pop("type", UNSET)

        undertitle_kor = d.pop("undertitleKor", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        verfkor = d.pop("verfkor", UNSET)

        vojs = d.pop("vojs", UNSET)

        vwg = d.pop("vwg", UNSET)

        year = d.pop("year", UNSET)

        zvert = d.pop("zvert", UNSET)

        rm_erp_common_account_subtitle = cls(
            field_foreigntext=field_foreigntext,
            akts=akts,
            ausz=ausz,
            chapter=chapter,
            cover_ring_hierarchy_level_one=cover_ring_hierarchy_level_one,
            cover_ring_hierarchy_level_two=cover_ring_hierarchy_level_two,
            cover_ring_kor=cover_ring_kor,
            defaulttext=defaulttext,
            dtgr=dtgr,
            ein=ein,
            fest=fest,
            financial_stat=financial_stat,
            hhans=hhans,
            hiskey_id=hiskey_id,
            id=id,
            indicator_ueber=indicator_ueber,
            is_changed=is_changed,
            korr_indicator=korr_indicator,
            lock=lock,
            lock_indicator=lock_indicator,
            lock_version=lock_version,
            longtext=longtext,
            mwpf=mwpf,
            o_number=o_number,
            obj_guid=obj_guid,
            remains=remains,
            shorttext=shorttext,
            soll=soll,
            soll_kontr=soll_kontr,
            sortorder=sortorder,
            subtitle=subtitle,
            subtitle_description=subtitle_description,
            text=text,
            title=title,
            title_kor=title_kor,
            type_=type_,
            undertitle_kor=undertitle_kor,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
            verfkor=verfkor,
            vojs=vojs,
            vwg=vwg,
            year=year,
            zvert=zvert,
        )

        rm_erp_common_account_subtitle.additional_properties = d
        return rm_erp_common_account_subtitle

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
