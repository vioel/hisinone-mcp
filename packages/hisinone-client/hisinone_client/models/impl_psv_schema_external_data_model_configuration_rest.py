from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.impl_psv_schema_external_data_model_configuration_rest_foreigntext import (
        ImplPsvSchemaExternalDataModelConfigurationRestForeigntext,
    )


T = TypeVar("T", bound="ImplPsvSchemaExternalDataModelConfigurationRest")


@_attrs_define
class ImplPsvSchemaExternalDataModelConfigurationRest:
    """
    Attributes:
        field_foreigntext (ImplPsvSchemaExternalDataModelConfigurationRestForeigntext | Unset):
        conf_src (str | Unset):
        configuration (str | Unset):
        data_model_key (str | Unset):
        data_model_version (str | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: ImplPsvSchemaExternalDataModelConfigurationRestForeigntext | Unset = UNSET
    conf_src: str | Unset = UNSET
    configuration: str | Unset = UNSET
    data_model_key: str | Unset = UNSET
    data_model_version: str | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        conf_src = self.conf_src

        configuration = self.configuration

        data_model_key = self.data_model_key

        data_model_version = self.data_model_version

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if conf_src is not UNSET:
            field_dict["confSrc"] = conf_src
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if data_model_key is not UNSET:
            field_dict["dataModelKey"] = data_model_key
        if data_model_version is not UNSET:
            field_dict["dataModelVersion"] = data_model_version
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.impl_psv_schema_external_data_model_configuration_rest_foreigntext import (
            ImplPsvSchemaExternalDataModelConfigurationRestForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: ImplPsvSchemaExternalDataModelConfigurationRestForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = ImplPsvSchemaExternalDataModelConfigurationRestForeigntext.from_dict(_field_foreigntext)

        conf_src = d.pop("confSrc", UNSET)

        configuration = d.pop("configuration", UNSET)

        data_model_key = d.pop("dataModelKey", UNSET)

        data_model_version = d.pop("dataModelVersion", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        impl_psv_schema_external_data_model_configuration_rest = cls(
            field_foreigntext=field_foreigntext,
            conf_src=conf_src,
            configuration=configuration,
            data_model_key=data_model_key,
            data_model_version=data_model_version,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        impl_psv_schema_external_data_model_configuration_rest.additional_properties = d
        return impl_psv_schema_external_data_model_configuration_rest

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
