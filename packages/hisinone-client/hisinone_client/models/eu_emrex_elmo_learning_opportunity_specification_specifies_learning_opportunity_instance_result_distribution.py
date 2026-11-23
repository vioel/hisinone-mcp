from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution_category import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory,
    )
    from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
        EuEmrexElmoPlaintextMultilineStringWithOptionalLang,
    )


T = TypeVar(
    "T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution"
)


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution:
    """
    Attributes:
        category
            (list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory]
            | Unset):
        description (list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset):
    """

    category: (
        list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory]
        | Unset
    ) = UNSET
    description: list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        category: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.to_dict()
                category.append(category_item)

        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution_category import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_plaintext_multiline_string_with_optional_lang import (
            EuEmrexElmoPlaintextMultilineStringWithOptionalLang,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: (
            list[
                EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory
            ]
            | Unset
        ) = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistributionCategory.from_dict(
                    category_item_data
                )

                category.append(category_item)

        _description = d.pop("description", UNSET)
        description: list[EuEmrexElmoPlaintextMultilineStringWithOptionalLang] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = EuEmrexElmoPlaintextMultilineStringWithOptionalLang.from_dict(description_item_data)

                description.append(description_item)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution = (
            cls(
                category=category,
                description=description,
            )
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution.additional_properties = d
        return (
            eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution
        )

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
