from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_node import (
        ImplCsSysAdminutilsEntityexplorerEntityExplorerNode,
    )


T = TypeVar("T", bound="ImplCsSysAdminutilsEntityexplorerEntityExplorerModel")


@_attrs_define
class ImplCsSysAdminutilsEntityexplorerEntityExplorerModel:
    """
    Attributes:
        nodes (list[ImplCsSysAdminutilsEntityexplorerEntityExplorerNode] | Unset):
    """

    nodes: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerNode] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_cs_sys_adminutils_entityexplorer_entity_explorer_node import (
            ImplCsSysAdminutilsEntityexplorerEntityExplorerNode,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _nodes = d.pop("nodes", UNSET)
        nodes: list[ImplCsSysAdminutilsEntityexplorerEntityExplorerNode] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = ImplCsSysAdminutilsEntityexplorerEntityExplorerNode.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_model = cls(
            nodes=nodes,
        )

        impl_cs_sys_adminutils_entityexplorer_entity_explorer_model.additional_properties = d
        return impl_cs_sys_adminutils_entityexplorer_entity_explorer_model

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
