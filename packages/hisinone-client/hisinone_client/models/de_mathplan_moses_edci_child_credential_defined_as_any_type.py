from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_child_credential_defined_as_any_type_other_attributes import (
        DeMathplanMosesEdciChildCredentialDefinedAsAnyTypeOtherAttributes,
    )
    from ..models.org_w3c_dom_element import OrgW3CDomElement


T = TypeVar("T", bound="DeMathplanMosesEdciChildCredentialDefinedAsAnyType")


@_attrs_define
class DeMathplanMosesEdciChildCredentialDefinedAsAnyType:
    """
    Attributes:
        any_ (list[OrgW3CDomElement] | Unset):
        id (str | Unset):
        other_attributes (DeMathplanMosesEdciChildCredentialDefinedAsAnyTypeOtherAttributes | Unset):
    """

    any_: list[OrgW3CDomElement] | Unset = UNSET
    id: str | Unset = UNSET
    other_attributes: DeMathplanMosesEdciChildCredentialDefinedAsAnyTypeOtherAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        any_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.any_, Unset):
            any_ = []
            for any_item_data in self.any_:
                any_item = any_item_data.to_dict()
                any_.append(any_item)

        id = self.id

        other_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_attributes, Unset):
            other_attributes = self.other_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if any_ is not UNSET:
            field_dict["any"] = any_
        if id is not UNSET:
            field_dict["id"] = id
        if other_attributes is not UNSET:
            field_dict["otherAttributes"] = other_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_child_credential_defined_as_any_type_other_attributes import (
            DeMathplanMosesEdciChildCredentialDefinedAsAnyTypeOtherAttributes,  # noqa: PLC0415
        )
        from ..models.org_w3c_dom_element import OrgW3CDomElement  # noqa: PLC0415

        d = dict(src_dict)
        _any_ = d.pop("any", UNSET)
        any_: list[OrgW3CDomElement] | Unset = UNSET
        if _any_ is not UNSET:
            any_ = []
            for any_item_data in _any_:
                any_item = OrgW3CDomElement.from_dict(any_item_data)

                any_.append(any_item)

        id = d.pop("id", UNSET)

        _other_attributes = d.pop("otherAttributes", UNSET)
        other_attributes: DeMathplanMosesEdciChildCredentialDefinedAsAnyTypeOtherAttributes | Unset
        if isinstance(_other_attributes, Unset):
            other_attributes = UNSET
        else:
            other_attributes = DeMathplanMosesEdciChildCredentialDefinedAsAnyTypeOtherAttributes.from_dict(
                _other_attributes
            )

        de_mathplan_moses_edci_child_credential_defined_as_any_type = cls(
            any_=any_,
            id=id,
            other_attributes=other_attributes,
        )

        de_mathplan_moses_edci_child_credential_defined_as_any_type.additional_properties = d
        return de_mathplan_moses_edci_child_credential_defined_as_any_type

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
