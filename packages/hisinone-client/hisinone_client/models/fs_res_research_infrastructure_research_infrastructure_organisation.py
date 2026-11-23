from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_research_partner_simple import (
        CsPsvExternalOrganisationResearchPartnerSimple,
    )
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_research_infrastructure_research_infrastructure_organisation_foreigntext_type_0 import (
        FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0,
    )


T = TypeVar("T", bound="FsResResearchInfrastructureResearchInfrastructureOrganisation")


@_attrs_define
class FsResResearchInfrastructureResearchInfrastructureOrganisation:
    """
    Attributes:
        field_foreigntext (FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0 | None |
            Unset):
        id (int | Unset):
        is_coordinator (bool | Unset):
        lock_version (int | Unset):
        obj_guid (None | str | Unset):
        orgunit (CsSysValueGenericValue | Unset):
        research_infrastructure_id (int | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | None | Unset):
    """

    field_foreigntext: FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0 | None | Unset = (
        UNSET
    )
    id: int | Unset = UNSET
    is_coordinator: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    orgunit: CsSysValueGenericValue | Unset = UNSET
    research_infrastructure_id: int | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.fs_res_research_infrastructure_research_infrastructure_organisation_foreigntext_type_0 import (
            FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(
            self.field_foreigntext, FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0
        ):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        id = self.id

        is_coordinator = self.is_coordinator

        lock_version = self.lock_version

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        orgunit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.orgunit, Unset):
            orgunit = self.orgunit.to_dict()

        research_infrastructure_id = self.research_infrastructure_id

        research_partner: dict[str, Any] | None | Unset
        if isinstance(self.research_partner, Unset):
            research_partner = UNSET
        elif isinstance(self.research_partner, CsPsvExternalOrganisationResearchPartnerSimple):
            research_partner = self.research_partner.to_dict()
        else:
            research_partner = self.research_partner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if is_coordinator is not UNSET:
            field_dict["isCoordinator"] = is_coordinator
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if orgunit is not UNSET:
            field_dict["orgunit"] = orgunit
        if research_infrastructure_id is not UNSET:
            field_dict["researchInfrastructureId"] = research_infrastructure_id
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_research_infrastructure_research_infrastructure_organisation_foreigntext_type_0 import (
            FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_field_foreigntext(
            data: object,
        ) -> FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = (
                FsResResearchInfrastructureResearchInfrastructureOrganisationForeigntextType0.from_dict(
                    cast(dict[str, Any], data)
                )
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        id = d.pop("id", UNSET)

        is_coordinator = d.pop("isCoordinator", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        _orgunit = d.pop("orgunit", UNSET)
        orgunit: CsSysValueGenericValue | Unset
        if isinstance(_orgunit, Unset):
            orgunit = UNSET
        else:
            orgunit = CsSysValueGenericValue.from_dict(_orgunit)

        research_infrastructure_id = d.pop("researchInfrastructureId", UNSET)

        def _parse_research_partner(data: object) -> CsPsvExternalOrganisationResearchPartnerSimple | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            research_partner_type_0 = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(
                cast(dict[str, Any], data)
            )

            return research_partner_type_0

        research_partner = _parse_research_partner(d.pop("researchPartner", UNSET))

        fs_res_research_infrastructure_research_infrastructure_organisation = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            is_coordinator=is_coordinator,
            lock_version=lock_version,
            obj_guid=obj_guid,
            orgunit=orgunit,
            research_infrastructure_id=research_infrastructure_id,
            research_partner=research_partner,
        )

        fs_res_research_infrastructure_research_infrastructure_organisation.additional_properties = d
        return fs_res_research_infrastructure_research_infrastructure_organisation

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
