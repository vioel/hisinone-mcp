from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType
    from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType


T = TypeVar("T", bound="DeMathplanMosesEdciImageObjectTypeContentType")


@_attrs_define
class DeMathplanMosesEdciImageObjectTypeContentType:
    """
    Attributes:
        description (str | Unset):
        target_description (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        target_framework_id (str | Unset):
        target_framework_name (list[DeMathplanMosesEdciLanguageStringType] | Unset):
        target_framework_spatial_id (str | Unset):
        target_framework_url (str | Unset):
        target_id (str | Unset):
        target_name (list[DeMathplanMosesEdciTextType] | Unset):
        target_notation (str | Unset):
        type_ (str | Unset):
        uri (str | Unset):
    """

    description: str | Unset = UNSET
    target_description: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    target_framework_id: str | Unset = UNSET
    target_framework_name: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
    target_framework_spatial_id: str | Unset = UNSET
    target_framework_url: str | Unset = UNSET
    target_id: str | Unset = UNSET
    target_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
    target_notation: str | Unset = UNSET
    type_: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        target_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_description, Unset):
            target_description = []
            for target_description_item_data in self.target_description:
                target_description_item = target_description_item_data.to_dict()
                target_description.append(target_description_item)

        target_framework_id = self.target_framework_id

        target_framework_name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_framework_name, Unset):
            target_framework_name = []
            for target_framework_name_item_data in self.target_framework_name:
                target_framework_name_item = target_framework_name_item_data.to_dict()
                target_framework_name.append(target_framework_name_item)

        target_framework_spatial_id = self.target_framework_spatial_id

        target_framework_url = self.target_framework_url

        target_id = self.target_id

        target_name: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_name, Unset):
            target_name = []
            for target_name_item_data in self.target_name:
                target_name_item = target_name_item_data.to_dict()
                target_name.append(target_name_item)

        target_notation = self.target_notation

        type_ = self.type_

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if target_description is not UNSET:
            field_dict["targetDescription"] = target_description
        if target_framework_id is not UNSET:
            field_dict["targetFrameworkID"] = target_framework_id
        if target_framework_name is not UNSET:
            field_dict["targetFrameworkName"] = target_framework_name
        if target_framework_spatial_id is not UNSET:
            field_dict["targetFrameworkSpatialID"] = target_framework_spatial_id
        if target_framework_url is not UNSET:
            field_dict["targetFrameworkUrl"] = target_framework_url
        if target_id is not UNSET:
            field_dict["targetID"] = target_id
        if target_name is not UNSET:
            field_dict["targetName"] = target_name
        if target_notation is not UNSET:
            field_dict["targetNotation"] = target_notation
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_language_string_type import DeMathplanMosesEdciLanguageStringType  # noqa: PLC0415
        from ..models.de_mathplan_moses_edci_text_type import DeMathplanMosesEdciTextType  # noqa: PLC0415

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _target_description = d.pop("targetDescription", UNSET)
        target_description: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _target_description is not UNSET:
            target_description = []
            for target_description_item_data in _target_description:
                target_description_item = DeMathplanMosesEdciLanguageStringType.from_dict(target_description_item_data)

                target_description.append(target_description_item)

        target_framework_id = d.pop("targetFrameworkID", UNSET)

        _target_framework_name = d.pop("targetFrameworkName", UNSET)
        target_framework_name: list[DeMathplanMosesEdciLanguageStringType] | Unset = UNSET
        if _target_framework_name is not UNSET:
            target_framework_name = []
            for target_framework_name_item_data in _target_framework_name:
                target_framework_name_item = DeMathplanMosesEdciLanguageStringType.from_dict(
                    target_framework_name_item_data
                )

                target_framework_name.append(target_framework_name_item)

        target_framework_spatial_id = d.pop("targetFrameworkSpatialID", UNSET)

        target_framework_url = d.pop("targetFrameworkUrl", UNSET)

        target_id = d.pop("targetID", UNSET)

        _target_name = d.pop("targetName", UNSET)
        target_name: list[DeMathplanMosesEdciTextType] | Unset = UNSET
        if _target_name is not UNSET:
            target_name = []
            for target_name_item_data in _target_name:
                target_name_item = DeMathplanMosesEdciTextType.from_dict(target_name_item_data)

                target_name.append(target_name_item)

        target_notation = d.pop("targetNotation", UNSET)

        type_ = d.pop("type", UNSET)

        uri = d.pop("uri", UNSET)

        de_mathplan_moses_edci_image_object_type_content_type = cls(
            description=description,
            target_description=target_description,
            target_framework_id=target_framework_id,
            target_framework_name=target_framework_name,
            target_framework_spatial_id=target_framework_spatial_id,
            target_framework_url=target_framework_url,
            target_id=target_id,
            target_name=target_name,
            target_notation=target_notation,
            type_=type_,
            uri=uri,
        )

        de_mathplan_moses_edci_image_object_type_content_type.additional_properties = d
        return de_mathplan_moses_edci_image_object_type_content_type

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
