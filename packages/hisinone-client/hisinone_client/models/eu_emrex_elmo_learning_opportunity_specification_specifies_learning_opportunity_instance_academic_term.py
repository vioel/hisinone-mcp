from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang
    from ..models.java_util_calendar import JavaUtilCalendar


T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm:
    """
    Attributes:
        end (JavaUtilCalendar | Unset):
        start (JavaUtilCalendar | Unset):
        title (list[EuEmrexElmoTokenWithOptionalLang] | Unset):
    """

    end: JavaUtilCalendar | Unset = UNSET
    start: JavaUtilCalendar | Unset = UNSET
    title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang  # noqa: PLC0415
        from ..models.java_util_calendar import JavaUtilCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _end = d.pop("end", UNSET)
        end: JavaUtilCalendar | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = JavaUtilCalendar.from_dict(_end)

        _start = d.pop("start", UNSET)
        start: JavaUtilCalendar | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = JavaUtilCalendar.from_dict(_start)

        _title = d.pop("title", UNSET)
        title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = EuEmrexElmoTokenWithOptionalLang.from_dict(title_item_data)

                title.append(title_item)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_academic_term = cls(
            end=end,
            start=start,
            title=title,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_academic_term.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_academic_term

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
