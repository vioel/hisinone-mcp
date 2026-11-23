from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_country_code import EuEmrexElmoCountryCode
    from ..models.eu_emrex_elmo_elmo_report_issuer_identifier import EuEmrexElmoElmoReportIssuerIdentifier
    from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang


T = TypeVar("T", bound="EuEmrexElmoElmoReportIssuer")


@_attrs_define
class EuEmrexElmoElmoReportIssuer:
    """
    Attributes:
        country (EuEmrexElmoCountryCode | Unset):
        identifier (list[EuEmrexElmoElmoReportIssuerIdentifier] | Unset):
        title (list[EuEmrexElmoTokenWithOptionalLang] | Unset):
        url (str | Unset):
    """

    country: EuEmrexElmoCountryCode | Unset = UNSET
    identifier: list[EuEmrexElmoElmoReportIssuerIdentifier] | Unset = UNSET
    title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        title: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = []
            for title_item_data in self.title:
                title_item = title_item_data.to_dict()
                title.append(title_item)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_country_code import EuEmrexElmoCountryCode  # noqa: PLC0415
        from ..models.eu_emrex_elmo_elmo_report_issuer_identifier import EuEmrexElmoElmoReportIssuerIdentifier  # noqa: PLC0415
        from ..models.eu_emrex_elmo_token_with_optional_lang import EuEmrexElmoTokenWithOptionalLang  # noqa: PLC0415

        d = dict(src_dict)
        _country = d.pop("country", UNSET)
        country: EuEmrexElmoCountryCode | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = EuEmrexElmoCountryCode.from_dict(_country)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[EuEmrexElmoElmoReportIssuerIdentifier] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = EuEmrexElmoElmoReportIssuerIdentifier.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        _title = d.pop("title", UNSET)
        title: list[EuEmrexElmoTokenWithOptionalLang] | Unset = UNSET
        if _title is not UNSET:
            title = []
            for title_item_data in _title:
                title_item = EuEmrexElmoTokenWithOptionalLang.from_dict(title_item_data)

                title.append(title_item)

        url = d.pop("url", UNSET)

        eu_emrex_elmo_elmo_report_issuer = cls(
            country=country,
            identifier=identifier,
            title=title,
            url=url,
        )

        eu_emrex_elmo_elmo_report_issuer.additional_properties = d
        return eu_emrex_elmo_elmo_report_issuer

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
