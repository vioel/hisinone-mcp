from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search_criteria_operator import (
        CsSysGenericSearchSearchResultHisSearchCriteriaOperator,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchResultHisSearchCriteria")


@_attrs_define
class CsSysGenericSearchSearchResultHisSearchCriteria:
    """
    Attributes:
        field (str | Unset):
        not_ (bool | Unset):
        operator (CsSysGenericSearchSearchResultHisSearchCriteriaOperator | Unset):
        value (str | Unset):
    """

    field: str | Unset = UNSET
    not_: bool | Unset = UNSET
    operator: CsSysGenericSearchSearchResultHisSearchCriteriaOperator | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        not_ = self.not_

        operator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if not_ is not UNSET:
            field_dict["not"] = not_
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search_criteria_operator import (
            CsSysGenericSearchSearchResultHisSearchCriteriaOperator,  # noqa: PLC0415
        )

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        not_ = d.pop("not", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: CsSysGenericSearchSearchResultHisSearchCriteriaOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = CsSysGenericSearchSearchResultHisSearchCriteriaOperator.from_dict(_operator)

        value = d.pop("value", UNSET)

        cs_sys_generic_search_search_result_his_search_criteria = cls(
            field=field,
            not_=not_,
            operator=operator,
            value=value,
        )

        cs_sys_generic_search_search_result_his_search_criteria.additional_properties = d
        return cs_sys_generic_search_search_result_his_search_criteria

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
