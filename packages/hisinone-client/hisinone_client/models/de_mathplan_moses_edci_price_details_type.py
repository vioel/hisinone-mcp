from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_amount_type import DeMathplanMosesEdciAmountType
    from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType


T = TypeVar("T", bound="DeMathplanMosesEdciPriceDetailsType")


@_attrs_define
class DeMathplanMosesEdciPriceDetailsType:
    """
    Attributes:
        additional_note (list[DeMathplanMosesEdciNoteType] | Unset):
        amount (DeMathplanMosesEdciAmountType | Unset):
        description (list[DeMathplanMosesEdciNoteType] | Unset):
        id (str | Unset):
        identifier (list[DeMathplanMosesEdciGenericIdentifierType] | Unset):
        name (list[DeMathplanMosesEdciLanguageStringType] | Unset):
    """

    additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    amount: DeMathplanMosesEdciAmountType | Unset = UNSET
    description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
    id: str | Unset = UNSET
    identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
    name: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        additional_note: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_note, Unset):
            additional_note = []
            for additional_note_item_data in self.additional_note:
                additional_note_item = additional_note_item_data.to_dict()
                additional_note.append(additional_note_item)

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.description, Unset):
            description = []
            for description_item_data in self.description:
                description_item = description_item_data.to_dict()
                description.append(description_item)

        id = self.id

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = []
            for name_item_data in self.name:
                name_item = name_item_data.to_dict()
                name.append(name_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_note is not UNSET:
            field_dict["additionalNote"] = additional_note
        if amount is not UNSET:
            field_dict["amount"] = amount
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_amount_type import DeMathplanMosesEdciAmountType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_generic_identifier_type import DeMathplanMosesEdciGenericIdentifierType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_note_type import DeMathplanMosesEdciNoteType  # noqa: PLC0415

        d = dict(src_dict)
        _additional_note = d.pop("additionalNote", UNSET)
        additional_note: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _additional_note is not UNSET:
            additional_note = []
            for additional_note_item_data in _additional_note:
                additional_note_item = DeMathplanMosesEdciNoteType.from_dict(additional_note_item_data)

                additional_note.append(additional_note_item)

        _amount = d.pop("amount", UNSET)
        amount: DeMathplanMosesEdciAmountType | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = DeMathplanMosesEdciAmountType.from_dict(_amount)

        _description = d.pop("description", UNSET)
        description: list[DeMathplanMosesEdciNoteType] | Unset = UNSET
        if _description is not UNSET:
            description = []
            for description_item_data in _description:
                description_item = DeMathplanMosesEdciNoteType.from_dict(description_item_data)

                description.append(description_item)

        id = d.pop("id", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[DeMathplanMosesEdciGenericIdentifierType] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = DeMathplanMosesEdciGenericIdentifierType.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _name = d.pop("name", UNSET)
        name: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _name is not UNSET:
            name = []
            for name_item_data in _name:
                name_item = DeMathplanMosesEdciLanguageStringType.from_dict(name_item_data)

                name.append(name_item)

        de_mathplan_moses_edci_price_details_type = cls(
            additional_note=additional_note,
            amount=amount,
            description=description,
            id=id,
            identifier=identifier,
            name=name,
        )

        de_mathplan_moses_edci_price_details_type.additional_properties = d
        return de_mathplan_moses_edci_price_details_type

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
