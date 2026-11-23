from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_request_request_base_declaration_foreigntext import (
        FsResRequestRequestBaseDeclarationForeigntext,
    )


T = TypeVar("T", bound="FsResRequestRequestBaseDeclaration")


@_attrs_define
class FsResRequestRequestBaseDeclaration:
    """
    Attributes:
        field_foreigntext (FsResRequestRequestBaseDeclarationForeigntext | Unset):
        checkbox_value (CsSysValueGenericValue | Unset):
        declaration_definiton (CsSysValueGenericValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        textfield_value (str | Unset):
    """

    field_foreigntext: FsResRequestRequestBaseDeclarationForeigntext | Unset = UNSET
    checkbox_value: CsSysValueGenericValue | Unset = UNSET
    declaration_definiton: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    textfield_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        checkbox_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checkbox_value, Unset):
            checkbox_value = self.checkbox_value.to_dict()

        declaration_definiton: dict[str, Any] | Unset = UNSET
        if not isinstance(self.declaration_definiton, Unset):
            declaration_definiton = self.declaration_definiton.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        textfield_value = self.textfield_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if checkbox_value is not UNSET:
            field_dict["checkboxValue"] = checkbox_value
        if declaration_definiton is not UNSET:
            field_dict["declarationDefiniton"] = declaration_definiton
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if textfield_value is not UNSET:
            field_dict["textfieldValue"] = textfield_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_request_request_base_declaration_foreigntext import (
            FsResRequestRequestBaseDeclarationForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResRequestRequestBaseDeclarationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResRequestRequestBaseDeclarationForeigntext.from_dict(_field_foreigntext)

        _checkbox_value = d.pop("checkboxValue", UNSET)
        checkbox_value: CsSysValueGenericValue | Unset
        if isinstance(_checkbox_value, Unset):
            checkbox_value = UNSET
        else:
            checkbox_value = CsSysValueGenericValue.from_dict(_checkbox_value)

        _declaration_definiton = d.pop("declarationDefiniton", UNSET)
        declaration_definiton: CsSysValueGenericValue | Unset
        if isinstance(_declaration_definiton, Unset):
            declaration_definiton = UNSET
        else:
            declaration_definiton = CsSysValueGenericValue.from_dict(_declaration_definiton)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        textfield_value = d.pop("textfieldValue", UNSET)

        fs_res_request_request_base_declaration = cls(
            field_foreigntext=field_foreigntext,
            checkbox_value=checkbox_value,
            declaration_definiton=declaration_definiton,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            textfield_value=textfield_value,
        )

        fs_res_request_request_base_declaration.additional_properties = d
        return fs_res_request_request_base_declaration

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
