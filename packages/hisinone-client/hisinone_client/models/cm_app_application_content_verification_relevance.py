from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_object import JavaLangObject


T = TypeVar("T", bound="CmAppApplicationContentVerificationRelevance")


@_attrs_define
class CmAppApplicationContentVerificationRelevance:
    """
    Attributes:
        declaring_class (Any | Unset):
        i_18_n_key (str | Unset):
        key (JavaLangObject | Unset):
    """

    declaring_class: Any | Unset = UNSET
    i_18_n_key: str | Unset = UNSET
    key: JavaLangObject | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        declaring_class = self.declaring_class

        i_18_n_key = self.i_18_n_key

        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if declaring_class is not UNSET:
            field_dict["declaringClass"] = declaring_class
        if i_18_n_key is not UNSET:
            field_dict["i18nKey"] = i_18_n_key
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_object import JavaLangObject  # noqa: PLC0415

        d = dict(src_dict)
        declaring_class = d.pop("declaringClass", UNSET)

        i_18_n_key = d.pop("i18nKey", UNSET)

        _key = d.pop("key", UNSET)
        key: JavaLangObject | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = JavaLangObject.from_dict(_key)

        cm_app_application_content_verification_relevance = cls(
            declaring_class=declaring_class,
            i_18_n_key=i_18_n_key,
            key=key,
        )

        cm_app_application_content_verification_relevance.additional_properties = d
        return cm_app_application_content_verification_relevance

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
