from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_project_foreigntext import RmErpCommonAccountProjectForeigntext


T = TypeVar("T", bound="RmErpCommonAccountProject")


@_attrs_define
class RmErpCommonAccountProject:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountProjectForeigntext | Unset):
        az (str | Unset):
        bau_relevant (str | Unset):
        bes_relevant (str | Unset):
        betterment_tax_duty (str | Unset):
        bewdat_one (int | Unset):
        bewdat_two (int | Unset):
        choosable_date_one (int | Unset):
        choosable_date_two (int | Unset):
        choosable_text_eight (str | Unset):
        choosable_text_five (str | Unset):
        choosable_text_four (str | Unset):
        choosable_text_nine (str | Unset):
        choosable_text_one (str | Unset):
        choosable_text_seven (str | Unset):
        choosable_text_six (str | Unset):
        choosable_text_ten (str | Unset):
        choosable_text_three (str | Unset):
        choosable_text_two (str | Unset):
        cob_relevant (str | Unset):
        coordination (str | Unset):
        defaulttext (str | Unset):
        department (str | Unset):
        economical (str | Unset):
        fins (str | Unset):
        hiskey_id (str | Unset):
        id (int | Unset):
        input_tax_share (float | Unset):
        institution (str | Unset):
        ivs_relevant (str | Unset):
        k_tax_pf (str | Unset):
        key_external (str | Unset):
        key_extkotr (str | Unset):
        lehr (str | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        longtext_one (str | Unset):
        longtext_two (str | Unset):
        lsf_relevant (str | Unset):
        mbs_relevant (str | Unset):
        mig_relevant (str | Unset):
        obj_guid (str | Unset):
        ov_rate (float | Unset):
        ov_type (str | Unset):
        project_director_name_one (str | Unset):
        project_director_name_three (str | Unset):
        project_director_name_two (str | Unset):
        project_number (str | Unset):
        rka_relevant (str | Unset):
        runtime_begin (int | Unset):
        sem_relevant (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        spkl_number_four (str | Unset):
        spkl_number_one (str | Unset):
        spkl_number_three (str | Unset):
        spkl_number_two (str | Unset):
        sum_project (str | Unset):
        sum_project_indicator (str | Unset):
        sva_relevant (str | Unset):
        text (str | Unset):
        titzus (str | Unset):
        type_one (str | Unset):
        type_two (str | Unset):
        ueber_key (str | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: RmErpCommonAccountProjectForeigntext | Unset = UNSET
    az: str | Unset = UNSET
    bau_relevant: str | Unset = UNSET
    bes_relevant: str | Unset = UNSET
    betterment_tax_duty: str | Unset = UNSET
    bewdat_one: int | Unset = UNSET
    bewdat_two: int | Unset = UNSET
    choosable_date_one: int | Unset = UNSET
    choosable_date_two: int | Unset = UNSET
    choosable_text_eight: str | Unset = UNSET
    choosable_text_five: str | Unset = UNSET
    choosable_text_four: str | Unset = UNSET
    choosable_text_nine: str | Unset = UNSET
    choosable_text_one: str | Unset = UNSET
    choosable_text_seven: str | Unset = UNSET
    choosable_text_six: str | Unset = UNSET
    choosable_text_ten: str | Unset = UNSET
    choosable_text_three: str | Unset = UNSET
    choosable_text_two: str | Unset = UNSET
    cob_relevant: str | Unset = UNSET
    coordination: str | Unset = UNSET
    defaulttext: str | Unset = UNSET
    department: str | Unset = UNSET
    economical: str | Unset = UNSET
    fins: str | Unset = UNSET
    hiskey_id: str | Unset = UNSET
    id: int | Unset = UNSET
    input_tax_share: float | Unset = UNSET
    institution: str | Unset = UNSET
    ivs_relevant: str | Unset = UNSET
    k_tax_pf: str | Unset = UNSET
    key_external: str | Unset = UNSET
    key_extkotr: str | Unset = UNSET
    lehr: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    longtext_one: str | Unset = UNSET
    longtext_two: str | Unset = UNSET
    lsf_relevant: str | Unset = UNSET
    mbs_relevant: str | Unset = UNSET
    mig_relevant: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    ov_rate: float | Unset = UNSET
    ov_type: str | Unset = UNSET
    project_director_name_one: str | Unset = UNSET
    project_director_name_three: str | Unset = UNSET
    project_director_name_two: str | Unset = UNSET
    project_number: str | Unset = UNSET
    rka_relevant: str | Unset = UNSET
    runtime_begin: int | Unset = UNSET
    sem_relevant: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    spkl_number_four: str | Unset = UNSET
    spkl_number_one: str | Unset = UNSET
    spkl_number_three: str | Unset = UNSET
    spkl_number_two: str | Unset = UNSET
    sum_project: str | Unset = UNSET
    sum_project_indicator: str | Unset = UNSET
    sva_relevant: str | Unset = UNSET
    text: str | Unset = UNSET
    titzus: str | Unset = UNSET
    type_one: str | Unset = UNSET
    type_two: str | Unset = UNSET
    ueber_key: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        az = self.az

        bau_relevant = self.bau_relevant

        bes_relevant = self.bes_relevant

        betterment_tax_duty = self.betterment_tax_duty

        bewdat_one = self.bewdat_one

        bewdat_two = self.bewdat_two

        choosable_date_one = self.choosable_date_one

        choosable_date_two = self.choosable_date_two

        choosable_text_eight = self.choosable_text_eight

        choosable_text_five = self.choosable_text_five

        choosable_text_four = self.choosable_text_four

        choosable_text_nine = self.choosable_text_nine

        choosable_text_one = self.choosable_text_one

        choosable_text_seven = self.choosable_text_seven

        choosable_text_six = self.choosable_text_six

        choosable_text_ten = self.choosable_text_ten

        choosable_text_three = self.choosable_text_three

        choosable_text_two = self.choosable_text_two

        cob_relevant = self.cob_relevant

        coordination = self.coordination

        defaulttext = self.defaulttext

        department = self.department

        economical = self.economical

        fins = self.fins

        hiskey_id = self.hiskey_id

        id = self.id

        input_tax_share = self.input_tax_share

        institution = self.institution

        ivs_relevant = self.ivs_relevant

        k_tax_pf = self.k_tax_pf

        key_external = self.key_external

        key_extkotr = self.key_extkotr

        lehr = self.lehr

        lock_version = self.lock_version

        longtext = self.longtext

        longtext_one = self.longtext_one

        longtext_two = self.longtext_two

        lsf_relevant = self.lsf_relevant

        mbs_relevant = self.mbs_relevant

        mig_relevant = self.mig_relevant

        obj_guid = self.obj_guid

        ov_rate = self.ov_rate

        ov_type = self.ov_type

        project_director_name_one = self.project_director_name_one

        project_director_name_three = self.project_director_name_three

        project_director_name_two = self.project_director_name_two

        project_number = self.project_number

        rka_relevant = self.rka_relevant

        runtime_begin = self.runtime_begin

        sem_relevant = self.sem_relevant

        shorttext = self.shorttext

        sortorder = self.sortorder

        spkl_number_four = self.spkl_number_four

        spkl_number_one = self.spkl_number_one

        spkl_number_three = self.spkl_number_three

        spkl_number_two = self.spkl_number_two

        sum_project = self.sum_project

        sum_project_indicator = self.sum_project_indicator

        sva_relevant = self.sva_relevant

        text = self.text

        titzus = self.titzus

        type_one = self.type_one

        type_two = self.type_two

        ueber_key = self.ueber_key

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if az is not UNSET:
            field_dict["az"] = az
        if bau_relevant is not UNSET:
            field_dict["bauRelevant"] = bau_relevant
        if bes_relevant is not UNSET:
            field_dict["besRelevant"] = bes_relevant
        if betterment_tax_duty is not UNSET:
            field_dict["bettermentTaxDuty"] = betterment_tax_duty
        if bewdat_one is not UNSET:
            field_dict["bewdatOne"] = bewdat_one
        if bewdat_two is not UNSET:
            field_dict["bewdatTwo"] = bewdat_two
        if choosable_date_one is not UNSET:
            field_dict["choosableDateOne"] = choosable_date_one
        if choosable_date_two is not UNSET:
            field_dict["choosableDateTwo"] = choosable_date_two
        if choosable_text_eight is not UNSET:
            field_dict["choosableTextEight"] = choosable_text_eight
        if choosable_text_five is not UNSET:
            field_dict["choosableTextFive"] = choosable_text_five
        if choosable_text_four is not UNSET:
            field_dict["choosableTextFour"] = choosable_text_four
        if choosable_text_nine is not UNSET:
            field_dict["choosableTextNine"] = choosable_text_nine
        if choosable_text_one is not UNSET:
            field_dict["choosableTextOne"] = choosable_text_one
        if choosable_text_seven is not UNSET:
            field_dict["choosableTextSeven"] = choosable_text_seven
        if choosable_text_six is not UNSET:
            field_dict["choosableTextSix"] = choosable_text_six
        if choosable_text_ten is not UNSET:
            field_dict["choosableTextTen"] = choosable_text_ten
        if choosable_text_three is not UNSET:
            field_dict["choosableTextThree"] = choosable_text_three
        if choosable_text_two is not UNSET:
            field_dict["choosableTextTwo"] = choosable_text_two
        if cob_relevant is not UNSET:
            field_dict["cobRelevant"] = cob_relevant
        if coordination is not UNSET:
            field_dict["coordination"] = coordination
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if department is not UNSET:
            field_dict["department"] = department
        if economical is not UNSET:
            field_dict["economical"] = economical
        if fins is not UNSET:
            field_dict["fins"] = fins
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if input_tax_share is not UNSET:
            field_dict["inputTaxShare"] = input_tax_share
        if institution is not UNSET:
            field_dict["institution"] = institution
        if ivs_relevant is not UNSET:
            field_dict["ivsRelevant"] = ivs_relevant
        if k_tax_pf is not UNSET:
            field_dict["kTaxPf"] = k_tax_pf
        if key_external is not UNSET:
            field_dict["keyExternal"] = key_external
        if key_extkotr is not UNSET:
            field_dict["keyExtkotr"] = key_extkotr
        if lehr is not UNSET:
            field_dict["lehr"] = lehr
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if longtext_one is not UNSET:
            field_dict["longtextOne"] = longtext_one
        if longtext_two is not UNSET:
            field_dict["longtextTwo"] = longtext_two
        if lsf_relevant is not UNSET:
            field_dict["lsfRelevant"] = lsf_relevant
        if mbs_relevant is not UNSET:
            field_dict["mbsRelevant"] = mbs_relevant
        if mig_relevant is not UNSET:
            field_dict["migRelevant"] = mig_relevant
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if ov_rate is not UNSET:
            field_dict["ovRate"] = ov_rate
        if ov_type is not UNSET:
            field_dict["ovType"] = ov_type
        if project_director_name_one is not UNSET:
            field_dict["projectDirectorNameOne"] = project_director_name_one
        if project_director_name_three is not UNSET:
            field_dict["projectDirectorNameThree"] = project_director_name_three
        if project_director_name_two is not UNSET:
            field_dict["projectDirectorNameTwo"] = project_director_name_two
        if project_number is not UNSET:
            field_dict["projectNumber"] = project_number
        if rka_relevant is not UNSET:
            field_dict["rkaRelevant"] = rka_relevant
        if runtime_begin is not UNSET:
            field_dict["runtimeBegin"] = runtime_begin
        if sem_relevant is not UNSET:
            field_dict["semRelevant"] = sem_relevant
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if spkl_number_four is not UNSET:
            field_dict["spklNumberFour"] = spkl_number_four
        if spkl_number_one is not UNSET:
            field_dict["spklNumberOne"] = spkl_number_one
        if spkl_number_three is not UNSET:
            field_dict["spklNumberThree"] = spkl_number_three
        if spkl_number_two is not UNSET:
            field_dict["spklNumberTwo"] = spkl_number_two
        if sum_project is not UNSET:
            field_dict["sumProject"] = sum_project
        if sum_project_indicator is not UNSET:
            field_dict["sumProjectIndicator"] = sum_project_indicator
        if sva_relevant is not UNSET:
            field_dict["svaRelevant"] = sva_relevant
        if text is not UNSET:
            field_dict["text"] = text
        if titzus is not UNSET:
            field_dict["titzus"] = titzus
        if type_one is not UNSET:
            field_dict["typeOne"] = type_one
        if type_two is not UNSET:
            field_dict["typeTwo"] = type_two
        if ueber_key is not UNSET:
            field_dict["ueberKey"] = ueber_key
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_project_foreigntext import RmErpCommonAccountProjectForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountProjectForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountProjectForeigntext.from_dict(_field_foreigntext)

        az = d.pop("az", UNSET)

        bau_relevant = d.pop("bauRelevant", UNSET)

        bes_relevant = d.pop("besRelevant", UNSET)

        betterment_tax_duty = d.pop("bettermentTaxDuty", UNSET)

        bewdat_one = d.pop("bewdatOne", UNSET)

        bewdat_two = d.pop("bewdatTwo", UNSET)

        choosable_date_one = d.pop("choosableDateOne", UNSET)

        choosable_date_two = d.pop("choosableDateTwo", UNSET)

        choosable_text_eight = d.pop("choosableTextEight", UNSET)

        choosable_text_five = d.pop("choosableTextFive", UNSET)

        choosable_text_four = d.pop("choosableTextFour", UNSET)

        choosable_text_nine = d.pop("choosableTextNine", UNSET)

        choosable_text_one = d.pop("choosableTextOne", UNSET)

        choosable_text_seven = d.pop("choosableTextSeven", UNSET)

        choosable_text_six = d.pop("choosableTextSix", UNSET)

        choosable_text_ten = d.pop("choosableTextTen", UNSET)

        choosable_text_three = d.pop("choosableTextThree", UNSET)

        choosable_text_two = d.pop("choosableTextTwo", UNSET)

        cob_relevant = d.pop("cobRelevant", UNSET)

        coordination = d.pop("coordination", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        department = d.pop("department", UNSET)

        economical = d.pop("economical", UNSET)

        fins = d.pop("fins", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        input_tax_share = d.pop("inputTaxShare", UNSET)

        institution = d.pop("institution", UNSET)

        ivs_relevant = d.pop("ivsRelevant", UNSET)

        k_tax_pf = d.pop("kTaxPf", UNSET)

        key_external = d.pop("keyExternal", UNSET)

        key_extkotr = d.pop("keyExtkotr", UNSET)

        lehr = d.pop("lehr", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        longtext_one = d.pop("longtextOne", UNSET)

        longtext_two = d.pop("longtextTwo", UNSET)

        lsf_relevant = d.pop("lsfRelevant", UNSET)

        mbs_relevant = d.pop("mbsRelevant", UNSET)

        mig_relevant = d.pop("migRelevant", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        ov_rate = d.pop("ovRate", UNSET)

        ov_type = d.pop("ovType", UNSET)

        project_director_name_one = d.pop("projectDirectorNameOne", UNSET)

        project_director_name_three = d.pop("projectDirectorNameThree", UNSET)

        project_director_name_two = d.pop("projectDirectorNameTwo", UNSET)

        project_number = d.pop("projectNumber", UNSET)

        rka_relevant = d.pop("rkaRelevant", UNSET)

        runtime_begin = d.pop("runtimeBegin", UNSET)

        sem_relevant = d.pop("semRelevant", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        spkl_number_four = d.pop("spklNumberFour", UNSET)

        spkl_number_one = d.pop("spklNumberOne", UNSET)

        spkl_number_three = d.pop("spklNumberThree", UNSET)

        spkl_number_two = d.pop("spklNumberTwo", UNSET)

        sum_project = d.pop("sumProject", UNSET)

        sum_project_indicator = d.pop("sumProjectIndicator", UNSET)

        sva_relevant = d.pop("svaRelevant", UNSET)

        text = d.pop("text", UNSET)

        titzus = d.pop("titzus", UNSET)

        type_one = d.pop("typeOne", UNSET)

        type_two = d.pop("typeTwo", UNSET)

        ueber_key = d.pop("ueberKey", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        rm_erp_common_account_project = cls(
            field_foreigntext=field_foreigntext,
            az=az,
            bau_relevant=bau_relevant,
            bes_relevant=bes_relevant,
            betterment_tax_duty=betterment_tax_duty,
            bewdat_one=bewdat_one,
            bewdat_two=bewdat_two,
            choosable_date_one=choosable_date_one,
            choosable_date_two=choosable_date_two,
            choosable_text_eight=choosable_text_eight,
            choosable_text_five=choosable_text_five,
            choosable_text_four=choosable_text_four,
            choosable_text_nine=choosable_text_nine,
            choosable_text_one=choosable_text_one,
            choosable_text_seven=choosable_text_seven,
            choosable_text_six=choosable_text_six,
            choosable_text_ten=choosable_text_ten,
            choosable_text_three=choosable_text_three,
            choosable_text_two=choosable_text_two,
            cob_relevant=cob_relevant,
            coordination=coordination,
            defaulttext=defaulttext,
            department=department,
            economical=economical,
            fins=fins,
            hiskey_id=hiskey_id,
            id=id,
            input_tax_share=input_tax_share,
            institution=institution,
            ivs_relevant=ivs_relevant,
            k_tax_pf=k_tax_pf,
            key_external=key_external,
            key_extkotr=key_extkotr,
            lehr=lehr,
            lock_version=lock_version,
            longtext=longtext,
            longtext_one=longtext_one,
            longtext_two=longtext_two,
            lsf_relevant=lsf_relevant,
            mbs_relevant=mbs_relevant,
            mig_relevant=mig_relevant,
            obj_guid=obj_guid,
            ov_rate=ov_rate,
            ov_type=ov_type,
            project_director_name_one=project_director_name_one,
            project_director_name_three=project_director_name_three,
            project_director_name_two=project_director_name_two,
            project_number=project_number,
            rka_relevant=rka_relevant,
            runtime_begin=runtime_begin,
            sem_relevant=sem_relevant,
            shorttext=shorttext,
            sortorder=sortorder,
            spkl_number_four=spkl_number_four,
            spkl_number_one=spkl_number_one,
            spkl_number_three=spkl_number_three,
            spkl_number_two=spkl_number_two,
            sum_project=sum_project,
            sum_project_indicator=sum_project_indicator,
            sva_relevant=sva_relevant,
            text=text,
            titzus=titzus,
            type_one=type_one,
            type_two=type_two,
            ueber_key=ueber_key,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        rm_erp_common_account_project.additional_properties = d
        return rm_erp_common_account_project

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
