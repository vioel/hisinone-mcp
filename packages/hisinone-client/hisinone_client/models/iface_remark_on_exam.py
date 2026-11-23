from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IfaceRemarkOnExam")


@_attrs_define
class IfaceRemarkOnExam:
    """
    Attributes:
        defaulttext (str | Unset):
        id (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        uniquename (str | Unset):
    """

    defaulttext: str | Unset = UNSET
    id: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defaulttext = self.defaulttext

        id = self.id

        longtext = self.longtext

        obj_guid = self.obj_guid

        shorttext = self.shorttext

        sortorder = self.sortorder

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if id is not UNSET:
            field_dict["id"] = id
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        defaulttext = d.pop("defaulttext", UNSET)

        id = d.pop("id", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        iface_remark_on_exam = cls(
            defaulttext=defaulttext,
            id=id,
            longtext=longtext,
            obj_guid=obj_guid,
            shorttext=shorttext,
            sortorder=sortorder,
            uniquename=uniquename,
        )

        iface_remark_on_exam.additional_properties = d
        return iface_remark_on_exam

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
