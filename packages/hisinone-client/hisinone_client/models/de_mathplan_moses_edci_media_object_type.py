from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.de_mathplan_moses_edci_media_object_type_content_encoding import (
        DeMathplanMosesEdciMediaObjectTypeContentEncoding,
    )
    from ..models.de_mathplan_moses_edci_media_object_type_content_type import (
        DeMathplanMosesEdciMediaObjectTypeContentType,
    )
    from ..models.java_math_big_integer import JavaMathBigInteger


T = TypeVar("T", bound="DeMathplanMosesEdciMediaObjectType")


@_attrs_define
class DeMathplanMosesEdciMediaObjectType:
    """
    Attributes:
        content (list[int] | Unset):
        content_encoding (DeMathplanMosesEdciMediaObjectTypeContentEncoding | Unset):
        content_size (JavaMathBigInteger | Unset):
        content_type (DeMathplanMosesEdciMediaObjectTypeContentType | Unset):
        content_url (str | Unset):
        id (str | Unset):
    """

    content: list[int] | Unset = UNSET
    content_encoding: DeMathplanMosesEdciMediaObjectTypeContentEncoding | Unset = UNSET
    content_size: JavaMathBigInteger | Unset = UNSET
    content_type: DeMathplanMosesEdciMediaObjectTypeContentType | Unset = UNSET
    content_url: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        content: list[int] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content

        content_encoding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_encoding, Unset):
            content_encoding = self.content_encoding.to_dict()

        content_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_size, Unset):
            content_size = self.content_size.to_dict()

        content_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.to_dict()

        content_url = self.content_url

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if content_encoding is not UNSET:
            field_dict["contentEncoding"] = content_encoding
        if content_size is not UNSET:
            field_dict["contentSize"] = content_size
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if content_url is not UNSET:
            field_dict["contentUrl"] = content_url
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.de_mathplan_moses_edci_media_object_type_content_encoding import (
            DeMathplanMosesEdciMediaObjectTypeContentEncoding,  # noqa: PLC0415
        )
        from ..models.de_mathplan_moses_edci_media_object_type_content_type import (
            DeMathplanMosesEdciMediaObjectTypeContentType,  # noqa: PLC0415
        )
        from ..models.java_math_big_integer import JavaMathBigInteger  # noqa: PLC0415

        d = dict(src_dict)
        content = cast(list[int], d.pop("content", UNSET))

        _content_encoding = d.pop("contentEncoding", UNSET)
        content_encoding: DeMathplanMosesEdciMediaObjectTypeContentEncoding | Unset
        if isinstance(_content_encoding, Unset):
            content_encoding = UNSET
        else:
            content_encoding = DeMathplanMosesEdciMediaObjectTypeContentEncoding.from_dict(_content_encoding)

        _content_size = d.pop("contentSize", UNSET)
        content_size: JavaMathBigInteger | Unset
        if isinstance(_content_size, Unset):
            content_size = UNSET
        else:
            content_size = JavaMathBigInteger.from_dict(_content_size)

        _content_type = d.pop("contentType", UNSET)
        content_type: DeMathplanMosesEdciMediaObjectTypeContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = DeMathplanMosesEdciMediaObjectTypeContentType.from_dict(_content_type)

        content_url = d.pop("contentUrl", UNSET)

        id = d.pop("id", UNSET)

        de_mathplan_moses_edci_media_object_type = cls(
            content=content,
            content_encoding=content_encoding,
            content_size=content_size,
            content_type=content_type,
            content_url=content_url,
            id=id,
        )

        de_mathplan_moses_edci_media_object_type.additional_properties = d
        return de_mathplan_moses_edci_media_object_type

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
