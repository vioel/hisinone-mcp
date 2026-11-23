from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_springframework_context_application_context import OrgSpringframeworkContextApplicationContext
    from ..models.org_springframework_web_servlet_view_redirect_view_attributes_map import (
        OrgSpringframeworkWebServletViewRedirectViewAttributesMap,
    )
    from ..models.org_springframework_web_servlet_view_redirect_view_static_attributes import (
        OrgSpringframeworkWebServletViewRedirectViewStaticAttributes,
    )


T = TypeVar("T", bound="OrgSpringframeworkWebServletViewRedirectView")


@_attrs_define
class OrgSpringframeworkWebServletViewRedirectView:
    """
    Attributes:
        application_context (OrgSpringframeworkContextApplicationContext | Unset):
        attributes_map (OrgSpringframeworkWebServletViewRedirectViewAttributesMap | Unset):
        bean_name (str | Unset):
        content_type (str | Unset):
        expose_path_variables (bool | Unset):
        hosts (list[str] | Unset):
        propagate_query_properties (bool | Unset):
        redirect_view (bool | Unset):
        request_context_attribute (str | Unset):
        static_attributes (OrgSpringframeworkWebServletViewRedirectViewStaticAttributes | Unset):
        url (str | Unset):
    """

    application_context: OrgSpringframeworkContextApplicationContext | Unset = UNSET
    attributes_map: OrgSpringframeworkWebServletViewRedirectViewAttributesMap | Unset = UNSET
    bean_name: str | Unset = UNSET
    content_type: str | Unset = UNSET
    expose_path_variables: bool | Unset = UNSET
    hosts: list[str] | Unset = UNSET
    propagate_query_properties: bool | Unset = UNSET
    redirect_view: bool | Unset = UNSET
    request_context_attribute: str | Unset = UNSET
    static_attributes: OrgSpringframeworkWebServletViewRedirectViewStaticAttributes | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        application_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_context, Unset):
            application_context = self.application_context.to_dict()

        attributes_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes_map, Unset):
            attributes_map = self.attributes_map.to_dict()

        bean_name = self.bean_name

        content_type = self.content_type

        expose_path_variables = self.expose_path_variables

        hosts: list[str] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        propagate_query_properties = self.propagate_query_properties

        redirect_view = self.redirect_view

        request_context_attribute = self.request_context_attribute

        static_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.static_attributes, Unset):
            static_attributes = self.static_attributes.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_context is not UNSET:
            field_dict["applicationContext"] = application_context
        if attributes_map is not UNSET:
            field_dict["attributesMap"] = attributes_map
        if bean_name is not UNSET:
            field_dict["beanName"] = bean_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if expose_path_variables is not UNSET:
            field_dict["exposePathVariables"] = expose_path_variables
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if propagate_query_properties is not UNSET:
            field_dict["propagateQueryProperties"] = propagate_query_properties
        if redirect_view is not UNSET:
            field_dict["redirectView"] = redirect_view
        if request_context_attribute is not UNSET:
            field_dict["requestContextAttribute"] = request_context_attribute
        if static_attributes is not UNSET:
            field_dict["staticAttributes"] = static_attributes
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_springframework_context_application_context import OrgSpringframeworkContextApplicationContext  # noqa: PLC0415
        from ..models.org_springframework_web_servlet_view_redirect_view_attributes_map import (
            OrgSpringframeworkWebServletViewRedirectViewAttributesMap,  # noqa: PLC0415
        )
        from ..models.org_springframework_web_servlet_view_redirect_view_static_attributes import (
            OrgSpringframeworkWebServletViewRedirectViewStaticAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _application_context = d.pop("applicationContext", UNSET)
        application_context: OrgSpringframeworkContextApplicationContext | Unset
        if isinstance(_application_context, Unset):
            application_context = UNSET
        else:
            application_context = OrgSpringframeworkContextApplicationContext.from_dict(_application_context)

        _attributes_map = d.pop("attributesMap", UNSET)
        attributes_map: OrgSpringframeworkWebServletViewRedirectViewAttributesMap | Unset
        if isinstance(_attributes_map, Unset):
            attributes_map = UNSET
        else:
            attributes_map = OrgSpringframeworkWebServletViewRedirectViewAttributesMap.from_dict(_attributes_map)

        bean_name = d.pop("beanName", UNSET)

        content_type = d.pop("contentType", UNSET)

        expose_path_variables = d.pop("exposePathVariables", UNSET)

        hosts = cast(list[str], d.pop("hosts", UNSET))

        propagate_query_properties = d.pop("propagateQueryProperties", UNSET)

        redirect_view = d.pop("redirectView", UNSET)

        request_context_attribute = d.pop("requestContextAttribute", UNSET)

        _static_attributes = d.pop("staticAttributes", UNSET)
        static_attributes: OrgSpringframeworkWebServletViewRedirectViewStaticAttributes | Unset
        if isinstance(_static_attributes, Unset):
            static_attributes = UNSET
        else:
            static_attributes = OrgSpringframeworkWebServletViewRedirectViewStaticAttributes.from_dict(
                _static_attributes
            )

        url = d.pop("url", UNSET)

        org_springframework_web_servlet_view_redirect_view = cls(
            application_context=application_context,
            attributes_map=attributes_map,
            bean_name=bean_name,
            content_type=content_type,
            expose_path_variables=expose_path_variables,
            hosts=hosts,
            propagate_query_properties=propagate_query_properties,
            redirect_view=redirect_view,
            request_context_attribute=request_context_attribute,
            static_attributes=static_attributes,
            url=url,
        )

        org_springframework_web_servlet_view_redirect_view.additional_properties = d
        return org_springframework_web_servlet_view_redirect_view

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
