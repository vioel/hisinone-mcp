from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search_request import (
        CsSysGenericSearchSearchResultHisSearchRequest,
    )
    from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
        ModelCmAppBackendEntranceExaminationEntranceExamTerm,
    )
    from ..models.model_cm_app_backend_entrance_examination_search_request_params_foreigntext import (
        ModelCmAppBackendEntranceExaminationSearchRequestParamsForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendEntranceExaminationSearchRequestParams")


@_attrs_define
class ModelCmAppBackendEntranceExaminationSearchRequestParams:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendEntranceExaminationSearchRequestParamsForeigntext | Unset):
        applicant_ids (list[int] | Unset):
        entrance_exam_guid (str | Unset):
        entrance_exam_term (ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset):
        his_search_request (CsSysGenericSearchSearchResultHisSearchRequest | Unset):  Example: {'offset': 0,
            'configFile': 'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key':
            'Publication.publicationType.id', 'selectList': [5]}]}.
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendEntranceExaminationSearchRequestParamsForeigntext | Unset = UNSET
    applicant_ids: list[int] | Unset = UNSET
    entrance_exam_guid: str | Unset = UNSET
    entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset = UNSET
    his_search_request: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        applicant_ids: list[int] | Unset = UNSET
        if not isinstance(self.applicant_ids, Unset):
            applicant_ids = self.applicant_ids

        entrance_exam_guid = self.entrance_exam_guid

        entrance_exam_term: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrance_exam_term, Unset):
            entrance_exam_term = self.entrance_exam_term.to_dict()

        his_search_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.his_search_request, Unset):
            his_search_request = self.his_search_request.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if applicant_ids is not UNSET:
            field_dict["applicantIds"] = applicant_ids
        if entrance_exam_guid is not UNSET:
            field_dict["entranceExamGuid"] = entrance_exam_guid
        if entrance_exam_term is not UNSET:
            field_dict["entranceExamTerm"] = entrance_exam_term
        if his_search_request is not UNSET:
            field_dict["hisSearchRequest"] = his_search_request
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search_request import (
            CsSysGenericSearchSearchResultHisSearchRequest,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_entrance_exam_term import (
            ModelCmAppBackendEntranceExaminationEntranceExamTerm,  # noqa: PLC0415
        )
        from ..models.model_cm_app_backend_entrance_examination_search_request_params_foreigntext import (
            ModelCmAppBackendEntranceExaminationSearchRequestParamsForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendEntranceExaminationSearchRequestParamsForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendEntranceExaminationSearchRequestParamsForeigntext.from_dict(
                _field_foreigntext
            )

        applicant_ids = cast(list[int], d.pop("applicantIds", UNSET))

        entrance_exam_guid = d.pop("entranceExamGuid", UNSET)

        _entrance_exam_term = d.pop("entranceExamTerm", UNSET)
        entrance_exam_term: ModelCmAppBackendEntranceExaminationEntranceExamTerm | Unset
        if isinstance(_entrance_exam_term, Unset):
            entrance_exam_term = UNSET
        else:
            entrance_exam_term = ModelCmAppBackendEntranceExaminationEntranceExamTerm.from_dict(_entrance_exam_term)

        _his_search_request = d.pop("hisSearchRequest", UNSET)
        his_search_request: CsSysGenericSearchSearchResultHisSearchRequest | Unset
        if isinstance(_his_search_request, Unset):
            his_search_request = UNSET
        else:
            his_search_request = CsSysGenericSearchSearchResultHisSearchRequest.from_dict(_his_search_request)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_entrance_examination_search_request_params = cls(
            field_foreigntext=field_foreigntext,
            applicant_ids=applicant_ids,
            entrance_exam_guid=entrance_exam_guid,
            entrance_exam_term=entrance_exam_term,
            his_search_request=his_search_request,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_entrance_examination_search_request_params.additional_properties = d
        return model_cm_app_backend_entrance_examination_search_request_params

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
