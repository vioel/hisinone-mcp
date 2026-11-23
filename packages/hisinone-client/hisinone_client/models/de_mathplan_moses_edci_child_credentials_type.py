from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_child_credential_defined_as_any_type import (
        DeMathplanMosesEdciChildCredentialDefinedAsAnyType,
    )


T = TypeVar("T", bound="DeMathplanMosesEdciChildCredentialsType")


@_attrs_define
class DeMathplanMosesEdciChildCredentialsType:
    """
    Attributes:
        child_credential (list[DeMathplanMosesEdciChildCredentialDefinedAsAnyType] | Unset):
    """

    child_credential: list[DeMathplanMosesEdciChildCredentialDefinedAsAnyType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        child_credential: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_credential, Unset):
            child_credential = []
            for child_credential_item_data in self.child_credential:
                child_credential_item = child_credential_item_data.to_dict()
                child_credential.append(child_credential_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if child_credential is not UNSET:
            field_dict["childCredential"] = child_credential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_child_credential_defined_as_any_type import (
            DeMathplanMosesEdciChildCredentialDefinedAsAnyType,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _child_credential = d.pop("childCredential", UNSET)
        child_credential: list[DeMathplanMosesEdciChildCredentialDefinedAsAnyType] | Unset = UNSET
        if _child_credential is not UNSET:
            child_credential = []
            for child_credential_item_data in _child_credential:
                child_credential_item = DeMathplanMosesEdciChildCredentialDefinedAsAnyType.from_dict(
                    child_credential_item_data
                )

                child_credential.append(child_credential_item)

        de_mathplan_moses_edci_child_credentials_type = cls(
            child_credential=child_credential,
        )

        de_mathplan_moses_edci_child_credentials_type.additional_properties = d
        return de_mathplan_moses_edci_child_credentials_type

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
