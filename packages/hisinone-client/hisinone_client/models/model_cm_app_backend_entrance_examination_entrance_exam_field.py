from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_field_foreigntext import (
        ModelCmAppBackendEntranceExaminationEntranceExamFieldForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationEntranceExamField")


@_attrs_define
class ModelCmAppBackendEntranceExaminationEntranceExamField:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationEntranceExamFieldForeigntext | Unset):
        field_unique_name (str | Unset):
        fieldname (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamFieldForeigntext | Unset = UNSET
    field_unique_name: str | Unset = UNSET
    fieldname: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        field_unique_name = self.field_unique_name

        fieldname = self.fieldname

        id = self.id

        lock_version = self.lock_version

        name = self.name

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if field_unique_name is not UNSET:
            field_dict["fieldUniqueName"] = field_unique_name
        if fieldname is not UNSET:
            field_dict["fieldname"] = fieldname
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if name is not UNSET:
            field_dict["name"] = name
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_field_foreigntext import (
            ModelCmAppBackendEntranceExaminationEntranceExamFieldForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExamFieldForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationEntranceExamFieldForeigntext.from_dict(
                _field_foreigntext
            )

        field_unique_name = d.pop("fieldUniqueName", UNSET)

        fieldname = d.pop("fieldname", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_entrance_examination_entrance_exam_field = cls(
            field_foreigntext=field_foreigntext,
            field_unique_name=field_unique_name,
            fieldname=fieldname,
            id=id,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_entrance_examination_entrance_exam_field.additional_properties = d
        return model_cm_app_backend_entrance_examination_entrance_exam_field

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
