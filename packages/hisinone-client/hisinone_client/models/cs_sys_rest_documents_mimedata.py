from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_documents_mimedata_foreigntext import CsSysRestDocumentsMimedataForeigntext


T = TypeVar("T", bound="CsSysRestDocumentsMimedata")


@_attrs_define
class CsSysRestDocumentsMimedata:
    """
    Attributes:
        field_foreigntext (CsSysRestDocumentsMimedataForeigntext | Unset):
        created_at (int | Unset):
        description (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        mime_filename (str | Unset):
        mime_path (str | Unset):
        mime_type (str | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: CsSysRestDocumentsMimedataForeigntext | Unset = UNSET
    created_at: int | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    mime_filename: str | Unset = UNSET
    mime_path: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        created_at = self.created_at

        description = self.description

        id = self.id

        lock_version = self.lock_version

        mime_filename = self.mime_filename

        mime_path = self.mime_path

        mime_type = self.mime_type

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if mime_filename is not UNSET:
            field_dict["mimeFilename"] = mime_filename
        if mime_path is not UNSET:
            field_dict["mimePath"] = mime_path
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_documents_mimedata_foreigntext import CsSysRestDocumentsMimedataForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsSysRestDocumentsMimedataForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsSysRestDocumentsMimedataForeigntext.from_dict(_field_foreigntext)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        mime_filename = d.pop("mimeFilename", UNSET)

        mime_path = d.pop("mimePath", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        cs_sys_rest_documents_mimedata = cls(
            field_foreigntext=field_foreigntext,
            created_at=created_at,
            description=description,
            id=id,
            lock_version=lock_version,
            mime_filename=mime_filename,
            mime_path=mime_path,
            mime_type=mime_type,
            obj_guid=obj_guid,
        )

        cs_sys_rest_documents_mimedata.additional_properties = d
        return cs_sys_rest_documents_mimedata

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
