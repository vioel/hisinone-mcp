from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_term_rest import ConditionTermRest


T = TypeVar("T", bound="ContextConfigRest")


@_attrs_define
class ContextConfigRest:
    """
    Attributes:
        confsrc_id (int | Unset):
        defaulttext (str | Unset):
        description (str | Unset):
        dnf_expression (list[list[ConditionTermRest]] | Unset):
        id (int | Unset):
        valid_from (int | Unset):
        valid_to (int | Unset):
    """

    confsrc_id: int | Unset = UNSET
    defaulttext: str | Unset = UNSET
    description: str | Unset = UNSET
    dnf_expression: list[list[ConditionTermRest]] | Unset = UNSET
    id: int | Unset = UNSET
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        confsrc_id = self.confsrc_id

        defaulttext = self.defaulttext

        description = self.description

        dnf_expression: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.dnf_expression, Unset):
            dnf_expression = []
            for dnf_expression_item_data in self.dnf_expression:
                dnf_expression_item: list[dict[str, Any]] = []
                for dnf_expression_item_item_data in dnf_expression_item_data:
                    dnf_expression_item_item = dnf_expression_item_item_data.to_dict()
                    dnf_expression_item.append(dnf_expression_item_item)

                dnf_expression.append(dnf_expression_item)

        id = self.id

        valid_from = self.valid_from

        valid_to = self.valid_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confsrc_id is not UNSET:
            field_dict["confsrcId"] = confsrc_id
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if description is not UNSET:
            field_dict["description"] = description
        if dnf_expression is not UNSET:
            field_dict["dnfExpression"] = dnf_expression
        if id is not UNSET:
            field_dict["id"] = id
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.condition_term_rest import ConditionTermRest  # noqa: PLC0415

        d = dict(src_dict)
        confsrc_id = d.pop("confsrcId", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        description = d.pop("description", UNSET)

        _dnf_expression = d.pop("dnfExpression", UNSET)
        dnf_expression: list[list[ConditionTermRest]] | Unset = UNSET
        if _dnf_expression is not UNSET:
            dnf_expression = []
            for dnf_expression_item_data in _dnf_expression:
                dnf_expression_item: list[ConditionTermRest] = []
                _dnf_expression_item = dnf_expression_item_data
                for dnf_expression_item_item_data in _dnf_expression_item:
                    dnf_expression_item_item = ConditionTermRest.from_dict(dnf_expression_item_item_data)

                    dnf_expression_item.append(dnf_expression_item_item)

                dnf_expression.append(dnf_expression_item)

        id = d.pop("id", UNSET)

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        context_config_rest = cls(
            confsrc_id=confsrc_id,
            defaulttext=defaulttext,
            description=description,
            dnf_expression=dnf_expression,
            id=id,
            valid_from=valid_from,
            valid_to=valid_to,
        )

        context_config_rest.additional_properties = d
        return context_config_rest

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
