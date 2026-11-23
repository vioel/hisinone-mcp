from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_e_address_rest_foreigntext import CsPsvEAddressRestForeigntext
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvEAddressRest")


@_attrs_define
class CsPsvEAddressRest:
    """
    Attributes:
        field_foreigntext (CsPsvEAddressRestForeigntext | Unset):
        eaddress (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        type_ (CsSysValueGenericValue | Unset):
    """

    field_foreigntext: CsPsvEAddressRestForeigntext | Unset = UNSET
    eaddress: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    type_: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        eaddress = self.eaddress

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if eaddress is not UNSET:
            field_dict["eaddress"] = eaddress
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_e_address_rest_foreigntext import CsPsvEAddressRestForeigntext  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvEAddressRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvEAddressRestForeigntext.from_dict(_field_foreigntext)

        eaddress = d.pop("eaddress", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CsSysValueGenericValue | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CsSysValueGenericValue.from_dict(_type_)

        cs_psv_e_address_rest = cls(
            field_foreigntext=field_foreigntext,
            eaddress=eaddress,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            type_=type_,
        )

        cs_psv_e_address_rest.additional_properties = d
        return cs_psv_e_address_rest

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
