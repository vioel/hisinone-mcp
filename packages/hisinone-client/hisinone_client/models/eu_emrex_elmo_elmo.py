from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_attachment import EuEmrexElmoAttachment
    from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer
    from ..models.eu_emrex_elmo_elmo_learner import EuEmrexElmoElmoLearner
    from ..models.eu_emrex_elmo_elmo_report import EuEmrexElmoElmoReport
    from ..models.eu_emrex_elmo_groups import EuEmrexElmoGroups
    from ..models.eu_emrex_elmo_signature_type import EuEmrexElmoSignatureType
    from ..models.java_util_calendar import JavaUtilCalendar


T = TypeVar("T", bound="EuEmrexElmoElmo")


@_attrs_define
class EuEmrexElmoElmo:
    """
    Attributes:
        attachment (list[EuEmrexElmoAttachment] | Unset):
        extension (EuEmrexElmoCustomExtensionsContainer | Unset):
        generated_date (JavaUtilCalendar | Unset):
        groups (EuEmrexElmoGroups | Unset):
        learner (EuEmrexElmoElmoLearner | Unset):
        report (list[EuEmrexElmoElmoReport] | Unset):
        signature (EuEmrexElmoSignatureType | Unset):
    """

    attachment: list[EuEmrexElmoAttachment] | Unset = UNSET
    extension: EuEmrexElmoCustomExtensionsContainer | Unset = UNSET
    generated_date: JavaUtilCalendar | Unset = UNSET
    groups: EuEmrexElmoGroups | Unset = UNSET
    learner: EuEmrexElmoElmoLearner | Unset = UNSET
    report: list[EuEmrexElmoElmoReport] | Unset = UNSET
    signature: EuEmrexElmoSignatureType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attachment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = []
            for attachment_item_data in self.attachment:
                attachment_item = attachment_item_data.to_dict()
                attachment.append(attachment_item)

        extension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension, Unset):
            extension = self.extension.to_dict()

        generated_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.generated_date, Unset):
            generated_date = self.generated_date.to_dict()

        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        learner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.learner, Unset):
            learner = self.learner.to_dict()

        report: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.report, Unset):
            report = []
            for report_item_data in self.report:
                report_item = report_item_data.to_dict()
                report.append(report_item)

        signature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if extension is not UNSET:
            field_dict["extension"] = extension
        if generated_date is not UNSET:
            field_dict["generatedDate"] = generated_date
        if groups is not UNSET:
            field_dict["groups"] = groups
        if learner is not UNSET:
            field_dict["learner"] = learner
        if report is not UNSET:
            field_dict["report"] = report
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_attachment import EuEmrexElmoAttachment  # noqa: PLC0415
        from ..models.eu_emrex_elmo_custom_extensions_container import EuEmrexElmoCustomExtensionsContainer  # noqa: PLC0415
        from ..models.eu_emrex_elmo_elmo_learner import EuEmrexElmoElmoLearner  # noqa: PLC0415
        from ..models.eu_emrex_elmo_elmo_report import EuEmrexElmoElmoReport  # noqa: PLC0415
        from ..models.eu_emrex_elmo_groups import EuEmrexElmoGroups  # noqa: PLC0415
        from ..models.eu_emrex_elmo_signature_type import EuEmrexElmoSignatureType  # noqa: PLC0415
        from ..models.java_util_calendar import JavaUtilCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _attachment = d.pop("attachment", UNSET)
        attachment: list[EuEmrexElmoAttachment] | Unset = UNSET
        if _attachment is not UNSET:
            attachment = []
            for attachment_item_data in _attachment:
                attachment_item = EuEmrexElmoAttachment.from_dict(attachment_item_data)

                attachment.append(attachment_item)

        _extension = d.pop("extension", UNSET)
        extension: EuEmrexElmoCustomExtensionsContainer | Unset
        if isinstance(_extension, Unset):
            extension = UNSET
        else:
            extension = EuEmrexElmoCustomExtensionsContainer.from_dict(_extension)

        _generated_date = d.pop("generatedDate", UNSET)
        generated_date: JavaUtilCalendar | Unset
        if isinstance(_generated_date, Unset):
            generated_date = UNSET
        else:
            generated_date = JavaUtilCalendar.from_dict(_generated_date)

        _groups = d.pop("groups", UNSET)
        groups: EuEmrexElmoGroups | Unset
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = EuEmrexElmoGroups.from_dict(_groups)

        _learner = d.pop("learner", UNSET)
        learner: EuEmrexElmoElmoLearner | Unset
        if isinstance(_learner, Unset):
            learner = UNSET
        else:
            learner = EuEmrexElmoElmoLearner.from_dict(_learner)

        _report = d.pop("report", UNSET)
        report: list[EuEmrexElmoElmoReport] | Unset = UNSET
        if _report is not UNSET:
            report = []
            for report_item_data in _report:
                report_item = EuEmrexElmoElmoReport.from_dict(report_item_data)

                report.append(report_item)

        _signature = d.pop("signature", UNSET)
        signature: EuEmrexElmoSignatureType | Unset
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = EuEmrexElmoSignatureType.from_dict(_signature)

        eu_emrex_elmo_elmo = cls(
            attachment=attachment,
            extension=extension,
            generated_date=generated_date,
            groups=groups,
            learner=learner,
            report=report,
            signature=signature,
        )

        eu_emrex_elmo_elmo.additional_properties = d
        return eu_emrex_elmo_elmo

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
