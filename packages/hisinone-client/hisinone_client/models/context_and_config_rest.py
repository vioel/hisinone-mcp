from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context_config_rest import ContextConfigRest
    from ..models.context_definition_rest import ContextDefinitionRest


T = TypeVar("T", bound="ContextAndConfigRest")


@_attrs_define
class ContextAndConfigRest:
    """
    Attributes:
        config (ContextConfigRest | Unset):
        definition (ContextDefinitionRest | Unset):
        used_confsrc_ids (list[int] | Unset):
    """

    config: ContextConfigRest | Unset = UNSET
    definition: ContextDefinitionRest | Unset = UNSET
    used_confsrc_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        used_confsrc_ids: list[int] | Unset = UNSET
        if not isinstance(self.used_confsrc_ids, Unset):
            used_confsrc_ids = self.used_confsrc_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if definition is not UNSET:
            field_dict["definition"] = definition
        if used_confsrc_ids is not UNSET:
            field_dict["usedConfsrcIds"] = used_confsrc_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_config_rest import ContextConfigRest  # noqa: PLC0415
        from ..models.context_definition_rest import ContextDefinitionRest  # noqa: PLC0415

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: ContextConfigRest | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ContextConfigRest.from_dict(_config)

        _definition = d.pop("definition", UNSET)
        definition: ContextDefinitionRest | Unset
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = ContextDefinitionRest.from_dict(_definition)

        used_confsrc_ids = cast(list[int], d.pop("usedConfsrcIds", UNSET))

        context_and_config_rest = cls(
            config=config,
            definition=definition,
            used_confsrc_ids=used_confsrc_ids,
        )

        context_and_config_rest.additional_properties = d
        return context_and_config_rest

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
