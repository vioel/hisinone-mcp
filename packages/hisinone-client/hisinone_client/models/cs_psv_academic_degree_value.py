from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_academic_degree_value_foreigntext import CsPsvAcademicDegreeValueForeigntext


T = TypeVar("T", bound="CsPsvAcademicDegreeValue")


@_attrs_define
class CsPsvAcademicDegreeValue:
    """
    Attributes:
        field_foreigntext (CsPsvAcademicDegreeValueForeigntext | Unset):
        defaulttext (str | Unset):
        hiskey_id (int | Unset):
        id (int | Unset):
        lettersalutation (str | Unset):
        lettersalutation_female (str | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        obj_guid (str | Unset):
        position_of_title (int | Unset):
        shorttext (str | Unset):
        sortorder (int | Unset):
        text (str | Unset):
        uniquename (str | Unset):
    """

    field_foreigntext: CsPsvAcademicDegreeValueForeigntext | Unset = UNSET
    defaulttext: str | Unset = UNSET
    hiskey_id: int | Unset = UNSET
    id: int | Unset = UNSET
    lettersalutation: str | Unset = UNSET
    lettersalutation_female: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    position_of_title: int | Unset = UNSET
    shorttext: str | Unset = UNSET
    sortorder: int | Unset = UNSET
    text: str | Unset = UNSET
    uniquename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        defaulttext = self.defaulttext

        hiskey_id = self.hiskey_id

        id = self.id

        lettersalutation = self.lettersalutation

        lettersalutation_female = self.lettersalutation_female

        lock_version = self.lock_version

        longtext = self.longtext

        obj_guid = self.obj_guid

        position_of_title = self.position_of_title

        shorttext = self.shorttext

        sortorder = self.sortorder

        text = self.text

        uniquename = self.uniquename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if hiskey_id is not UNSET:
            field_dict["hiskeyId"] = hiskey_id
        if id is not UNSET:
            field_dict["id"] = id
        if lettersalutation is not UNSET:
            field_dict["lettersalutation"] = lettersalutation
        if lettersalutation_female is not UNSET:
            field_dict["lettersalutationFemale"] = lettersalutation_female
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if position_of_title is not UNSET:
            field_dict["positionOfTitle"] = position_of_title
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if text is not UNSET:
            field_dict["text"] = text
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_academic_degree_value_foreigntext import CsPsvAcademicDegreeValueForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvAcademicDegreeValueForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvAcademicDegreeValueForeigntext.from_dict(_field_foreigntext)

        defaulttext = d.pop("defaulttext", UNSET)

        hiskey_id = d.pop("hiskeyId", UNSET)

        id = d.pop("id", UNSET)

        lettersalutation = d.pop("lettersalutation", UNSET)

        lettersalutation_female = d.pop("lettersalutationFemale", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        position_of_title = d.pop("positionOfTitle", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        text = d.pop("text", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        cs_psv_academic_degree_value = cls(
            field_foreigntext=field_foreigntext,
            defaulttext=defaulttext,
            hiskey_id=hiskey_id,
            id=id,
            lettersalutation=lettersalutation,
            lettersalutation_female=lettersalutation_female,
            lock_version=lock_version,
            longtext=longtext,
            obj_guid=obj_guid,
            position_of_title=position_of_title,
            shorttext=shorttext,
            sortorder=sortorder,
            text=text,
            uniquename=uniquename,
        )

        cs_psv_academic_degree_value.additional_properties = d
        return cs_psv_academic_degree_value

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
