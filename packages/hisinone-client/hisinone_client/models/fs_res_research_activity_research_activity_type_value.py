from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_research_activity_research_activity_type_value_foreigntext import (
        FsResResearchActivityResearchActivityTypeValueForeigntext,
    )


T = TypeVar("T", bound="FsResResearchActivityResearchActivityTypeValue")


@_attrs_define
class FsResResearchActivityResearchActivityTypeValue:
    """
    Attributes:
        field_foreigntext (FsResResearchActivityResearchActivityTypeValueForeigntext | Unset):
        defaulttext (str | Unset):
        hiskey_id (int | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        parent (FsResResearchActivityResearchActivityTypeValue | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
    """

    field_foreigntext: FsResResearchActivityResearchActivityTypeValueForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    parent: FsResResearchActivityResearchActivityTypeValue | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        hiskey_id = self.hiskey_id

        id = self.id

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent is not UNSET:
            field_dict["parent"] = parent
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_research_activity_research_activity_type_value_foreigntext import (
            FsResResearchActivityResearchActivityTypeValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResResearchActivityResearchActivityTypeValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResResearchActivityResearchActivityTypeValueForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: FsResResearchActivityResearchActivityTypeValue | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FsResResearchActivityResearchActivityTypeValue.from_dict(_parent)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        fs_res_research_activity_research_activity_type_value = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            hiskey_id=hiskey_id,
            id=id,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            parent=parent,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
        )

        fs_res_research_activity_research_activity_type_value.additional_properties = d
        return fs_res_research_activity_research_activity_type_value

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
