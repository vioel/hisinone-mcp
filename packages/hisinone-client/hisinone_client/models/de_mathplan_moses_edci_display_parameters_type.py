from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_image_object_type import DeMathplanMosesEdciImageObjectType
    from ..models.de_mathplan_moses_edci_key_language_string_type import DeMathplanMosesEdciKeyLanguageStringType


T = TypeVar("T", bound="DeMathplanMosesEdciDisplayParametersType")


@_attrs_define
class DeMathplanMosesEdciDisplayParametersType:
    """
    Attributes:
        background (DeMathplanMosesEdciImageObjectType | Unset):
        html (str | Unset):
        labels (list[DeMathplanMosesEdciKeyLanguageStringType] | Unset):
    """

    background: DeMathplanMosesEdciImageObjectType | Unset = UNSET
    html: str | Unset = UNSET
    labels: list[DeMathplanMosesEdciKeyLanguageStringType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        background: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background, Unset):
            background = self.background.to_dict()

        html = self.html

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background is not UNSET:
            field_dict["background"] = background
        if html is not UNSET:
            field_dict["html"] = html
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_image_object_type import DeMathplanMosesEdciImageObjectType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_key_language_string_type import DeMathplanMosesEdciKeyLanguageStringType  # noqa: PLC0415

        d = dict(src_dict)
        _background = d.pop("background", UNSET)
        background: DeMathplanMosesEdciImageObjectType | Unset
        if isinstance(_background, Unset):
            background = UNSET
        else:
            background = DeMathplanMosesEdciImageObjectType.from_dict(_background)

        html = d.pop("html", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[DeMathplanMosesEdciKeyLanguageStringType] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = DeMathplanMosesEdciKeyLanguageStringType.from_dict(labels_item_data)

                labels.append(labels_item)

        de_mathplan_moses_edci_display_parameters_type = cls(
            background=background,
            html=html,
            labels=labels,
        )

        de_mathplan_moses_edci_display_parameters_type.additional_properties = d
        return de_mathplan_moses_edci_display_parameters_type

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
