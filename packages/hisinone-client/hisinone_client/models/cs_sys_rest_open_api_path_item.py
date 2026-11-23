from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_open_api_operation import CsSysRestOpenApiOperation


T = TypeVar("T", bound="CsSysRestOpenApiPathItem")


@_attrs_define
class CsSysRestOpenApiPathItem:
    """
    Attributes:
        delete (CsSysRestOpenApiOperation | Unset):
        get (CsSysRestOpenApiOperation | Unset):
        post (CsSysRestOpenApiOperation | Unset):
        put (CsSysRestOpenApiOperation | Unset):
    """

    delete: CsSysRestOpenApiOperation | Unset = UNSET
    get: CsSysRestOpenApiOperation | Unset = UNSET
    post: CsSysRestOpenApiOperation | Unset = UNSET
    put: CsSysRestOpenApiOperation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        delete: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        get: dict[str, Any] | Unset = UNSET
        if not isinstance(self.get, Unset):
            get = self.get.to_dict()

        post: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        put: dict[str, Any] | Unset = UNSET
        if not isinstance(self.put, Unset):
            put = self.put.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete is not UNSET:
            field_dict["delete"] = delete
        if get is not UNSET:
            field_dict["get"] = get
        if post is not UNSET:
            field_dict["post"] = post
        if put is not UNSET:
            field_dict["put"] = put

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_open_api_operation import CsSysRestOpenApiOperation  # noqa: PLC0415

        d = dict(src_dict)
        _delete = d.pop("delete", UNSET)
        delete: CsSysRestOpenApiOperation | Unset
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = CsSysRestOpenApiOperation.from_dict(_delete)

        _get = d.pop("get", UNSET)
        get: CsSysRestOpenApiOperation | Unset
        if isinstance(_get, Unset):
            get = UNSET
        else:
            get = CsSysRestOpenApiOperation.from_dict(_get)

        _post = d.pop("post", UNSET)
        post: CsSysRestOpenApiOperation | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = CsSysRestOpenApiOperation.from_dict(_post)

        _put = d.pop("put", UNSET)
        put: CsSysRestOpenApiOperation | Unset
        if isinstance(_put, Unset):
            put = UNSET
        else:
            put = CsSysRestOpenApiOperation.from_dict(_put)

        cs_sys_rest_open_api_path_item = cls(
            delete=delete,
            get=get,
            post=post,
            put=put,
        )

        cs_sys_rest_open_api_path_item.additional_properties = d
        return cs_sys_rest_open_api_path_item

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
