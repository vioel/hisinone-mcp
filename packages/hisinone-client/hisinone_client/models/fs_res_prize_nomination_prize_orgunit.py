from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_research_partner_simple import (
        CsPsvExternalOrganisationResearchPartnerSimple,
    )
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_prize_nomination_prize_orgunit_foreigntext import FsResPrizeNominationPrizeOrgunitForeigntext


T = TypeVar("T", bound="FsResPrizeNominationPrizeOrgunit")


@_attrs_define
class FsResPrizeNominationPrizeOrgunit:
    """
    Attributes:
        field_foreigntext (FsResPrizeNominationPrizeOrgunitForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        orgunit_obj (CsSysValueGenericValue | Unset):
        prize_id (int | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
    """

    field_foreigntext: FsResPrizeNominationPrizeOrgunitForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    orgunit_obj: CsSysValueGenericValue | Unset = UNSET
    prize_id: int | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        orgunit_obj: dict[str, Any] | Unset = UNSET
        if not isinstance(self.orgunit_obj, Unset):
            orgunit_obj = self.orgunit_obj.to_dict()

        prize_id = self.prize_id

        research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_partner, Unset):
            research_partner = self.research_partner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if orgunit_obj is not UNSET:
            field_dict["orgunitObj"] = orgunit_obj
        if prize_id is not UNSET:
            field_dict["prizeId"] = prize_id
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_prize_orgunit_foreigntext import (
            FsResPrizeNominationPrizeOrgunitForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPrizeNominationPrizeOrgunitForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPrizeNominationPrizeOrgunitForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _orgunit_obj = d.pop("orgunitObj", UNSET)
        orgunit_obj: CsSysValueGenericValue | Unset
        if isinstance(_orgunit_obj, Unset):
            orgunit_obj = UNSET
        else:
            orgunit_obj = CsSysValueGenericValue.from_dict(_orgunit_obj)

        prize_id = d.pop("prizeId", UNSET)

        _research_partner = d.pop("researchPartner", UNSET)
        research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_research_partner, Unset):
            research_partner = UNSET
        else:
            research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_research_partner)

        fs_res_prize_nomination_prize_orgunit = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            orgunit_obj=orgunit_obj,
            prize_id=prize_id,
            research_partner=research_partner,
        )

        fs_res_prize_nomination_prize_orgunit.additional_properties = d
        return fs_res_prize_nomination_prize_orgunit

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
