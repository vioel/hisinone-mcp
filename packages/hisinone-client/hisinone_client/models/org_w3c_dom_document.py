from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_w3c_dom_document_type import OrgW3CDomDocumentType
    from ..models.org_w3c_dom_dom_configuration import OrgW3CDomDOMConfiguration
    from ..models.org_w3c_dom_dom_implementation import OrgW3CDomDOMImplementation
    from ..models.org_w3c_dom_element import OrgW3CDomElement
    from ..models.org_w3c_dom_named_node_map import OrgW3CDomNamedNodeMap
    from ..models.org_w3c_dom_node import OrgW3CDomNode
    from ..models.org_w3c_dom_node_list import OrgW3CDomNodeList


T = TypeVar("T", bound="OrgW3CDomDocument")


@_attrs_define
class OrgW3CDomDocument:
    """
    Attributes:
        attributes (OrgW3CDomNamedNodeMap | Unset):
        base_uri (str | Unset):
        child_nodes (OrgW3CDomNodeList | Unset):
        doctype (OrgW3CDomDocumentType | Unset):
        document_element (OrgW3CDomElement | Unset):
        document_uri (str | Unset):
        dom_config (OrgW3CDomDOMConfiguration | Unset):
        first_child (OrgW3CDomNode | Unset):
        implementation (OrgW3CDomDOMImplementation | Unset):
        input_encoding (str | Unset):
        last_child (OrgW3CDomNode | Unset):
        local_name (str | Unset):
        namespace_uri (str | Unset):
        next_sibling (OrgW3CDomNode | Unset):
        node_name (str | Unset):
        node_type (int | Unset):
        node_value (str | Unset):
        owner_document (OrgW3CDomDocument | Unset):
        parent_node (OrgW3CDomNode | Unset):
        prefix (str | Unset):
        previous_sibling (OrgW3CDomNode | Unset):
        strict_error_checking (bool | Unset):
        text_content (str | Unset):
        xml_encoding (str | Unset):
        xml_standalone (bool | Unset):
        xml_version (str | Unset):
    """

    attributes: OrgW3CDomNamedNodeMap | Unset = UNSET
    base_uri: str | Unset = UNSET
    child_nodes: OrgW3CDomNodeList | Unset = UNSET
    doctype: OrgW3CDomDocumentType | Unset = UNSET
    document_element: OrgW3CDomElement | Unset = UNSET
    document_uri: str | Unset = UNSET
    dom_config: OrgW3CDomDOMConfiguration | Unset = UNSET
    first_child: OrgW3CDomNode | Unset = UNSET
    implementation: OrgW3CDomDOMImplementation | Unset = UNSET
    input_encoding: str | Unset = UNSET
    last_child: OrgW3CDomNode | Unset = UNSET
    local_name: str | Unset = UNSET
    namespace_uri: str | Unset = UNSET
    next_sibling: OrgW3CDomNode | Unset = UNSET
    node_name: str | Unset = UNSET
    node_type: int | Unset = UNSET
    node_value: str | Unset = UNSET
    owner_document: OrgW3CDomDocument | Unset = UNSET
    parent_node: OrgW3CDomNode | Unset = UNSET
    prefix: str | Unset = UNSET
    previous_sibling: OrgW3CDomNode | Unset = UNSET
    strict_error_checking: bool | Unset = UNSET
    text_content: str | Unset = UNSET
    xml_encoding: str | Unset = UNSET
    xml_standalone: bool | Unset = UNSET
    xml_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        base_uri = self.base_uri

        child_nodes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_nodes, Unset):
            child_nodes = self.child_nodes.to_dict()

        doctype: dict[str, Any] | Unset = UNSET
        if not isinstance(self.doctype, Unset):
            doctype = self.doctype.to_dict()

        document_element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.document_element, Unset):
            document_element = self.document_element.to_dict()

        document_uri = self.document_uri

        dom_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dom_config, Unset):
            dom_config = self.dom_config.to_dict()

        first_child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_child, Unset):
            first_child = self.first_child.to_dict()

        implementation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.implementation, Unset):
            implementation = self.implementation.to_dict()

        input_encoding = self.input_encoding

        last_child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_child, Unset):
            last_child = self.last_child.to_dict()

        local_name = self.local_name

        namespace_uri = self.namespace_uri

        next_sibling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_sibling, Unset):
            next_sibling = self.next_sibling.to_dict()

        node_name = self.node_name

        node_type = self.node_type

        node_value = self.node_value

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

        strict_error_checking = self.strict_error_checking

        text_content = self.text_content

        xml_encoding = self.xml_encoding

        xml_standalone = self.xml_standalone

        xml_version = self.xml_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if base_uri is not UNSET:
            field_dict["baseURI"] = base_uri
        if child_nodes is not UNSET:
            field_dict["childNodes"] = child_nodes
        if doctype is not UNSET:
            field_dict["doctype"] = doctype
        if document_element is not UNSET:
            field_dict["documentElement"] = document_element
        if document_uri is not UNSET:
            field_dict["documentURI"] = document_uri
        if dom_config is not UNSET:
            field_dict["domConfig"] = dom_config
        if first_child is not UNSET:
            field_dict["firstChild"] = first_child
        if implementation is not UNSET:
            field_dict["implementation"] = implementation
        if input_encoding is not UNSET:
            field_dict["inputEncoding"] = input_encoding
        if last_child is not UNSET:
            field_dict["lastChild"] = last_child
        if local_name is not UNSET:
            field_dict["localName"] = local_name
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
        if owner_document is not UNSET:
            field_dict["ownerDocument"] = owner_document
        if parent_node is not UNSET:
            field_dict["parentNode"] = parent_node
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if previous_sibling is not UNSET:
            field_dict["previousSibling"] = previous_sibling
        if strict_error_checking is not UNSET:
            field_dict["strictErrorChecking"] = strict_error_checking
        if text_content is not UNSET:
            field_dict["textContent"] = text_content
        if xml_encoding is not UNSET:
            field_dict["xmlEncoding"] = xml_encoding
        if xml_standalone is not UNSET:
            field_dict["xmlStandalone"] = xml_standalone
        if xml_version is not UNSET:
            field_dict["xmlVersion"] = xml_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_w3c_dom_document_type import OrgW3CDomDocumentType  # noqa: PLC0415
        from ..models.org_w3c_dom_dom_configuration import OrgW3CDomDOMConfiguration  # noqa: PLC0415
        from ..models.org_w3c_dom_dom_implementation import OrgW3CDomDOMImplementation  # noqa: PLC0415
        from ..models.org_w3c_dom_element import OrgW3CDomElement  # noqa: PLC0415
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

        _doctype = d.pop("doctype", UNSET)
        doctype: OrgW3CDomDocumentType | Unset
        if isinstance(_doctype, Unset):
            doctype = UNSET
        else:
            doctype = OrgW3CDomDocumentType.from_dict(_doctype)

        _document_element = d.pop("documentElement", UNSET)
        document_element: OrgW3CDomElement | Unset
        if isinstance(_document_element, Unset):
            document_element = UNSET
        else:
            document_element = OrgW3CDomElement.from_dict(_document_element)

        document_uri = d.pop("documentURI", UNSET)

        _dom_config = d.pop("domConfig", UNSET)
        dom_config: OrgW3CDomDOMConfiguration | Unset
        if isinstance(_dom_config, Unset):
            dom_config = UNSET
        else:
            dom_config = OrgW3CDomDOMConfiguration.from_dict(_dom_config)

        _first_child = d.pop("firstChild", UNSET)
        first_child: OrgW3CDomNode | Unset
        if isinstance(_first_child, Unset):
            first_child = UNSET
        else:
            first_child = OrgW3CDomNode.from_dict(_first_child)

        _implementation = d.pop("implementation", UNSET)
        implementation: OrgW3CDomDOMImplementation | Unset
        if isinstance(_implementation, Unset):
            implementation = UNSET
        else:
            implementation = OrgW3CDomDOMImplementation.from_dict(_implementation)

        input_encoding = d.pop("inputEncoding", UNSET)

        _last_child = d.pop("lastChild", UNSET)
        last_child: OrgW3CDomNode | Unset
        if isinstance(_last_child, Unset):
            last_child = UNSET
        else:
            last_child = OrgW3CDomNode.from_dict(_last_child)

        local_name = d.pop("localName", UNSET)

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

        strict_error_checking = d.pop("strictErrorChecking", UNSET)

        text_content = d.pop("textContent", UNSET)

        xml_encoding = d.pop("xmlEncoding", UNSET)

        xml_standalone = d.pop("xmlStandalone", UNSET)

        xml_version = d.pop("xmlVersion", UNSET)

        org_w3c_dom_document = cls(
            attributes=attributes,
            base_uri=base_uri,
            child_nodes=child_nodes,
            doctype=doctype,
            document_element=document_element,
            document_uri=document_uri,
            dom_config=dom_config,
            first_child=first_child,
            implementation=implementation,
            input_encoding=input_encoding,
            last_child=last_child,
            local_name=local_name,
            namespace_uri=namespace_uri,
            next_sibling=next_sibling,
            node_name=node_name,
            node_type=node_type,
            node_value=node_value,
            owner_document=owner_document,
            parent_node=parent_node,
            prefix=prefix,
            previous_sibling=previous_sibling,
            strict_error_checking=strict_error_checking,
            text_content=text_content,
            xml_encoding=xml_encoding,
            xml_standalone=xml_standalone,
            xml_version=xml_version,
        )

        org_w3c_dom_document.additional_properties = d
        return org_w3c_dom_document

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
