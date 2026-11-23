from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_project_project_member_position_foreigntext_type_0 import (
        FsResProjectProjectMemberPositionForeigntextType0,
    )


T = TypeVar("T", bound="FsResProjectProjectMemberPosition")


@_attrs_define
class FsResProjectProjectMemberPosition:
    """
    Attributes:
        field_foreigntext (FsResProjectProjectMemberPositionForeigntextType0 | None | Unset):
        firstname (str | Unset):
        has_visible_affiliations (bool | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (None | str | Unset):
        organization (CsSysValueGenericValue | Unset):
        person_id (int | Unset):
        position_type (CsSysValueGenericValue | Unset):
        project_id (int | Unset):
        project_period_status (CsSysValueGenericValue | None | Unset):
        surname (str | Unset):
        valid_from (int | None | Unset):
        valid_to (int | None | Unset):
    """

    field_foreigntext: FsResProjectProjectMemberPositionForeigntextType0 | None | Unset = UNSET
    firstname: str | Unset = UNSET
    has_visible_affiliations: bool | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    organization: CsSysValueGenericValue | Unset = UNSET
    person_id: int | Unset = UNSET
    position_type: CsSysValueGenericValue | Unset = UNSET
    project_id: int | Unset = UNSET
    project_period_status: CsSysValueGenericValue | None | Unset = UNSET
    surname: str | Unset = UNSET
    valid_from: int | None | Unset = UNSET
    valid_to: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_project_project_member_position_foreigntext_type_0 import (
            FsResProjectProjectMemberPositionForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResProjectProjectMemberPositionForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        firstname = self.firstname

        has_visible_affiliations = self.has_visible_affiliations

        id = self.id

        lock_version = self.lock_version

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        person_id = self.person_id

        position_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position_type, Unset):
            position_type = self.position_type.to_dict()

        project_id = self.project_id

        project_period_status: dict[str, Any] | None | Unset
        if isinstance(self.project_period_status, Unset):
            project_period_status = UNSET
        elif isinstance(self.project_period_status, CsSysValueGenericValue):
            project_period_status = self.project_period_status.to_dict()
        else:
            project_period_status = self.project_period_status

        surname = self.surname

        valid_from: int | None | Unset
        if isinstance(self.valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = self.valid_from

        valid_to: int | None | Unset
        if isinstance(self.valid_to, Unset):
            valid_to = UNSET
        else:
            valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if has_visible_affiliations is not UNSET:
            field_dict["hasVisibleAffiliations"] = has_visible_affiliations
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organization is not UNSET:
            field_dict["organization"] = organization
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if position_type is not UNSET:
            field_dict["positionType"] = position_type
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_period_status is not UNSET:
            field_dict["projectPeriodStatus"] = project_period_status
        if surname is not UNSET:
            field_dict["surname"] = surname
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_project_project_member_position_foreigntext_type_0 import (
            FsResProjectProjectMemberPositionForeigntextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_field_foreigntext(data: object) -> FsResProjectProjectMemberPositionForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResProjectProjectMemberPositionForeigntextType0.from_dict(
                cast(dict[str, Any], data)
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        firstname = d.pop("firstname", UNSET)

        has_visible_affiliations = d.pop("hasVisibleAffiliations", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        _organization = d.pop("organization", UNSET)
        organization: CsSysValueGenericValue | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CsSysValueGenericValue.from_dict(_organization)

        person_id = d.pop("personId", UNSET)

        _position_type = d.pop("positionType", UNSET)
        position_type: CsSysValueGenericValue | Unset
        if isinstance(_position_type, Unset):
            position_type = UNSET
        else:
            position_type = CsSysValueGenericValue.from_dict(_position_type)

        project_id = d.pop("projectId", UNSET)

        def _parse_project_period_status(data: object) -> CsSysValueGenericValue | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            project_period_status_type_0 = CsSysValueGenericValue.from_dict(cast(dict[str, Any], data))

            return project_period_status_type_0

        project_period_status = _parse_project_period_status(d.pop("projectPeriodStatus", UNSET))

        surname = d.pop("surname", UNSET)

        def _parse_valid_from(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        valid_from = _parse_valid_from(d.pop("validFrom", UNSET))

        def _parse_valid_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        valid_to = _parse_valid_to(d.pop("validTo", UNSET))

        fs_res_project_project_member_position = cls(
            field_foreigntext=field_foreigntext,
            firstname=firstname,
            has_visible_affiliations=has_visible_affiliations,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organization=organization,
            person_id=person_id,
            position_type=position_type,
            project_id=project_id,
            project_period_status=project_period_status,
            surname=surname,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        fs_res_project_project_member_position.additional_properties = d
        return fs_res_project_project_member_position

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
