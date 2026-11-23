from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_digest_method_type import EuEmrexElmoDigestMethodType
    from ..models.eu_emrex_elmo_transforms_type import EuEmrexElmoTransformsType


T = TypeVar("T", bound="EuEmrexElmoReferenceType")


@_attrs_define
class EuEmrexElmoReferenceType:
    """
    Attributes:
        digest_method (EuEmrexElmoDigestMethodType | Unset):
        digest_value (list[int] | Unset):
        id (str | Unset):
        transforms (EuEmrexElmoTransformsType | Unset):
        type_ (str | Unset):
        u_ri (str | Unset):
    """

    digest_method: EuEmrexElmoDigestMethodType | Unset = UNSET
    digest_value: list[int] | Unset = UNSET
    id: str | Unset = UNSET
    transforms: EuEmrexElmoTransformsType | Unset = UNSET
    type_: str | Unset = UNSET
    u_ri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        digest_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.digest_method, Unset):
            digest_method = self.digest_method.to_dict()

        digest_value: list[int] | Unset = UNSET
        if not isinstance(self.digest_value, Unset):
            digest_value = self.digest_value

        id = self.id

        transforms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transforms, Unset):
            transforms = self.transforms.to_dict()

        type_ = self.type_

        u_ri = self.u_ri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest_method is not UNSET:
            field_dict["digestMethod"] = digest_method
        if digest_value is not UNSET:
            field_dict["digestValue"] = digest_value
        if id is not UNSET:
            field_dict["id"] = id
        if transforms is not UNSET:
            field_dict["transforms"] = transforms
        if type_ is not UNSET:
            field_dict["type"] = type_
        if u_ri is not UNSET:
            field_dict["uRI"] = u_ri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_digest_method_type import EuEmrexElmoDigestMethodType  # noqa: PLC0415
        from ..models.eu_emrex_elmo_transforms_type import EuEmrexElmoTransformsType  # noqa: PLC0415

        d = dict(src_dict)
        _digest_method = d.pop("digestMethod", UNSET)
        digest_method: EuEmrexElmoDigestMethodType | Unset
        if isinstance(_digest_method, Unset):
            digest_method = UNSET
        else:
            digest_method = EuEmrexElmoDigestMethodType.from_dict(_digest_method)

        digest_value = cast(list[int], d.pop("digestValue", UNSET))

        id = d.pop("id", UNSET)

        _transforms = d.pop("transforms", UNSET)
        transforms: EuEmrexElmoTransformsType | Unset
        if isinstance(_transforms, Unset):
            transforms = UNSET
        else:
            transforms = EuEmrexElmoTransformsType.from_dict(_transforms)

        type_ = d.pop("type", UNSET)

        u_ri = d.pop("uRI", UNSET)

        eu_emrex_elmo_reference_type = cls(
            digest_method=digest_method,
            digest_value=digest_value,
            id=id,
            transforms=transforms,
            type_=type_,
            u_ri=u_ri,
        )

        eu_emrex_elmo_reference_type.additional_properties = d
        return eu_emrex_elmo_reference_type

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
