from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_person_person_basic_data import RmErpCommonPersonPersonBasicData
    from ..models.rm_erp_jobadvertisement_job_advertisement_state_foreigntext import (
        RmErpJobadvertisementJobAdvertisementStateForeigntext,
    )


T = TypeVar("T", bound="RmErpJobadvertisementJobAdvertisementState")


@_attrs_define
class RmErpJobadvertisementJobAdvertisementState:
    """
    Attributes:
        field_foreigntext (RmErpJobadvertisementJobAdvertisementStateForeigntext | Unset):
        executing_person (RmErpCommonPersonPersonBasicData | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        state (RmErpCommonErpGenericValue | Unset):
        timestamp (int | Unset):
    """

    field_foreigntext: RmErpJobadvertisementJobAdvertisementStateForeigntext | Unset = UNSET
    executing_person: RmErpCommonPersonPersonBasicData | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    state: RmErpCommonErpGenericValue | Unset = UNSET
    timestamp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        executing_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executing_person, Unset):
            executing_person = self.executing_person.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if executing_person is not UNSET:
            field_dict["executingPerson"] = executing_person
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if state is not UNSET:
            field_dict["state"] = state
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_person_basic_data import RmErpCommonPersonPersonBasicData  # noqa: PLC0415
        from ..models.rm_erp_jobadvertisement_job_advertisement_state_foreigntext import (
            RmErpJobadvertisementJobAdvertisementStateForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpJobadvertisementJobAdvertisementStateForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpJobadvertisementJobAdvertisementStateForeigntext.from_dict(_field_foreigntext)

        _executing_person = d.pop("executingPerson", UNSET)
        executing_person: RmErpCommonPersonPersonBasicData | Unset
        if isinstance(_executing_person, Unset):
            executing_person = UNSET
        else:
            executing_person = RmErpCommonPersonPersonBasicData.from_dict(_executing_person)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _state = d.pop("state", UNSET)
        state: RmErpCommonErpGenericValue | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RmErpCommonErpGenericValue.from_dict(_state)

        timestamp = d.pop("timestamp", UNSET)

        rm_erp_jobadvertisement_job_advertisement_state = cls(
            field_foreigntext=field_foreigntext,
            executing_person=executing_person,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            state=state,
            timestamp=timestamp,
        )

        rm_erp_jobadvertisement_job_advertisement_state.additional_properties = d
        return rm_erp_jobadvertisement_job_advertisement_state

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
