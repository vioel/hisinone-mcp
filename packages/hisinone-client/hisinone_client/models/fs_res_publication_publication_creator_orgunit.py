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
    from ..models.fs_res_publication_publication_creator_orgunit_foreigntext import (
        FsResPublicationPublicationCreatorOrgunitForeigntext,
    )


T = TypeVar("T", bound="FsResPublicationPublicationCreatorOrgunit")


@_attrs_define
class FsResPublicationPublicationCreatorOrgunit:
    """
    Attributes:
        field_foreigntext (FsResPublicationPublicationCreatorOrgunitForeigntext | Unset):
        creator_id (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organization (CsSysValueGenericValue | Unset):
        research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        sortorder (int | Unset):
    """

    field_foreigntext: FsResPublicationPublicationCreatorOrgunitForeigntext | Unset = UNSET
    creator_id: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organization: CsSysValueGenericValue | Unset = UNSET
    research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        creator_id = self.creator_id

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_partner, Unset):
            research_partner = self.research_partner.to_dict()

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organization is not UNSET:
            field_dict["organization"] = organization
        if research_partner is not UNSET:
            field_dict["researchPartner"] = research_partner
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_publication_creator_orgunit_foreigntext import (
            FsResPublicationPublicationCreatorOrgunitForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationPublicationCreatorOrgunitForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationPublicationCreatorOrgunitForeigntext.from_dict(_field_foreigntext)

        creator_id = d.pop("creatorId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: CsSysValueGenericValue | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CsSysValueGenericValue.from_dict(_organization)

        _research_partner = d.pop("researchPartner", UNSET)
        research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_research_partner, Unset):
            research_partner = UNSET
        else:
            research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(_research_partner)

        sortorder = d.pop("sortorder", UNSET)

        fs_res_publication_publication_creator_orgunit = cls(
            field_foreigntext=field_foreigntext,
            creator_id=creator_id,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organization=organization,
            research_partner=research_partner,
            sortorder=sortorder,
        )

        fs_res_publication_publication_creator_orgunit.additional_properties = d
        return fs_res_publication_publication_creator_orgunit

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
