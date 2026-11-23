from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_open_api_response_content import CsSysRestOpenApiResponseContent


T = TypeVar("T", bound="CsSysRestOpenApiResponse")


@_attrs_define
class CsSysRestOpenApiResponse:
    """
    Attributes:
        content (CsSysRestOpenApiResponseContent | Unset):
        description (str | Unset):
    """

    content: CsSysRestOpenApiResponseContent | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_open_api_response_content import CsSysRestOpenApiResponseContent  # noqa: PLC0415

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: CsSysRestOpenApiResponseContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = CsSysRestOpenApiResponseContent.from_dict(_content)

        description = d.pop("description", UNSET)

        cs_sys_rest_open_api_response = cls(
            content=content,
            description=description,
        )

        cs_sys_rest_open_api_response.additional_properties = d
        return cs_sys_rest_open_api_response

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
