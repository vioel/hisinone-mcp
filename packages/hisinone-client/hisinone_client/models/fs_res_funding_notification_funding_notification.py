from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract
    from ..models.fs_res_funding_notification_funding_notification_foreigntext import (
        FsResFundingNotificationFundingNotificationForeigntext,
    )
    from ..models.fs_res_project_snapshot_project_snapshot import FsResProjectSnapshotProjectSnapshot
    from ..models.fs_res_request_output_request import FsResRequestOutputRequest
    from ..models.fs_res_request_request_base_declaration import FsResRequestRequestBaseDeclaration
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent


T = TypeVar("T", bound="FsResFundingNotificationFundingNotification")


@_attrs_define
class FsResFundingNotificationFundingNotification:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResFundingNotificationFundingNotificationForeigntext | Unset):
        active_since (int | Unset):
        applicant (CsPsvPersonRest | Unset):
        applicant_role (CsSysValueGenericValue | Unset):
        approval_status_value (CsSysValueGenericValue | Unset):
        changedate (int | Unset):
        commentary (str | Unset):
        commentary_applicant (str | Unset):
        commentary_internal (str | Unset):
        commentary_status (str | Unset):
        declarations (list[FsResRequestRequestBaseDeclaration] | Unset):
        funding_programs (list[FsResFinanceResearchContract] | Unset):
        id (int | Unset):
        inboxdate (int | Unset):
        internal_commentary (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organizations (list[CsSysValueGenericValue] | Unset):
        output_requests (list[FsResRequestOutputRequest] | Unset):
        processing_status_value (CsSysValueGenericValue | Unset):
        project_snapshot (FsResProjectSnapshotProjectSnapshot | Unset):
        reasonable_req_type (CsSysValueGenericValue | Unset):
        receiptdate (int | Unset):
        signdate (int | Unset):
        topic_area (str | Unset):
        typist (CsPsvPersonRest | Unset):
        typist_role (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResFundingNotificationFundingNotificationForeigntext | Unset = UNSET
    active_since: int | Unset = UNSET
    applicant: CsPsvPersonRest | Unset = UNSET
    applicant_role: CsSysValueGenericValue | Unset = UNSET
    approval_status_value: CsSysValueGenericValue | Unset = UNSET
    changedate: int | Unset = UNSET
    commentary: str | Unset = UNSET
    commentary_applicant: str | Unset = UNSET
    commentary_internal: str | Unset = UNSET
    commentary_status: str | Unset = UNSET
    declarations: list[FsResRequestRequestBaseDeclaration] | Unset = UNSET
    funding_programs: list[FsResFinanceResearchContract] | Unset = UNSET
    id: int | Unset = UNSET
    inboxdate: int | Unset = UNSET
    internal_commentary: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organizations: list[CsSysValueGenericValue] | Unset = UNSET
    output_requests: list[FsResRequestOutputRequest] | Unset = UNSET
    processing_status_value: CsSysValueGenericValue | Unset = UNSET
    project_snapshot: FsResProjectSnapshotProjectSnapshot | Unset = UNSET
    reasonable_req_type: CsSysValueGenericValue | Unset = UNSET
    receiptdate: int | Unset = UNSET
    signdate: int | Unset = UNSET
    topic_area: str | Unset = UNSET
    typist: CsPsvPersonRest | Unset = UNSET
    typist_role: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        active_since = self.active_since

        applicant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applicant, Unset):
            applicant = self.applicant.to_dict()

        applicant_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.applicant_role, Unset):
            applicant_role = self.applicant_role.to_dict()

        approval_status_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.approval_status_value, Unset):
            approval_status_value = self.approval_status_value.to_dict()

        changedate = self.changedate

        commentary = self.commentary

        commentary_applicant = self.commentary_applicant

        commentary_internal = self.commentary_internal

        commentary_status = self.commentary_status

        declarations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.declarations, Unset):
            declarations = []
            for declarations_item_data in self.declarations:
                declarations_item = declarations_item_data.to_dict()
                declarations.append(declarations_item)

        funding_programs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.funding_programs, Unset):
            funding_programs = []
            for funding_programs_item_data in self.funding_programs:
                funding_programs_item = funding_programs_item_data.to_dict()
                funding_programs.append(funding_programs_item)

        id = self.id

        inboxdate = self.inboxdate

        internal_commentary = self.internal_commentary

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        output_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.output_requests, Unset):
            output_requests = []
            for output_requests_item_data in self.output_requests:
                output_requests_item = output_requests_item_data.to_dict()
                output_requests.append(output_requests_item)

        processing_status_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.processing_status_value, Unset):
            processing_status_value = self.processing_status_value.to_dict()

        project_snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_snapshot, Unset):
            project_snapshot = self.project_snapshot.to_dict()

        reasonable_req_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reasonable_req_type, Unset):
            reasonable_req_type = self.reasonable_req_type.to_dict()

        receiptdate = self.receiptdate

        signdate = self.signdate

        topic_area = self.topic_area

        typist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.typist, Unset):
            typist = self.typist.to_dict()

        typist_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.typist_role, Unset):
            typist_role = self.typist_role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if active_since is not UNSET:
            field_dict["activeSince"] = active_since
        if applicant is not UNSET:
            field_dict["applicant"] = applicant
        if applicant_role is not UNSET:
            field_dict["applicantRole"] = applicant_role
        if approval_status_value is not UNSET:
            field_dict["approvalStatusValue"] = approval_status_value
        if changedate is not UNSET:
            field_dict["changedate"] = changedate
        if commentary is not UNSET:
            field_dict["commentary"] = commentary
        if commentary_applicant is not UNSET:
            field_dict["commentaryApplicant"] = commentary_applicant
        if commentary_internal is not UNSET:
            field_dict["commentaryInternal"] = commentary_internal
        if commentary_status is not UNSET:
            field_dict["commentaryStatus"] = commentary_status
        if declarations is not UNSET:
            field_dict["declarations"] = declarations
        if funding_programs is not UNSET:
            field_dict["fundingPrograms"] = funding_programs
        if id is not UNSET:
            field_dict["id"] = id
        if inboxdate is not UNSET:
            field_dict["inboxdate"] = inboxdate
        if internal_commentary is not UNSET:
            field_dict["internalCommentary"] = internal_commentary
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if output_requests is not UNSET:
            field_dict["outputRequests"] = output_requests
        if processing_status_value is not UNSET:
            field_dict["processingStatusValue"] = processing_status_value
        if project_snapshot is not UNSET:
            field_dict["projectSnapshot"] = project_snapshot
        if reasonable_req_type is not UNSET:
            field_dict["reasonableReqType"] = reasonable_req_type
        if receiptdate is not UNSET:
            field_dict["receiptdate"] = receiptdate
        if signdate is not UNSET:
            field_dict["signdate"] = signdate
        if topic_area is not UNSET:
            field_dict["topicArea"] = topic_area
        if typist is not UNSET:
            field_dict["typist"] = typist
        if typist_role is not UNSET:
            field_dict["typistRole"] = typist_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_finance_research_contract import FsResFinanceResearchContract  # noqa: PLC0415
        from ..models.fs_res_funding_notification_funding_notification_foreigntext import (
            FsResFundingNotificationFundingNotificationForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_project_snapshot_project_snapshot import FsResProjectSnapshotProjectSnapshot  # noqa: PLC0415
        from ..models.fs_res_request_output_request import FsResRequestOutputRequest  # noqa: PLC0415
        from ..models.fs_res_request_request_base_declaration import FsResRequestRequestBaseDeclaration  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResFundingNotificationFundingNotificationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResFundingNotificationFundingNotificationForeigntext.from_dict(_field_foreigntext)

        active_since = d.pop("activeSince", UNSET)

        _applicant = d.pop("applicant", UNSET)
        applicant: CsPsvPersonRest | Unset
        if isinstance(_applicant, Unset):
            applicant = UNSET
        else:
            applicant = CsPsvPersonRest.from_dict(_applicant)

        _applicant_role = d.pop("applicantRole", UNSET)
        applicant_role: CsSysValueGenericValue | Unset
        if isinstance(_applicant_role, Unset):
            applicant_role = UNSET
        else:
            applicant_role = CsSysValueGenericValue.from_dict(_applicant_role)

        _approval_status_value = d.pop("approvalStatusValue", UNSET)
        approval_status_value: CsSysValueGenericValue | Unset
        if isinstance(_approval_status_value, Unset):
            approval_status_value = UNSET
        else:
            approval_status_value = CsSysValueGenericValue.from_dict(_approval_status_value)

        changedate = d.pop("changedate", UNSET)

        commentary = d.pop("commentary", UNSET)

        commentary_applicant = d.pop("commentaryApplicant", UNSET)

        commentary_internal = d.pop("commentaryInternal", UNSET)

        commentary_status = d.pop("commentaryStatus", UNSET)

        _declarations = d.pop("declarations", UNSET)
        declarations: list[FsResRequestRequestBaseDeclaration] | Unset = UNSET
        if _declarations is not UNSET:
            declarations = []
            for declarations_item_data in _declarations:
                declarations_item = FsResRequestRequestBaseDeclaration.from_dict(declarations_item_data)

                declarations.append(declarations_item)

        _funding_programs = d.pop("fundingPrograms", UNSET)
        funding_programs: list[FsResFinanceResearchContract] | Unset = UNSET
        if _funding_programs is not UNSET:
            funding_programs = []
            for funding_programs_item_data in _funding_programs:
                funding_programs_item = FsResFinanceResearchContract.from_dict(funding_programs_item_data)

                funding_programs.append(funding_programs_item)

        id = d.pop("id", UNSET)

        inboxdate = d.pop("inboxdate", UNSET)

        internal_commentary = d.pop("internalCommentary", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[CsSysValueGenericValue] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = CsSysValueGenericValue.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        _output_requests = d.pop("outputRequests", UNSET)
        output_requests: list[FsResRequestOutputRequest] | Unset = UNSET
        if _output_requests is not UNSET:
            output_requests = []
            for output_requests_item_data in _output_requests:
                output_requests_item = FsResRequestOutputRequest.from_dict(output_requests_item_data)

                output_requests.append(output_requests_item)

        _processing_status_value = d.pop("processingStatusValue", UNSET)
        processing_status_value: CsSysValueGenericValue | Unset
        if isinstance(_processing_status_value, Unset):
            processing_status_value = UNSET
        else:
            processing_status_value = CsSysValueGenericValue.from_dict(_processing_status_value)

        _project_snapshot = d.pop("projectSnapshot", UNSET)
        project_snapshot: FsResProjectSnapshotProjectSnapshot | Unset
        if isinstance(_project_snapshot, Unset):
            project_snapshot = UNSET
        else:
            project_snapshot = FsResProjectSnapshotProjectSnapshot.from_dict(_project_snapshot)

        _reasonable_req_type = d.pop("reasonableReqType", UNSET)
        reasonable_req_type: CsSysValueGenericValue | Unset
        if isinstance(_reasonable_req_type, Unset):
            reasonable_req_type = UNSET
        else:
            reasonable_req_type = CsSysValueGenericValue.from_dict(_reasonable_req_type)

        receiptdate = d.pop("receiptdate", UNSET)

        signdate = d.pop("signdate", UNSET)

        topic_area = d.pop("topicArea", UNSET)

        _typist = d.pop("typist", UNSET)
        typist: CsPsvPersonRest | Unset
        if isinstance(_typist, Unset):
            typist = UNSET
        else:
            typist = CsPsvPersonRest.from_dict(_typist)

        _typist_role = d.pop("typistRole", UNSET)
        typist_role: CsSysValueGenericValue | Unset
        if isinstance(_typist_role, Unset):
            typist_role = UNSET
        else:
            typist_role = CsSysValueGenericValue.from_dict(_typist_role)

        fs_res_funding_notification_funding_notification = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            active_since=active_since,
            applicant=applicant,
            applicant_role=applicant_role,
            approval_status_value=approval_status_value,
            changedate=changedate,
            commentary=commentary,
            commentary_applicant=commentary_applicant,
            commentary_internal=commentary_internal,
            commentary_status=commentary_status,
            declarations=declarations,
            funding_programs=funding_programs,
            id=id,
            inboxdate=inboxdate,
            internal_commentary=internal_commentary,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organizations=organizations,
            output_requests=output_requests,
            processing_status_value=processing_status_value,
            project_snapshot=project_snapshot,
            reasonable_req_type=reasonable_req_type,
            receiptdate=receiptdate,
            signdate=signdate,
            topic_area=topic_area,
            typist=typist,
            typist_role=typist_role,
        )

        fs_res_funding_notification_funding_notification.additional_properties = d
        return fs_res_funding_notification_funding_notification

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
