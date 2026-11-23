from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_employment_employment import CsPsvEmploymentEmployment
    from ..models.fs_res_research_infrastructure_research_infrastructure_employment_foreigntext import (
        FsResResearchInfrastructureResearchInfrastructureEmploymentForeigntext,
    )


T = TypeVar("T", bound="FsResResearchInfrastructureResearchInfrastructureEmployment")


@_attrs_define
class FsResResearchInfrastructureResearchInfrastructureEmployment:
    """
    Attributes:
        field_foreigntext (FsResResearchInfrastructureResearchInfrastructureEmploymentForeigntext | Unset):
        employment (CsPsvEmploymentEmployment | Unset):
        full_time_percentage (float | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        research_infrastructure_id (int | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    field_foreigntext: FsResResearchInfrastructureResearchInfrastructureEmploymentForeigntext | Unset = UNSET
    employment: CsPsvEmploymentEmployment | Unset = UNSET
    full_time_percentage: float | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    research_infrastructure_id: int | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        employment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.employment, Unset):
            employment = self.employment.to_dict()

        full_time_percentage = self.full_time_percentage

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        research_infrastructure_id = self.research_infrastructure_id

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if employment is not UNSET:
            field_dict["employment"] = employment
        if full_time_percentage is not UNSET:
            field_dict["fullTimePercentage"] = full_time_percentage
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if research_infrastructure_id is not UNSET:
            field_dict["researchInfrastructureId"] = research_infrastructure_id
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_employment_employment import CsPsvEmploymentEmployment  # noqa: PLC0415
        from ..models.fs_res_research_infrastructure_research_infrastructure_employment_foreigntext import (
            FsResResearchInfrastructureResearchInfrastructureEmploymentForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResResearchInfrastructureResearchInfrastructureEmploymentForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResResearchInfrastructureResearchInfrastructureEmploymentForeigntext.from_dict(
                _field_foreigntext
            )

        _employment = d.pop("employment", UNSET)
        employment: CsPsvEmploymentEmployment | Unset
        if isinstance(_employment, Unset):
            employment = UNSET
        else:
            employment = CsPsvEmploymentEmployment.from_dict(_employment)

        full_time_percentage = d.pop("fullTimePercentage", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        research_infrastructure_id = d.pop("researchInfrastructureId", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        fs_res_research_infrastructure_research_infrastructure_employment = cls(
            field_foreigntext=field_foreigntext,
            employment=employment,
            full_time_percentage=full_time_percentage,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            research_infrastructure_id=research_infrastructure_id,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        fs_res_research_infrastructure_research_infrastructure_employment.additional_properties = d
        return fs_res_research_infrastructure_research_infrastructure_employment

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
