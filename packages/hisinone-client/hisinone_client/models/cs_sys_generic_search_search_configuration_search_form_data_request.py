from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_configuration_versioned_key import (
        CsSysGenericSearchSearchConfigurationVersionedKey,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationSearchFormDataRequest")


@_attrs_define
class CsSysGenericSearchSearchConfigurationSearchFormDataRequest:
    """
    Attributes:
        config_file (str | Unset):
        requested_keys (list[CsSysGenericSearchSearchConfigurationVersionedKey] | Unset):
    """

    config_file: str | Unset = UNSET
    requested_keys: list[CsSysGenericSearchSearchConfigurationVersionedKey] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config_file = self.config_file

        requested_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requested_keys, Unset):
            requested_keys = []
            for requested_keys_item_data in self.requested_keys:
                requested_keys_item = requested_keys_item_data.to_dict()
                requested_keys.append(requested_keys_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_file is not UNSET:
            field_dict["configFile"] = config_file
        if requested_keys is not UNSET:
            field_dict["requestedKeys"] = requested_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_configuration_versioned_key import (
            CsSysGenericSearchSearchConfigurationVersionedKey,  # noqa: PLC0415
        )

        d = dict(src_dict)
        config_file = d.pop("configFile", UNSET)

        _requested_keys = d.pop("requestedKeys", UNSET)
        requested_keys: list[CsSysGenericSearchSearchConfigurationVersionedKey] | Unset = UNSET
        if _requested_keys is not UNSET:
            requested_keys = []
            for requested_keys_item_data in _requested_keys:
                requested_keys_item = CsSysGenericSearchSearchConfigurationVersionedKey.from_dict(
                    requested_keys_item_data
                )

                requested_keys.append(requested_keys_item)

        cs_sys_generic_search_search_configuration_search_form_data_request = cls(
            config_file=config_file,
            requested_keys=requested_keys,
        )

        cs_sys_generic_search_search_configuration_search_form_data_request.additional_properties = d
        return cs_sys_generic_search_search_configuration_search_form_data_request

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
