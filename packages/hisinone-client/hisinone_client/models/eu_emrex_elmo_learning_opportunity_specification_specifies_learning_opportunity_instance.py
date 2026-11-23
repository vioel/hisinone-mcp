from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer
    from ..models.eu_emrex_elmo_diploma_supplement import EuEmrexElmoDiplomaSupplement
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_academic_term import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_attachments import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAttachments,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_credit import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_grouping import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_identifier import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceIdentifier,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_level import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution,
    )
    from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_shortened_grading import (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading,
    )
    from ..models.java_util_calendar import JavaUtilCalendar


T = TypeVar("T", bound="EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance")


@_attrs_define
class EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstance:
    """
    Attributes:
        academic_term (EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm |
            Unset):
        attachments (EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAttachments |
            Unset):
        credit (list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit] | Unset):
        date (JavaUtilCalendar | Unset):
        diploma_supplement (EuEmrexElmoDiplomaSupplement | Unset):
        engagement_hours (float | Unset):
        extension (EuEmrexElmoCustomExtensionsContainer | Unset):
        grading_scheme_local_id (str | Unset):
        grouping (EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping | Unset):
        identifier (list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceIdentifier] |
            Unset):
        language_of_instruction (str | Unset):
        level (list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel] | Unset):
        result_distribution
            (EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution | Unset):
        result_label (str | Unset):
        shortened_grading
            (EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading | Unset):
        start (JavaUtilCalendar | Unset):
        status (str | Unset):
    """

    academic_term: (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm | Unset
    ) = UNSET
    attachments: EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAttachments | Unset = (
        UNSET
    )
    credit: list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit] | Unset = UNSET
    date: JavaUtilCalendar | Unset = UNSET
    diploma_supplement: EuEmrexElmoDiplomaSupplement | Unset = UNSET
    engagement_hours: float | Unset = UNSET
    extension: EuEmrexElmoCustomExtensionsContainer | Unset = UNSET
    grading_scheme_local_id: str | Unset = UNSET
    grouping: EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping | Unset = UNSET
    identifier: (
        list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceIdentifier] | Unset
    ) = UNSET
    language_of_instruction: str | Unset = UNSET
    level: list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel] | Unset = UNSET
    result_distribution: (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution | Unset
    ) = UNSET
    result_label: str | Unset = UNSET
    shortened_grading: (
        EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading | Unset
    ) = UNSET
    start: JavaUtilCalendar | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        academic_term: dict[str, Any] | Unset = UNSET
        if not isinstance(self.academic_term, Unset):
            academic_term = self.academic_term.to_dict()

        attachments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        credit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credit, Unset):
            credit = []
            for credit_item_data in self.credit:
                credit_item = credit_item_data.to_dict()
                credit.append(credit_item)

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        diploma_supplement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diploma_supplement, Unset):
            diploma_supplement = self.diploma_supplement.to_dict()

        engagement_hours = self.engagement_hours

        extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension, Unset):
            extension = self.extension.to_dict()

        grading_scheme_local_id = self.grading_scheme_local_id

        grouping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grouping, Unset):
            grouping = self.grouping.to_dict()

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        language_of_instruction = self.language_of_instruction

        level: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = []
            for level_item_data in self.level:
                level_item = level_item_data.to_dict()
                level.append(level_item)

        result_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result_distribution, Unset):
            result_distribution = self.result_distribution.to_dict()

        result_label = self.result_label

        shortened_grading: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shortened_grading, Unset):
            shortened_grading = self.shortened_grading.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if academic_term is not UNSET:
            field_dict["academicTerm"] = academic_term
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if credit is not UNSET:
            field_dict["credit"] = credit
        if date is not UNSET:
            field_dict["date"] = date
        if diploma_supplement is not UNSET:
            field_dict["diplomaSupplement"] = diploma_supplement
        if engagement_hours is not UNSET:
            field_dict["engagementHours"] = engagement_hours
        if extension is not UNSET:
            field_dict["extension"] = extension
        if grading_scheme_local_id is not UNSET:
            field_dict["gradingSchemeLocalId"] = grading_scheme_local_id
        if grouping is not UNSET:
            field_dict["grouping"] = grouping
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if language_of_instruction is not UNSET:
            field_dict["languageOfInstruction"] = language_of_instruction
        if level is not UNSET:
            field_dict["level"] = level
        if result_distribution is not UNSET:
            field_dict["resultDistribution"] = result_distribution
        if result_label is not UNSET:
            field_dict["resultLabel"] = result_label
        if shortened_grading is not UNSET:
            field_dict["shortenedGrading"] = shortened_grading
        if start is not UNSET:
            field_dict["start"] = start
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer  # noqa: PLC0415
        from ..models.eu_emrex_elmo_diploma_supplement import EuEmrexElmoDiplomaSupplement  # noqa: PLC0415
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_academic_term import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_attachments import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAttachments,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_credit import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_grouping import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_identifier import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceIdentifier,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_level import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_result_distribution import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution,  # noqa: PLC0415
        )
        from ..models.eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance_shortened_grading import (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading,  # noqa: PLC0415
        )
        from ..models.java_util_calendar import JavaUtilCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _academic_term = d.pop("academicTerm", UNSET)
        academic_term: (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm | Unset
        )
        if isinstance(_academic_term, Unset):
            academic_term = UNSET
        else:
            academic_term = (
                EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAcademicTerm.from_dict(
                    _academic_term
                )
            )

        _attachments = d.pop("attachments", UNSET)
        attachments: EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAttachments | Unset
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = (
                EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceAttachments.from_dict(
                    _attachments
                )
            )

        _credit = d.pop("credit", UNSET)
        credit: list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit] | Unset = (
            UNSET
        )
        if _credit is not UNSET:
            credit = []
            for credit_item_data in _credit:
                credit_item = (
                    EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceCredit.from_dict(
                        credit_item_data
                    )
                )

                credit.append(credit_item)

        _date = d.pop("date", UNSET)
        date: JavaUtilCalendar | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = JavaUtilCalendar.from_dict(_date)

        _diploma_supplement = d.pop("diplomaSupplement", UNSET)
        diploma_supplement: EuEmrexElmoDiplomaSupplement | Unset
        if isinstance(_diploma_supplement, Unset):
            diploma_supplement = UNSET
        else:
            diploma_supplement = EuEmrexElmoDiplomaSupplement.from_dict(_diploma_supplement)

        engagement_hours = d.pop("engagementHours", UNSET)

        _extension = d.pop("extension", UNSET)
        extension: EuEmrexElmoCustomExtensionsContainer | Unset
        if isinstance(_extension, Unset):
            extension = UNSET
        else:
            extension = EuEmrexElmoCustomExtensionsContainer.from_dict(_extension)

        grading_scheme_local_id = d.pop("gradingSchemeLocalId", UNSET)

        _grouping = d.pop("grouping", UNSET)
        grouping: EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping | Unset
        if isinstance(_grouping, Unset):
            grouping = UNSET
        else:
            grouping = (
                EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceGrouping.from_dict(
                    _grouping
                )
            )

        _identifier = d.pop("identifier", UNSET)
        identifier: (
            list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceIdentifier] | Unset
        ) = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = (
                    EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceIdentifier.from_dict(
                        identifier_item_data
                    )
                )

                identifier.append(identifier_item)

        language_of_instruction = d.pop("languageOfInstruction", UNSET)

        _level = d.pop("level", UNSET)
        level: list[EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel] | Unset = (
            UNSET
        )
        if _level is not UNSET:
            level = []
            for level_item_data in _level:
                level_item = (
                    EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceLevel.from_dict(
                        level_item_data
                    )
                )

                level.append(level_item)

        _result_distribution = d.pop("resultDistribution", UNSET)
        result_distribution: (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution | Unset
        )
        if isinstance(_result_distribution, Unset):
            result_distribution = UNSET
        else:
            result_distribution = EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceResultDistribution.from_dict(
                _result_distribution
            )

        result_label = d.pop("resultLabel", UNSET)

        _shortened_grading = d.pop("shortenedGrading", UNSET)
        shortened_grading: (
            EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading | Unset
        )
        if isinstance(_shortened_grading, Unset):
            shortened_grading = UNSET
        else:
            shortened_grading = EuEmrexElmoLearningOpportunitySpecificationSpecifiesLearningOpportunityInstanceShortenedGrading.from_dict(
                _shortened_grading
            )

        _start = d.pop("start", UNSET)
        start: JavaUtilCalendar | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = JavaUtilCalendar.from_dict(_start)

        status = d.pop("status", UNSET)

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance = cls(
            academic_term=academic_term,
            attachments=attachments,
            credit=credit,
            date=date,
            diploma_supplement=diploma_supplement,
            engagement_hours=engagement_hours,
            extension=extension,
            grading_scheme_local_id=grading_scheme_local_id,
            grouping=grouping,
            identifier=identifier,
            language_of_instruction=language_of_instruction,
            level=level,
            result_distribution=result_distribution,
            result_label=result_label,
            shortened_grading=shortened_grading,
            start=start,
            status=status,
        )

        eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance.additional_properties = d
        return eu_emrex_elmo_learning_opportunity_specification_specifies_learning_opportunity_instance

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
