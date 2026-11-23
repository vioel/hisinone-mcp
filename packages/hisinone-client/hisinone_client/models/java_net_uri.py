from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaNetURI")


@_attrs_define
class JavaNetURI:
    """
    Attributes:
        absolute (bool | Unset):
        authority (str | Unset):
        fragment (str | Unset):
        host (str | Unset):
        opaque (bool | Unset):
        path (str | Unset):
        port (int | Unset):
        query (str | Unset):
        raw_authority (str | Unset):
        raw_fragment (str | Unset):
        raw_path (str | Unset):
        raw_query (str | Unset):
        raw_scheme_specific_part (str | Unset):
        raw_user_info (str | Unset):
        scheme (str | Unset):
        scheme_specific_part (str | Unset):
        user_info (str | Unset):
    """

    absolute: bool | Unset = UNSET
    authority: str | Unset = UNSET
    fragment: str | Unset = UNSET
    host: str | Unset = UNSET
    opaque: bool | Unset = UNSET
    path: str | Unset = UNSET
    port: int | Unset = UNSET
    query: str | Unset = UNSET
    raw_authority: str | Unset = UNSET
    raw_fragment: str | Unset = UNSET
    raw_path: str | Unset = UNSET
    raw_query: str | Unset = UNSET
    raw_scheme_specific_part: str | Unset = UNSET
    raw_user_info: str | Unset = UNSET
    scheme: str | Unset = UNSET
    scheme_specific_part: str | Unset = UNSET
    user_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        absolute = self.absolute

        authority = self.authority

        fragment = self.fragment

        host = self.host

        opaque = self.opaque

        path = self.path

        port = self.port

        query = self.query

        raw_authority = self.raw_authority

        raw_fragment = self.raw_fragment

        raw_path = self.raw_path

        raw_query = self.raw_query

        raw_scheme_specific_part = self.raw_scheme_specific_part

        raw_user_info = self.raw_user_info

        scheme = self.scheme

        scheme_specific_part = self.scheme_specific_part

        user_info = self.user_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if absolute is not UNSET:
            field_dict["absolute"] = absolute
        if authority is not UNSET:
            field_dict["authority"] = authority
        if fragment is not UNSET:
            field_dict["fragment"] = fragment
        if host is not UNSET:
            field_dict["host"] = host
        if opaque is not UNSET:
            field_dict["opaque"] = opaque
        if path is not UNSET:
            field_dict["path"] = path
        if port is not UNSET:
            field_dict["port"] = port
        if query is not UNSET:
            field_dict["query"] = query
        if raw_authority is not UNSET:
            field_dict["rawAuthority"] = raw_authority
        if raw_fragment is not UNSET:
            field_dict["rawFragment"] = raw_fragment
        if raw_path is not UNSET:
            field_dict["rawPath"] = raw_path
        if raw_query is not UNSET:
            field_dict["rawQuery"] = raw_query
        if raw_scheme_specific_part is not UNSET:
            field_dict["rawSchemeSpecificPart"] = raw_scheme_specific_part
        if raw_user_info is not UNSET:
            field_dict["rawUserInfo"] = raw_user_info
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if scheme_specific_part is not UNSET:
            field_dict["schemeSpecificPart"] = scheme_specific_part
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        absolute = d.pop("absolute", UNSET)

        authority = d.pop("authority", UNSET)

        fragment = d.pop("fragment", UNSET)

        host = d.pop("host", UNSET)

        opaque = d.pop("opaque", UNSET)

        path = d.pop("path", UNSET)

        port = d.pop("port", UNSET)

        query = d.pop("query", UNSET)

        raw_authority = d.pop("rawAuthority", UNSET)

        raw_fragment = d.pop("rawFragment", UNSET)

        raw_path = d.pop("rawPath", UNSET)

        raw_query = d.pop("rawQuery", UNSET)

        raw_scheme_specific_part = d.pop("rawSchemeSpecificPart", UNSET)

        raw_user_info = d.pop("rawUserInfo", UNSET)

        scheme = d.pop("scheme", UNSET)

        scheme_specific_part = d.pop("schemeSpecificPart", UNSET)

        user_info = d.pop("userInfo", UNSET)

        java_net_uri = cls(
            absolute=absolute,
            authority=authority,
            fragment=fragment,
            host=host,
            opaque=opaque,
            path=path,
            port=port,
            query=query,
            raw_authority=raw_authority,
            raw_fragment=raw_fragment,
            raw_path=raw_path,
            raw_query=raw_query,
            raw_scheme_specific_part=raw_scheme_specific_part,
            raw_user_info=raw_user_info,
            scheme=scheme,
            scheme_specific_part=scheme_specific_part,
            user_info=user_info,
        )

        java_net_uri.additional_properties = d
        return java_net_uri

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
