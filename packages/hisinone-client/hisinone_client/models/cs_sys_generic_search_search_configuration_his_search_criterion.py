from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationHisSearchCriterion")


@_attrs_define
class CsSysGenericSearchSearchConfigurationHisSearchCriterion:
    """
    Attributes:
        helptext (str | Unset):
        input_type (str | Unset):
        label (str | Unset):
        multiple_select (bool | Unset):
        not_ (str | Unset):
        path (str | Unset):
        quick_search_criterion (bool | Unset):
        required (bool | Unset):
        search_config_file (str | Unset):
        search_entity (str | Unset):
        select_from (str | Unset):
        select_from_tree (str | Unset):
        show_dropdown_icon (bool | Unset):
        show_null_item (bool | Unset):
        show_search_filter (bool | Unset):
        show_unequal_option (str | Unset):
        tree_name (str | Unset):
        typeahead_max_results (int | Unset):
        typeahead_min_length (int | Unset):
        value (JavaLangObject | Unset):
    """

    helptext: str | Unset = UNSET
    input_type: str | Unset = UNSET
    label: str | Unset = UNSET
    multiple_select: bool | Unset = UNSET
    not_: str | Unset = UNSET
    path: str | Unset = UNSET
    quick_search_criterion: bool | Unset = UNSET
    required: bool | Unset = UNSET
    search_config_file: str | Unset = UNSET
    search_entity: str | Unset = UNSET
    select_from: str | Unset = UNSET
    select_from_tree: str | Unset = UNSET
    show_dropdown_icon: bool | Unset = UNSET
    show_null_item: bool | Unset = UNSET
    show_search_filter: bool | Unset = UNSET
    show_unequal_option: str | Unset = UNSET
    tree_name: str | Unset = UNSET
    typeahead_max_results: int | Unset = UNSET
    typeahead_min_length: int | Unset = UNSET
    value: JavaLangObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        helptext = self.helptext

        input_type = self.input_type

        label = self.label

        multiple_select = self.multiple_select

        not_ = self.not_

        path = self.path

        quick_search_criterion = self.quick_search_criterion

        required = self.required

        search_config_file = self.search_config_file

        search_entity = self.search_entity

        select_from = self.select_from

        select_from_tree = self.select_from_tree

        show_dropdown_icon = self.show_dropdown_icon

        show_null_item = self.show_null_item

        show_search_filter = self.show_search_filter

        show_unequal_option = self.show_unequal_option

        tree_name = self.tree_name

        typeahead_max_results = self.typeahead_max_results

        typeahead_min_length = self.typeahead_min_length

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if helptext is not UNSET:
            field_dict["helptext"] = helptext
        if input_type is not UNSET:
            field_dict["inputType"] = input_type
        if label is not UNSET:
            field_dict["label"] = label
        if multiple_select is not UNSET:
            field_dict["multipleSelect"] = multiple_select
        if not_ is not UNSET:
            field_dict["not"] = not_
        if path is not UNSET:
            field_dict["path"] = path
        if quick_search_criterion is not UNSET:
            field_dict["quickSearchCriterion"] = quick_search_criterion
        if required is not UNSET:
            field_dict["required"] = required
        if search_config_file is not UNSET:
            field_dict["searchConfigFile"] = search_config_file
        if search_entity is not UNSET:
            field_dict["searchEntity"] = search_entity
        if select_from is not UNSET:
            field_dict["selectFrom"] = select_from
        if select_from_tree is not UNSET:
            field_dict["selectFromTree"] = select_from_tree
        if show_dropdown_icon is not UNSET:
            field_dict["showDropdownIcon"] = show_dropdown_icon
        if show_null_item is not UNSET:
            field_dict["showNullItem"] = show_null_item
        if show_search_filter is not UNSET:
            field_dict["showSearchFilter"] = show_search_filter
        if show_unequal_option is not UNSET:
            field_dict["showUnequalOption"] = show_unequal_option
        if tree_name is not UNSET:
            field_dict["treeName"] = tree_name
        if typeahead_max_results is not UNSET:
            field_dict["typeaheadMaxResults"] = typeahead_max_results
        if typeahead_min_length is not UNSET:
            field_dict["typeaheadMinLength"] = typeahead_min_length
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        helptext = d.pop("helptext", UNSET)

        input_type = d.pop("inputType", UNSET)

        label = d.pop("label", UNSET)

        multiple_select = d.pop("multipleSelect", UNSET)

        not_ = d.pop("not", UNSET)

        path = d.pop("path", UNSET)

        quick_search_criterion = d.pop("quickSearchCriterion", UNSET)

        required = d.pop("required", UNSET)

        search_config_file = d.pop("searchConfigFile", UNSET)

        search_entity = d.pop("searchEntity", UNSET)

        select_from = d.pop("selectFrom", UNSET)

        select_from_tree = d.pop("selectFromTree", UNSET)

        show_dropdown_icon = d.pop("showDropdownIcon", UNSET)

        show_null_item = d.pop("showNullItem", UNSET)

        show_search_filter = d.pop("showSearchFilter", UNSET)

        show_unequal_option = d.pop("showUnequalOption", UNSET)

        tree_name = d.pop("treeName", UNSET)

        typeahead_max_results = d.pop("typeaheadMaxResults", UNSET)

        typeahead_min_length = d.pop("typeaheadMinLength", UNSET)

        _value = d.pop("value", UNSET)
        value: JavaLangObject | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = JavaLangObject.from_dict(_value)

        cs_sys_generic_search_search_configuration_his_search_criterion = cls(
            helptext=helptext,
            input_type=input_type,
            label=label,
            multiple_select=multiple_select,
            not_=not_,
            path=path,
            quick_search_criterion=quick_search_criterion,
            required=required,
            search_config_file=search_config_file,
            search_entity=search_entity,
            select_from=select_from,
            select_from_tree=select_from_tree,
            show_dropdown_icon=show_dropdown_icon,
            show_null_item=show_null_item,
            show_search_filter=show_search_filter,
            show_unequal_option=show_unequal_option,
            tree_name=tree_name,
            typeahead_max_results=typeahead_max_results,
            typeahead_min_length=typeahead_min_length,
            value=value,
        )

        cs_sys_generic_search_search_configuration_his_search_criterion.additional_properties = d
        return cs_sys_generic_search_search_configuration_his_search_criterion

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
