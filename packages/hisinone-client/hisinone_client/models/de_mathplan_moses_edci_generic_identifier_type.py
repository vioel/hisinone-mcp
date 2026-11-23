from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar


T = TypeVar("T", bound="DeMathplanMosesEdciGenericIdentifierType")


@_attrs_define
class DeMathplanMosesEdciGenericIdentifierType:
    """
    Attributes:
        issued_date (JavaxXmlDatatypeXMLGregorianCalendar | Unset):
        scheme_agency_name (str | Unset):
        scheme_id (str | Unset):
        scheme_name (str | Unset):
        spatial_id (str | Unset):
        type_ (str | Unset):
        value (str | Unset):
    """

    issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset = UNSET
    scheme_agency_name: str | Unset = UNSET
    scheme_id: str | Unset = UNSET
    scheme_name: str | Unset = UNSET
    spatial_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        issued_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.to_dict()

        scheme_agency_name = self.scheme_agency_name

        scheme_id = self.scheme_id

        scheme_name = self.scheme_name

        spatial_id = self.spatial_id

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if scheme_agency_name is not UNSET:
            field_dict["schemeAgencyName"] = scheme_agency_name
        if scheme_id is not UNSET:
            field_dict["schemeID"] = scheme_id
        if scheme_name is not UNSET:
            field_dict["schemeName"] = scheme_name
        if spatial_id is not UNSET:
            field_dict["spatialID"] = spatial_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.javax_xml_datatype_xml_gregorian_calendar import JavaxXmlDatatypeXMLGregorianCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _issued_date = d.pop("issuedDate", UNSET)
        issued_date: JavaxXmlDatatypeXMLGregorianCalendar | Unset
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = JavaxXmlDatatypeXMLGregorianCalendar.from_dict(_issued_date)

        scheme_agency_name = d.pop("schemeAgencyName", UNSET)

        scheme_id = d.pop("schemeID", UNSET)

        scheme_name = d.pop("schemeName", UNSET)

        spatial_id = d.pop("spatialID", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        de_mathplan_moses_edci_generic_identifier_type = cls(
            issued_date=issued_date,
            scheme_agency_name=scheme_agency_name,
            scheme_id=scheme_id,
            scheme_name=scheme_name,
            spatial_id=spatial_id,
            type_=type_,
            value=value,
        )

        de_mathplan_moses_edci_generic_identifier_type.additional_properties = d
        return de_mathplan_moses_edci_generic_identifier_type

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
