from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_open_api_components import CsSysRestOpenApiComponents
    from ..models.cs_sys_rest_open_api_info import CsSysRestOpenApiInfo
    from ..models.cs_sys_rest_open_api_paths import CsSysRestOpenApiPaths
    from ..models.cs_sys_rest_open_api_server import CsSysRestOpenApiServer
    from ..models.cs_sys_rest_open_api_tags_item import CsSysRestOpenApiTagsItem


T = TypeVar("T", bound="CsSysRestOpenApi")


@_attrs_define
class CsSysRestOpenApi:
    """
    Attributes:
        components (CsSysRestOpenApiComponents | Unset):
        info (CsSysRestOpenApiInfo | Unset):
        openapi (str | Unset):
        paths (CsSysRestOpenApiPaths | Unset):
        servers (list[CsSysRestOpenApiServer] | Unset):
        tags (list[CsSysRestOpenApiTagsItem] | Unset):
    """

    components: CsSysRestOpenApiComponents | Unset = UNSET
    info: CsSysRestOpenApiInfo | Unset = UNSET
    openapi: str | Unset = UNSET
    paths: CsSysRestOpenApiPaths | Unset = UNSET
    servers: list[CsSysRestOpenApiServer] | Unset = UNSET
    tags: list[CsSysRestOpenApiTagsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        openapi = self.openapi

        paths: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths.to_dict()

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if info is not UNSET:
            field_dict["info"] = info
        if openapi is not UNSET:
            field_dict["openapi"] = openapi
        if paths is not UNSET:
            field_dict["paths"] = paths
        if servers is not UNSET:
            field_dict["servers"] = servers
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_open_api_components import CsSysRestOpenApiComponents  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_info import CsSysRestOpenApiInfo  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_paths import CsSysRestOpenApiPaths  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_server import CsSysRestOpenApiServer  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_tags_item import CsSysRestOpenApiTagsItem  # noqa: PLC0415

        d = dict(src_dict)
        _components = d.pop("components", UNSET)
        components: CsSysRestOpenApiComponents | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = CsSysRestOpenApiComponents.from_dict(_components)

        _info = d.pop("info", UNSET)
        info: CsSysRestOpenApiInfo | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = CsSysRestOpenApiInfo.from_dict(_info)

        openapi = d.pop("openapi", UNSET)

        _paths = d.pop("paths", UNSET)
        paths: CsSysRestOpenApiPaths | Unset
        if isinstance(_paths, Unset):
            paths = UNSET
        else:
            paths = CsSysRestOpenApiPaths.from_dict(_paths)

        _servers = d.pop("servers", UNSET)
        servers: list[CsSysRestOpenApiServer] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = CsSysRestOpenApiServer.from_dict(servers_item_data)

                servers.append(servers_item)

        _tags = d.pop("tags", UNSET)
        tags: list[CsSysRestOpenApiTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = CsSysRestOpenApiTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        cs_sys_rest_open_api = cls(
            components=components,
            info=info,
            openapi=openapi,
            paths=paths,
            servers=servers,
            tags=tags,
        )

        cs_sys_rest_open_api.additional_properties = d
        return cs_sys_rest_open_api

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
