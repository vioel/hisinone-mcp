from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iface_grading_type import IfaceGradingType


T = TypeVar("T", bound="IfaceGradingTypeConversionAdapter")


@_attrs_define
class IfaceGradingTypeConversionAdapter:
    """
    Attributes:
        destination (IfaceGradingType | Unset):
        from_ (float | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        result (float | Unset):
        sortorder (int | Unset):
        to (float | Unset):
    """

    destination: IfaceGradingType | Unset = UNSET
    from_: float | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    result: float | Unset = UNSET
    sortorder: int | Unset = UNSET
    to: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        from_ = self.from_

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        result = self.result

        sortorder = self.sortorder

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination is not UNSET:
            field_dict["destination"] = destination
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if result is not UNSET:
            field_dict["result"] = result
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iface_grading_type import IfaceGradingType  # noqa: PLC0415

        d = dict(src_dict)
        _destination = d.pop("destination", UNSET)
        destination: IfaceGradingType | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = IfaceGradingType.from_dict(_destination)

        from_ = d.pop("from", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        result = d.pop("result", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        to = d.pop("to", UNSET)

        iface_grading_type_conversion_adapter = cls(
            destination=destination,
            from_=from_,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            result=result,
            sortorder=sortorder,
            to=to,
        )

        iface_grading_type_conversion_adapter.additional_properties = d
        return iface_grading_type_conversion_adapter

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
