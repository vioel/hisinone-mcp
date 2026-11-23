from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_change_request_change_request_changed_value_foreigntext import (
        FsResPublicationChangeRequestChangeRequestChangedValueForeigntext,
    )


T = TypeVar("T", bound="FsResPublicationChangeRequestChangeRequestChangedValue")


@_attrs_define
class FsResPublicationChangeRequestChangeRequestChangedValue:
    """
    Attributes:
        field_foreigntext (FsResPublicationChangeRequestChangeRequestChangedValueForeigntext | Unset):
        attribute_identificator (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        old_value (str | Unset):
        val (str | Unset):
    """

    field_foreigntext: FsResPublicationChangeRequestChangeRequestChangedValueForeigntext | Unset = UNSET
    attribute_identificator: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    old_value: str | Unset = UNSET
    val: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        attribute_identificator = self.attribute_identificator

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        old_value = self.old_value

        val = self.val

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if attribute_identificator is not UNSET:
            field_dict["attributeIdentificator"] = attribute_identificator
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if old_value is not UNSET:
            field_dict["oldValue"] = old_value
        if val is not UNSET:
            field_dict["val"] = val

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_change_request_change_request_changed_value_foreigntext import (
            FsResPublicationChangeRequestChangeRequestChangedValueForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationChangeRequestChangeRequestChangedValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationChangeRequestChangeRequestChangedValueForeigntext.from_dict(
                _field_foreigntext
            )

        attribute_identificator = d.pop("attributeIdentificator", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        old_value = d.pop("oldValue", UNSET)

        val = d.pop("val", UNSET)

        fs_res_publication_change_request_change_request_changed_value = cls(
            field_foreigntext=field_foreigntext,
            attribute_identificator=attribute_identificator,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            old_value=old_value,
            val=val,
        )

        fs_res_publication_change_request_change_request_changed_value.additional_properties = d
        return fs_res_publication_change_request_change_request_changed_value

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
