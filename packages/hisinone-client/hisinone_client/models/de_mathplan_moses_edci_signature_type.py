from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_key_info_type import DeMathplanMosesEdciKeyInfoType
    from ..models.de_mathplan_moses_edci_object_type import DeMathplanMosesEdciObjectType
    from ..models.de_mathplan_moses_edci_signature_value_type import DeMathplanMosesEdciSignatureValueType
    from ..models.de_mathplan_moses_edci_signed_info_type import DeMathplanMosesEdciSignedInfoType


T = TypeVar("T", bound="DeMathplanMosesEdciSignatureType")


@_attrs_define
class DeMathplanMosesEdciSignatureType:
    """
    Attributes:
        id (str | Unset):
        key_info (DeMathplanMosesEdciKeyInfoType | Unset):
        object_ (list[DeMathplanMosesEdciObjectType] | Unset):
        signature_value (DeMathplanMosesEdciSignatureValueType | Unset):
        signed_info (DeMathplanMosesEdciSignedInfoType | Unset):
    """

    id: str | Unset = UNSET
    key_info: DeMathplanMosesEdciKeyInfoType | Unset = UNSET
    object_: list[DeMathplanMosesEdciObjectType] | Unset = UNSET
    signature_value: DeMathplanMosesEdciSignatureValueType | Unset = UNSET
    signed_info: DeMathplanMosesEdciSignedInfoType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        object_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = []
            for object_item_data in self.object_:
                object_item = object_item_data.to_dict()
                object_.append(object_item)

        signature_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature_value, Unset):
            signature_value = self.signature_value.to_dict()

        signed_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signed_info, Unset):
            signed_info = self.signed_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if object_ is not UNSET:
            field_dict["object"] = object_
        if signature_value is not UNSET:
            field_dict["signatureValue"] = signature_value
        if signed_info is not UNSET:
            field_dict["signedInfo"] = signed_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_key_info_type import DeMathplanMosesEdciKeyInfoType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_object_type import DeMathplanMosesEdciObjectType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_signature_value_type import DeMathplanMosesEdciSignatureValueType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_signed_info_type import DeMathplanMosesEdciSignedInfoType  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: DeMathplanMosesEdciKeyInfoType | Unset
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = DeMathplanMosesEdciKeyInfoType.from_dict(_key_info)

        _object_ = d.pop("object", UNSET)
        object_: list[DeMathplanMosesEdciObjectType] | Unset = UNSET
        if _object_ is not UNSET:
            object_ = []
            for object_item_data in _object_:
                object_item = DeMathplanMosesEdciObjectType.from_dict(object_item_data)

                object_.append(object_item)

        _signature_value = d.pop("signatureValue", UNSET)
        signature_value: DeMathplanMosesEdciSignatureValueType | Unset
        if isinstance(_signature_value, Unset):
            signature_value = UNSET
        else:
            signature_value = DeMathplanMosesEdciSignatureValueType.from_dict(_signature_value)

        _signed_info = d.pop("signedInfo", UNSET)
        signed_info: DeMathplanMosesEdciSignedInfoType | Unset
        if isinstance(_signed_info, Unset):
            signed_info = UNSET
        else:
            signed_info = DeMathplanMosesEdciSignedInfoType.from_dict(_signed_info)

        de_mathplan_moses_edci_signature_type = cls(
            id=id,
            key_info=key_info,
            object_=object_,
            signature_value=signature_value,
            signed_info=signed_info,
        )

        de_mathplan_moses_edci_signature_type.additional_properties = d
        return de_mathplan_moses_edci_signature_type

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
