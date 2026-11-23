from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JavaUtilLocale")


@_attrs_define
class JavaUtilLocale:
    """
    Attributes:
        available_locales (list[JavaUtilLocale] | Unset):
        country (str | Unset):
        default (JavaUtilLocale | Unset):
        display_country (str | Unset):
        display_language (str | Unset):
        display_name (str | Unset):
        display_script (str | Unset):
        display_variant (str | Unset):
        extension_keys (list[str] | Unset):
        i_so3_country (str | Unset):
        i_so3_language (str | Unset):
        i_so_countries (list[str] | Unset):
        i_so_languages (list[str] | Unset):
        language (str | Unset):
        script (str | Unset):
        unicode_locale_attributes (list[str] | Unset):
        unicode_locale_keys (list[str] | Unset):
        variant (str | Unset):
    """

    available_locales: list[JavaUtilLocale] | Unset = UNSET
    country: str | Unset = UNSET
    default: JavaUtilLocale | Unset = UNSET
    display_country: str | Unset = UNSET
    display_language: str | Unset = UNSET
    display_name: str | Unset = UNSET
    display_script: str | Unset = UNSET
    display_variant: str | Unset = UNSET
    extension_keys: list[str] | Unset = UNSET
    i_so3_country: str | Unset = UNSET
    i_so3_language: str | Unset = UNSET
    i_so_countries: list[str] | Unset = UNSET
    i_so_languages: list[str] | Unset = UNSET
    language: str | Unset = UNSET
    script: str | Unset = UNSET
    unicode_locale_attributes: list[str] | Unset = UNSET
    unicode_locale_keys: list[str] | Unset = UNSET
    variant: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        available_locales: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_locales, Unset):
            available_locales = []
            for available_locales_item_data in self.available_locales:
                available_locales_item = available_locales_item_data.to_dict()
                available_locales.append(available_locales_item)

        country = self.country

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        display_country = self.display_country

        display_language = self.display_language

        display_name = self.display_name

        display_script = self.display_script

        display_variant = self.display_variant

        extension_keys: list[str] | Unset = UNSET
        if not isinstance(self.extension_keys, Unset):
            extension_keys = self.extension_keys

        i_so3_country = self.i_so3_country

        i_so3_language = self.i_so3_language

        i_so_countries: list[str] | Unset = UNSET
        if not isinstance(self.i_so_countries, Unset):
            i_so_countries = self.i_so_countries

        i_so_languages: list[str] | Unset = UNSET
        if not isinstance(self.i_so_languages, Unset):
            i_so_languages = self.i_so_languages

        language = self.language

        script = self.script

        unicode_locale_attributes: list[str] | Unset = UNSET
        if not isinstance(self.unicode_locale_attributes, Unset):
            unicode_locale_attributes = self.unicode_locale_attributes

        unicode_locale_keys: list[str] | Unset = UNSET
        if not isinstance(self.unicode_locale_keys, Unset):
            unicode_locale_keys = self.unicode_locale_keys

        variant = self.variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_locales is not UNSET:
            field_dict["availableLocales"] = available_locales
        if country is not UNSET:
            field_dict["country"] = country
        if default is not UNSET:
            field_dict["default"] = default
        if display_country is not UNSET:
            field_dict["displayCountry"] = display_country
        if display_language is not UNSET:
            field_dict["displayLanguage"] = display_language
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_script is not UNSET:
            field_dict["displayScript"] = display_script
        if display_variant is not UNSET:
            field_dict["displayVariant"] = display_variant
        if extension_keys is not UNSET:
            field_dict["extensionKeys"] = extension_keys
        if i_so3_country is not UNSET:
            field_dict["iSO3Country"] = i_so3_country
        if i_so3_language is not UNSET:
            field_dict["iSO3Language"] = i_so3_language
        if i_so_countries is not UNSET:
            field_dict["iSOCountries"] = i_so_countries
        if i_so_languages is not UNSET:
            field_dict["iSOLanguages"] = i_so_languages
        if language is not UNSET:
            field_dict["language"] = language
        if script is not UNSET:
            field_dict["script"] = script
        if unicode_locale_attributes is not UNSET:
            field_dict["unicodeLocaleAttributes"] = unicode_locale_attributes
        if unicode_locale_keys is not UNSET:
            field_dict["unicodeLocaleKeys"] = unicode_locale_keys
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _available_locales = d.pop("availableLocales", UNSET)
        available_locales: list[JavaUtilLocale] | Unset = UNSET
        if _available_locales is not UNSET:
            available_locales = []
            for available_locales_item_data in _available_locales:
                available_locales_item = JavaUtilLocale.from_dict(available_locales_item_data)

                available_locales.append(available_locales_item)

        country = d.pop("country", UNSET)

        _default = d.pop("default", UNSET)
        default: JavaUtilLocale | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = JavaUtilLocale.from_dict(_default)

        display_country = d.pop("displayCountry", UNSET)

        display_language = d.pop("displayLanguage", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_script = d.pop("displayScript", UNSET)

        display_variant = d.pop("displayVariant", UNSET)

        extension_keys = cast(list[str], d.pop("extensionKeys", UNSET))

        i_so3_country = d.pop("iSO3Country", UNSET)

        i_so3_language = d.pop("iSO3Language", UNSET)

        i_so_countries = cast(list[str], d.pop("iSOCountries", UNSET))

        i_so_languages = cast(list[str], d.pop("iSOLanguages", UNSET))

        language = d.pop("language", UNSET)

        script = d.pop("script", UNSET)

        unicode_locale_attributes = cast(list[str], d.pop("unicodeLocaleAttributes", UNSET))

        unicode_locale_keys = cast(list[str], d.pop("unicodeLocaleKeys", UNSET))

        variant = d.pop("variant", UNSET)

        java_util_locale = cls(
            available_locales=available_locales,
            country=country,
            default=default,
            display_country=display_country,
            display_language=display_language,
            display_name=display_name,
            display_script=display_script,
            display_variant=display_variant,
            extension_keys=extension_keys,
            i_so3_country=i_so3_country,
            i_so3_language=i_so3_language,
            i_so_countries=i_so_countries,
            i_so_languages=i_so_languages,
            language=language,
            script=script,
            unicode_locale_attributes=unicode_locale_attributes,
            unicode_locale_keys=unicode_locale_keys,
            variant=variant,
        )

        java_util_locale.additional_properties = d
        return java_util_locale

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
