from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_digest_method_type import DeMathplanMosesEdciDigestMethodType
    from ..models.de_mathplan_moses_edci_transform_type import DeMathplanMosesEdciTransformType


T = TypeVar("T", bound="DeMathplanMosesEdciReferenceType")


@_attrs_define
class DeMathplanMosesEdciReferenceType:
    """
    Attributes:
        digest_method (DeMathplanMosesEdciDigestMethodType | Unset):
        digest_value (list[int] | Unset):
        id (str | Unset):
        transforms (list[DeMathplanMosesEdciTransformType] | Unset):
        type_ (str | Unset):
        u_ri (str | Unset):
    """

    digest_method: DeMathplanMosesEdciDigestMethodType | Unset = UNSET
    digest_value: list[int] | Unset = UNSET
    id: str | Unset = UNSET
    transforms: list[DeMathplanMosesEdciTransformType] | Unset = UNSET
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

        transforms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transforms, Unset):
            transforms = []
            for transforms_item_data in self.transforms:
                transforms_item = transforms_item_data.to_dict()
                transforms.append(transforms_item)

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
        from ..models.de_mathplan_moses_edci_digest_method_type import DeMathplanMosesEdciDigestMethodType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_transform_type import DeMathplanMosesEdciTransformType  # noqa: PLC0415

        d = dict(src_dict)
        _digest_method = d.pop("digestMethod", UNSET)
        digest_method: DeMathplanMosesEdciDigestMethodType | Unset
        if isinstance(_digest_method, Unset):
            digest_method = UNSET
        else:
            digest_method = DeMathplanMosesEdciDigestMethodType.from_dict(_digest_method)

        digest_value = cast(list[int], d.pop("digestValue", UNSET))

        id = d.pop("id", UNSET)

        _transforms = d.pop("transforms", UNSET)
        transforms: list[DeMathplanMosesEdciTransformType] | Unset = UNSET
        if _transforms is not UNSET:
            transforms = []
            for transforms_item_data in _transforms:
                transforms_item = DeMathplanMosesEdciTransformType.from_dict(transforms_item_data)

                transforms.append(transforms_item)

        type_ = d.pop("type", UNSET)

        u_ri = d.pop("uRI", UNSET)

        de_mathplan_moses_edci_reference_type = cls(
            digest_method=digest_method,
            digest_value=digest_value,
            id=id,
            transforms=transforms,
            type_=type_,
            u_ri=u_ri,
        )

        de_mathplan_moses_edci_reference_type.additional_properties = d
        return de_mathplan_moses_edci_reference_type

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
