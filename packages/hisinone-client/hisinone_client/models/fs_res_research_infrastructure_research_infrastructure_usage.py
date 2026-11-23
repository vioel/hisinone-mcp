from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_research_infrastructure_research_infrastructure_usage_foreigntext import (
        FsResResearchInfrastructureResearchInfrastructureUsageForeigntext,
    )


T = TypeVar("T", bound="FsResResearchInfrastructureResearchInfrastructureUsage")


@_attrs_define
class FsResResearchInfrastructureResearchInfrastructureUsage:
    """
    Attributes:
        field_foreigntext (FsResResearchInfrastructureResearchInfrastructureUsageForeigntext | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        research_infrastructure_id (int | Unset):
        research_infrastructure_usage_type (CsSysValueGenericValue | Unset):
        usage_amount (float | Unset):
        usage_year (int | Unset):
    """

    field_foreigntext: FsResResearchInfrastructureResearchInfrastructureUsageForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    research_infrastructure_id: int | Unset = UNSET
    research_infrastructure_usage_type: CsSysValueGenericValue | Unset = UNSET
    usage_amount: float | Unset = UNSET
    usage_year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        research_infrastructure_id = self.research_infrastructure_id

        research_infrastructure_usage_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_infrastructure_usage_type, Unset):
            research_infrastructure_usage_type = self.research_infrastructure_usage_type.to_dict()

        usage_amount = self.usage_amount

        usage_year = self.usage_year

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
        if research_infrastructure_id is not UNSET:
            field_dict["researchInfrastructureId"] = research_infrastructure_id
        if research_infrastructure_usage_type is not UNSET:
            field_dict["researchInfrastructureUsageType"] = research_infrastructure_usage_type
        if usage_amount is not UNSET:
            field_dict["usageAmount"] = usage_amount
        if usage_year is not UNSET:
            field_dict["usageYear"] = usage_year

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_research_infrastructure_research_infrastructure_usage_foreigntext import (
            FsResResearchInfrastructureResearchInfrastructureUsageForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResResearchInfrastructureResearchInfrastructureUsageForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResResearchInfrastructureResearchInfrastructureUsageForeigntext.from_dict(
                _field_foreigntext
            )

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        research_infrastructure_id = d.pop("researchInfrastructureId", UNSET)

        _research_infrastructure_usage_type = d.pop("researchInfrastructureUsageType", UNSET)
        research_infrastructure_usage_type: CsSysValueGenericValue | Unset
        if isinstance(_research_infrastructure_usage_type, Unset):
            research_infrastructure_usage_type = UNSET
        else:
            research_infrastructure_usage_type = CsSysValueGenericValue.from_dict(_research_infrastructure_usage_type)

        usage_amount = d.pop("usageAmount", UNSET)

        usage_year = d.pop("usageYear", UNSET)

        fs_res_research_infrastructure_research_infrastructure_usage = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            research_infrastructure_id=research_infrastructure_id,
            research_infrastructure_usage_type=research_infrastructure_usage_type,
            usage_amount=usage_amount,
            usage_year=usage_year,
        )

        fs_res_research_infrastructure_research_infrastructure_usage.additional_properties = d
        return fs_res_research_infrastructure_research_infrastructure_usage

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
