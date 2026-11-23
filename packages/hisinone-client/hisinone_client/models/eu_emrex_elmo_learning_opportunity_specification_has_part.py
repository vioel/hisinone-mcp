from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_learning_opportunity_specification import EuEmrexElmoLearningOpportunitySpecification


T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationHasPart")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationHasPart:
    """
    Attributes:
        learning_opportunity_specification (EuEmrexElmoLearningOpportunitySpecification | Unset):
    """

    learning_opportunity_specification: EuEmrexElmoLearningOpportunitySpecification | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        learning_opportunity_specification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.learning_opportunity_specification, Unset):
            learning_opportunity_specification = self.learning_opportunity_specification.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if learning_opportunity_specification is not UNSET:
            field_dict["learningOpportunitySpecification"] = learning_opportunity_specification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_learning_opportunity_specification import (
            EuEmrexElmoLearningOpportunitySpecification,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _learning_opportunity_specification = d.pop("learningOpportunitySpecification", UNSET)
        learning_opportunity_specification: EuEmrexElmoLearningOpportunitySpecification | Unset
        if isinstance(_learning_opportunity_specification, Unset):
            learning_opportunity_specification = UNSET
        else:
            learning_opportunity_specification = EuEmrexElmoLearningOpportunitySpecification.from_dict(
                _learning_opportunity_specification
            )

        eu_emrex_elmo_learning_opportunity_specification_has_part = cls(
            learning_opportunity_specification=learning_opportunity_specification,
        )

        eu_emrex_elmo_learning_opportunity_specification_has_part.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_has_part

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
