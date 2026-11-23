from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CsSysGenericSearchSearchResultHisColumnMetadata")


@_attrs_define
class CsSysGenericSearchSearchResultHisColumnMetadata:
    """
    Attributes:
        data_type (str | Unset):
        filter_path (str | Unset):
        format_ (str | Unset):
        id (str | Unset):
        label (str | Unset):
        sort_path (str | Unset):
        sortable (bool | Unset):
        visible (bool | Unset):
    """

    data_type: str | Unset = UNSET
    filter_path: str | Unset = UNSET
    format_: str | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    sort_path: str | Unset = UNSET
    sortable: bool | Unset = UNSET
    visible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        data_type = self.data_type

        filter_path = self.filter_path

        format_ = self.format_

        id = self.id

        label = self.label

        sort_path = self.sort_path

        sortable = self.sortable

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if filter_path is not UNSET:
            field_dict["filterPath"] = filter_path
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if sort_path is not UNSET:
            field_dict["sortPath"] = sort_path
        if sortable is not UNSET:
            field_dict["sortable"] = sortable
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_type = d.pop("dataType", UNSET)

        filter_path = d.pop("filterPath", UNSET)

        format_ = d.pop("format", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        sort_path = d.pop("sortPath", UNSET)

        sortable = d.pop("sortable", UNSET)

        visible = d.pop("visible", UNSET)

        cs_sys_generic_search_search_result_his_column_metadata = cls(
            data_type=data_type,
            filter_path=filter_path,
            format_=format_,
            id=id,
            label=label,
            sort_path=sort_path,
            sortable=sortable,
            visible=visible,
        )

        cs_sys_generic_search_search_result_his_column_metadata.additional_properties = d
        return cs_sys_generic_search_search_result_his_column_metadata

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
