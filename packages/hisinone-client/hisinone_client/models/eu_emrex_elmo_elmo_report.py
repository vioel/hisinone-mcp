from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_attachment import EuEmrexElmoAttachment
    from ..models.eu_emrex_elmo_elmo_report_grading_scheme import EuEmrexElmoElmoReportGradingScheme
    from ..models.eu_emrex_elmo_elmo_report_issuer import EuEmrexElmoElmoReportIssuer
    from ..models.eu_emrex_elmo_learning_opportunity_specification import EuEmrexElmoLearningOpportunitySpecification
    from ..models.java_util_calendar import JavaUtilCalendar


T = TypeVar("T", bound="EuEmrexElmoElmoReport")


@_attrs_define
class EuEmrexElmoElmoReport:
    """
    Attributes:
        attachment (list[EuEmrexElmoAttachment] | Unset):
        grading_scheme (list[EuEmrexElmoElmoReportGradingScheme] | Unset):
        issue_date (JavaUtilCalendar | Unset):
        issuer (EuEmrexElmoElmoReportIssuer | Unset):
        learning_opportunity_specification (list[EuEmrexElmoLearningOpportunitySpecification] | Unset):
    """

    attachment: list[EuEmrexElmoAttachment] | Unset = UNSET
    grading_scheme: list[EuEmrexElmoElmoReportGradingScheme] | Unset = UNSET
    issue_date: JavaUtilCalendar | Unset = UNSET
    issuer: EuEmrexElmoElmoReportIssuer | Unset = UNSET
    learning_opportunity_specification: list[EuEmrexElmoLearningOpportunitySpecification] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attachment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = []
            for attachment_item_data in self.attachment:
                attachment_item = attachment_item_data.to_dict()
                attachment.append(attachment_item)

        grading_scheme: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grading_scheme, Unset):
            grading_scheme = []
            for grading_scheme_item_data in self.grading_scheme:
                grading_scheme_item = grading_scheme_item_data.to_dict()
                grading_scheme.append(grading_scheme_item)

        issue_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.to_dict()

        issuer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issuer, Unset):
            issuer = self.issuer.to_dict()

        learning_opportunity_specification: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.learning_opportunity_specification, Unset):
            learning_opportunity_specification = []
            for learning_opportunity_specification_item_data in self.learning_opportunity_specification:
                learning_opportunity_specification_item = learning_opportunity_specification_item_data.to_dict()
                learning_opportunity_specification.append(learning_opportunity_specification_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if grading_scheme is not UNSET:
            field_dict["gradingScheme"] = grading_scheme
        if issue_date is not UNSET:
            field_dict["issueDate"] = issue_date
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if learning_opportunity_specification is not UNSET:
            field_dict["learningOpportunitySpecification"] = learning_opportunity_specification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_attachment import EuEmrexElmoAttachment  # noqa: PLC0415
        from ..models.eu_emrex_elmo_elmo_report_grading_scheme import EuEmrexElmoElmoReportGradingScheme  # noqa: PLC0415
        from ..models.eu_emrex_elmo_elmo_report_issuer import EuEmrexElmoElmoReportIssuer  # noqa: PLC0415
        from ..models.eu_emrex_elmo_learning_opportunity_specification import (
            EuEmrexElmoLearningOpportunitySpecification,  # noqa: PLC0415
        )
        from ..models.java_util_calendar import JavaUtilCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _attachment = d.pop("attachment", UNSET)
        attachment: list[EuEmrexElmoAttachment] | Unset = UNSET
        if _attachment is not UNSET:
            attachment = []
            for attachment_item_data in _attachment:
                attachment_item = EuEmrexElmoAttachment.from_dict(attachment_item_data)

                attachment.append(attachment_item)

        _grading_scheme = d.pop("gradingScheme", UNSET)
        grading_scheme: list[EuEmrexElmoElmoReportGradingScheme] | Unset = UNSET
        if _grading_scheme is not UNSET:
            grading_scheme = []
            for grading_scheme_item_data in _grading_scheme:
                grading_scheme_item = EuEmrexElmoElmoReportGradingScheme.from_dict(grading_scheme_item_data)

                grading_scheme.append(grading_scheme_item)

        _issue_date = d.pop("issueDate", UNSET)
        issue_date: JavaUtilCalendar | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = JavaUtilCalendar.from_dict(_issue_date)

        _issuer = d.pop("issuer", UNSET)
        issuer: EuEmrexElmoElmoReportIssuer | Unset
        if isinstance(_issuer, Unset):
            issuer = UNSET
        else:
            issuer = EuEmrexElmoElmoReportIssuer.from_dict(_issuer)

        _learning_opportunity_specification = d.pop("learningOpportunitySpecification", UNSET)
        learning_opportunity_specification: list[EuEmrexElmoLearningOpportunitySpecification] | Unset = UNSET
        if _learning_opportunity_specification is not UNSET:
            learning_opportunity_specification = []
            for learning_opportunity_specification_item_data in _learning_opportunity_specification:
                learning_opportunity_specification_item = EuEmrexElmoLearningOpportunitySpecification.from_dict(
                    learning_opportunity_specification_item_data
                )

                learning_opportunity_specification.append(learning_opportunity_specification_item)

        eu_emrex_elmo_elmo_report = cls(
            attachment=attachment,
            grading_scheme=grading_scheme,
            issue_date=issue_date,
            issuer=issuer,
            learning_opportunity_specification=learning_opportunity_specification,
        )

        eu_emrex_elmo_elmo_report.additional_properties = d
        return eu_emrex_elmo_elmo_report

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
