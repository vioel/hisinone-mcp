from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_rest_open_api_body import CsSysRestOpenApiBody
    from ..models.cs_sys_rest_open_api_operation_responses import CsSysRestOpenApiOperationResponses
    from ..models.cs_sys_rest_open_api_parameter import CsSysRestOpenApiParameter
    from ..models.cs_sys_rest_open_api_security_requirement import CsSysRestOpenApiSecurityRequirement


T = TypeVar("T", bound="CsSysRestOpenApiOperation")


@_attrs_define
class CsSysRestOpenApiOperation:
    """
    Attributes:
        deprecated (bool | Unset):
        description (str | Unset):
        operation_id (str | Unset):
        parameters (list[CsSysRestOpenApiParameter] | Unset):
        request_body (CsSysRestOpenApiBody | Unset):
        responses (CsSysRestOpenApiOperationResponses | Unset):
        security (list[CsSysRestOpenApiSecurityRequirement] | Unset):
        tags (list[str] | Unset):
    """

    deprecated: bool | Unset = UNSET
    description: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    parameters: list[CsSysRestOpenApiParameter] | Unset = UNSET
    request_body: CsSysRestOpenApiBody | Unset = UNSET
    responses: CsSysRestOpenApiOperationResponses | Unset = UNSET
    security: list[CsSysRestOpenApiSecurityRequirement] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        deprecated = self.deprecated

        description = self.description

        operation_id = self.operation_id

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        request_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_body, Unset):
            request_body = self.request_body.to_dict()

        responses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.responses, Unset):
            responses = self.responses.to_dict()

        security: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.security, Unset):
            security = []
            for security_item_data in self.security:
                security_item = security_item_data.to_dict()
                security.append(security_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if description is not UNSET:
            field_dict["description"] = description
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body
        if responses is not UNSET:
            field_dict["responses"] = responses
        if security is not UNSET:
            field_dict["security"] = security
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_rest_open_api_body import CsSysRestOpenApiBody  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_operation_responses import CsSysRestOpenApiOperationResponses  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_parameter import CsSysRestOpenApiParameter  # noqa: PLC0415
        from ..models.cs_sys_rest_open_api_security_requirement import CsSysRestOpenApiSecurityRequirement  # noqa: PLC0415

        d = dict(src_dict)
        deprecated = d.pop("deprecated", UNSET)

        description = d.pop("description", UNSET)

        operation_id = d.pop("operationId", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[CsSysRestOpenApiParameter] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = CsSysRestOpenApiParameter.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        _request_body = d.pop("requestBody", UNSET)
        request_body: CsSysRestOpenApiBody | Unset
        if isinstance(_request_body, Unset):
            request_body = UNSET
        else:
            request_body = CsSysRestOpenApiBody.from_dict(_request_body)

        _responses = d.pop("responses", UNSET)
        responses: CsSysRestOpenApiOperationResponses | Unset
        if isinstance(_responses, Unset):
            responses = UNSET
        else:
            responses = CsSysRestOpenApiOperationResponses.from_dict(_responses)

        _security = d.pop("security", UNSET)
        security: list[CsSysRestOpenApiSecurityRequirement] | Unset = UNSET
        if _security is not UNSET:
            security = []
            for security_item_data in _security:
                security_item = CsSysRestOpenApiSecurityRequirement.from_dict(security_item_data)

                security.append(security_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        cs_sys_rest_open_api_operation = cls(
            deprecated=deprecated,
            description=description,
            operation_id=operation_id,
            parameters=parameters,
            request_body=request_body,
            responses=responses,
            security=security,
            tags=tags,
        )

        cs_sys_rest_open_api_operation.additional_properties = d
        return cs_sys_rest_open_api_operation

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
