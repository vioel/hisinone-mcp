from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_canonicalization_method_type import EuEmrexElmoCanonicalizationMethodType
    from ..models.eu_emrex_elmo_reference_type import EuEmrexElmoReferenceType
    from ..models.eu_emrex_elmo_signature_method_type import EuEmrexElmoSignatureMethodType


T = TypeVar("T", bound="EuEmrexElmoSignedInfoType")


@_attrs_define
class EuEmrexElmoSignedInfoType:
    """
    Attributes:
        canonicalization_method (EuEmrexElmoCanonicalizationMethodType | Unset):
        id (str | Unset):
        reference (list[EuEmrexElmoReferenceType] | Unset):
        signature_method (EuEmrexElmoSignatureMethodType | Unset):
    """

    canonicalization_method: EuEmrexElmoCanonicalizationMethodType | Unset = UNSET
    id: str | Unset = UNSET
    reference: list[EuEmrexElmoReferenceType] | Unset = UNSET
    signature_method: EuEmrexElmoSignatureMethodType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        canonicalization_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.canonicalization_method, Unset):
            canonicalization_method = self.canonicalization_method.to_dict()

        id = self.id

        reference: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reference, Unset):
            reference = []
            for reference_item_data in self.reference:
                reference_item = reference_item_data.to_dict()
                reference.append(reference_item)

        signature_method: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature_method, Unset):
            signature_method = self.signature_method.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if canonicalization_method is not UNSET:
            field_dict["canonicalizationMethod"] = canonicalization_method
        if id is not UNSET:
            field_dict["id"] = id
        if reference is not UNSET:
            field_dict["reference"] = reference
        if signature_method is not UNSET:
            field_dict["signatureMethod"] = signature_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_canonicalization_method_type import EuEmrexElmoCanonicalizationMethodType  # noqa: PLC0415
        from ..models.eu_emrex_elmo_reference_type import EuEmrexElmoReferenceType  # noqa: PLC0415
        from ..models.eu_emrex_elmo_signature_method_type import EuEmrexElmoSignatureMethodType  # noqa: PLC0415

        d = dict(src_dict)
        _canonicalization_method = d.pop("canonicalizationMethod", UNSET)
        canonicalization_method: EuEmrexElmoCanonicalizationMethodType | Unset
        if isinstance(_canonicalization_method, Unset):
            canonicalization_method = UNSET
        else:
            canonicalization_method = EuEmrexElmoCanonicalizationMethodType.from_dict(_canonicalization_method)

        id = d.pop("id", UNSET)

        _reference = d.pop("reference", UNSET)
        reference: list[EuEmrexElmoReferenceType] | Unset = UNSET
        if _reference is not UNSET:
            reference = []
            for reference_item_data in _reference:
                reference_item = EuEmrexElmoReferenceType.from_dict(reference_item_data)

                reference.append(reference_item)

        _signature_method = d.pop("signatureMethod", UNSET)
        signature_method: EuEmrexElmoSignatureMethodType | Unset
        if isinstance(_signature_method, Unset):
            signature_method = UNSET
        else:
            signature_method = EuEmrexElmoSignatureMethodType.from_dict(_signature_method)

        eu_emrex_elmo_signed_info_type = cls(
            canonicalization_method=canonicalization_method,
            id=id,
            reference=reference,
            signature_method=signature_method,
        )

        eu_emrex_elmo_signed_info_type.additional_properties = d
        return eu_emrex_elmo_signed_info_type

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
