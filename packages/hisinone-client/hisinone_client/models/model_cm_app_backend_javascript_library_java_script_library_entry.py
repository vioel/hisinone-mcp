from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_error_message import CsSysRestErrorMessage
    from ..models.model_cm_app_backend_javascript_library_java_script_library_entry_foreigntext import (
        ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntryForeigntext,
    )


T = TypeVar("T", bound="ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry")


@_attrs_define
class ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntry:
    """
    Attributes:
        field_foreigntext (ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntryForeigntext | Unset):
        defaulttext (str | Unset):
        description (str | Unset):
        error_description (str | Unset):
        error_messages (list[CsSysRestErrorMessage] | Unset):
        id (int | Unset):
        java_script_expression (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntryForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    description: str | Unset = UNSET
    error_description: str | Unset = UNSET
    error_messages: list[CsSysRestErrorMessage] | Unset = UNSET
    id: int | Unset = UNSET
    java_script_expression: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        description = self.description

        error_description = self.error_description

        error_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.error_messages, Unset):
            error_messages = []
            for error_messages_item_data in self.error_messages:
                error_messages_item = error_messages_item_data.to_dict()
                error_messages.append(error_messages_item)

        id = self.id

        java_script_expression = self.java_script_expression

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if description is not UNSET:
            field_dict["description"] = description
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_messages is not UNSET:
            field_dict["errorMessages"] = error_messages
        if id is not UNSET:
            field_dict["id"] = id
        if java_script_expression is not UNSET:
            field_dict["javaScriptExpression"] = java_script_expression
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_error_message import CsSysRestErrorMessage  # noqa: PLC0415
        from ..models.model_cm_app_backend_javascript_library_java_script_library_entry_foreigntext import (
            ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntryForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntryForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ModelCmAppBackendJavascriptLibraryJavaScriptLibraryEntryForeigntext.from_dict(
                _field_foreigntext
            )

        defaulttext = d.pop("defaulttext", UNSET)

        description = d.pop("description", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_messages = d.pop("errorMessages", UNSET)
        error_messages: list[CsSysRestErrorMessage] | Unset = UNSET
        if _error_messages is not UNSET:
            error_messages = []
            for error_messages_item_data in _error_messages:
                error_messages_item = CsSysRestErrorMessage.from_dict(error_messages_item_data)

                error_messages.append(error_messages_item)

        id = d.pop("id", UNSET)

        java_script_expression = d.pop("javaScriptExpression", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        model_cm_app_backend_javascript_library_java_script_library_entry = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            description=description,
            error_description=error_description,
            error_messages=error_messages,
            id=id,
            java_script_expression=java_script_expression,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        model_cm_app_backend_javascript_library_java_script_library_entry.additional_properties = d
        return model_cm_app_backend_javascript_library_java_script_library_entry

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
