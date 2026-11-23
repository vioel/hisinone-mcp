from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_research_funds_foreigntext import FsResFinanceResearchFundsForeigntext


T = TypeVar("T", bound="FsResFinanceResearchFunds")


@_attrs_define
class FsResFinanceResearchFunds:
    """
    Attributes:
        field_foreigntext (FsResFinanceResearchFundsForeigntext | Unset):
        budget_position (CsSysValueGenericValue | Unset):
        budget_source_name (str | Unset):
        id (int | Unset):
        income_amount (float | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        research_fund_type (CsSysValueGenericValue | Unset):
        year (int | Unset):
    """

    field_foreigntext: FsResFinanceResearchFundsForeigntext | Unset = UNSET
    budget_position: CsSysValueGenericValue | Unset = UNSET
    budget_source_name: str | Unset = UNSET
    id: int | Unset = UNSET
    income_amount: float | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    research_fund_type: CsSysValueGenericValue | Unset = UNSET
    year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        budget_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_position, Unset):
            budget_position = self.budget_position.to_dict()

        budget_source_name = self.budget_source_name

        id = self.id

        income_amount = self.income_amount

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        research_fund_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_fund_type, Unset):
            research_fund_type = self.research_fund_type.to_dict()

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if budget_position is not UNSET:
            field_dict["budgetPosition"] = budget_position
        if budget_source_name is not UNSET:
            field_dict["budgetSourceName"] = budget_source_name
        if id is not UNSET:
            field_dict["id"] = id
        if income_amount is not UNSET:
            field_dict["incomeAmount"] = income_amount
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if research_fund_type is not UNSET:
            field_dict["researchFundType"] = research_fund_type
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_research_funds_foreigntext import FsResFinanceResearchFundsForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResFinanceResearchFundsForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResFinanceResearchFundsForeigntext.from_dict(_field_foreigntext)

        _budget_position = d.pop("budgetPosition", UNSET)
        budget_position: CsSysValueGenericValue | Unset
        if isinstance(_budget_position, Unset):
            budget_position = UNSET
        else:
            budget_position = CsSysValueGenericValue.from_dict(_budget_position)

        budget_source_name = d.pop("budgetSourceName", UNSET)

        id = d.pop("id", UNSET)

        income_amount = d.pop("incomeAmount", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _research_fund_type = d.pop("researchFundType", UNSET)
        research_fund_type: CsSysValueGenericValue | Unset
        if isinstance(_research_fund_type, Unset):
            research_fund_type = UNSET
        else:
            research_fund_type = CsSysValueGenericValue.from_dict(_research_fund_type)

        year = d.pop("year", UNSET)

        fs_res_finance_research_funds = cls(
            field_foreigntext=field_foreigntext,
            budget_position=budget_position,
            budget_source_name=budget_source_name,
            id=id,
            income_amount=income_amount,
            lock_version=lock_version,
            obj_guid=obj_guid,
            research_fund_type=research_fund_type,
            year=year,
        )

        fs_res_finance_research_funds.additional_properties = d
        return fs_res_finance_research_funds

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
