from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_travelmanagement_businesstripapplication_assets_foreigntext import (
        RmErpTravelmanagementBusinesstripapplicationAssetsForeigntext,
    )


T = TypeVar("T", bound="RmErpTravelmanagementBusinesstripapplicationAssets")


@_attrs_define
class RmErpTravelmanagementBusinesstripapplicationAssets:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementBusinesstripapplicationAssetsForeigntext | Unset):
        cost_coverage (RmErpCommonErpGenericValue | Unset):
        cost_coverage_amount (int | Unset):
        faculty_resources_amount (int | Unset):
        faculty_resources_approved (RmErpCommonErpGenericValue | Unset):
        faculty_resources_requested (RmErpCommonErpGenericValue | Unset):
        fee (RmErpCommonErpGenericValue | Unset):
        fee_amount (int | Unset):
        id (int | Unset):
        international_budget (RmErpCommonErpGenericValue | Unset):
        international_budget_amount (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        own_project_funds (RmErpCommonErpGenericValue | Unset):
        own_project_funds_amount (int | Unset):
        research_funds_amount (int | Unset):
        research_funds_approved (RmErpCommonErpGenericValue | Unset):
        research_funds_requested (RmErpCommonErpGenericValue | Unset):
    """

    field_foreigntext: RmErpTravelmanagementBusinesstripapplicationAssetsForeigntext | Unset = UNSET
    cost_coverage: RmErpCommonErpGenericValue | Unset = UNSET
    cost_coverage_amount: int | Unset = UNSET
    faculty_resources_amount: int | Unset = UNSET
    faculty_resources_approved: RmErpCommonErpGenericValue | Unset = UNSET
    faculty_resources_requested: RmErpCommonErpGenericValue | Unset = UNSET
    fee: RmErpCommonErpGenericValue | Unset = UNSET
    fee_amount: int | Unset = UNSET
    id: int | Unset = UNSET
    international_budget: RmErpCommonErpGenericValue | Unset = UNSET
    international_budget_amount: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    own_project_funds: RmErpCommonErpGenericValue | Unset = UNSET
    own_project_funds_amount: int | Unset = UNSET
    research_funds_amount: int | Unset = UNSET
    research_funds_approved: RmErpCommonErpGenericValue | Unset = UNSET
    research_funds_requested: RmErpCommonErpGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        cost_coverage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_coverage, Unset):
            cost_coverage = self.cost_coverage.to_dict()

        cost_coverage_amount = self.cost_coverage_amount

        faculty_resources_amount = self.faculty_resources_amount

        faculty_resources_approved: dict[str, Any] | Unset = UNSET
        if not isinstance(self.faculty_resources_approved, Unset):
            faculty_resources_approved = self.faculty_resources_approved.to_dict()

        faculty_resources_requested: dict[str, Any] | Unset = UNSET
        if not isinstance(self.faculty_resources_requested, Unset):
            faculty_resources_requested = self.faculty_resources_requested.to_dict()

        fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fee, Unset):
            fee = self.fee.to_dict()

        fee_amount = self.fee_amount

        id = self.id

        international_budget: dict[str, Any] | Unset = UNSET
        if not isinstance(self.international_budget, Unset):
            international_budget = self.international_budget.to_dict()

        international_budget_amount = self.international_budget_amount

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        own_project_funds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.own_project_funds, Unset):
            own_project_funds = self.own_project_funds.to_dict()

        own_project_funds_amount = self.own_project_funds_amount

        research_funds_amount = self.research_funds_amount

        research_funds_approved: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_funds_approved, Unset):
            research_funds_approved = self.research_funds_approved.to_dict()

        research_funds_requested: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_funds_requested, Unset):
            research_funds_requested = self.research_funds_requested.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if cost_coverage is not UNSET:
            field_dict["costCoverage"] = cost_coverage
        if cost_coverage_amount is not UNSET:
            field_dict["costCoverageAmount"] = cost_coverage_amount
        if faculty_resources_amount is not UNSET:
            field_dict["facultyResourcesAmount"] = faculty_resources_amount
        if faculty_resources_approved is not UNSET:
            field_dict["facultyResourcesApproved"] = faculty_resources_approved
        if faculty_resources_requested is not UNSET:
            field_dict["facultyResourcesRequested"] = faculty_resources_requested
        if fee is not UNSET:
            field_dict["fee"] = fee
        if fee_amount is not UNSET:
            field_dict["feeAmount"] = fee_amount
        if id is not UNSET:
            field_dict["id"] = id
        if international_budget is not UNSET:
            field_dict["internationalBudget"] = international_budget
        if international_budget_amount is not UNSET:
            field_dict["internationalBudgetAmount"] = international_budget_amount
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if own_project_funds is not UNSET:
            field_dict["ownProjectFunds"] = own_project_funds
        if own_project_funds_amount is not UNSET:
            field_dict["ownProjectFundsAmount"] = own_project_funds_amount
        if research_funds_amount is not UNSET:
            field_dict["researchFundsAmount"] = research_funds_amount
        if research_funds_approved is not UNSET:
            field_dict["researchFundsApproved"] = research_funds_approved
        if research_funds_requested is not UNSET:
            field_dict["researchFundsRequested"] = research_funds_requested

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_travelmanagement_businesstripapplication_assets_foreigntext import (
            RmErpTravelmanagementBusinesstripapplicationAssetsForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTravelmanagementBusinesstripapplicationAssetsForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpTravelmanagementBusinesstripapplicationAssetsForeigntext.from_dict(
                _field_foreigntext
            )

        _cost_coverage = d.pop("costCoverage", UNSET)
        cost_coverage: RmErpCommonErpGenericValue | Unset
        if isinstance(_cost_coverage, Unset):
            cost_coverage = UNSET
        else:
            cost_coverage = RmErpCommonErpGenericValue.from_dict(_cost_coverage)

        cost_coverage_amount = d.pop("costCoverageAmount", UNSET)

        faculty_resources_amount = d.pop("facultyResourcesAmount", UNSET)

        _faculty_resources_approved = d.pop("facultyResourcesApproved", UNSET)
        faculty_resources_approved: RmErpCommonErpGenericValue | Unset
        if isinstance(_faculty_resources_approved, Unset):
            faculty_resources_approved = UNSET
        else:
            faculty_resources_approved = RmErpCommonErpGenericValue.from_dict(_faculty_resources_approved)

        _faculty_resources_requested = d.pop("facultyResourcesRequested", UNSET)
        faculty_resources_requested: RmErpCommonErpGenericValue | Unset
        if isinstance(_faculty_resources_requested, Unset):
            faculty_resources_requested = UNSET
        else:
            faculty_resources_requested = RmErpCommonErpGenericValue.from_dict(_faculty_resources_requested)

        _fee = d.pop("fee", UNSET)
        fee: RmErpCommonErpGenericValue | Unset
        if isinstance(_fee, Unset):
            fee = UNSET
        else:
            fee = RmErpCommonErpGenericValue.from_dict(_fee)

        fee_amount = d.pop("feeAmount", UNSET)

        id = d.pop("id", UNSET)

        _international_budget = d.pop("internationalBudget", UNSET)
        international_budget: RmErpCommonErpGenericValue | Unset
        if isinstance(_international_budget, Unset):
            international_budget = UNSET
        else:
            international_budget = RmErpCommonErpGenericValue.from_dict(_international_budget)

        international_budget_amount = d.pop("internationalBudgetAmount", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _own_project_funds = d.pop("ownProjectFunds", UNSET)
        own_project_funds: RmErpCommonErpGenericValue | Unset
        if isinstance(_own_project_funds, Unset):
            own_project_funds = UNSET
        else:
            own_project_funds = RmErpCommonErpGenericValue.from_dict(_own_project_funds)

        own_project_funds_amount = d.pop("ownProjectFundsAmount", UNSET)

        research_funds_amount = d.pop("researchFundsAmount", UNSET)

        _research_funds_approved = d.pop("researchFundsApproved", UNSET)
        research_funds_approved: RmErpCommonErpGenericValue | Unset
        if isinstance(_research_funds_approved, Unset):
            research_funds_approved = UNSET
        else:
            research_funds_approved = RmErpCommonErpGenericValue.from_dict(_research_funds_approved)

        _research_funds_requested = d.pop("researchFundsRequested", UNSET)
        research_funds_requested: RmErpCommonErpGenericValue | Unset
        if isinstance(_research_funds_requested, Unset):
            research_funds_requested = UNSET
        else:
            research_funds_requested = RmErpCommonErpGenericValue.from_dict(_research_funds_requested)

        rm_erp_travelmanagement_businesstripapplication_assets = cls(
            field_foreigntext=field_foreigntext,
            cost_coverage=cost_coverage,
            cost_coverage_amount=cost_coverage_amount,
            faculty_resources_amount=faculty_resources_amount,
            faculty_resources_approved=faculty_resources_approved,
            faculty_resources_requested=faculty_resources_requested,
            fee=fee,
            fee_amount=fee_amount,
            id=id,
            international_budget=international_budget,
            international_budget_amount=international_budget_amount,
            lock_version=lock_version,
            obj_guid=obj_guid,
            own_project_funds=own_project_funds,
            own_project_funds_amount=own_project_funds_amount,
            research_funds_amount=research_funds_amount,
            research_funds_approved=research_funds_approved,
            research_funds_requested=research_funds_requested,
        )

        rm_erp_travelmanagement_businesstripapplication_assets.additional_properties = d
        return rm_erp_travelmanagement_businesstripapplication_assets

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
