from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FsResPublicationPublicationImportInterfaceType")


@_attrs_define
class FsResPublicationPublicationImportInterfaceType:
    """
    Attributes:
        documentation_url (str | Unset):
        his_repo_type (str | Unset):
        interface_name (str | Unset):
        search_configuration_path (str | Unset):
        system_name (str | Unset):
    """

    documentation_url: str | Unset = UNSET
    his_repo_type: str | Unset = UNSET
    interface_name: str | Unset = UNSET
    search_configuration_path: str | Unset = UNSET
    system_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        documentation_url = self.documentation_url

        his_repo_type = self.his_repo_type

        interface_name = self.interface_name

        search_configuration_path = self.search_configuration_path

        system_name = self.system_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url
        if his_repo_type is not UNSET:
            field_dict["hisRepoType"] = his_repo_type
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if search_configuration_path is not UNSET:
            field_dict["searchConfigurationPath"] = search_configuration_path
        if system_name is not UNSET:
            field_dict["systemName"] = system_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        documentation_url = d.pop("documentationUrl", UNSET)

        his_repo_type = d.pop("hisRepoType", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        search_configuration_path = d.pop("searchConfigurationPath", UNSET)

        system_name = d.pop("systemName", UNSET)

        fs_res_publication_publication_import_interface_type = cls(
            documentation_url=documentation_url,
            his_repo_type=his_repo_type,
            interface_name=interface_name,
            search_configuration_path=search_configuration_path,
            system_name=system_name,
        )

        fs_res_publication_publication_import_interface_type.additional_properties = d
        return fs_res_publication_publication_import_interface_type

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
