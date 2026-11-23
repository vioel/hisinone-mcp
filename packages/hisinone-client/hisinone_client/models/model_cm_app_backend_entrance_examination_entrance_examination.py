from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_entrance_examination_entrance_examination_foreigntext import (
        ModelCmAppBackendEntranceExaminationEntranceExaminationForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationEntranceExamination")


@_attrs_define
class ModelCmAppBackendEntranceExaminationEntranceExamination:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationEntranceExaminationForeigntext | Unset):
        element_number (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        name (str | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExaminationForeigntext | Unset = UNSET
    element_number: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    name: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        element_number = self.element_number

        id = self.id

        lock_version = self.lock_version

        name = self.name

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if element_number is not UNSET:
            field_dict["elementNumber"] = element_number
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
        from ..models.model_cm_app_backend_entrance_examination_entrance_examination_foreigntext import (
            ModelCmAppBackendEntranceExaminationEntranceExaminationForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationEntranceExaminationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationEntranceExaminationForeigntext.from_dict(
                _field_foreigntext
            )

        element_number = d.pop("elementNumber", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        name = d.pop("name", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_entrance_examination_entrance_examination = cls(
            field_foreigntext=field_foreigntext,
            element_number=element_number,
            id=id,
            lock_version=lock_version,
            name=name,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_entrance_examination_entrance_examination.additional_properties = d
        return model_cm_app_backend_entrance_examination_entrance_examination

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
