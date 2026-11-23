from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_expense_type_foreigntext import RmErpCommonAccountExpenseTypeForeigntext


T = TypeVar("T", bound="RmErpCommonAccountExpenseType")


@_attrs_define
class RmErpCommonAccountExpenseType:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountExpenseTypeForeigntext | Unset):
        account_type_from_his_in_one (str | Unset):
        aost_number (str | Unset):
        bau_relevant (str | Unset):
        cob_relevant (str | Unset):
        defaulttext (str | Unset):
        hab_position (str | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        ivs_bga (str | Unset):
        ivs_relevant (str | Unset):
        key (str | Unset):
        lock_version (int | Unset):
        long_description (str | Unset):
        longtext (str | Unset):
        mbs_relevant (str | Unset):
        mbs_to_cob (str | Unset):
        mw_satz (float | Unset):
        obj_guid (str | Unset):
        parent_financial_account_id (str | Unset):
        rka_relevant (str | Unset):
        sem_relevant (str | Unset):
        short_description (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        sva_relevant (str | Unset):
        syf (str | Unset):
        text (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: RmErpCommonAccountExpenseTypeForeigntext | Unset = UNSET
    account_type_from_his_in_one: str | Unset = UNSET
    aost_number: str | Unset = UNSET
    bau_relevant: str | Unset = UNSET
    cob_relevant: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    hab_position: str | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    ivs_bga: str | Unset = UNSET
    ivs_relevant: str | Unset = UNSET
    key: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    long_description: str | Unset = UNSET
    longtext: str | Unset = UNSET
    mbs_relevant: str | Unset = UNSET
    mbs_to_cob: str | Unset = UNSET
    mw_satz: float | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent_financial_account_id: str | Unset = UNSET
    rka_relevant: str | Unset = UNSET
    sem_relevant: str | Unset = UNSET
    short_description: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    sva_relevant: str | Unset = UNSET
    syf: str | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        account_type_from_his_in_one = self.account_type_from_his_in_one

        aost_number = self.aost_number

        bau_relevant = self.bau_relevant

        cob_relevant = self.cob_relevant

        defaulttext = self.defaulttext

        hab_position = self.hab_position

        hiskey_id = self.hiskey_id

        id = self.id

        ivs_bga = self.ivs_bga

        ivs_relevant = self.ivs_relevant

        key = self.key

        lock_version = self.lock_version

        long_description = self.long_description

        longtext = self.longtext

        mbs_relevant = self.mbs_relevant

        mbs_to_cob = self.mbs_to_cob

        mw_satz = self.mw_satz

        obj_guid = self.obj_guid

        parent_financial_account_id = self.parent_financial_account_id

        rka_relevant = self.rka_relevant

        sem_relevant = self.sem_relevant

        short_description = self.short_description

        shorttext = self.shorttext

        sortorder = self.sortorder

        sva_relevant = self.sva_relevant

        syf = self.syf

        text = self.text

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if account_type_from_his_in_one is not UNSET:
            field_dict["accountTypeFromHisInOne"] = account_type_from_his_in_one
        if aost_number is not UNSET:
            field_dict["aostNumber"] = aost_number
        if bau_relevant is not UNSET:
            field_dict["bauRelevant"] = bau_relevant
        if cob_relevant is not UNSET:
            field_dict["cobRelevant"] = cob_relevant
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if hab_position is not UNSET:
            field_dict["habPosition"] = hab_position
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if ivs_bga is not UNSET:
            field_dict["ivsBga"] = ivs_bga
        if ivs_relevant is not UNSET:
            field_dict["ivsRelevant"] = ivs_relevant
        if key is not UNSET:
            field_dict["key"] = key
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if long_description is not UNSET:
            field_dict["longDescription"] = long_description
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if mbs_relevant is not UNSET:
            field_dict["mbsRelevant"] = mbs_relevant
        if mbs_to_cob is not UNSET:
            field_dict["mbsToCob"] = mbs_to_cob
        if mw_satz is not UNSET:
            field_dict["mwSatz"] = mw_satz
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent_financial_account_id is not UNSET:
            field_dict["parentFinancialAccountId"] = parent_financial_account_id
        if rka_relevant is not UNSET:
            field_dict["rkaRelevant"] = rka_relevant
        if sem_relevant is not UNSET:
            field_dict["semRelevant"] = sem_relevant
        if short_description is not UNSET:
            field_dict["shortDescription"] = short_description
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if sva_relevant is not UNSET:
            field_dict["svaRelevant"] = sva_relevant
        if syf is not UNSET:
            field_dict["syf"] = syf
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_expense_type_foreigntext import RmErpCommonAccountExpenseTypeForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountExpenseTypeForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountExpenseTypeForeigntext.from_dict(_field_foreigntext)

        account_type_from_his_in_one = d.pop("accountTypeFromHisInOne", UNSET)

        aost_number = d.pop("aostNumber", UNSET)

        bau_relevant = d.pop("bauRelevant", UNSET)

        cob_relevant = d.pop("cobRelevant", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        hab_position = d.pop("habPosition", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        ivs_bga = d.pop("ivsBga", UNSET)

        ivs_relevant = d.pop("ivsRelevant", UNSET)

        key = d.pop("key", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        long_description = d.pop("longDescription", UNSET)

        longtext = d.pop("longtext", UNSET)

        mbs_relevant = d.pop("mbsRelevant", UNSET)

        mbs_to_cob = d.pop("mbsToCob", UNSET)

        mw_satz = d.pop("mwSatz", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        parent_financial_account_id = d.pop("parentFinancialAccountId", UNSET)

        rka_relevant = d.pop("rkaRelevant", UNSET)

        sem_relevant = d.pop("semRelevant", UNSET)

        short_description = d.pop("shortDescription", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        sva_relevant = d.pop("svaRelevant", UNSET)

        syf = d.pop("syf", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        rm_erp_common_account_expense_type = cls(
            field_foreigntext=field_foreigntext,
            account_type_from_his_in_one=account_type_from_his_in_one,
            aost_number=aost_number,
            bau_relevant=bau_relevant,
            cob_relevant=cob_relevant,
            defaulttext=defaulttext,
            hab_position=hab_position,
            hiskey_id=hiskey_id,
            id=id,
            ivs_bga=ivs_bga,
            ivs_relevant=ivs_relevant,
            key=key,
            lock_version=lock_version,
            long_description=long_description,
            longtext=longtext,
            mbs_relevant=mbs_relevant,
            mbs_to_cob=mbs_to_cob,
            mw_satz=mw_satz,
            obj_guid=obj_guid,
            parent_financial_account_id=parent_financial_account_id,
            rka_relevant=rka_relevant,
            sem_relevant=sem_relevant,
            short_description=short_description,
            shorttext=shorttext,
            sortorder=sortorder,
            sva_relevant=sva_relevant,
            syf=syf,
            text=text,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        rm_erp_common_account_expense_type.additional_properties = d
        return rm_erp_common_account_expense_type

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
