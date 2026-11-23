from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_publication_global_identifier_foreigntext_type_0 import (
        FsResPublicationGlobalIdentifierForeigntextType0,
    )


T = TypeVar("T", bound="FsResPublicationGlobalIdentifier")


@_attrs_define
class FsResPublicationGlobalIdentifier:
    """
    Attributes:
        field_foreigntext (FsResPublicationGlobalIdentifierForeigntextType0 | None | Unset):
        global_identifier_type (CsSysValueGenericValue | Unset):
        id (int | Unset):
        identifier (str | Unset):
        lock_version (int | Unset):
        obj_guid (None | str | Unset):
        tablename (str | Unset):
        tabpk (int | Unset):
    """

    field_foreigntext: FsResPublicationGlobalIdentifierForeigntextType0 | None | Unset = UNSET
    global_identifier_type: CsSysValueGenericValue | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    tablename: str | Unset = UNSET
    tabpk: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_res_publication_global_identifier_foreigntext_type_0 import (
            FsResPublicationGlobalIdentifierForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResPublicationGlobalIdentifierForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        global_identifier_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_identifier_type, Unset):
            global_identifier_type = self.global_identifier_type.to_dict()

        id = self.id

        identifier = self.identifier

        lock_version = self.lock_version

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        tablename = self.tablename

        tabpk = self.tabpk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if global_identifier_type is not UNSET:
            field_dict["globalIdentifierType"] = global_identifier_type
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if tablename is not UNSET:
            field_dict["tablename"] = tablename
        if tabpk is not UNSET:
            field_dict["tabpk"] = tabpk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_global_identifier_foreigntext_type_0 import (
            FsResPublicationGlobalIdentifierForeigntextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_field_foreigntext(data: object) -> FsResPublicationGlobalIdentifierForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResPublicationGlobalIdentifierForeigntextType0.from_dict(
                cast(dict[str, Any], data)
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        _global_identifier_type = d.pop("globalIdentifierType", UNSET)
        global_identifier_type: CsSysValueGenericValue | Unset
        if isinstance(_global_identifier_type, Unset):
            global_identifier_type = UNSET
        else:
            global_identifier_type = CsSysValueGenericValue.from_dict(_global_identifier_type)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        tablename = d.pop("tablename", UNSET)

        tabpk = d.pop("tabpk", UNSET)

        fs_res_publication_global_identifier = cls(
            field_foreigntext=field_foreigntext,
            global_identifier_type=global_identifier_type,
            id=id,
            identifier=identifier,
            lock_version=lock_version,
            obj_guid=obj_guid,
            tablename=tablename,
            tabpk=tabpk,
        )

        fs_res_publication_global_identifier.additional_properties = d
        return fs_res_publication_global_identifier

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
