from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_publication_type_relation_foreigntext import (
        FsResPublicationPublicationTypeRelationForeigntext,
    )
    from ..models.fs_res_publication_publication_type_value import FsResPublicationPublicationTypeValue


T = TypeVar("T", bound="FsResPublicationPublicationTypeRelation")


@_attrs_define
class FsResPublicationPublicationTypeRelation:
    """
    Attributes:
        field_foreigntext (FsResPublicationPublicationTypeRelationForeigntext | Unset):
        child (FsResPublicationPublicationTypeValue | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        parent (FsResPublicationPublicationTypeValue | Unset):
    """

    field_foreigntext: FsResPublicationPublicationTypeRelationForeigntext | Unset = UNSET
    child: FsResPublicationPublicationTypeValue | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent: FsResPublicationPublicationTypeValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        child: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child, Unset):
            child = self.child.to_dict()

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if child is not UNSET:
            field_dict["child"] = child
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_publication_type_relation_foreigntext import (
            FsResPublicationPublicationTypeRelationForeigntext,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_publication_type_value import FsResPublicationPublicationTypeValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationPublicationTypeRelationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationPublicationTypeRelationForeigntext.from_dict(_field_foreigntext)

        _child = d.pop("child", UNSET)
        child: FsResPublicationPublicationTypeValue | Unset
        if isinstance(_child, Unset):
            child = UNSET
        else:
            child = FsResPublicationPublicationTypeValue.from_dict(_child)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: FsResPublicationPublicationTypeValue | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FsResPublicationPublicationTypeValue.from_dict(_parent)

        fs_res_publication_publication_type_relation = cls(
            field_foreigntext=field_foreigntext,
            child=child,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            parent=parent,
        )

        fs_res_publication_publication_type_relation.additional_properties = d
        return fs_res_publication_publication_type_relation

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
