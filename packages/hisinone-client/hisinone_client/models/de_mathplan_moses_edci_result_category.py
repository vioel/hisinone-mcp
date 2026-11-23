from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_text_score_type import DeMathplanMosesEdciTextScoreType
    from ..models.java_math_big_integer import JavaMathBigInteger


T = TypeVar("T", bound="DeMathplanMosesEdciResultCategory")


@_attrs_define
class DeMathplanMosesEdciResultCategory:
    """
    Attributes:
        count (JavaMathBigInteger | Unset):
        label (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        max_score (DeMathplanMosesEdciTextScoreType | Unset):
        min_score (DeMathplanMosesEdciTextScoreType | Unset):
        score (DeMathplanMosesEdciTextScoreType | Unset):
    """

    count: JavaMathBigInteger | Unset = UNSET
    label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    max_score: DeMathplanMosesEdciTextScoreType | Unset = UNSET
    min_score: DeMathplanMosesEdciTextScoreType | Unset = UNSET
    score: DeMathplanMosesEdciTextScoreType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        label: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = []
            for label_item_data in self.label:
                label_item = label_item_data.to_dict()
                label.append(label_item)

        max_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_score, Unset):
            max_score = self.max_score.to_dict()

        min_score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_score, Unset):
            min_score = self.min_score.to_dict()

        score: dict[str, Any] | Unset = UNSET
        if not isinstance(self.score, Unset):
            score = self.score.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if label is not UNSET:
            field_dict["label"] = label
        if max_score is not UNSET:
            field_dict["maxScore"] = max_score
        if min_score is not UNSET:
            field_dict["minScore"] = min_score
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_score_type import DeMathplanMosesEdciTextScoreType  # noqa: PLC0415
        from ..models.java_math_big_integer import JavaMathBigInteger  # noqa: PLC0415

        d = dict(src_dict)
        _count = d.pop("count", UNSET)
        count: JavaMathBigInteger | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = JavaMathBigInteger.from_dict(_count)

        _label = d.pop("label", UNSET)
        label: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _label is not UNSET:
            label = []
            for label_item_data in _label:
                label_item = DeMathplanMosesEdciLanguageStringType.from_dict(label_item_data)

                label.append(label_item)

        _max_score = d.pop("maxScore", UNSET)
        max_score: DeMathplanMosesEdciTextScoreType | Unset
        if isinstance(_max_score, Unset):
            max_score = UNSET
        else:
            max_score = DeMathplanMosesEdciTextScoreType.from_dict(_max_score)

        _min_score = d.pop("minScore", UNSET)
        min_score: DeMathplanMosesEdciTextScoreType | Unset
        if isinstance(_min_score, Unset):
            min_score = UNSET
        else:
            min_score = DeMathplanMosesEdciTextScoreType.from_dict(_min_score)

        _score = d.pop("score", UNSET)
        score: DeMathplanMosesEdciTextScoreType | Unset
        if isinstance(_score, Unset):
            score = UNSET
        else:
            score = DeMathplanMosesEdciTextScoreType.from_dict(_score)

        de_mathplan_moses_edci_result_category = cls(
            count=count,
            label=label,
            max_score=max_score,
            min_score=min_score,
            score=score,
        )

        de_mathplan_moses_edci_result_category.additional_properties = d
        return de_mathplan_moses_edci_result_category

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
