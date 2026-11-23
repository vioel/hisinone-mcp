from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_w3c_dom_document import OrgW3CDomDocument
    from ..models.org_w3c_dom_named_node_map import OrgW3CDomNamedNodeMap
    from ..models.org_w3c_dom_node import OrgW3CDomNode
    from ..models.org_w3c_dom_node_list import OrgW3CDomNodeList


T = TypeVar("T", bound="OrgW3CDomDocumentType")


@_attrs_define
class OrgW3CDomDocumentType:
    """
    Attributes:
        attributes (OrgW3CDomNamedNodeMap | Unset):
        base_uri (str | Unset):
        child_nodes (OrgW3CDomNodeList | Unset):
        entities (OrgW3CDomNamedNodeMap | Unset):
        first_child (OrgW3CDomNode | Unset):
        internal_subset (str | Unset):
        last_child (OrgW3CDomNode | Unset):
        local_name (str | Unset):
        name (str | Unset):
        namespace_uri (str | Unset):
        next_sibling (OrgW3CDomNode | Unset):
        node_name (str | Unset):
        node_type (int | Unset):
        node_value (str | Unset):
        notations (OrgW3CDomNamedNodeMap | Unset):
        owner_document (OrgW3CDomDocument | Unset):
        parent_node (OrgW3CDomNode | Unset):
        prefix (str | Unset):
        previous_sibling (OrgW3CDomNode | Unset):
        public_id (str | Unset):
        system_id (str | Unset):
        text_content (str | Unset):
    """

    attributes: OrgW3CDomNamedNodeMap | Unset = UNSET
    base_uri: str | Unset = UNSET
    child_nodes: OrgW3CDomNodeList | Unset = UNSET
    entities: OrgW3CDomNamedNodeMap | Unset = UNSET
    first_child: OrgW3CDomNode | Unset = UNSET
    internal_subset: str | Unset = UNSET
    last_child: OrgW3CDomNode | Unset = UNSET
    local_name: str | Unset = UNSET
    name: str | Unset = UNSET
    namespace_uri: str | Unset = UNSET
    next_sibling: OrgW3CDomNode | Unset = UNSET
    node_name: str | Unset = UNSET
    node_type: int | Unset = UNSET
    node_value: str | Unset = UNSET
    notations: OrgW3CDomNamedNodeMap | Unset = UNSET
    owner_document: OrgW3CDomDocument | Unset = UNSET
    parent_node: OrgW3CDomNode | Unset = UNSET
    prefix: str | Unset = UNSET
    previous_sibling: OrgW3CDomNode | Unset = UNSET
    public_id: str | Unset = UNSET
    system_id: str | Unset = UNSET
    text_content: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        base_uri = self.base_uri

        child_nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_nodes, Unset):
            child_nodes = self.child_nodes.to_dict()

        entities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        first_child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_child, Unset):
            first_child = self.first_child.to_dict()

        internal_subset = self.internal_subset

        last_child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_child, Unset):
            last_child = self.last_child.to_dict()

        local_name = self.local_name

        name = self.name

        namespace_uri = self.namespace_uri

        next_sibling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_sibling, Unset):
            next_sibling = self.next_sibling.to_dict()

        node_name = self.node_name

        node_type = self.node_type

        node_value = self.node_value

        notations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notations, Unset):
            notations = self.notations.to_dict()

        owner_document: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner_document, Unset):
            owner_document = self.owner_document.to_dict()

        parent_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_node, Unset):
            parent_node = self.parent_node.to_dict()

        prefix = self.prefix

        previous_sibling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_sibling, Unset):
            previous_sibling = self.previous_sibling.to_dict()

        public_id = self.public_id

        system_id = self.system_id

        text_content = self.text_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if base_uri is not UNSET:
            field_dict["baseURI"] = base_uri
        if child_nodes is not UNSET:
            field_dict["childNodes"] = child_nodes
        if entities is not UNSET:
            field_dict["entities"] = entities
        if first_child is not UNSET:
            field_dict["firstChild"] = first_child
        if internal_subset is not UNSET:
            field_dict["internalSubset"] = internal_subset
        if last_child is not UNSET:
            field_dict["lastChild"] = last_child
        if local_name is not UNSET:
            field_dict["localName"] = local_name
        if name is not UNSET:
            field_dict["name"] = name
        if namespace_uri is not UNSET:
            field_dict["namespaceURI"] = namespace_uri
        if next_sibling is not UNSET:
            field_dict["nextSibling"] = next_sibling
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if node_value is not UNSET:
            field_dict["nodeValue"] = node_value
        if notations is not UNSET:
            field_dict["notations"] = notations
        if owner_document is not UNSET:
            field_dict["ownerDocument"] = owner_document
        if parent_node is not UNSET:
            field_dict["parentNode"] = parent_node
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if previous_sibling is not UNSET:
            field_dict["previousSibling"] = previous_sibling
        if public_id is not UNSET:
            field_dict["publicId"] = public_id
        if system_id is not UNSET:
            field_dict["systemId"] = system_id
        if text_content is not UNSET:
            field_dict["textContent"] = text_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_w3c_dom_document import OrgW3CDomDocument  # noqa: PLC0415
        from ..models.org_w3c_dom_named_node_map import OrgW3CDomNamedNodeMap  # noqa: PLC0415
        from ..models.org_w3c_dom_node import OrgW3CDomNode  # noqa: PLC0415
        from ..models.org_w3c_dom_node_list import OrgW3CDomNodeList  # noqa: PLC0415

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: OrgW3CDomNamedNodeMap | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = OrgW3CDomNamedNodeMap.from_dict(_attributes)

        base_uri = d.pop("baseURI", UNSET)

        _child_nodes = d.pop("childNodes", UNSET)
        child_nodes: OrgW3CDomNodeList | Unset
        if isinstance(_child_nodes, Unset):
            child_nodes = UNSET
        else:
            child_nodes = OrgW3CDomNodeList.from_dict(_child_nodes)

        _entities = d.pop("entities", UNSET)
        entities: OrgW3CDomNamedNodeMap | Unset
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = OrgW3CDomNamedNodeMap.from_dict(_entities)

        _first_child = d.pop("firstChild", UNSET)
        first_child: OrgW3CDomNode | Unset
        if isinstance(_first_child, Unset):
            first_child = UNSET
        else:
            first_child = OrgW3CDomNode.from_dict(_first_child)

        internal_subset = d.pop("internalSubset", UNSET)

        _last_child = d.pop("lastChild", UNSET)
        last_child: OrgW3CDomNode | Unset
        if isinstance(_last_child, Unset):
            last_child = UNSET
        else:
            last_child = OrgW3CDomNode.from_dict(_last_child)

        local_name = d.pop("localName", UNSET)

        name = d.pop("name", UNSET)

        namespace_uri = d.pop("namespaceURI", UNSET)

        _next_sibling = d.pop("nextSibling", UNSET)
        next_sibling: OrgW3CDomNode | Unset
        if isinstance(_next_sibling, Unset):
            next_sibling = UNSET
        else:
            next_sibling = OrgW3CDomNode.from_dict(_next_sibling)

        node_name = d.pop("nodeName", UNSET)

        node_type = d.pop("nodeType", UNSET)

        node_value = d.pop("nodeValue", UNSET)

        _notations = d.pop("notations", UNSET)
        notations: OrgW3CDomNamedNodeMap | Unset
        if isinstance(_notations, Unset):
            notations = UNSET
        else:
            notations = OrgW3CDomNamedNodeMap.from_dict(_notations)

        _owner_document = d.pop("ownerDocument", UNSET)
        owner_document: OrgW3CDomDocument | Unset
        if isinstance(_owner_document, Unset):
            owner_document = UNSET
        else:
            owner_document = OrgW3CDomDocument.from_dict(_owner_document)

        _parent_node = d.pop("parentNode", UNSET)
        parent_node: OrgW3CDomNode | Unset
        if isinstance(_parent_node, Unset):
            parent_node = UNSET
        else:
            parent_node = OrgW3CDomNode.from_dict(_parent_node)

        prefix = d.pop("prefix", UNSET)

        _previous_sibling = d.pop("previousSibling", UNSET)
        previous_sibling: OrgW3CDomNode | Unset
        if isinstance(_previous_sibling, Unset):
            previous_sibling = UNSET
        else:
            previous_sibling = OrgW3CDomNode.from_dict(_previous_sibling)

        public_id = d.pop("publicId", UNSET)

        system_id = d.pop("systemId", UNSET)

        text_content = d.pop("textContent", UNSET)

        org_w3c_dom_document_type = cls(
            attributes=attributes,
            base_uri=base_uri,
            child_nodes=child_nodes,
            entities=entities,
            first_child=first_child,
            internal_subset=internal_subset,
            last_child=last_child,
            local_name=local_name,
            name=name,
            namespace_uri=namespace_uri,
            next_sibling=next_sibling,
            node_name=node_name,
            node_type=node_type,
            node_value=node_value,
            notations=notations,
            owner_document=owner_document,
            parent_node=parent_node,
            prefix=prefix,
            previous_sibling=previous_sibling,
            public_id=public_id,
            system_id=system_id,
            text_content=text_content,
        )

        org_w3c_dom_document_type.additional_properties = d
        return org_w3c_dom_document_type

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
