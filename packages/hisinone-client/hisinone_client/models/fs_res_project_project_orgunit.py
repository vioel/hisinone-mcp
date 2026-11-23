from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_external_organisation_research_partner_simple import (
        CsPsvExternalOrganisationResearchPartnerSimple,
    )
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_project_project_orgunit_foreigntext import FsResProjectProjectOrgunitForeigntext


T = TypeVar("T", bound="FsResProjectProjectOrgunit")


@_attrs_define
class FsResProjectProjectOrgunit:
    """
    Attributes:
        field_foreigntext (FsResProjectProjectOrgunitForeigntext | Unset):
        id (int | Unset):
        information (str | Unset):
        is_additional (bool | Unset):
        is_adviser (bool | Unset):
        is_cooperation (bool | Unset):
        is_coordinator (bool | Unset):
        is_spokesperson (bool | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organization (CsSysValueGenericValue | Unset):
        project_id (int | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
    """

    field_foreigntext: FsResProjectProjectOrgunitForeigntext | Unset = UNSET
    id: int | Unset = UNSET
    information: str | Unset = UNSET
    is_additional: bool | Unset = UNSET
    is_adviser: bool | Unset = UNSET
    is_cooperation: bool | Unset = UNSET
    is_coordinator: bool | Unset = UNSET
    is_spokesperson: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organization: CsSysValueGenericValue | Unset = UNSET
    project_id: int | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        information = self.information

        is_additional = self.is_additional

        is_adviser = self.is_adviser

        is_cooperation = self.is_cooperation

        is_coordinator = self.is_coordinator

        is_spokesperson = self.is_spokesperson

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        project_id = self.project_id

        research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_partner, Unset):
            research_partner = self.research_partner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if information is not UNSET:
            field_dict["information"] = information
        if is_additional is not UNSET:
            field_dict["isAdditional"] = is_additional
        if is_adviser is not UNSET:
            field_dict["isAdviser"] = is_adviser
        if is_cooperation is not UNSET:
            field_dict["isCooperation"] = is_cooperation
        if is_coordinator is not UNSET:
            field_dict["isCoordinator"] = is_coordinator
        if is_spokesperson is not UNSET:
            field_dict["isSpokesperson"] = is_spokesperson
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organization is not UNSET:
            field_dict["organization"] = organization
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_project_project_orgunit_foreigntext import FsResProjectProjectOrgunitForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResProjectProjectOrgunitForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResProjectProjectOrgunitForeigntext.from_dict(_field_foreigntext)

        id = d.pop("id", UNSET)

        information = d.pop("information", UNSET)

        is_additional = d.pop("isAdditional", UNSET)

        is_adviser = d.pop("isAdviser", UNSET)

        is_cooperation = d.pop("isCooperation", UNSET)

        is_coordinator = d.pop("isCoordinator", UNSET)

        is_spokesperson = d.pop("isSpokesperson", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: CsSysValueGenericValue | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CsSysValueGenericValue.from_dict(_organization)

        project_id = d.pop("projectId", UNSET)

        _research_partner = d.pop("researchPartner", UNSET)
        research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_research_partner, Unset):
            research_partner = UNSET
        else:
            research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_research_partner)

        fs_res_project_project_orgunit = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            information=information,
            is_additional=is_additional,
            is_adviser=is_adviser,
            is_cooperation=is_cooperation,
            is_coordinator=is_coordinator,
            is_spokesperson=is_spokesperson,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organization=organization,
            project_id=project_id,
            research_partner=research_partner,
        )

        fs_res_project_project_orgunit.additional_properties = d
        return fs_res_project_project_orgunit

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
