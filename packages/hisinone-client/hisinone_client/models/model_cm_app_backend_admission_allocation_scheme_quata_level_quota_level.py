from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level_foreigntext import (
        ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelForeigntext,
    )
    from ..models.model_cm_app_backend_admission_allocation_scheme_quota_quota import (
        ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota,
    )


T = TypeVar("T", bound="ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel")


@_attrs_define
class ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevel:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelForeigntext | Unset):
        id (int | Unset):
        id_not_persistent (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        quotas (list[ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota] | Unset):
        sortorder (int | Unset):
        unique_name (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    id_not_persistent: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    quotas: list[ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota] | Unset = UNSET
    sortorder: int | Unset = UNSET
    unique_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        id_not_persistent = self.id_not_persistent

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        quotas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotas, Unset):
            quotas = []
            for quotas_item_data in self.quotas:
                quotas_item = quotas_item_data.to_dict()
                quotas.append(quotas_item)

        sortorder = self.sortorder

        unique_name = self.unique_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if id_not_persistent is not UNSET:
            field_dict["idNotPersistent"] = id_not_persistent
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if quotas is not UNSET:
            field_dict["quotas"] = quotas
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level_foreigntext import (
            ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelForeigntext,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_admission_allocation_scheme_quota_quota import (
            ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendAdmissionAllocationSchemeQuataLevelQuotaLevelForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        id_not_persistent = d.pop("idNotPersistent", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _quotas = d.pop("quotas", UNSET)
        quotas: list[ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota] | Unset = UNSET
        if _quotas is not UNSET:
            quotas = []
            for quotas_item_data in _quotas:
                quotas_item = ModelCmAppBackendAdmissionAllocationSchemeQuotaQuota.from_dict(quotas_item_data)

                quotas.append(quotas_item)

        sortorder = d.pop("sortorder", UNSET)

        unique_name = d.pop("uniqueName", UNSET)

        model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            id_not_persistent=id_not_persistent,
            lock_version=lock_version,
            obj_guid=obj_guid,
            quotas=quotas,
            sortorder=sortorder,
            unique_name=unique_name,
        )

        model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level.additional_properties = d
        return model_cm_app_backend_admission_allocation_scheme_quata_level_quota_level

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
