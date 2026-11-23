from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_business import CsPsvExternalOrganisationBusiness
    from ..models.cs_psv_external_organisation_research_partner_foreigntext import (
        CsPsvExternalOrganisationResearchPartnerForeigntext,
    )
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvExternalOrganisationResearchPartner")


@_attrs_define
class CsPsvExternalOrganisationResearchPartner:
    """
    Attributes:
        field_foreigntext (CsPsvExternalOrganisationResearchPartnerForeigntext | Unset):
        business (CsPsvExternalOrganisationBusiness | Unset):
        doctoral_cooperation_type_kdsf (CsSysValueGenericValue | Unset):
        funder_category_kdsf (CsSysValueGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: CsPsvExternalOrganisationResearchPartnerForeigntext | Unset = UNSET
    business: CsPsvExternalOrganisationBusiness | Unset = UNSET
    doctoral_cooperation_type_kdsf: CsSysValueGenericValue | Unset = UNSET
    funder_category_kdsf: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        business: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        doctoral_cooperation_type_kdsf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doctoral_cooperation_type_kdsf, Unset):
            doctoral_cooperation_type_kdsf = self.doctoral_cooperation_type_kdsf.to_dict()

        funder_category_kdsf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funder_category_kdsf, Unset):
            funder_category_kdsf = self.funder_category_kdsf.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if business is not UNSET:
            field_dict["business"] = business
        if doctoral_cooperation_type_kdsf is not UNSET:
            field_dict["doctoralCooperationTypeKdsf"] = doctoral_cooperation_type_kdsf
        if funder_category_kdsf is not UNSET:
            field_dict["funderCategoryKdsf"] = funder_category_kdsf
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_business import CsPsvExternalOrganisationBusiness  # noqa: PLC0415
        from ..models.cs_psv_external_organisation_research_partner_foreigntext import (
            CsPsvExternalOrganisationResearchPartnerForeigntext,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvExternalOrganisationResearchPartnerForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvExternalOrganisationResearchPartnerForeigntext.from_dict(_field_foreigntext)

        _business = d.pop("business", UNSET)
        business: CsPsvExternalOrganisationBusiness | Unset
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = CsPsvExternalOrganisationBusiness.from_dict(_business)

        _doctoral_cooperation_type_kdsf = d.pop("doctoralCooperationTypeKdsf", UNSET)
        doctoral_cooperation_type_kdsf: CsSysValueGenericValue | Unset
        if isinstance(_doctoral_cooperation_type_kdsf, Unset):
            doctoral_cooperation_type_kdsf = UNSET
        else:
            doctoral_cooperation_type_kdsf = CsSysValueGenericValue.from_dict(_doctoral_cooperation_type_kdsf)

        _funder_category_kdsf = d.pop("funderCategoryKdsf", UNSET)
        funder_category_kdsf: CsSysValueGenericValue | Unset
        if isinstance(_funder_category_kdsf, Unset):
            funder_category_kdsf = UNSET
        else:
            funder_category_kdsf = CsSysValueGenericValue.from_dict(_funder_category_kdsf)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        cs_psv_external_organisation_research_partner = cls(
            field_foreigntext=field_foreigntext,
            business=business,
            doctoral_cooperation_type_kdsf=doctoral_cooperation_type_kdsf,
            funder_category_kdsf=funder_category_kdsf,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        cs_psv_external_organisation_research_partner.additional_properties = d
        return cs_psv_external_organisation_research_partner

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
