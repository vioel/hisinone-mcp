from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_psv_schema_external_data_model_configuration_rest import (
        ImplPsvSchemaExternalDataModelConfigurationRest,
    )
    from ..models.impl_psv_schema_external_data_model_rest_foreigntext import (
        ImplPsvSchemaExternalDataModelRestForeigntext,
    )


T = TypeVar("T", bound="ImplPsvSchemaExternalDataModelRest")


@_attrs_define
class ImplPsvSchemaExternalDataModelRest:
    """
    Attributes:
        field_foreigntext (ImplPsvSchemaExternalDataModelRestForeigntext | Unset):
        configurations (list[ImplPsvSchemaExternalDataModelConfigurationRest] | Unset):
        data_model (str | Unset):
        description (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        publisher (str | Unset):
        subtype (str | Unset):
        template_name (str | Unset):
        uniquename (str | Unset):
        version (str | Unset):
        websites (list[str] | Unset):
    """

    field_foreigntext: ImplPsvSchemaExternalDataModelRestForeigntext | Unset = UNSET
    configurations: list[ImplPsvSchemaExternalDataModelConfigurationRest] | Unset = UNSET
    data_model: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    publisher: str | Unset = UNSET
    subtype: str | Unset = UNSET
    template_name: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    version: str | Unset = UNSET
    websites: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = []
            for configurations_item_data in self.configurations:
                configurations_item = configurations_item_data.to_dict()
                configurations.append(configurations_item)

        data_model = self.data_model

        description = self.description

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        publisher = self.publisher

        subtype = self.subtype

        template_name = self.template_name

        uniquename = self.uniquename

        version = self.version

        websites: list[str] | Unset = UNSET
        if not isinstance(self.websites, Unset):
            websites = self.websites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if data_model is not UNSET:
            field_dict["dataModel"] = data_model
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if version is not UNSET:
            field_dict["version"] = version
        if websites is not UNSET:
            field_dict["websites"] = websites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_psv_schema_external_data_model_configuration_rest import (
            ImplPsvSchemaExternalDataModelConfigurationRest,  # noqa: PLC0415
        )
        from ..models.impl_psv_schema_external_data_model_rest_foreigntext import (
            ImplPsvSchemaExternalDataModelRestForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplPsvSchemaExternalDataModelRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplPsvSchemaExternalDataModelRestForeigntext.from_dict(_field_foreigntext)

        _configurations = d.pop("configurations", UNSET)
        configurations: list[ImplPsvSchemaExternalDataModelConfigurationRest] | Unset = UNSET
        if _configurations is not UNSET:
            configurations = []
            for configurations_item_data in _configurations:
                configurations_item = ImplPsvSchemaExternalDataModelConfigurationRest.from_dict(
                    configurations_item_data
                )

                configurations.append(configurations_item)

        data_model = d.pop("dataModel", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        publisher = d.pop("publisher", UNSET)

        subtype = d.pop("subtype", UNSET)

        template_name = d.pop("templateName", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        version = d.pop("version", UNSET)

        websites = cast(list[str], d.pop("websites", UNSET))

        impl_psv_schema_external_data_model_rest = cls(
            field_foreigntext=field_foreigntext,
            configurations=configurations,
            data_model=data_model,
            description=description,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            publisher=publisher,
            subtype=subtype,
            template_name=template_name,
            uniquename=uniquename,
            version=version,
            websites=websites,
        )

        impl_psv_schema_external_data_model_rest.additional_properties = d
        return impl_psv_schema_external_data_model_rest

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
