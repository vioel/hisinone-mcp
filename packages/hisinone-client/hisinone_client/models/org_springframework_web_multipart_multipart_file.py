from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_springframework_core_io_resource import OrgSpringframeworkCoreIoResource


T = TypeVar("T", bound="OrgSpringframeworkWebMultipartMultipartFile")


@_attrs_define
class OrgSpringframeworkWebMultipartMultipartFile:
    """
    Attributes:
        bytes_ (list[int] | Unset):
        content_type (str | Unset):
        empty (bool | Unset):
        name (str | Unset):
        original_filename (str | Unset):
        resource (OrgSpringframeworkCoreIoResource | Unset):
        size (int | Unset):
    """

    bytes_: list[int] | Unset = UNSET
    content_type: str | Unset = UNSET
    empty: bool | Unset = UNSET
    name: str | Unset = UNSET
    original_filename: str | Unset = UNSET
    resource: OrgSpringframeworkCoreIoResource | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        bytes_: list[int] | Unset = UNSET
        if not isinstance(self.bytes_, Unset):
            bytes_ = self.bytes_

        content_type = self.content_type

        empty = self.empty

        name = self.name

        original_filename = self.original_filename

        resource: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource, Unset):
            resource = self.resource.to_dict()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if empty is not UNSET:
            field_dict["empty"] = empty
        if name is not UNSET:
            field_dict["name"] = name
        if original_filename is not UNSET:
            field_dict["originalFilename"] = original_filename
        if resource is not UNSET:
            field_dict["resource"] = resource
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_springframework_core_io_resource import OrgSpringframeworkCoreIoResource  # noqa: PLC0415

        d = dict(src_dict)
        bytes_ = cast(list[int], d.pop("bytes", UNSET))

        content_type = d.pop("contentType", UNSET)

        empty = d.pop("empty", UNSET)

        name = d.pop("name", UNSET)

        original_filename = d.pop("originalFilename", UNSET)

        _resource = d.pop("resource", UNSET)
        resource: OrgSpringframeworkCoreIoResource | Unset
        if isinstance(_resource, Unset):
            resource = UNSET
        else:
            resource = OrgSpringframeworkCoreIoResource.from_dict(_resource)

        size = d.pop("size", UNSET)

        org_springframework_web_multipart_multipart_file = cls(
            bytes_=bytes_,
            content_type=content_type,
            empty=empty,
            name=name,
            original_filename=original_filename,
            resource=resource,
            size=size,
        )

        org_springframework_web_multipart_multipart_file.additional_properties = d
        return org_springframework_web_multipart_multipart_file

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
