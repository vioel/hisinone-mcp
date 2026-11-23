from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_budget_source import FsResFinanceBudgetSource
    from ..models.fs_res_finance_research_contract_foreigntext import FsResFinanceResearchContractForeigntext
    from ..models.fs_res_finance_research_funds import FsResFinanceResearchFunds


T = TypeVar("T", bound="FsResFinanceResearchContract")


@_attrs_define
class FsResFinanceResearchContract:
    """
    Attributes:
        field_foreigntext (FsResFinanceResearchContractForeigntext | Unset):
        budget_source (FsResFinanceBudgetSource | Unset):
        commentary (str | Unset):
        contract_name (str | Unset):
        external_reference_number (str | Unset):
        funder_name (str | Unset):
        id (int | Unset):
        incomes (list[FsResFinanceResearchFunds] | Unset):
        internal_reference_number (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        request_funds (list[FsResFinanceResearchFunds] | Unset):
        status (CsSysValueGenericValue | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: FsResFinanceResearchContractForeigntext | Unset = UNSET
    budget_source: FsResFinanceBudgetSource | Unset = UNSET
    commentary: str | Unset = UNSET
    contract_name: str | Unset = UNSET
    external_reference_number: str | Unset = UNSET
    funder_name: str | Unset = UNSET
    id: int | Unset = UNSET
    incomes: list[FsResFinanceResearchFunds] | Unset = UNSET
    internal_reference_number: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    request_funds: list[FsResFinanceResearchFunds] | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        budget_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.budget_source, Unset):
            budget_source = self.budget_source.to_dict()

        commentary = self.commentary

        contract_name = self.contract_name

        external_reference_number = self.external_reference_number

        funder_name = self.funder_name

        id = self.id

        incomes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incomes, Unset):
            incomes = []
            for incomes_item_data in self.incomes:
                incomes_item = incomes_item_data.to_dict()
                incomes.append(incomes_item)

        internal_reference_number = self.internal_reference_number

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        request_funds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.request_funds, Unset):
            request_funds = []
            for request_funds_item_data in self.request_funds:
                request_funds_item = request_funds_item_data.to_dict()
                request_funds.append(request_funds_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if budget_source is not UNSET:
            field_dict["budgetSource"] = budget_source
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if contract_name is not UNSET:
            field_dict["contractName"] = contract_name
        if external_reference_number is not UNSET:
            field_dict["externalReferenceNumber"] = external_reference_number
        if funder_name is not UNSET:
            field_dict["funderName"] = funder_name
        if id is not UNSET:
            field_dict["id"] = id
        if incomes is not UNSET:
            field_dict["incomes"] = incomes
        if internal_reference_number is not UNSET:
            field_dict["internalReferenceNumber"] = internal_reference_number
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if request_funds is not UNSET:
            field_dict["requestFunds"] = request_funds
        if status is not UNSET:
            field_dict["status"] = status
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_budget_source import FsResFinanceBudgetSource  # noqa: PLC0415
        from ..models.fs_res_finance_research_contract_foreigntext import FsResFinanceResearchContractForeigntext  # noqa: PLC0415
        from ..models.fs_res_finance_research_funds import FsResFinanceResearchFunds  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResFinanceResearchContractForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResFinanceResearchContractForeigntext.from_dict(_field_foreigntext)

        _budget_source = d.pop("budgetSource", UNSET)
        budget_source: FsResFinanceBudgetSource | Unset
        if isinstance(_budget_source, Unset):
            budget_source = UNSET
        else:
            budget_source = FsResFinanceBudgetSource.from_dict(_budget_source)

        commentary = d.pop("commentary", UNSET)

        contract_name = d.pop("contractName", UNSET)

        external_reference_number = d.pop("externalReferenceNumber", UNSET)

        funder_name = d.pop("funderName", UNSET)

        id = d.pop("id", UNSET)

        _incomes = d.pop("incomes", UNSET)
        incomes: list[FsResFinanceResearchFunds] | Unset = UNSET
        if _incomes is not UNSET:
            incomes = []
            for incomes_item_data in _incomes:
                incomes_item = FsResFinanceResearchFunds.from_dict(incomes_item_data)

                incomes.append(incomes_item)

        internal_reference_number = d.pop("internalReferenceNumber", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _request_funds = d.pop("requestFunds", UNSET)
        request_funds: list[FsResFinanceResearchFunds] | Unset = UNSET
        if _request_funds is not UNSET:
            request_funds = []
            for request_funds_item_data in _request_funds:
                request_funds_item = FsResFinanceResearchFunds.from_dict(request_funds_item_data)

                request_funds.append(request_funds_item)

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        fs_res_finance_research_contract = cls(
            field_foreigntext=field_foreigntext,
            budget_source=budget_source,
            commentary=commentary,
            contract_name=contract_name,
            external_reference_number=external_reference_number,
            funder_name=funder_name,
            id=id,
            incomes=incomes,
            internal_reference_number=internal_reference_number,
            lock_version=lock_version,
            obj_guid=obj_guid,
            request_funds=request_funds,
            status=status,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        fs_res_finance_research_contract.additional_properties = d
        return fs_res_finance_research_contract

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
