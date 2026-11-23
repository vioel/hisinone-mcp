from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_title_foreigntext import RmErpCommonAccountTitleForeigntext


T = TypeVar("T", bound="RmErpCommonAccountTitle")


@_attrs_define
class RmErpCommonAccountTitle:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountTitleForeigntext | Unset):
        akts (float | Unset):
        aktsf (float | Unset):
        apl_umsetz (str | Unset):
        ausz (float | Unset):
        belast_title (str | Unset):
        chapter (str | Unset):
        chapter_umsetz (str | Unset):
        cover_ring_hierarchy_level_one (str | Unset):
        cover_ring_hierarchy_level_two (str | Unset):
        cover_ring_kor (str | Unset):
        datlae (int | Unset):
        defaulttext (str | Unset):
        dtgr (int | Unset):
        ea (str | Unset):
        ein (float | Unset):
        entlast_title (str | Unset):
        fest (float | Unset):
        finz_stat (str | Unset):
        hhans (float | Unset):
        hhansa (float | Unset):
        hiskey_id (str | Unset):
        hueli (int | Unset):
        huels (int | Unset):
        id (int | Unset):
        identification_number (str | Unset):
        indicator_department (str | Unset):
        indicator_institution_hierarchy_level_one (str | Unset):
        indicator_institution_hierarchy_level_three (str | Unset):
        indicator_institution_hierarchy_level_two (str | Unset):
        indicator_ueber (str | Unset):
        inidcator_subttitle (str | Unset):
        is_changed (bool | Unset):
        korr_indicator (str | Unset):
        kz_vhhf (str | Unset):
        lock (float | Unset):
        lock_indicator (str | Unset):
        lock_indiciator_decentralized (str | Unset):
        lock_version (int | Unset):
        long_title_description (str | Unset):
        longtext (str | Unset):
        mwpf (str | Unset):
        o_number (str | Unset):
        obj_guid (str | Unset):
        ov_type (str | Unset):
        pruef (str | Unset):
        pz_umsetz (str | Unset):
        remains (float | Unset):
        remains_v (float | Unset):
        sblae (str | Unset):
        shorttext (str | Unset):
        soll (float | Unset):
        soll_kontr (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        title (str | Unset):
        title_description (str | Unset):
        title_kor (str | Unset):
        title_umsetz (str | Unset):
        type_ (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
        vojs (float | Unset):
        vrfkor (float | Unset):
        vwg (int | Unset):
        year (str | Unset):
        zvert (float | Unset):
    """

    field_foreigntext: RmErpCommonAccountTitleForeigntext | Unset = UNSET
    akts: float | Unset = UNSET
    aktsf: float | Unset = UNSET
    apl_umsetz: str | Unset = UNSET
    ausz: float | Unset = UNSET
    belast_title: str | Unset = UNSET
    chapter: str | Unset = UNSET
    chapter_umsetz: str | Unset = UNSET
    cover_ring_hierarchy_level_one: str | Unset = UNSET
    cover_ring_hierarchy_level_two: str | Unset = UNSET
    cover_ring_kor: str | Unset = UNSET
    datlae: int | Unset = UNSET
    defaulttext: str | Unset = UNSET
    dtgr: int | Unset = UNSET
    ea: str | Unset = UNSET
    ein: float | Unset = UNSET
    entlast_title: str | Unset = UNSET
    fest: float | Unset = UNSET
    finz_stat: str | Unset = UNSET
    hhans: float | Unset = UNSET
    hhansa: float | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    hueli: int | Unset = UNSET
    huels: int | Unset = UNSET
    id: int | Unset = UNSET
    identification_number: str | Unset = UNSET
    indicator_department: str | Unset = UNSET
    indicator_institution_hierarchy_level_one: str | Unset = UNSET
    indicator_institution_hierarchy_level_three: str | Unset = UNSET
    indicator_institution_hierarchy_level_two: str | Unset = UNSET
    indicator_ueber: str | Unset = UNSET
    inidcator_subttitle: str | Unset = UNSET
    is_changed: bool | Unset = UNSET
    korr_indicator: str | Unset = UNSET
    kz_vhhf: str | Unset = UNSET
    lock: float | Unset = UNSET
    lock_indicator: str | Unset = UNSET
    lock_indiciator_decentralized: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    long_title_description: str | Unset = UNSET
    longtext: str | Unset = UNSET
    mwpf: str | Unset = UNSET
    o_number: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    ov_type: str | Unset = UNSET
    pruef: str | Unset = UNSET
    pz_umsetz: str | Unset = UNSET
    remains: float | Unset = UNSET
    remains_v: float | Unset = UNSET
    sblae: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    soll: float | Unset = UNSET
    soll_kontr: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    title_description: str | Unset = UNSET
    title_kor: str | Unset = UNSET
    title_umsetz: str | Unset = UNSET
    type_: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    vojs: float | Unset = UNSET
    vrfkor: float | Unset = UNSET
    vwg: int | Unset = UNSET
    year: str | Unset = UNSET
    zvert: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        akts = self.akts

        aktsf = self.aktsf

        apl_umsetz = self.apl_umsetz

        ausz = self.ausz

        belast_title = self.belast_title

        chapter = self.chapter

        chapter_umsetz = self.chapter_umsetz

        cover_ring_hierarchy_level_one = self.cover_ring_hierarchy_level_one

        cover_ring_hierarchy_level_two = self.cover_ring_hierarchy_level_two

        cover_ring_kor = self.cover_ring_kor

        datlae = self.datlae

        defaulttext = self.defaulttext

        dtgr = self.dtgr

        ea = self.ea

        ein = self.ein

        entlast_title = self.entlast_title

        fest = self.fest

        finz_stat = self.finz_stat

        hhans = self.hhans

        hhansa = self.hhansa

        hiskey_id = self.hiskey_id

        hueli = self.hueli

        huels = self.huels

        id = self.id

        identification_number = self.identification_number

        indicator_department = self.indicator_department

        indicator_institution_hierarchy_level_one = self.indicator_institution_hierarchy_level_one

        indicator_institution_hierarchy_level_three = self.indicator_institution_hierarchy_level_three

        indicator_institution_hierarchy_level_two = self.indicator_institution_hierarchy_level_two

        indicator_ueber = self.indicator_ueber

        inidcator_subttitle = self.inidcator_subttitle

        is_changed = self.is_changed

        korr_indicator = self.korr_indicator

        kz_vhhf = self.kz_vhhf

        lock = self.lock

        lock_indicator = self.lock_indicator

        lock_indiciator_decentralized = self.lock_indiciator_decentralized

        lock_version = self.lock_version

        long_title_description = self.long_title_description

        longtext = self.longtext

        mwpf = self.mwpf

        o_number = self.o_number

        obj_guid = self.obj_guid

        ov_type = self.ov_type

        pruef = self.pruef

        pz_umsetz = self.pz_umsetz

        remains = self.remains

        remains_v = self.remains_v

        sblae = self.sblae

        shorttext = self.shorttext

        soll = self.soll

        soll_kontr = self.soll_kontr

        sortorder = self.sortorder

        text = self.text

        title = self.title

        title_description = self.title_description

        title_kor = self.title_kor

        title_umsetz = self.title_umsetz

        type_ = self.type_

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        vojs = self.vojs

        vrfkor = self.vrfkor

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
        if aktsf is not UNSET:
            field_dict["aktsf"] = aktsf
        if apl_umsetz is not UNSET:
            field_dict["aplUmsetz"] = apl_umsetz
        if ausz is not UNSET:
            field_dict["ausz"] = ausz
        if belast_title is not UNSET:
            field_dict["belastTitle"] = belast_title
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if chapter_umsetz is not UNSET:
            field_dict["chapterUmsetz"] = chapter_umsetz
        if cover_ring_hierarchy_level_one is not UNSET:
            field_dict["coverRingHierarchyLevelOne"] = cover_ring_hierarchy_level_one
        if cover_ring_hierarchy_level_two is not UNSET:
            field_dict["coverRingHierarchyLevelTwo"] = cover_ring_hierarchy_level_two
        if cover_ring_kor is not UNSET:
            field_dict["coverRingKor"] = cover_ring_kor
        if datlae is not UNSET:
            field_dict["datlae"] = datlae
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if dtgr is not UNSET:
            field_dict["dtgr"] = dtgr
        if ea is not UNSET:
            field_dict["ea"] = ea
        if ein is not UNSET:
            field_dict["ein"] = ein
        if entlast_title is not UNSET:
            field_dict["entlastTitle"] = entlast_title
        if fest is not UNSET:
            field_dict["fest"] = fest
        if finz_stat is not UNSET:
            field_dict["finzStat"] = finz_stat
        if hhans is not UNSET:
            field_dict["hhans"] = hhans
        if hhansa is not UNSET:
            field_dict["hhansa"] = hhansa
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if hueli is not UNSET:
            field_dict["hueli"] = hueli
        if huels is not UNSET:
            field_dict["huels"] = huels
        if id is not UNSET:
            field_dict["id"] = id
        if identification_number is not UNSET:
            field_dict["identificationNumber"] = identification_number
        if indicator_department is not UNSET:
            field_dict["indicatorDepartment"] = indicator_department
        if indicator_institution_hierarchy_level_one is not UNSET:
            field_dict["indicatorInstitutionHierarchyLevelOne"] = indicator_institution_hierarchy_level_one
        if indicator_institution_hierarchy_level_three is not UNSET:
            field_dict["indicatorInstitutionHierarchyLevelThree"] = indicator_institution_hierarchy_level_three
        if indicator_institution_hierarchy_level_two is not UNSET:
            field_dict["indicatorInstitutionHierarchyLevelTwo"] = indicator_institution_hierarchy_level_two
        if indicator_ueber is not UNSET:
            field_dict["indicatorUeber"] = indicator_ueber
        if inidcator_subttitle is not UNSET:
            field_dict["inidcatorSubttitle"] = inidcator_subttitle
        if is_changed is not UNSET:
            field_dict["isChanged"] = is_changed
        if korr_indicator is not UNSET:
            field_dict["korrIndicator"] = korr_indicator
        if kz_vhhf is not UNSET:
            field_dict["kzVhhf"] = kz_vhhf
        if lock is not UNSET:
            field_dict["lock"] = lock
        if lock_indicator is not UNSET:
            field_dict["lockIndicator"] = lock_indicator
        if lock_indiciator_decentralized is not UNSET:
            field_dict["lockIndiciatorDecentralized"] = lock_indiciator_decentralized
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if long_title_description is not UNSET:
            field_dict["longTitleDescription"] = long_title_description
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if mwpf is not UNSET:
            field_dict["mwpf"] = mwpf
        if o_number is not UNSET:
            field_dict["oNumber"] = o_number
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if ov_type is not UNSET:
            field_dict["ovType"] = ov_type
        if pruef is not UNSET:
            field_dict["pruef"] = pruef
        if pz_umsetz is not UNSET:
            field_dict["pzUmsetz"] = pz_umsetz
        if remains is not UNSET:
            field_dict["remains"] = remains
        if remains_v is not UNSET:
            field_dict["remainsV"] = remains_v
        if sblae is not UNSET:
            field_dict["sblae"] = sblae
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if soll is not UNSET:
            field_dict["soll"] = soll
        if soll_kontr is not UNSET:
            field_dict["sollKontr"] = soll_kontr
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if title_description is not UNSET:
            field_dict["titleDescription"] = title_description
        if title_kor is not UNSET:
            field_dict["titleKor"] = title_kor
        if title_umsetz is not UNSET:
            field_dict["titleUmsetz"] = title_umsetz
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if vojs is not UNSET:
            field_dict["vojs"] = vojs
        if vrfkor is not UNSET:
            field_dict["vrfkor"] = vrfkor
        if vwg is not UNSET:
            field_dict["vwg"] = vwg
        if year is not UNSET:
            field_dict["year"] = year
        if zvert is not UNSET:
            field_dict["zvert"] = zvert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_title_foreigntext import RmErpCommonAccountTitleForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountTitleForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountTitleForeigntext.from_dict(_field_foreigntext)

        akts = d.pop("akts", UNSET)

        aktsf = d.pop("aktsf", UNSET)

        apl_umsetz = d.pop("aplUmsetz", UNSET)

        ausz = d.pop("ausz", UNSET)

        belast_title = d.pop("belastTitle", UNSET)

        chapter = d.pop("chapter", UNSET)

        chapter_umsetz = d.pop("chapterUmsetz", UNSET)

        cover_ring_hierarchy_level_one = d.pop("coverRingHierarchyLevelOne", UNSET)

        cover_ring_hierarchy_level_two = d.pop("coverRingHierarchyLevelTwo", UNSET)

        cover_ring_kor = d.pop("coverRingKor", UNSET)

        datlae = d.pop("datlae", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        dtgr = d.pop("dtgr", UNSET)

        ea = d.pop("ea", UNSET)

        ein = d.pop("ein", UNSET)

        entlast_title = d.pop("entlastTitle", UNSET)

        fest = d.pop("fest", UNSET)

        finz_stat = d.pop("finzStat", UNSET)

        hhans = d.pop("hhans", UNSET)

        hhansa = d.pop("hhansa", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        hueli = d.pop("hueli", UNSET)

        huels = d.pop("huels", UNSET)

        id = d.pop("id", UNSET)

        identification_number = d.pop("identificationNumber", UNSET)

        indicator_department = d.pop("indicatorDepartment", UNSET)

        indicator_institution_hierarchy_level_one = d.pop("indicatorInstitutionHierarchyLevelOne", UNSET)

        indicator_institution_hierarchy_level_three = d.pop("indicatorInstitutionHierarchyLevelThree", UNSET)

        indicator_institution_hierarchy_level_two = d.pop("indicatorInstitutionHierarchyLevelTwo", UNSET)

        indicator_ueber = d.pop("indicatorUeber", UNSET)

        inidcator_subttitle = d.pop("inidcatorSubttitle", UNSET)

        is_changed = d.pop("isChanged", UNSET)

        korr_indicator = d.pop("korrIndicator", UNSET)

        kz_vhhf = d.pop("kzVhhf", UNSET)

        lock = d.pop("lock", UNSET)

        lock_indicator = d.pop("lockIndicator", UNSET)

        lock_indiciator_decentralized = d.pop("lockIndiciatorDecentralized", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        long_title_description = d.pop("longTitleDescription", UNSET)

        longtext = d.pop("longtext", UNSET)

        mwpf = d.pop("mwpf", UNSET)

        o_number = d.pop("oNumber", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        ov_type = d.pop("ovType", UNSET)

        pruef = d.pop("pruef", UNSET)

        pz_umsetz = d.pop("pzUmsetz", UNSET)

        remains = d.pop("remains", UNSET)

        remains_v = d.pop("remainsV", UNSET)

        sblae = d.pop("sblae", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        soll = d.pop("soll", UNSET)

        soll_kontr = d.pop("sollKontr", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        title_description = d.pop("titleDescription", UNSET)

        title_kor = d.pop("titleKor", UNSET)

        title_umsetz = d.pop("titleUmsetz", UNSET)

        type_ = d.pop("type", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        vojs = d.pop("vojs", UNSET)

        vrfkor = d.pop("vrfkor", UNSET)

        vwg = d.pop("vwg", UNSET)

        year = d.pop("year", UNSET)

        zvert = d.pop("zvert", UNSET)

        rm_erp_common_account_title = cls(
            field_foreigntext=field_foreigntext,
            akts=akts,
            aktsf=aktsf,
            apl_umsetz=apl_umsetz,
            ausz=ausz,
            belast_title=belast_title,
            chapter=chapter,
            chapter_umsetz=chapter_umsetz,
            cover_ring_hierarchy_level_one=cover_ring_hierarchy_level_one,
            cover_ring_hierarchy_level_two=cover_ring_hierarchy_level_two,
            cover_ring_kor=cover_ring_kor,
            datlae=datlae,
            defaulttext=defaulttext,
            dtgr=dtgr,
            ea=ea,
            ein=ein,
            entlast_title=entlast_title,
            fest=fest,
            finz_stat=finz_stat,
            hhans=hhans,
            hhansa=hhansa,
            hiskey_id=hiskey_id,
            hueli=hueli,
            huels=huels,
            id=id,
            identification_number=identification_number,
            indicator_department=indicator_department,
            indicator_institution_hierarchy_level_one=indicator_institution_hierarchy_level_one,
            indicator_institution_hierarchy_level_three=indicator_institution_hierarchy_level_three,
            indicator_institution_hierarchy_level_two=indicator_institution_hierarchy_level_two,
            indicator_ueber=indicator_ueber,
            inidcator_subttitle=inidcator_subttitle,
            is_changed=is_changed,
            korr_indicator=korr_indicator,
            kz_vhhf=kz_vhhf,
            lock=lock,
            lock_indicator=lock_indicator,
            lock_indiciator_decentralized=lock_indiciator_decentralized,
            lock_version=lock_version,
            long_title_description=long_title_description,
            longtext=longtext,
            mwpf=mwpf,
            o_number=o_number,
            obj_guid=obj_guid,
            ov_type=ov_type,
            pruef=pruef,
            pz_umsetz=pz_umsetz,
            remains=remains,
            remains_v=remains_v,
            sblae=sblae,
            shorttext=shorttext,
            soll=soll,
            soll_kontr=soll_kontr,
            sortorder=sortorder,
            text=text,
            title=title,
            title_description=title_description,
            title_kor=title_kor,
            title_umsetz=title_umsetz,
            type_=type_,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
            vojs=vojs,
            vrfkor=vrfkor,
            vwg=vwg,
            year=year,
            zvert=zvert,
        )

        rm_erp_common_account_title.additional_properties = d
        return rm_erp_common_account_title

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
