from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_research_infrastructure_simple_research_infrastructure_foreigntext_type_0 import (
        FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0,
    )


T = TypeVar("T", bound="FsResResearchInfrastructureSimpleResearchInfrastructure")


@_attrs_define
class FsResResearchInfrastructureSimpleResearchInfrastructure:
    """
    Attributes:
        field_foreigntext (FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0 | None | Unset):
        id (int | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        title (str | Unset):
    """

    field_foreigntext: FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0 | None | Unset = UNSET
    id: int | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_res_research_infrastructure_simple_research_infrastructure_foreigntext_type_0 import (
            FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(
            self.field_foreigntext, FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0
        ):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        id = self.id

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_research_infrastructure_simple_research_infrastructure_foreigntext_type_0 import (
            FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_field_foreigntext(
            data: object,
        ) -> FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = (
                FsResResearchInfrastructureSimpleResearchInfrastructureForeigntextType0.from_dict(
                    cast(dict[str, Any], data)
                )
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        title = d.pop("title", UNSET)

        fs_res_research_infrastructure_simple_research_infrastructure = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            lock_version=lock_version,
            obj_guid=obj_guid,
            title=title,
        )

        fs_res_research_infrastructure_simple_research_infrastructure.additional_properties = d
        return fs_res_research_infrastructure_simple_research_infrastructure

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
