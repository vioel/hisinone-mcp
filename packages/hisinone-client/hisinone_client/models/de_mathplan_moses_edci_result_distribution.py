from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType
    from ..models.de_mathplan_moses_edci_result_category import DeMathplanMosesEdciResultCategory


T = TypeVar("T", bound="DeMathplanMosesEdciResultDistribution")


@_attrs_define
class DeMathplanMosesEdciResultDistribution:
    """
    Attributes:
        category (list[DeMathplanMosesEdciResultCategory] | Unset):
        description (DeMathplanMosesEdciNoteType | Unset):
    """

    category: list[DeMathplanMosesEdciResultCategory] | Unset = UNSET
    description: DeMathplanMosesEdciNoteType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        category: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.to_dict()
                category.append(category_item)

        description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

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
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_result_category import DeMathplanMosesEdciResultCategory  # noqa: PLC0415

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: list[DeMathplanMosesEdciResultCategory] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = DeMathplanMosesEdciResultCategory.from_dict(category_item_data)

                category.append(category_item)

        _description = d.pop("description", UNSET)
        description: DeMathplanMosesEdciNoteType | Unset
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = DeMathplanMosesEdciNoteType.from_dict(_description)

        de_mathplan_moses_edci_result_distribution = cls(
            category=category,
            description=description,
        )

        de_mathplan_moses_edci_result_distribution.additional_properties = d
        return de_mathplan_moses_edci_result_distribution

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
