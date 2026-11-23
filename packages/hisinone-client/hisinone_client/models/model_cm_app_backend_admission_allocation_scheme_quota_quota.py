from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level_simple import (
        ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple,
    )
    from ..models.model_cm_app_backend_admission_allocation_scheme_quota_quota_foreigntext import (
        ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaForeigntext,
    )
    from ..models.model_cm_app_backend_admission_allocation_scheme_quota_quota_simple import (
        ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaSimple,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota")


@_attrs_define
class ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaForeigntext | Unset):
        absolute_overbooking (int | Unset):
        allocates_places (bool | Unset):
        defaulttext (str | Unset):
        delayed_allocation (bool | Unset):
        id (int | Unset):
        id_not_persistent (int | Unset):
        limited (bool | Unset):
        lock_version (int | Unset):
        min_num_of_places (int | Unset):
        obj_guid (str | Unset):
        percentage (float | Unset):
        quota_for_remaining_places (ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaSimple | Unset):
        quota_level (ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple | Unset):
        quota_level_for_remaining_places (ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple | Unset):
        relative_overbooking (int | Unset):
        remaning_places_id_not_persistent (int | Unset):
        reserves (bool | Unset):
        sortorder (int | Unset):
        subgroups (bool | Unset):
        unique_name (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaForeigntext | Unset = UNSET
    absolute_overbooking: int | Unset = UNSET
    allocates_places: bool | Unset = UNSET
    defaulttext: str | Unset = UNSET
    delayed_allocation: bool | Unset = UNSET
    id: int | Unset = UNSET
    id_not_persistent: int | Unset = UNSET
    limited: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    min_num_of_places: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    percentage: float | Unset = UNSET
    quota_for_remaining_places: ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaSimple | Unset = UNSET
    quota_level: ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple | Unset = UNSET
    quota_level_for_remaining_places: ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple | Unset = (
        UNSET
    )
    relative_overbooking: int | Unset = UNSET
    remaning_places_id_not_persistent: int | Unset = UNSET
    reserves: bool | Unset = UNSET
    sortorder: int | Unset = UNSET
    subgroups: bool | Unset = UNSET
    unique_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        absolute_overbooking = self.absolute_overbooking

        allocates_places = self.allocates_places

        defaulttext = self.defaulttext

        delayed_allocation = self.delayed_allocation

        id = self.id

        id_not_persistent = self.id_not_persistent

        limited = self.limited

        lock_version = self.lock_version

        min_num_of_places = self.min_num_of_places

        obj_guid = self.obj_guid

        percentage = self.percentage

        quota_for_remaining_places: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota_for_remaining_places, Unset):
            quota_for_remaining_places = self.quota_for_remaining_places.to_dict()

        quota_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota_level, Unset):
            quota_level = self.quota_level.to_dict()

        quota_level_for_remaining_places: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quota_level_for_remaining_places, Unset):
            quota_level_for_remaining_places = self.quota_level_for_remaining_places.to_dict()

        relative_overbooking = self.relative_overbooking

        remaning_places_id_not_persistent = self.remaning_places_id_not_persistent

        reserves = self.reserves

        sortorder = self.sortorder

        subgroups = self.subgroups

        unique_name = self.unique_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if absolute_overbooking is not UNSET:
            field_dict["absoluteOverbooking"] = absolute_overbooking
        if allocates_places is not UNSET:
            field_dict["allocatesPlaces"] = allocates_places
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if delayed_allocation is not UNSET:
            field_dict["delayedAllocation"] = delayed_allocation
        if id is not UNSET:
            field_dict["id"] = id
        if id_not_persistent is not UNSET:
            field_dict["idNotPersistent"] = id_not_persistent
        if limited is not UNSET:
            field_dict["limited"] = limited
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if min_num_of_places is not UNSET:
            field_dict["minNumOfPlaces"] = min_num_of_places
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if quota_for_remaining_places is not UNSET:
            field_dict["quotaForRemainingPlaces"] = quota_for_remaining_places
        if quota_level is not UNSET:
            field_dict["quotaLevel"] = quota_level
        if quota_level_for_remaining_places is not UNSET:
            field_dict["quotaLevelForRemainingPlaces"] = quota_level_for_remaining_places
        if relative_overbooking is not UNSET:
            field_dict["relativeOverbooking"] = relative_overbooking
        if remaning_places_id_not_persistent is not UNSET:
            field_dict["remaningPlacesIdNotPersistent"] = remaning_places_id_not_persistent
        if reserves is not UNSET:
            field_dict["reserves"] = reserves
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if subgroups is not UNSET:
            field_dict["subgroups"] = subgroups
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level_simple import (
            ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_allocation_scheme_quota_quota_foreigntext import (
            ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_allocation_scheme_quota_quota_simple import (
            ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaSimple,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaForeigntext.from_dict(
                _field_foreigntext
            )

        absolute_overbooking = d.pop("absoluteOverbooking", UNSET)

        allocates_places = d.pop("allocatesPlaces", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        delayed_allocation = d.pop("delayedAllocation", UNSET)

        id = d.pop("id", UNSET)

        id_not_persistent = d.pop("idNotPersistent", UNSET)

        limited = d.pop("limited", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        min_num_of_places = d.pop("minNumOfPlaces", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        percentage = d.pop("percentage", UNSET)

        _quota_for_remaining_places = d.pop("quotaForRemainingPlaces", UNSET)
        quota_for_remaining_places: ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaSimple | Unset
        if isinstance(_quota_for_remaining_places, Unset):
            quota_for_remaining_places = UNSET
        else:
            quota_for_remaining_places = ModelCmAppBackendAdmissionAllocationSchemeQuotaQuotaSimple.from_dict(
                _quota_for_remaining_places
            )

        _quota_level = d.pop("quotaLevel", UNSET)
        quota_level: ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple | Unset
        if isinstance(_quota_level, Unset):
            quota_level = UNSET
        else:
            quota_level = ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple.from_dict(_quota_level)

        _quota_level_for_remaining_places = d.pop("quotaLevelForRemainingPlaces", UNSET)
        quota_level_for_remaining_places: ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple | Unset
        if isinstance(_quota_level_for_remaining_places, Unset):
            quota_level_for_remaining_places = UNSET
        else:
            quota_level_for_remaining_places = (
                ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelSimple.from_dict(
                    _quota_level_for_remaining_places
                )
            )

        relative_overbooking = d.pop("relativeOverbooking", UNSET)

        remaning_places_id_not_persistent = d.pop("remaningPlacesIdNotPersistent", UNSET)

        reserves = d.pop("reserves", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        subgroups = d.pop("subgroups", UNSET)

        unique_name = d.pop("uniqueName", UNSET)

        model_cm_app_backend_admission_allocation_scheme_quota_quota = cls(
            field_foreigntext=field_foreigntext,
            absolute_overbooking=absolute_overbooking,
            allocates_places=allocates_places,
            defaulttext=defaulttext,
            delayed_allocation=delayed_allocation,
            id=id,
            id_not_persistent=id_not_persistent,
            limited=limited,
            lock_version=lock_version,
            min_num_of_places=min_num_of_places,
            obj_guid=obj_guid,
            percentage=percentage,
            quota_for_remaining_places=quota_for_remaining_places,
            quota_level=quota_level,
            quota_level_for_remaining_places=quota_level_for_remaining_places,
            relative_overbooking=relative_overbooking,
            remaning_places_id_not_persistent=remaning_places_id_not_persistent,
            reserves=reserves,
            sortorder=sortorder,
            subgroups=subgroups,
            unique_name=unique_name,
        )

        model_cm_app_backend_admission_allocation_scheme_quota_quota.additional_properties = d
        return model_cm_app_backend_admission_allocation_scheme_quota_quota

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
