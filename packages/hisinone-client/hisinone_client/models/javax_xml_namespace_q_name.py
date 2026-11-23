from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaxXmlNamespaceQName")


@_attrs_define
class JavaxXmlNamespaceQName:
    """
    Attributes:
        local_part (str | Unset):
        namespace_uri (str | Unset):
        prefix (str | Unset):
    """

    local_part: str | Unset = UNSET
    namespace_uri: str | Unset = UNSET
    prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        local_part = self.local_part

        namespace_uri = self.namespace_uri

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if local_part is not UNSET:
            field_dict["localPart"] = local_part
        if namespace_uri is not UNSET:
            field_dict["namespaceURI"] = namespace_uri
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        local_part = d.pop("localPart", UNSET)

        namespace_uri = d.pop("namespaceURI", UNSET)

        prefix = d.pop("prefix", UNSET)

        javax_xml_namespace_q_name = cls(
            local_part=local_part,
            namespace_uri=namespace_uri,
            prefix=prefix,
        )

        javax_xml_namespace_q_name.additional_properties = d
        return javax_xml_namespace_q_name

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
