from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance,
    )


T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifies")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifies:
    """
    Attributes:
        extension (EuEmrexElmoCustomExtensionsContainer | Unset):
        learning_opportunity_instance (EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance |
            Unset):
    """

    extension: EuEmrexElmoCustomExtensionsContainer | Unset = UNSET
    learning_opportunity_instance: (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension, Unset):
            extension = self.extension.to_dict()

        learning_opportunity_instance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.learning_opportunity_instance, Unset):
            learning_opportunity_instance = self.learning_opportunity_instance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extension is not UNSET:
            field_dict["extension"] = extension
        if learning_opportunity_instance is not UNSET:
            field_dict["learningOpportunityInstance"] = learning_opportunity_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer  # noqa: PLC0415
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _extension = d.pop("extension", UNSET)
        extension: EuEmrexElmoCustomExtensionsContainer | Unset
        if isinstance(_extension, Unset):
            extension = UNSET
        else:
            extension = EuEmrexElmoCustomExtensionsContainer.from_dict(_extension)

        _learning_opportunity_instance = d.pop("learningOpportunityInstance", UNSET)
        learning_opportunity_instance: (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance | Unset
        )
        if isinstance(_learning_opportunity_instance, Unset):
            learning_opportunity_instance = UNSET
        else:
            learning_opportunity_instance = (
                EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance.from_dict(
                    _learning_opportunity_instance
                )
            )

        eu_emrex_elmo_learning_opportunity_specification_specifies = cls(
            extension=extension,
            learning_opportunity_instance=learning_opportunity_instance,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies

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
