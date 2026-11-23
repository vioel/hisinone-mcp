from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_change_request_change_request_changed_value import (
        FsResPublicationChangeRequestChangeRequestChangedValue,
    )
    from ..models.fs_res_publication_change_request_publication_change_request_foreigntext import (
        FsResPublicationChangeRequestPublicationChangeRequestForeigntext,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent


T = TypeVar("T", bound="FsResPublicationChangeRequestPublicationChangeRequest")


@_attrs_define
class FsResPublicationChangeRequestPublicationChangeRequest:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResPublicationChangeRequestPublicationChangeRequestForeigntext | Unset):
        changed_values (list[FsResPublicationChangeRequestChangeRequestChangedValue] | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResPublicationChangeRequestPublicationChangeRequestForeigntext | Unset = UNSET
    changed_values: list[FsResPublicationChangeRequestChangeRequestChangedValue] | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        changed_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changed_values, Unset):
            changed_values = []
            for changed_values_item_data in self.changed_values:
                changed_values_item = changed_values_item_data.to_dict()
                changed_values.append(changed_values_item)

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if changed_values is not UNSET:
            field_dict["changedValues"] = changed_values
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_change_request_change_request_changed_value import (
            FsResPublicationChangeRequestChangeRequestChangedValue,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_change_request_publication_change_request_foreigntext import (
            FsResPublicationChangeRequestPublicationChangeRequestForeigntext,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPublicationChangeRequestPublicationChangeRequestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPublicationChangeRequestPublicationChangeRequestForeigntext.from_dict(
                _field_foreigntext
            )

        _changed_values = d.pop("changedValues", UNSET)
        changed_values: list[FsResPublicationChangeRequestChangeRequestChangedValue] | Unset = UNSET
        if _changed_values is not UNSET:
            changed_values = []
            for changed_values_item_data in _changed_values:
                changed_values_item = FsResPublicationChangeRequestChangeRequestChangedValue.from_dict(
                    changed_values_item_data
                )

                changed_values.append(changed_values_item)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        fs_res_publication_change_request_publication_change_request = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            changed_values=changed_values,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        fs_res_publication_change_request_publication_change_request.additional_properties = d
        return fs_res_publication_change_request_publication_change_request

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
