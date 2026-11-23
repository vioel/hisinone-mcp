from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_net_uri import JavaNetURI
    from ..models.java_net_url import JavaNetURL


T = TypeVar("T", bound="OrgSpringframeworkCoreIoResource")


@_attrs_define
class OrgSpringframeworkCoreIoResource:
    """
    Attributes:
        description (str | Unset):
        file (bool | Unset):
        filename (str | Unset):
        open_ (bool | Unset):
        readable (bool | Unset):
        u_ri (JavaNetURI | Unset):
        u_rl (JavaNetURL | Unset):
    """

    description: str | Unset = UNSET
    file: bool | Unset = UNSET
    filename: str | Unset = UNSET
    open_: bool | Unset = UNSET
    readable: bool | Unset = UNSET
    u_ri: JavaNetURI | Unset = UNSET
    u_rl: JavaNetURL | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        file = self.file

        filename = self.filename

        open_ = self.open_

        readable = self.readable

        u_ri: dict[str, Any] | Unset = UNSET
        if not isinstance(self.u_ri, Unset):
            u_ri = self.u_ri.to_dict()

        u_rl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.u_rl, Unset):
            u_rl = self.u_rl.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if file is not UNSET:
            field_dict["file"] = file
        if filename is not UNSET:
            field_dict["filename"] = filename
        if open_ is not UNSET:
            field_dict["open"] = open_
        if readable is not UNSET:
            field_dict["readable"] = readable
        if u_ri is not UNSET:
            field_dict["uRI"] = u_ri
        if u_rl is not UNSET:
            field_dict["uRL"] = u_rl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_net_uri import JavaNetURI  # noqa: PLC0415
        from ..models.java_net_url import JavaNetURL  # noqa: PLC0415

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        file = d.pop("file", UNSET)

        filename = d.pop("filename", UNSET)

        open_ = d.pop("open", UNSET)

        readable = d.pop("readable", UNSET)

        _u_ri = d.pop("uRI", UNSET)
        u_ri: JavaNetURI | Unset
        if isinstance(_u_ri, Unset):
            u_ri = UNSET
        else:
            u_ri = JavaNetURI.from_dict(_u_ri)

        _u_rl = d.pop("uRL", UNSET)
        u_rl: JavaNetURL | Unset
        if isinstance(_u_rl, Unset):
            u_rl = UNSET
        else:
            u_rl = JavaNetURL.from_dict(_u_rl)

        org_springframework_core_io_resource = cls(
            description=description,
            file=file,
            filename=filename,
            open_=open_,
            readable=readable,
            u_ri=u_ri,
            u_rl=u_rl,
        )

        org_springframework_core_io_resource.additional_properties = d
        return org_springframework_core_io_resource

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
