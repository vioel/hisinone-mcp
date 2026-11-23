from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_allocation_scheme_allocation_scheme_foreigntext import (
        ModelCmAppBackendAdmissionAllocationSchemeAllocationSchemeForeigntext,
    )
    from ..models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level import (
        ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme")


@_attrs_define
class ModelCmAppBackendAdmissionAllocationSchemeAllocationScheme:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAllocationSchemeAllocationSchemeForeigntext | Unset):
        defaulttext (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        quota_levels (list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset):
        unique_name (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAllocationSchemeAllocationSchemeForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    quota_levels: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET
    unique_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        quota_levels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quota_levels, Unset):
            quota_levels = []
            for quota_levels_item_data in self.quota_levels:
                quota_levels_item = quota_levels_item_data.to_dict()
                quota_levels.append(quota_levels_item)

        unique_name = self.unique_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if quota_levels is not UNSET:
            field_dict["quotaLevels"] = quota_levels
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_allocation_scheme_allocation_scheme_foreigntext import (
            ModelCmAppBackendAdmissionAllocationSchemeAllocationSchemeForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level import (
            ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAllocationSchemeAllocationSchemeForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAllocationSchemeAllocationSchemeForeigntext.from_dict(
                _field_foreigntext
            )

        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _quota_levels = d.pop("quotaLevels", UNSET)
        quota_levels: list[ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel] | Unset = UNSET
        if _quota_levels is not UNSET:
            quota_levels = []
            for quota_levels_item_data in _quota_levels:
                quota_levels_item = ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel.from_dict(
                    quota_levels_item_data
                )

                quota_levels.append(quota_levels_item)

        unique_name = d.pop("uniqueName", UNSET)

        model_cm_app_backend_admission_allocation_scheme_allocation_scheme = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            quota_levels=quota_levels,
            unique_name=unique_name,
        )

        model_cm_app_backend_admission_allocation_scheme_allocation_scheme.additional_properties = d
        return model_cm_app_backend_admission_allocation_scheme_allocation_scheme

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
