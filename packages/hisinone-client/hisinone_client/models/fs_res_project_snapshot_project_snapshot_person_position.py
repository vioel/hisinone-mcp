from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_project_snapshot_project_snapshot_person_position_foreigntext import (
        FsResProjectSnapshotProjectSnapshotPersonPositionForeigntext,
    )


T = TypeVar("T", bound="FsResProjectSnapshotProjectSnapshotPersonPosition")


@_attrs_define
class FsResProjectSnapshotProjectSnapshotPersonPosition:
    """
    Attributes:
        field_foreigntext (FsResProjectSnapshotProjectSnapshotPersonPositionForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person (CsPsvPersonRest | Unset):
        position_type (CsSysValueGenericValue | Unset):
        project_snapshot_id (int | Unset):
    """

    field_foreigntext: FsResProjectSnapshotProjectSnapshotPersonPositionForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person: CsPsvPersonRest | Unset = UNSET
    position_type: CsSysValueGenericValue | Unset = UNSET
    project_snapshot_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        position_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position_type, Unset):
            position_type = self.position_type.to_dict()

        project_snapshot_id = self.project_snapshot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person is not UNSET:
            field_dict["person"] = person
        if position_type is not UNSET:
            field_dict["positionType"] = position_type
        if project_snapshot_id is not UNSET:
            field_dict["projectSnapshotId"] = project_snapshot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_project_snapshot_project_snapshot_person_position_foreigntext import (
            FsResProjectSnapshotProjectSnapshotPersonPositionForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResProjectSnapshotProjectSnapshotPersonPositionForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResProjectSnapshotProjectSnapshotPersonPositionForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _person = d.pop("person", UNSET)
        person: CsPsvPersonRest | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CsPsvPersonRest.from_dict(_person)

        _position_type = d.pop("positionType", UNSET)
        position_type: CsSysValueGenericValue | Unset
        if isinstance(_position_type, Unset):
            position_type = UNSET
        else:
            position_type = CsSysValueGenericValue.from_dict(_position_type)

        project_snapshot_id = d.pop("projectSnapshotId", UNSET)

        fs_res_project_snapshot_project_snapshot_person_position = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person=person,
            position_type=position_type,
            project_snapshot_id=project_snapshot_id,
        )

        fs_res_project_snapshot_project_snapshot_person_position.additional_properties = d
        return fs_res_project_snapshot_project_snapshot_person_position

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
