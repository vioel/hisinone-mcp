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
    from ..models.fs_res_project_project_obj import FsResProjectProjectObj
    from ..models.fs_res_project_snapshot_project_snapshot_foreigntext import (
        FsResProjectSnapshotProjectSnapshotForeigntext,
    )
    from ..models.fs_res_project_snapshot_project_snapshot_person_position import (
        FsResProjectSnapshotProjectSnapshotPersonPosition,
    )


T = TypeVar("T", bound="FsResProjectSnapshotProjectSnapshot")


@_attrs_define
class FsResProjectSnapshotProjectSnapshot:
    """
    Attributes:
        field_foreigntext (FsResProjectSnapshotProjectSnapshotForeigntext | Unset):
        defaulttext (str | Unset):
        enddate (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        members (list[FsResProjectSnapshotProjectSnapshotPersonPosition] | Unset):
        obj_guid (str | Unset):
        predecessor (FsResProjectProjectObj | Unset):
        project (FsResProjectProjectObj | Unset):
        spokesperson_orgunit (CsSysValueGenericValue | Unset):
        spokesperson_research_partner (CsPsvExternalOrganisationResearchPartnerSimple | Unset):
        startdate (int | Unset):
        subject_areas (list[CsSysValueGenericValue] | Unset):
    """

    field_foreigntext: FsResProjectSnapshotProjectSnapshotForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    enddate: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    members: list[FsResProjectSnapshotProjectSnapshotPersonPosition] | Unset = UNSET
    obj_guid: str | Unset = UNSET
    predecessor: FsResProjectProjectObj | Unset = UNSET
    project: FsResProjectProjectObj | Unset = UNSET
    spokesperson_orgunit: CsSysValueGenericValue | Unset = UNSET
    spokesperson_research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset = UNSET
    startdate: int | Unset = UNSET
    subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        enddate = self.enddate

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        obj_guid = self.obj_guid

        predecessor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.predecessor, Unset):
            predecessor = self.predecessor.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        spokesperson_orgunit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spokesperson_orgunit, Unset):
            spokesperson_orgunit = self.spokesperson_orgunit.to_dict()

        spokesperson_research_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spokesperson_research_partner, Unset):
            spokesperson_research_partner = self.spokesperson_research_partner.to_dict()

        startdate = self.startdate

        subject_areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subject_areas, Unset):
            subject_areas = []
            for subject_areas_item_data in self.subject_areas:
                subject_areas_item = subject_areas_item_data.to_dict()
                subject_areas.append(subject_areas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if enddate is not UNSET:
            field_dict["enddate"] = enddate
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if members is not UNSET:
            field_dict["members"] = members
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if predecessor is not UNSET:
            field_dict["predecessor"] = predecessor
        if project is not UNSET:
            field_dict["project"] = project
        if spokesperson_orgunit is not UNSET:
            field_dict["spokespersonOrgunit"] = spokesperson_orgunit
        if spokesperson_research_partner is not UNSET:
            field_dict["spokespersonResearchPartner"] = spokesperson_research_partner
        if startdate is not UNSET:
            field_dict["startdate"] = startdate
        if subject_areas is not UNSET:
            field_dict["subjectAreas"] = subject_areas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_external_organisation_research_partner_simple import (
            CsPsvExternalOrganisationResearchPartnerSimple,  # noqa: PLC0415
        )
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_project_project_obj import FsResProjectProjectObj  # noqa: PLC0415
        from ..models.fs_res_project_snapshot_project_snapshot_foreigntext import (
            FsResProjectSnapshotProjectSnapshotForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_project_snapshot_project_snapshot_person_position import (
            FsResProjectSnapshotProjectSnapshotPersonPosition,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResProjectSnapshotProjectSnapshotForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResProjectSnapshotProjectSnapshotForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        enddate = d.pop("enddate", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        _members = d.pop("members", UNSET)
        members: list[FsResProjectSnapshotProjectSnapshotPersonPosition] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = FsResProjectSnapshotProjectSnapshotPersonPosition.from_dict(members_item_data)

                members.append(members_item)

        obj_guid = d.pop("objGuid", UNSET)

        _predecessor = d.pop("predecessor", UNSET)
        predecessor: FsResProjectProjectObj | Unset
        if isinstance(_predecessor, Unset):
            predecessor = UNSET
        else:
            predecessor = FsResProjectProjectObj.from_dict(_predecessor)

        _project = d.pop("project", UNSET)
        project: FsResProjectProjectObj | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = FsResProjectProjectObj.from_dict(_project)

        _spokesperson_orgunit = d.pop("spokespersonOrgunit", UNSET)
        spokesperson_orgunit: CsSysValueGenericValue | Unset
        if isinstance(_spokesperson_orgunit, Unset):
            spokesperson_orgunit = UNSET
        else:
            spokesperson_orgunit = CsSysValueGenericValue.from_dict(_spokesperson_orgunit)

        _spokesperson_research_partner = d.pop("spokespersonResearchPartner", UNSET)
        spokesperson_research_partner: CsPsvExternalOrganisationResearchPartnerSimple | Unset
        if isinstance(_spokesperson_research_partner, Unset):
            spokesperson_research_partner = UNSET
        else:
            spokesperson_research_partner = CsPsvExternalOrganisationResearchPartnerSimple.from_dict(
                _spokesperson_research_partner
            )

        startdate = d.pop("startdate", UNSET)

        _subject_areas = d.pop("subjectAreas", UNSET)
        subject_areas: list[CsSysValueGenericValue] | Unset = UNSET
        if _subject_areas is not UNSET:
            subject_areas = []
            for subject_areas_item_data in _subject_areas:
                subject_areas_item = CsSysValueGenericValue.from_dict(subject_areas_item_data)

                subject_areas.append(subject_areas_item)

        fs_res_project_snapshot_project_snapshot = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            enddate=enddate,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            members=members,
            obj_guid=obj_guid,
            predecessor=predecessor,
            project=project,
            spokesperson_orgunit=spokesperson_orgunit,
            spokesperson_research_partner=spokesperson_research_partner,
            startdate=startdate,
            subject_areas=subject_areas,
        )

        fs_res_project_snapshot_project_snapshot.additional_properties = d
        return fs_res_project_snapshot_project_snapshot

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
