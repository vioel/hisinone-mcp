from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_association import (
        ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation,
    )
    from ..models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_attribute import (
        ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute,
    )


T = TypeVar("T", bound="ImplCsSysAdminutilsEntityexplorerEntityExplorerNode")


@_attrs_define
class ImplCsSysAdminutilsEntityexplorerEntityExplorerNode:
    """
    Attributes:
        associations (list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset):
        attributes (list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute] | Unset):
        class_name (str | Unset):
        domain (str | Unset):
        i_18_n_key (str | Unset):
        is_abstract (bool | Unset):
        is_embeddable (bool | Unset):
        is_value_type (bool | Unset):
        java_doc (str | Unset):
        search_path_definitions (list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset):
        sub_types (list[str] | Unset):
        table_name (str | Unset):
        unidirectional_associations (list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset):
    """

    associations: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset = UNSET
    attributes: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute] | Unset = UNSET
    class_name: str | Unset = UNSET
    domain: str | Unset = UNSET
    i_18_n_key: str | Unset = UNSET
    is_abstract: bool | Unset = UNSET
    is_embeddable: bool | Unset = UNSET
    is_value_type: bool | Unset = UNSET
    java_doc: str | Unset = UNSET
    search_path_definitions: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset = UNSET
    sub_types: list[str] | Unset = UNSET
    table_name: str | Unset = UNSET
    unidirectional_associations: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        associations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.associations, Unset):
            associations = []
            for associations_item_data in self.associations:
                associations_item = associations_item_data.to_dict()
                associations.append(associations_item)

        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        class_name = self.class_name

        domain = self.domain

        i_18_n_key = self.i_18_n_key

        is_abstract = self.is_abstract

        is_embeddable = self.is_embeddable

        is_value_type = self.is_value_type

        java_doc = self.java_doc

        search_path_definitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.search_path_definitions, Unset):
            search_path_definitions = []
            for search_path_definitions_item_data in self.search_path_definitions:
                search_path_definitions_item = search_path_definitions_item_data.to_dict()
                search_path_definitions.append(search_path_definitions_item)

        sub_types: list[str] | Unset = UNSET
        if not isinstance(self.sub_types, Unset):
            sub_types = self.sub_types

        table_name = self.table_name

        unidirectional_associations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unidirectional_associations, Unset):
            unidirectional_associations = []
            for unidirectional_associations_item_data in self.unidirectional_associations:
                unidirectional_associations_item = unidirectional_associations_item_data.to_dict()
                unidirectional_associations.append(unidirectional_associations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associations is not UNSET:
            field_dict["associations"] = associations
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if domain is not UNSET:
            field_dict["domain"] = domain
        if i_18_n_key is not UNSET:
            field_dict["i18nKey"] = i_18_n_key
        if is_abstract is not UNSET:
            field_dict["isAbstract"] = is_abstract
        if is_embeddable is not UNSET:
            field_dict["isEmbeddable"] = is_embeddable
        if is_value_type is not UNSET:
            field_dict["isValueType"] = is_value_type
        if java_doc is not UNSET:
            field_dict["javaDoc"] = java_doc
        if search_path_definitions is not UNSET:
            field_dict["searchPathDefinitions"] = search_path_definitions
        if sub_types is not UNSET:
            field_dict["subTypes"] = sub_types
        if table_name is not UNSET:
            field_dict["tableName"] = table_name
        if unidirectional_associations is not UNSET:
            field_dict["unidirectionalAssociations"] = unidirectional_associations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_association import (
            ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_attribute import (
            ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _associations = d.pop("associations", UNSET)
        associations: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset = UNSET
        if _associations is not UNSET:
            associations = []
            for associations_item_data in _associations:
                associations_item = ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation.from_dict(
                    associations_item_data
                )

                associations.append(associations_item)

        _attributes = d.pop("attributes", UNSET)
        attributes: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = ImplCsSysAdminutilsEntityexplorerEntityExplorerAttribute.from_dict(
                    attributes_item_data
                )

                attributes.append(attributes_item)

        class_name = d.pop("className", UNSET)

        domain = d.pop("domain", UNSET)

        i_18_n_key = d.pop("i18nKey", UNSET)

        is_abstract = d.pop("isAbstract", UNSET)

        is_embeddable = d.pop("isEmbeddable", UNSET)

        is_value_type = d.pop("isValueType", UNSET)

        java_doc = d.pop("javaDoc", UNSET)

        _search_path_definitions = d.pop("searchPathDefinitions", UNSET)
        search_path_definitions: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset = UNSET
        if _search_path_definitions is not UNSET:
            search_path_definitions = []
            for search_path_definitions_item_data in _search_path_definitions:
                search_path_definitions_item = ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation.from_dict(
                    search_path_definitions_item_data
                )

                search_path_definitions.append(search_path_definitions_item)

        sub_types = cast(list[str], d.pop("subTypes", UNSET))

        table_name = d.pop("tableName", UNSET)

        _unidirectional_associations = d.pop("unidirectionalAssociations", UNSET)
        unidirectional_associations: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation] | Unset = UNSET
        if _unidirectional_associations is not UNSET:
            unidirectional_associations = []
            for unidirectional_associations_item_data in _unidirectional_associations:
                unidirectional_associations_item = ImplCsSysAdminutilsEntityexplorerEntityExplorerAssociation.from_dict(
                    unidirectional_associations_item_data
                )

                unidirectional_associations.append(unidirectional_associations_item)

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_node = cls(
            associations=associations,
            attributes=attributes,
            class_name=class_name,
            domain=domain,
            i_18_n_key=i_18_n_key,
            is_abstract=is_abstract,
            is_embeddable=is_embeddable,
            is_value_type=is_value_type,
            java_doc=java_doc,
            search_path_definitions=search_path_definitions,
            sub_types=sub_types,
            table_name=table_name,
            unidirectional_associations=unidirectional_associations,
        )

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_node.additional_properties = d
        return impl_cs_sys_adminutils_entityexplorer_entity_explorer_node

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
