from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_department_foreigntext import RmErpCommonAccountDepartmentForeigntext


T = TypeVar("T", bound="RmErpCommonAccountDepartment")


@_attrs_define
class RmErpCommonAccountDepartment:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountDepartmentForeigntext | Unset):
        akts (float | Unset):
        ausz (float | Unset):
        changed (bool | Unset):
        chapter (str | Unset):
        cover_ring_hierarchy_level_one (str | Unset):
        cover_ring_hierarchy_level_two (str | Unset):
        defaulttext (str | Unset):
        department (str | Unset):
        department_description (str | Unset):
        dtgr (int | Unset):
        fest (float | Unset):
        financial_stat (str | Unset):
        hhans (float | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        in_ (float | Unset):
        indicator_ueber (str | Unset):
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
        text (str | Unset):
        title (str | Unset):
        type_ (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
        verfkor (float | Unset):
        vojs (float | Unset):
        vwg (int | Unset):
        year (str | Unset):
        zvert (float | Unset):
    """

    field_foreigntext: RmErpCommonAccountDepartmentForeigntext | Unset = UNSET
    akts: float | Unset = UNSET
    ausz: float | Unset = UNSET
    changed: bool | Unset = UNSET
    chapter: str | Unset = UNSET
    cover_ring_hierarchy_level_one: str | Unset = UNSET
    cover_ring_hierarchy_level_two: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    department: str | Unset = UNSET
    department_description: str | Unset = UNSET
    dtgr: int | Unset = UNSET
    fest: float | Unset = UNSET
    financial_stat: str | Unset = UNSET
    hhans: float | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    in_: float | Unset = UNSET
    indicator_ueber: str | Unset = UNSET
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
    text: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
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

        changed = self.changed

        chapter = self.chapter

        cover_ring_hierarchy_level_one = self.cover_ring_hierarchy_level_one

        cover_ring_hierarchy_level_two = self.cover_ring_hierarchy_level_two

        defaulttext = self.defaulttext

        department = self.department

        department_description = self.department_description

        dtgr = self.dtgr

        fest = self.fest

        financial_stat = self.financial_stat

        hhans = self.hhans

        hiskey_id = self.hiskey_id

        id = self.id

        in_ = self.in_

        indicator_ueber = self.indicator_ueber

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

        text = self.text

        title = self.title

        type_ = self.type_

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
        if changed is not UNSET:
            field_dict["changed"] = changed
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if cover_ring_hierarchy_level_one is not UNSET:
            field_dict["coverRingHierarchyLevelOne"] = cover_ring_hierarchy_level_one
        if cover_ring_hierarchy_level_two is not UNSET:
            field_dict["coverRingHierarchyLevelTwo"] = cover_ring_hierarchy_level_two
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if department is not UNSET:
            field_dict["department"] = department
        if department_description is not UNSET:
            field_dict["departmentDescription"] = department_description
        if dtgr is not UNSET:
            field_dict["dtgr"] = dtgr
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
        if in_ is not UNSET:
            field_dict["in"] = in_
        if indicator_ueber is not UNSET:
            field_dict["indicatorUeber"] = indicator_ueber
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
        if text is not UNSET:
            field_dict["text"] = text
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        from ..models.rm_erp_common_account_department_foreigntext import RmErpCommonAccountDepartmentForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountDepartmentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountDepartmentForeigntext.from_dict(_field_foreigntext)

        akts = d.pop("akts", UNSET)

        ausz = d.pop("ausz", UNSET)

        changed = d.pop("changed", UNSET)

        chapter = d.pop("chapter", UNSET)

        cover_ring_hierarchy_level_one = d.pop("coverRingHierarchyLevelOne", UNSET)

        cover_ring_hierarchy_level_two = d.pop("coverRingHierarchyLevelTwo", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        department = d.pop("department", UNSET)

        department_description = d.pop("departmentDescription", UNSET)

        dtgr = d.pop("dtgr", UNSET)

        fest = d.pop("fest", UNSET)

        financial_stat = d.pop("financialStat", UNSET)

        hhans = d.pop("hhans", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        in_ = d.pop("in", UNSET)

        indicator_ueber = d.pop("indicatorUeber", UNSET)

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

        text = d.pop("text", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        verfkor = d.pop("verfkor", UNSET)

        vojs = d.pop("vojs", UNSET)

        vwg = d.pop("vwg", UNSET)

        year = d.pop("year", UNSET)

        zvert = d.pop("zvert", UNSET)

        rm_erp_common_account_department = cls(
            field_foreigntext=field_foreigntext,
            akts=akts,
            ausz=ausz,
            changed=changed,
            chapter=chapter,
            cover_ring_hierarchy_level_one=cover_ring_hierarchy_level_one,
            cover_ring_hierarchy_level_two=cover_ring_hierarchy_level_two,
            defaulttext=defaulttext,
            department=department,
            department_description=department_description,
            dtgr=dtgr,
            fest=fest,
            financial_stat=financial_stat,
            hhans=hhans,
            hiskey_id=hiskey_id,
            id=id,
            in_=in_,
            indicator_ueber=indicator_ueber,
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
            text=text,
            title=title,
            type_=type_,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
            verfkor=verfkor,
            vojs=vojs,
            vwg=vwg,
            year=year,
            zvert=zvert,
        )

        rm_erp_common_account_department.additional_properties = d
        return rm_erp_common_account_department

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
