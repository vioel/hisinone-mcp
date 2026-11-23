from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_w3c_dom_dom_string_list import OrgW3CDomDOMStringList


T = TypeVar("T", bound="OrgW3CDomDOMConfiguration")


@_attrs_define
class OrgW3CDomDOMConfiguration:
    """
    Attributes:
        parameter_names (OrgW3CDomDOMStringList | Unset):
    """

    parameter_names: OrgW3CDomDOMStringList | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        parameter_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameter_names, Unset):
            parameter_names = self.parameter_names.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter_names is not UNSET:
            field_dict["parameterNames"] = parameter_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_w3c_dom_dom_string_list import OrgW3CDomDOMStringList  # noqa: PLC0415

        d = dict(src_dict)
        _parameter_names = d.pop("parameterNames", UNSET)
        parameter_names: OrgW3CDomDOMStringList | Unset
        if isinstance(_parameter_names, Unset):
            parameter_names = UNSET
        else:
            parameter_names = OrgW3CDomDOMStringList.from_dict(_parameter_names)

        org_w3c_dom_dom_configuration = cls(
            parameter_names=parameter_names,
        )

        org_w3c_dom_dom_configuration.additional_properties = d
        return org_w3c_dom_dom_configuration

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
