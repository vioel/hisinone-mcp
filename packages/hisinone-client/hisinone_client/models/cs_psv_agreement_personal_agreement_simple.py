from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_agreement_personal_agreement_simple_foreigntext import (
        CsPsvAgreementPersonalAgreementSimpleForeigntext,
    )


T = TypeVar("T", bound="CsPsvAgreementPersonalAgreementSimple")


@_attrs_define
class CsPsvAgreementPersonalAgreementSimple:
    """
    Attributes:
        field_foreigntext (CsPsvAgreementPersonalAgreementSimpleForeigntext | Unset):
        agreement_definition_id (int | Unset):
        agreement_definition_key (str | Unset):
        change_date (int | Unset):
        consented (bool | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        person_id (int | Unset):
    """

    field_foreigntext: CsPsvAgreementPersonalAgreementSimpleForeigntext | Unset = UNSET
    agreement_definition_id: int | Unset = UNSET
    agreement_definition_key: str | Unset = UNSET
    change_date: int | Unset = UNSET
    consented: bool | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    person_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        agreement_definition_id = self.agreement_definition_id

        agreement_definition_key = self.agreement_definition_key

        change_date = self.change_date

        consented = self.consented

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if agreement_definition_id is not UNSET:
            field_dict["agreementDefinitionId"] = agreement_definition_id
        if agreement_definition_key is not UNSET:
            field_dict["agreementDefinitionKey"] = agreement_definition_key
        if change_date is not UNSET:
            field_dict["changeDate"] = change_date
        if consented is not UNSET:
            field_dict["consented"] = consented
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if person_id is not UNSET:
            field_dict["personId"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_agreement_personal_agreement_simple_foreigntext import (
            CsPsvAgreementPersonalAgreementSimpleForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvAgreementPersonalAgreementSimpleForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvAgreementPersonalAgreementSimpleForeigntext.from_dict(_field_foreigntext)

        agreement_definition_id = d.pop("agreementDefinitionId", UNSET)

        agreement_definition_key = d.pop("agreementDefinitionKey", UNSET)

        change_date = d.pop("changeDate", UNSET)

        consented = d.pop("consented", UNSET)

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        person_id = d.pop("personId", UNSET)

        cs_psv_agreement_personal_agreement_simple = cls(
            field_foreigntext=field_foreigntext,
            agreement_definition_id=agreement_definition_id,
            agreement_definition_key=agreement_definition_key,
            change_date=change_date,
            consented=consented,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            person_id=person_id,
        )

        cs_psv_agreement_personal_agreement_simple.additional_properties = d
        return cs_psv_agreement_personal_agreement_simple

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
