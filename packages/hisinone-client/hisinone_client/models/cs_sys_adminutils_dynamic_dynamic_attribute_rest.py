from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta_hisidentifier_hisidentifier_datatype_enum import MetaHisidentifierHisidentifierDatatypeEnum


T = TypeVar("T", bound="CsSysAdminutilsDynamicDynamicAttributeRest")


@_attrs_define
class CsSysAdminutilsDynamicDynamicAttributeRest:
    """
    Attributes:
        data_source (str | Unset):
        id (int | Unset):
        label (str | Unset):
        marked_to_delete (bool | Unset):
        name (str | Unset):
        required (bool | Unset):
        type_ (MetaHisidentifierHisidentifierDatatypeEnum | Unset):
    """

    data_source: str | Unset = UNSET
    id: int | Unset = UNSET
    label: str | Unset = UNSET
    marked_to_delete: bool | Unset = UNSET
    name: str | Unset = UNSET
    required: bool | Unset = UNSET
    type_: MetaHisidentifierHisidentifierDatatypeEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        data_source = self.data_source

        id = self.id

        label = self.label

        marked_to_delete = self.marked_to_delete

        name = self.name

        required = self.required

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_source is not UNSET:
            field_dict["dataSource"] = data_source
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if marked_to_delete is not UNSET:
            field_dict["markedToDelete"] = marked_to_delete
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_hisidentifier_hisidentifier_datatype_enum import MetaHisidentifierHisidentifierDatatypeEnum  # noqa: PLC0415

        d = dict(src_dict)
        data_source = d.pop("dataSource", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        marked_to_delete = d.pop("markedToDelete", UNSET)

        name = d.pop("name", UNSET)

        required = d.pop("required", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: MetaHisidentifierHisidentifierDatatypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MetaHisidentifierHisidentifierDatatypeEnum.from_dict(_type_)

        cs_sys_adminutils_dynamic_dynamic_attribute_rest = cls(
            data_source=data_source,
            id=id,
            label=label,
            marked_to_delete=marked_to_delete,
            name=name,
            required=required,
            type_=type_,
        )

        cs_sys_adminutils_dynamic_dynamic_attribute_rest.additional_properties = d
        return cs_sys_adminutils_dynamic_dynamic_attribute_rest

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
