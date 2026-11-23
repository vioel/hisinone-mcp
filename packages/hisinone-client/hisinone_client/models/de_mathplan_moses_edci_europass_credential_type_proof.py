from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_signature_type import DeMathplanMosesEdciSignatureType


T = TypeVar("T", bound="DeMathplanMosesEdciEuropassCredentialTypeProof")


@_attrs_define
class DeMathplanMosesEdciEuropassCredentialTypeProof:
    """
    Attributes:
        signature (DeMathplanMosesEdciSignatureType | Unset):
    """

    signature: DeMathplanMosesEdciSignatureType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        signature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signature is not UNSET:
            field_dict["signature"] = signature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_signature_type import DeMathplanMosesEdciSignatureType  # noqa: PLC0415

        d = dict(src_dict)
        _signature = d.pop("signature", UNSET)
        signature: DeMathplanMosesEdciSignatureType | Unset
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = DeMathplanMosesEdciSignatureType.from_dict(_signature)

        de_mathplan_moses_edci_europass_credential_type_proof = cls(
            signature=signature,
        )

        de_mathplan_moses_edci_europass_credential_type_proof.additional_properties = d
        return de_mathplan_moses_edci_europass_credential_type_proof

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
