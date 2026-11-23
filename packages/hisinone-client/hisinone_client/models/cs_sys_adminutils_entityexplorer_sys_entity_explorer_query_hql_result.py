from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CsSysAdminutilsEntityexplorerSysEntityExplorerQueryHqlResult")


@_attrs_define
class CsSysAdminutilsEntityexplorerSysEntityExplorerQueryHqlResult:
    """
    Attributes:
        error_message (str | Unset):
        number_of_rows (int | Unset):
        result (list[list[JavaLangObject]] | Unset):
        result_table_column_names (list[str] | Unset):
    """

    error_message: str | Unset = UNSET
    number_of_rows: int | Unset = UNSET
    result: list[list[JavaLangObject]] | Unset = UNSET
    result_table_column_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        number_of_rows = self.number_of_rows

        result: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item: list[dict[str, Any]] = []
                for result_item_item_data in result_item_data:
                    result_item_item = result_item_item_data.to_dict()
                    result_item.append(result_item_item)

                result.append(result_item)

        result_table_column_names: list[str] | Unset = UNSET
        if not isinstance(self.result_table_column_names, Unset):
            result_table_column_names = self.result_table_column_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if number_of_rows is not UNSET:
            field_dict["numberOfRows"] = number_of_rows
        if result is not UNSET:
            field_dict["result"] = result
        if result_table_column_names is not UNSET:
            field_dict["resultTableColumnNames"] = result_table_column_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        number_of_rows = d.pop("numberOfRows", UNSET)

        _result = d.pop("result", UNSET)
        result: list[list[JavaLangObject]] | Unset = UNSET
        if _result is not UNSET:
            result = []
            for result_item_data in _result:
                result_item: list[JavaLangObject] = []
                _result_item = result_item_data
                for result_item_item_data in _result_item:
                    result_item_item = JavaLangObject.from_dict(result_item_item_data)

                    result_item.append(result_item_item)

                result.append(result_item)

        result_table_column_names = cast(list[str], d.pop("resultTableColumnNames", UNSET))

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_query_hql_result = cls(
            error_message=error_message,
            number_of_rows=number_of_rows,
            result=result,
            result_table_column_names=result_table_column_names,
        )

        cs_sys_adminutils_entityexplorer_sys_entity_explorer_query_hql_result.additional_properties = d
        return cs_sys_adminutils_entityexplorer_sys_entity_explorer_query_hql_result

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
