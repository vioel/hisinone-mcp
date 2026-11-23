from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_absencemanagement_absence_master_record_foreigntext import (
        RmErpAbsencemanagementAbsenceMasterRecordForeigntext,
    )
    from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData


T = TypeVar("T", bound="RmErpAbsencemanagementAbsenceMasterRecord")


@_attrs_define
class RmErpAbsencemanagementAbsenceMasterRecord:
    """
    Attributes:
        field_foreigntext (RmErpAbsencemanagementAbsenceMasterRecordForeigntext | Unset):
        comment (str | Unset):
        error_message (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        related_person (RmErpCommonPersonPersonBasicDataCoreData | Unset):
        related_year (int | Unset):
        serialversionuid (int | Unset):
        status (int | Unset):
    """

    field_foreigntext: RmErpAbsencemanagementAbsenceMasterRecordForeigntext | Unset = UNSET
    comment: str | Unset = UNSET
    error_message: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset = UNSET
    related_year: int | Unset = UNSET
    serialversionuid: int | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        comment = self.comment

        error_message = self.error_message

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        related_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.related_person, Unset):
            related_person = self.related_person.to_dict()

        related_year = self.related_year

        serialversionuid = self.serialversionuid

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if comment is not UNSET:
            field_dict["comment"] = comment
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if related_person is not UNSET:
            field_dict["relatedPerson"] = related_person
        if related_year is not UNSET:
            field_dict["relatedYear"] = related_year
        if serialversionuid is not UNSET:
            field_dict["serialversionuid"] = serialversionuid
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_absencemanagement_absence_master_record_foreigntext import (
            RmErpAbsencemanagementAbsenceMasterRecordForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpAbsencemanagementAbsenceMasterRecordForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpAbsencemanagementAbsenceMasterRecordForeigntext.from_dict(_field_foreigntext)

        comment = d.pop("comment", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _related_person = d.pop("relatedPerson", UNSET)
        related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset
        if isinstance(_related_person, Unset):
            related_person = UNSET
        else:
            related_person = RmErpCommonPersonPersonBasicDataCoreData.from_dict(_related_person)

        related_year = d.pop("relatedYear", UNSET)

        serialversionuid = d.pop("serialversionuid", UNSET)

        status = d.pop("status", UNSET)

        rm_erp_absencemanagement_absence_master_record = cls(
            field_foreigntext=field_foreigntext,
            comment=comment,
            error_message=error_message,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            related_person=related_person,
            related_year=related_year,
            serialversionuid=serialversionuid,
            status=status,
        )

        rm_erp_absencemanagement_absence_master_record.additional_properties = d
        return rm_erp_absencemanagement_absence_master_record

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
