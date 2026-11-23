from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_module import JavaLangModule
    from ..models.java_lang_package import JavaLangPackage


T = TypeVar("T", bound="JavaLangClassLoader")


@_attrs_define
class JavaLangClassLoader:
    """
    Attributes:
        defined_packages (list[JavaLangPackage] | Unset):
        name (str | Unset):
        parent (JavaLangClassLoader | Unset):
        platform_class_loader (JavaLangClassLoader | Unset):
        registered_as_parallel_capable (bool | Unset):
        system_class_loader (JavaLangClassLoader | Unset):
        unnamed_module (JavaLangModule | Unset):
    """

    defined_packages: list[JavaLangPackage] | Unset = UNSET
    name: str | Unset = UNSET
    parent: JavaLangClassLoader | Unset = UNSET
    platform_class_loader: JavaLangClassLoader | Unset = UNSET
    registered_as_parallel_capable: bool | Unset = UNSET
    system_class_loader: JavaLangClassLoader | Unset = UNSET
    unnamed_module: JavaLangModule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        defined_packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.defined_packages, Unset):
            defined_packages = []
            for defined_packages_item_data in self.defined_packages:
                defined_packages_item = defined_packages_item_data.to_dict()
                defined_packages.append(defined_packages_item)

        name = self.name

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        platform_class_loader: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_class_loader, Unset):
            platform_class_loader = self.platform_class_loader.to_dict()

        registered_as_parallel_capable = self.registered_as_parallel_capable

        system_class_loader: dict[str, Any] | Unset = UNSET
        if not isinstance(self.system_class_loader, Unset):
            system_class_loader = self.system_class_loader.to_dict()

        unnamed_module: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unnamed_module, Unset):
            unnamed_module = self.unnamed_module.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defined_packages is not UNSET:
            field_dict["definedPackages"] = defined_packages
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if platform_class_loader is not UNSET:
            field_dict["platformClassLoader"] = platform_class_loader
        if registered_as_parallel_capable is not UNSET:
            field_dict["registeredAsParallelCapable"] = registered_as_parallel_capable
        if system_class_loader is not UNSET:
            field_dict["systemClassLoader"] = system_class_loader
        if unnamed_module is not UNSET:
            field_dict["unnamedModule"] = unnamed_module

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_module import JavaLangModule  # noqa: PLC0415
        from ..models.java_lang_package import JavaLangPackage  # noqa: PLC0415

        d = dict(src_dict)
        _defined_packages = d.pop("definedPackages", UNSET)
        defined_packages: list[JavaLangPackage] | Unset = UNSET
        if _defined_packages is not UNSET:
            defined_packages = []
            for defined_packages_item_data in _defined_packages:
                defined_packages_item = JavaLangPackage.from_dict(defined_packages_item_data)

                defined_packages.append(defined_packages_item)

        name = d.pop("name", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: JavaLangClassLoader | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = JavaLangClassLoader.from_dict(_parent)

        _platform_class_loader = d.pop("platformClassLoader", UNSET)
        platform_class_loader: JavaLangClassLoader | Unset
        if isinstance(_platform_class_loader, Unset):
            platform_class_loader = UNSET
        else:
            platform_class_loader = JavaLangClassLoader.from_dict(_platform_class_loader)

        registered_as_parallel_capable = d.pop("registeredAsParallelCapable", UNSET)

        _system_class_loader = d.pop("systemClassLoader", UNSET)
        system_class_loader: JavaLangClassLoader | Unset
        if isinstance(_system_class_loader, Unset):
            system_class_loader = UNSET
        else:
            system_class_loader = JavaLangClassLoader.from_dict(_system_class_loader)

        _unnamed_module = d.pop("unnamedModule", UNSET)
        unnamed_module: JavaLangModule | Unset
        if isinstance(_unnamed_module, Unset):
            unnamed_module = UNSET
        else:
            unnamed_module = JavaLangModule.from_dict(_unnamed_module)

        java_lang_class_loader = cls(
            defined_packages=defined_packages,
            name=name,
            parent=parent,
            platform_class_loader=platform_class_loader,
            registered_as_parallel_capable=registered_as_parallel_capable,
            system_class_loader=system_class_loader,
            unnamed_module=unnamed_module,
        )

        java_lang_class_loader.additional_properties = d
        return java_lang_class_loader

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
