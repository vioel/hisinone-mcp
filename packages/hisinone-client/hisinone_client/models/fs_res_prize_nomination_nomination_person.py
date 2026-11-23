from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_prize_nomination_nomination_person_foreigntext import (
        FsResPrizeNominationNominationPersonForeigntext,
    )


T = TypeVar("T", bound="FsResPrizeNominationNominationPerson")


@_attrs_define
class FsResPrizeNominationNominationPerson:
    """
    Attributes:
        field_foreigntext (FsResPrizeNominationNominationPersonForeigntext | Unset):
        affiliation_type (CsSysValueGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        nomination_id (int | Unset):
        obj_guid (str | Unset):
        organization (CsSysValueGenericValue | Unset):
        person (CsPsvPersonRest | Unset):
    """

    field_foreigntext: FsResPrizeNominationNominationPersonForeigntext | Unset = UNSET
    affiliation_type: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    nomination_id: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organization: CsSysValueGenericValue | Unset = UNSET
    person: CsPsvPersonRest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        affiliation_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliation_type, Unset):
            affiliation_type = self.affiliation_type.to_dict()

        id = self.id

        lock_version = self.lock_version

        nomination_id = self.nomination_id

        obj_guid = self.obj_guid

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if affiliation_type is not UNSET:
            field_dict["affiliationType"] = affiliation_type
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if nomination_id is not UNSET:
            field_dict["nominationId"] = nomination_id
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organization is not UNSET:
            field_dict["organization"] = organization
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_nomination_person_foreigntext import (
            FsResPrizeNominationNominationPersonForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPrizeNominationNominationPersonForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPrizeNominationNominationPersonForeigntext.from_dict(_field_foreigntext)

        _affiliation_type = d.pop("affiliationType", UNSET)
        affiliation_type: CsSysValueGenericValue | Unset
        if isinstance(_affiliation_type, Unset):
            affiliation_type = UNSET
        else:
            affiliation_type = CsSysValueGenericValue.from_dict(_affiliation_type)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        nomination_id = d.pop("nominationId", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: CsSysValueGenericValue | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CsSysValueGenericValue.from_dict(_organization)

        _person = d.pop("person", UNSET)
        person: CsPsvPersonRest | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CsPsvPersonRest.from_dict(_person)

        fs_res_prize_nomination_nomination_person = cls(
            field_foreigntext=field_foreigntext,
            affiliation_type=affiliation_type,
            id=id,
            lock_version=lock_version,
            nomination_id=nomination_id,
            obj_guid=obj_guid,
            organization=organization,
            person=person,
        )

        fs_res_prize_nomination_nomination_person.additional_properties = d
        return fs_res_prize_nomination_nomination_person

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
