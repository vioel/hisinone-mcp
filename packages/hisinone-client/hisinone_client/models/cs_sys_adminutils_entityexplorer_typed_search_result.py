from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iface_common_generic_search_service_datatype import IfaceCommonGenericSearchServiceDatatype
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CsSysAdminutilsEntityexplorerTypedSearchResult")


@_attrs_define
class CsSysAdminutilsEntityexplorerTypedSearchResult:
    """
    Attributes:
        error_message (str | Unset):
        number_of_rows (int | Unset):
        search_result (list[list[JavaLangObject]] | Unset):
        types (list[IfaceCommonGenericSearchServiceDatatype] | Unset):
    """

    error_message: str | Unset = UNSET
    number_of_rows: int | Unset = UNSET
    search_result: list[list[JavaLangObject]] | Unset = UNSET
    types: list[IfaceCommonGenericSearchServiceDatatype] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        number_of_rows = self.number_of_rows

        search_result: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.search_result, Unset):
            search_result = []
            for search_result_item_data in self.search_result:
                search_result_item: list[dict[str, Any]] = []
                for search_result_item_item_data in search_result_item_data:
                    search_result_item_item = search_result_item_item_data.to_dict()
                    search_result_item.append(search_result_item_item)

                search_result.append(search_result_item)

        types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = []
            for types_item_data in self.types:
                types_item = types_item_data.to_dict()
                types.append(types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if number_of_rows is not UNSET:
            field_dict["numberOfRows"] = number_of_rows
        if search_result is not UNSET:
            field_dict["searchResult"] = search_result
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iface_common_generic_search_service_datatype import IfaceCommonGenericSearchServiceDatatype  # noqa: PLC0415
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        number_of_rows = d.pop("numberOfRows", UNSET)

        _search_result = d.pop("searchResult", UNSET)
        search_result: list[list[JavaLangObject]] | Unset = UNSET
        if _search_result is not UNSET:
            search_result = []
            for search_result_item_data in _search_result:
                search_result_item: list[JavaLangObject] = []
                _search_result_item = search_result_item_data
                for search_result_item_item_data in _search_result_item:
                    search_result_item_item = JavaLangObject.from_dict(search_result_item_item_data)

                    search_result_item.append(search_result_item_item)

                search_result.append(search_result_item)

        _types = d.pop("types", UNSET)
        types: list[IfaceCommonGenericSearchServiceDatatype] | Unset = UNSET
        if _types is not UNSET:
            types = []
            for types_item_data in _types:
                types_item = IfaceCommonGenericSearchServiceDatatype.from_dict(types_item_data)

                types.append(types_item)

        cs_sys_adminutils_entityexplorer_typed_search_result = cls(
            error_message=error_message,
            number_of_rows=number_of_rows,
            search_result=search_result,
            types=types,
        )

        cs_sys_adminutils_entityexplorer_typed_search_result.additional_properties = d
        return cs_sys_adminutils_entityexplorer_typed_search_result

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
