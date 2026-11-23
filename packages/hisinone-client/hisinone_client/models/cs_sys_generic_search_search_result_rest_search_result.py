from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_result_his_column_metadata import (
        CsSysGenericSearchSearchResultHisColumnMetadata,
    )
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CsSysGenericSearchSearchResultRestSearchResult")


@_attrs_define
class CsSysGenericSearchSearchResultRestSearchResult:
    """
    Attributes:
        columns (list[CsSysGenericSearchSearchResultHisColumnMetadata] | Unset):
        data (list[list[JavaLangObject]] | Unset):
        limit (int | Unset):
        max_result_rows (int | Unset):
        name (str | Unset):
        offset (int | Unset):
        total_count (int | Unset):
    """

    columns: list[CsSysGenericSearchSearchResultHisColumnMetadata] | Unset = UNSET
    data: list[list[JavaLangObject]] | Unset = UNSET
    limit: int | Unset = UNSET
    max_result_rows: int | Unset = UNSET
    name: str | Unset = UNSET
    offset: int | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        data: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: list[dict[str, Any]] = []
                for data_item_item_data in data_item_data:
                    data_item_item = data_item_item_data.to_dict()
                    data_item.append(data_item_item)

                data.append(data_item)

        limit = self.limit

        max_result_rows = self.max_result_rows

        name = self.name

        offset = self.offset

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if columns is not UNSET:
            field_dict["columns"] = columns
        if data is not UNSET:
            field_dict["data"] = data
        if limit is not UNSET:
            field_dict["limit"] = limit
        if max_result_rows is not UNSET:
            field_dict["maxResultRows"] = max_result_rows
        if name is not UNSET:
            field_dict["name"] = name
        if offset is not UNSET:
            field_dict["offset"] = offset
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_result_his_column_metadata import (
            CsSysGenericSearchSearchResultHisColumnMetadata,  # noqa: PLC0415
        )
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        _columns = d.pop("columns", UNSET)
        columns: list[CsSysGenericSearchSearchResultHisColumnMetadata] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = CsSysGenericSearchSearchResultHisColumnMetadata.from_dict(columns_item_data)

                columns.append(columns_item)

        _data = d.pop("data", UNSET)
        data: list[list[JavaLangObject]] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item: list[JavaLangObject] = []
                _data_item = data_item_data
                for data_item_item_data in _data_item:
                    data_item_item = JavaLangObject.from_dict(data_item_item_data)

                    data_item.append(data_item_item)

                data.append(data_item)

        limit = d.pop("limit", UNSET)

        max_result_rows = d.pop("maxResultRows", UNSET)

        name = d.pop("name", UNSET)

        offset = d.pop("offset", UNSET)

        total_count = d.pop("totalCount", UNSET)

        cs_sys_generic_search_search_result_rest_search_result = cls(
            columns=columns,
            data=data,
            limit=limit,
            max_result_rows=max_result_rows,
            name=name,
            offset=offset,
            total_count=total_count,
        )

        cs_sys_generic_search_search_result_rest_search_result.additional_properties = d
        return cs_sys_generic_search_search_result_rest_search_result

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
