from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_generic_error_message import CsSysRestGenericErrorMessage


T = TypeVar("T", bound="CsSysRestGenericExceptionResponse")


@_attrs_define
class CsSysRestGenericExceptionResponse:
    """
    Example:
        {'description': 'Validation exception.', 'messages': [{'field': 'fs.res.publication.Publication.title',
            'message': 'Titel: Eingabe erforderlich.'}, {'field': 'fs.res.publication.Publication.releaseYear', 'message':
            "Publikationsjahr: Der eingegebene Wert ist kleiner als das erlaubte Minimum '1450'."}], 'source': '/api'}

    Attributes:
        description (str | Unset):
        messages (list[CsSysRestGenericErrorMessage] | Unset):
        source (str | Unset):
    """

    description: str | Unset = UNSET
    messages: list[CsSysRestGenericErrorMessage] | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if messages is not UNSET:
            field_dict["messages"] = messages
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_generic_error_message import CsSysRestGenericErrorMessage  # noqa: PLC0415

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: list[CsSysRestGenericErrorMessage] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = CsSysRestGenericErrorMessage.from_dict(messages_item_data)

                messages.append(messages_item)

        source = d.pop("source", UNSET)

        cs_sys_rest_generic_exception_response = cls(
            description=description,
            messages=messages,
            source=source,
        )

        cs_sys_rest_generic_exception_response.additional_properties = d
        return cs_sys_rest_generic_exception_response

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
