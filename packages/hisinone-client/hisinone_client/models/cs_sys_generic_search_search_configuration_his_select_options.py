from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_generic_search_search_configuration_his_option import (
        CsSysGenericSearchSearchConfigurationHisOption,
    )
    from ..models.cs_sys_generic_search_search_configuration_versioned_key import (
        CsSysGenericSearchSearchConfigurationVersionedKey,
    )


T = TypeVar("T", bound="CsSysGenericSearchSearchConfigurationHisSelectOptions")


@_attrs_define
class CsSysGenericSearchSearchConfigurationHisSelectOptions:
    """
    Attributes:
        options (list[CsSysGenericSearchSearchConfigurationHisOption] | Unset):
        vkey (CsSysGenericSearchSearchConfigurationVersionedKey | Unset):
    """

    options: list[CsSysGenericSearchSearchConfigurationHisOption] | Unset = UNSET
    vkey: CsSysGenericSearchSearchConfigurationVersionedKey | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        vkey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vkey, Unset):
            vkey = self.vkey.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options
        if vkey is not UNSET:
            field_dict["vkey"] = vkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_generic_search_search_configuration_his_option import (
            CsSysGenericSearchSearchConfigurationHisOption,  # noqa: PLC0415
        )
        from ..models.cs_sys_generic_search_search_configuration_versioned_key import (
            CsSysGenericSearchSearchConfigurationVersionedKey,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: list[CsSysGenericSearchSearchConfigurationHisOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CsSysGenericSearchSearchConfigurationHisOption.from_dict(options_item_data)

                options.append(options_item)

        _vkey = d.pop("vkey", UNSET)
        vkey: CsSysGenericSearchSearchConfigurationVersionedKey | Unset
        if isinstance(_vkey, Unset):
            vkey = UNSET
        else:
            vkey = CsSysGenericSearchSearchConfigurationVersionedKey.from_dict(_vkey)

        cs_sys_generic_search_search_configuration_his_select_options = cls(
            options=options,
            vkey=vkey,
        )

        cs_sys_generic_search_search_configuration_his_select_options.additional_properties = d
        return cs_sys_generic_search_search_configuration_his_select_options

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
