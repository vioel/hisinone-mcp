from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_search_request import (
        CsSysGenericSearchSearchResultHisSearchRequest,
    )
    from ..models.cs_sys_jobs_job_request_job_params import CsSysJobsJobRequestJobParams
    from ..models.cs_sys_jobs_job_request_job_params_as_serializable_map import (
        CsSysJobsJobRequestJobParamsAsSerializableMap,
    )
    from ..models.cs_sys_jobs_job_request_selected_row_data_item import CsSysJobsJobRequestSelectedRowDataItem


T = TypeVar("T", bound="CsSysJobsJobRequest")


@_attrs_define
class CsSysJobsJobRequest:
    """
    Example:
        {'searchRequest': {'configFile': 'sucheRollen.xml', 'searchFields': [{'key': 'OrgroleValue.uniquename',
            'searchString': 'alumni', 'selectList': None}], 'offset': 0, 'limit': -1}, 'executionType': 'JobManagement',
            'jobKey': 'csvExport', 'selectedRowData': [{'OrgroleValue.id': 100069}]}

    Attributes:
        execution_type (str | Unset):
        job_configuration (str | Unset):
        job_key (str | Unset):
        job_params (CsSysJobsJobRequestJobParams | Unset):
        job_params_as_serializable_map (CsSysJobsJobRequestJobParamsAsSerializableMap | Unset):
        job_starter_key (str | Unset):
        search_request (CsSysGenericSearchSearchResultHisSearchRequest | Unset):  Example: {'offset': 0, 'configFile':
            'fs/res/searchPublication.xml', 'limit': 10, 'searchFields': [{'key': 'Publication.publicationType.id',
            'selectList': [5]}]}.
        selected_row_data (list[CsSysJobsJobRequestSelectedRowDataItem] | Unset):
    """

    execution_type: str | Unset = UNSET
    job_configuration: str | Unset = UNSET
    job_key: str | Unset = UNSET
    job_params: CsSysJobsJobRequestJobParams | Unset = UNSET
    job_params_as_serializable_map: CsSysJobsJobRequestJobParamsAsSerializableMap | Unset = UNSET
    job_starter_key: str | Unset = UNSET
    search_request: CsSysGenericSearchSearchResultHisSearchRequest | Unset = UNSET
    selected_row_data: list[CsSysJobsJobRequestSelectedRowDataItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        execution_type = self.execution_type

        job_configuration = self.job_configuration

        job_key = self.job_key

        job_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_params, Unset):
            job_params = self.job_params.to_dict()

        job_params_as_serializable_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_params_as_serializable_map, Unset):
            job_params_as_serializable_map = self.job_params_as_serializable_map.to_dict()

        job_starter_key = self.job_starter_key

        search_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_request, Unset):
            search_request = self.search_request.to_dict()

        selected_row_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selected_row_data, Unset):
            selected_row_data = []
            for selected_row_data_item_data in self.selected_row_data:
                selected_row_data_item = selected_row_data_item_data.to_dict()
                selected_row_data.append(selected_row_data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execution_type is not UNSET:
            field_dict["executionType"] = execution_type
        if job_configuration is not UNSET:
            field_dict["jobConfiguration"] = job_configuration
        if job_key is not UNSET:
            field_dict["jobKey"] = job_key
        if job_params is not UNSET:
            field_dict["jobParams"] = job_params
        if job_params_as_serializable_map is not UNSET:
            field_dict["jobParamsAsSerializableMap"] = job_params_as_serializable_map
        if job_starter_key is not UNSET:
            field_dict["jobStarterKey"] = job_starter_key
        if search_request is not UNSET:
            field_dict["searchRequest"] = search_request
        if selected_row_data is not UNSET:
            field_dict["selectedRowData"] = selected_row_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_search_request import (
            CsSysGenericSearchSearchResultHisSearchRequest,  # noqa: PLC0415
        )
        from ..models.cs_sys_jobs_job_request_job_params import CsSysJobsJobRequestJobParams  # noqa: PLC0415
        from ..models.cs_sys_jobs_job_request_job_params_as_serializable_map import (
            CsSysJobsJobRequestJobParamsAsSerializableMap,  # noqa: PLC0415
        )
        from ..models.cs_sys_jobs_job_request_selected_row_data_item import CsSysJobsJobRequestSelectedRowDataItem  # noqa: PLC0415

        d = dict(src_dict)
        execution_type = d.pop("executionType", UNSET)

        job_configuration = d.pop("jobConfiguration", UNSET)

        job_key = d.pop("jobKey", UNSET)

        _job_params = d.pop("jobParams", UNSET)
        job_params: CsSysJobsJobRequestJobParams | Unset
        if isinstance(_job_params, Unset):
            job_params = UNSET
        else:
            job_params = CsSysJobsJobRequestJobParams.from_dict(_job_params)

        _job_params_as_serializable_map = d.pop("jobParamsAsSerializableMap", UNSET)
        job_params_as_serializable_map: CsSysJobsJobRequestJobParamsAsSerializableMap | Unset
        if isinstance(_job_params_as_serializable_map, Unset):
            job_params_as_serializable_map = UNSET
        else:
            job_params_as_serializable_map = CsSysJobsJobRequestJobParamsAsSerializableMap.from_dict(
                _job_params_as_serializable_map
            )

        job_starter_key = d.pop("jobStarterKey", UNSET)

        _search_request = d.pop("searchRequest", UNSET)
        search_request: CsSysGenericSearchSearchResultHisSearchRequest | Unset
        if isinstance(_search_request, Unset):
            search_request = UNSET
        else:
            search_request = CsSysGenericSearchSearchResultHisSearchRequest.from_dict(_search_request)

        _selected_row_data = d.pop("selectedRowData", UNSET)
        selected_row_data: list[CsSysJobsJobRequestSelectedRowDataItem] | Unset = UNSET
        if _selected_row_data is not UNSET:
            selected_row_data = []
            for selected_row_data_item_data in _selected_row_data:
                selected_row_data_item = CsSysJobsJobRequestSelectedRowDataItem.from_dict(selected_row_data_item_data)

                selected_row_data.append(selected_row_data_item)

        cs_sys_jobs_job_request = cls(
            execution_type=execution_type,
            job_configuration=job_configuration,
            job_key=job_key,
            job_params=job_params,
            job_params_as_serializable_map=job_params_as_serializable_map,
            job_starter_key=job_starter_key,
            search_request=search_request,
            selected_row_data=selected_row_data,
        )

        cs_sys_jobs_job_request.additional_properties = d
        return cs_sys_jobs_job_request

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
