from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_springframework_web_servlet_mvc_support_redirect_attributes_flash_attributes import (
        OrgSpringframeworkWebServletMvcSupportRedirectAttributesFlashAttributes,
    )


T = TypeVar("T", bound="OrgSpringframeworkWebServletMvcSupportRedirectAttributes")


@_attrs_define
class OrgSpringframeworkWebServletMvcSupportRedirectAttributes:
    """
    Attributes:
        flash_attributes (OrgSpringframeworkWebServletMvcSupportRedirectAttributesFlashAttributes | Unset):
    """

    flash_attributes: OrgSpringframeworkWebServletMvcSupportRedirectAttributesFlashAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        flash_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flash_attributes, Unset):
            flash_attributes = self.flash_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flash_attributes is not UNSET:
            field_dict["flashAttributes"] = flash_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_springframework_web_servlet_mvc_support_redirect_attributes_flash_attributes import (
            OrgSpringframeworkWebServletMvcSupportRedirectAttributesFlashAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _flash_attributes = d.pop("flashAttributes", UNSET)
        flash_attributes: OrgSpringframeworkWebServletMvcSupportRedirectAttributesFlashAttributes | Unset
        if isinstance(_flash_attributes, Unset):
            flash_attributes = UNSET
        else:
            flash_attributes = OrgSpringframeworkWebServletMvcSupportRedirectAttributesFlashAttributes.from_dict(
                _flash_attributes
            )

        org_springframework_web_servlet_mvc_support_redirect_attributes = cls(
            flash_attributes=flash_attributes,
        )

        org_springframework_web_servlet_mvc_support_redirect_attributes.additional_properties = d
        return org_springframework_web_servlet_mvc_support_redirect_attributes

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
