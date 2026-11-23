from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term_foreigntext import (
        ModelCmAppBackendEntranceExaminationEntranceExamTermForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationEntranceExamTerm")


@_attrs_define
class ModelCmAppBackendEntranceExaminationEntranceExamTerm:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationEntranceExamTermForeigntext | Unset):
        default_application_term (bool | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        released_term_period_id (int | Unset):
        term_defaulttext (str | Unset):
        term_type (CsSysValueGenericValue | Unset):
        term_type_value_id (int | Unset):
        year (int | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamTermForeigntext | Unset = UNSET
    default_application_term: bool | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    released_term_period_id: int | Unset = UNSET
    term_defaulttext: str | Unset = UNSET
    term_type: CsSysValueGenericValue | Unset = UNSET
    term_type_value_id: int | Unset = UNSET
    year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        default_application_term = self.default_application_term

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        released_term_period_id = self.released_term_period_id

        term_defaulttext = self.term_defaulttext

        term_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.term_type, Unset):
            term_type = self.term_type.to_dict()

        term_type_value_id = self.term_type_value_id

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if default_application_term is not UNSET:
            field_dict["defaultApplicationTerm"] = default_application_term
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if released_term_period_id is not UNSET:
            field_dict["releasedTermPeriodId"] = released_term_period_id
        if term_defaulttext is not UNSET:
            field_dict["termDefaulttext"] = term_defaulttext
        if term_type is not UNSET:
            field_dict["termType"] = term_type
        if term_type_value_id is not UNSET:
            field_dict["termTypeValueId"] = term_type_value_id
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term_foreigntext import (
            ModelCmAppBackendEntranceExaminationEntranceExamTermForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamTermForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationEntranceExamTermForeigntext.from_dict(
                _field_foreigntext
            )

        default_application_term = d.pop("defaultApplicationTerm", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        released_term_period_id = d.pop("releasedTermPeriodId", UNSET)

        term_defaulttext = d.pop("termDefaulttext", UNSET)

        _term_type = d.pop("termType", UNSET)
        term_type: CsSysValueGenericValue | Unset
        if isinstance(_term_type, Unset):
            term_type = UNSET
        else:
            term_type = CsSysValueGenericValue.from_dict(_term_type)

        term_type_value_id = d.pop("termTypeValueId", UNSET)

        year = d.pop("year", UNSET)

        model_cm_app_backend_entrance_examination_entrance_exam_term = cls(
            field_foreigntext=field_foreigntext,
            default_application_term=default_application_term,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            released_term_period_id=released_term_period_id,
            term_defaulttext=term_defaulttext,
            term_type=term_type,
            term_type_value_id=term_type_value_id,
            year=year,
        )

        model_cm_app_backend_entrance_examination_entrance_exam_term.additional_properties = d
        return model_cm_app_backend_entrance_examination_entrance_exam_term

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
