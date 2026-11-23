from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_e_address_rest import CsPsvEAddressRest
    from ..models.cs_psv_post_address_rest import CsPsvPostAddressRest
    from ..models.cs_psv_psv_profile_affiliation_foreigntext import CsPsvPsvProfileAffiliationForeigntext
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue


T = TypeVar("T", bound="CsPsvPsvProfileAffiliation")


@_attrs_define
class CsPsvPsvProfileAffiliation:
    """
    Attributes:
        field_foreigntext (CsPsvPsvProfileAffiliationForeigntext | Unset):
        affiliation_type (CsSysValueGenericValue | Unset):
        eaddresses (list[CsPsvEAddressRest] | Unset):
        id (int | Unset):
        location (CsPsvPostAddressRest | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organization (CsSysValueGenericValue | Unset):
        supplement (str | Unset):
        visibility (CsSysValueGenericValue | Unset):
    """

    field_foreigntext: CsPsvPsvProfileAffiliationForeigntext | Unset = UNSET
    affiliation_type: CsSysValueGenericValue | Unset = UNSET
    eaddresses: list[CsPsvEAddressRest] | Unset = UNSET
    id: int | Unset = UNSET
    location: CsPsvPostAddressRest | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organization: CsSysValueGenericValue | Unset = UNSET
    supplement: str | Unset = UNSET
    visibility: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        affiliation_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliation_type, Unset):
            affiliation_type = self.affiliation_type.to_dict()

        eaddresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eaddresses, Unset):
            eaddresses = []
            for eaddresses_item_data in self.eaddresses:
                eaddresses_item = eaddresses_item_data.to_dict()
                eaddresses.append(eaddresses_item)

        id = self.id

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        supplement = self.supplement

        visibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if affiliation_type is not UNSET:
            field_dict["affiliationType"] = affiliation_type
        if eaddresses is not UNSET:
            field_dict["eaddresses"] = eaddresses
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organization is not UNSET:
            field_dict["organization"] = organization
        if supplement is not UNSET:
            field_dict["supplement"] = supplement
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_e_address_rest import CsPsvEAddressRest  # noqa: PLC0415
        from ..models.cs_psv_post_address_rest import CsPsvPostAddressRest  # noqa: PLC0415
        from ..models.cs_psv_psv_profile_affiliation_foreigntext import CsPsvPsvProfileAffiliationForeigntext  # noqa: PLC0415
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: CsPsvPsvProfileAffiliationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = CsPsvPsvProfileAffiliationForeigntext.from_dict(_field_foreigntext)

        _affiliation_type = d.pop("affiliationType", UNSET)
        affiliation_type: CsSysValueGenericValue | Unset
        if isinstance(_affiliation_type, Unset):
            affiliation_type = UNSET
        else:
            affiliation_type = CsSysValueGenericValue.from_dict(_affiliation_type)

        _eaddresses = d.pop("eaddresses", UNSET)
        eaddresses: list[CsPsvEAddressRest] | Unset = UNSET
        if _eaddresses is not UNSET:
            eaddresses = []
            for eaddresses_item_data in _eaddresses:
                eaddresses_item = CsPsvEAddressRest.from_dict(eaddresses_item_data)

                eaddresses.append(eaddresses_item)

        id = d.pop("id", UNSET)

        _location = d.pop("location", UNSET)
        location: CsPsvPostAddressRest | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = CsPsvPostAddressRest.from_dict(_location)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: CsSysValueGenericValue | Unset
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CsSysValueGenericValue.from_dict(_organization)

        supplement = d.pop("supplement", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: CsSysValueGenericValue | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = CsSysValueGenericValue.from_dict(_visibility)

        cs_psv_psv_profile_affiliation = cls(
            field_foreigntext=field_foreigntext,
            affiliation_type=affiliation_type,
            eaddresses=eaddresses,
            id=id,
            location=location,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organization=organization,
            supplement=supplement,
            visibility=visibility,
        )

        cs_psv_psv_profile_affiliation.additional_properties = d
        return cs_psv_psv_profile_affiliation

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
