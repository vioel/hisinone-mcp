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
    from ..models.fs_res_finance_budget_source_foreigntext import FsResFinanceBudgetSourceForeigntext
    from ..models.fs_res_finance_orgunit_simple import FsResFinanceOrgunitSimple
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent


T = TypeVar("T", bound="FsResFinanceBudgetSource")


@_attrs_define
class FsResFinanceBudgetSource:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResFinanceBudgetSourceForeigntext | Unset):
        budget_source_category (CsSysValueGenericValue | Unset):
        budget_source_type (CsSysValueGenericValue | Unset):
        defaulttext (str | Unset):
        id (int | Unset):
        is_selectable (CsSysValueGenericValue | Unset):
        kdsf_category (CsSysValueGenericValue | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        organization (FsResFinanceOrgunitSimple | Unset):
        parent (FsResFinanceBudgetSource | Unset):
        project_management (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        purpose_of_funding (str | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        shorttext (str | Unset):
        status (CsSysValueGenericValue | Unset):
        uniquename (str | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResFinanceBudgetSourceForeigntext | Unset = UNSET
    budget_source_category: CsSysValueGenericValue | Unset = UNSET
    budget_source_type: CsSysValueGenericValue | Unset = UNSET
    defaulttext: str | Unset = UNSET
    id: int | Unset = UNSET
    is_selectable: CsSysValueGenericValue | Unset = UNSET
    kdsf_category: CsSysValueGenericValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organization: FsResFinanceOrgunitSimple | Unset = UNSET
    parent: FsResFinanceBudgetSource | Unset = UNSET
    project_management: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    purpose_of_funding: str | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    shorttext: str | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    uniquename: str | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        budget_source_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_source_category, Unset):
            budget_source_category = self.budget_source_category.to_dict()

        budget_source_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_source_type, Unset):
            budget_source_type = self.budget_source_type.to_dict()

        defaulttext = self.defaulttext

        id = self.id

        is_selectable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.is_selectable, Unset):
            is_selectable = self.is_selectable.to_dict()

        kdsf_category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kdsf_category, Unset):
            kdsf_category = self.kdsf_category.to_dict()

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        project_management: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_management, Unset):
            project_management = self.project_management.to_dict()

        purpose_of_funding = self.purpose_of_funding

        research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_partner, Unset):
            research_partner = self.research_partner.to_dict()

        shorttext = self.shorttext

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        uniquename = self.uniquename

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if budget_source_category is not UNSET:
            field_dict["budgetSourceCategory"] = budget_source_category
        if budget_source_type is not UNSET:
            field_dict["budgetSourceType"] = budget_source_type
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if is_selectable is not UNSET:
            field_dict["isSelectable"] = is_selectable
        if kdsf_category is not UNSET:
            field_dict["kdsfCategory"] = kdsf_category
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organization is not UNSET:
            field_dict["organization"] = organization
        if parent is not UNSET:
            field_dict["parent"] = parent
        if project_management is not UNSET:
            field_dict["projectManagement"] = project_management
        if purpose_of_funding is not UNSET:
            field_dict["purposeOfFunding"] = purpose_of_funding
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if status is not UNSET:
            field_dict["status"] = status
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_budget_source_foreigntext import FsResFinanceBudgetSourceForeigntext  # noqa: PLC0415
        from ..models.fs_res_finance_orgunit_simple import FsResFinanceOrgunitSimple  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResFinanceBudgetSourceForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResFinanceBudgetSourceForeigntext.from_dict(_field_foreigntext)

        _budget_source_category = d.pop("budgetSourceCategory", UNSET)
        budget_source_category: CsSysValueGenericValue | Unset
        if isinstance(_budget_source_category, Unset):
            budget_source_category = UNSET
        else:
            budget_source_category = CsSysValueGenericValue.from_dict(_budget_source_category)

        _budget_source_type = d.pop("budgetSourceType", UNSET)
        budget_source_type: CsSysValueGenericValue | Unset
        if isinstance(_budget_source_type, Unset):
            budget_source_type = UNSET
        else:
            budget_source_type = CsSysValueGenericValue.from_dict(_budget_source_type)

        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        _is_selectable = d.pop("isSelectable", UNSET)
        is_selectable: CsSysValueGenericValue | Unset
        if isinstance(_is_selectable, Unset):
            is_selectable = UNSET
        else:
            is_selectable = CsSysValueGenericValue.from_dict(_is_selectable)

        _kdsf_category = d.pop("kdsfCategory", UNSET)
        kdsf_category: CsSysValueGenericValue | Unset
        if isinstance(_kdsf_category, Unset):
            kdsf_category = UNSET
        else:
            kdsf_category = CsSysValueGenericValue.from_dict(_kdsf_category)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: FsResFinanceOrgunitSimple | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = FsResFinanceOrgunitSimple.from_dict(_organization)

        _parent = d.pop("parent", UNSET)
        parent: FsResFinanceBudgetSource | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FsResFinanceBudgetSource.from_dict(_parent)

        _project_management = d.pop("projectManagement", UNSET)
        project_management: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_project_management, Unset):
            project_management = UNSET
        else:
            project_management = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_project_management)

        purpose_of_funding = d.pop("purposeOfFunding", UNSET)

        _research_partner = d.pop("researchPartner", UNSET)
        research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_research_partner, Unset):
            research_partner = UNSET
        else:
            research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_research_partner)

        shorttext = d.pop("shorttext", UNSET)

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        uniquename = d.pop("uniquename", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        fs_res_finance_budget_source = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            budget_source_category=budget_source_category,
            budget_source_type=budget_source_type,
            defaulttext=defaulttext,
            id=id,
            is_selectable=is_selectable,
            kdsf_category=kdsf_category,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            organization=organization,
            parent=parent,
            project_management=project_management,
            purpose_of_funding=purpose_of_funding,
            research_partner=research_partner,
            shorttext=shorttext,
            status=status,
            uniquename=uniquename,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        fs_res_finance_budget_source.additional_properties = d
        return fs_res_finance_budget_source

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
