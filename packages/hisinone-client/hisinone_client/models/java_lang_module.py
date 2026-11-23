from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_annotation_annotation import JavaLangAnnotationAnnotation
    from ..models.java_lang_class_loader import JavaLangClassLoader
    from ..models.java_lang_module_layer import JavaLangModuleLayer
    from ..models.java_lang_module_module_descriptor import JavaLangModuleModuleDescriptor


T = TypeVar("T", bound="JavaLangModule")


@_attrs_define
class JavaLangModule:
    """
    Attributes:
        annotations (list[JavaLangAnnotationAnnotation] | Unset):
        class_loader (JavaLangClassLoader | Unset):
        declared_annotations (list[JavaLangAnnotationAnnotation] | Unset):
        descriptor (JavaLangModuleModuleDescriptor | Unset):
        layer (JavaLangModuleLayer | Unset):
        name (str | Unset):
        named (bool | Unset):
        packages (list[str] | Unset):
    """

    annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
    class_loader: JavaLangClassLoader | Unset = UNSET
    declared_annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
    descriptor: JavaLangModuleModuleDescriptor | Unset = UNSET
    layer: JavaLangModuleLayer | Unset = UNSET
    name: str | Unset = UNSET
    named: bool | Unset = UNSET
    packages: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        class_loader: dict[str, Any] | Unset = UNSET
        if not isinstance(self.class_loader, Unset):
            class_loader = self.class_loader.to_dict()

        declared_annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.declared_annotations, Unset):
            declared_annotations = []
            for declared_annotations_item_data in self.declared_annotations:
                declared_annotations_item = declared_annotations_item_data.to_dict()
                declared_annotations.append(declared_annotations_item)

        descriptor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor, Unset):
            descriptor = self.descriptor.to_dict()

        layer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.layer, Unset):
            layer = self.layer.to_dict()

        name = self.name

        named = self.named

        packages: list[str] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = self.packages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if class_loader is not UNSET:
            field_dict["classLoader"] = class_loader
        if declared_annotations is not UNSET:
            field_dict["declaredAnnotations"] = declared_annotations
        if descriptor is not UNSET:
            field_dict["descriptor"] = descriptor
        if layer is not UNSET:
            field_dict["layer"] = layer
        if name is not UNSET:
            field_dict["name"] = name
        if named is not UNSET:
            field_dict["named"] = named
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_annotation_annotation import JavaLangAnnotationAnnotation  # noqa: PLC0415
        from ..models.java_lang_class_loader import JavaLangClassLoader  # noqa: PLC0415
        from ..models.java_lang_module_layer import JavaLangModuleLayer  # noqa: PLC0415
        from ..models.java_lang_module_module_descriptor import JavaLangModuleModuleDescriptor  # noqa: PLC0415

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
        if _annotations is not UNSET:
            annotations = []
            for annotations_item_data in _annotations:
                annotations_item = JavaLangAnnotationAnnotation.from_dict(annotations_item_data)

                annotations.append(annotations_item)

        _class_loader = d.pop("classLoader", UNSET)
        class_loader: JavaLangClassLoader | Unset
        if isinstance(_class_loader, Unset):
            class_loader = UNSET
        else:
            class_loader = JavaLangClassLoader.from_dict(_class_loader)

        _declared_annotations = d.pop("declaredAnnotations", UNSET)
        declared_annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
        if _declared_annotations is not UNSET:
            declared_annotations = []
            for declared_annotations_item_data in _declared_annotations:
                declared_annotations_item = JavaLangAnnotationAnnotation.from_dict(declared_annotations_item_data)

                declared_annotations.append(declared_annotations_item)

        _descriptor = d.pop("descriptor", UNSET)
        descriptor: JavaLangModuleModuleDescriptor | Unset
        if isinstance(_descriptor, Unset):
            descriptor = UNSET
        else:
            descriptor = JavaLangModuleModuleDescriptor.from_dict(_descriptor)

        _layer = d.pop("layer", UNSET)
        layer: JavaLangModuleLayer | Unset
        if isinstance(_layer, Unset):
            layer = UNSET
        else:
            layer = JavaLangModuleLayer.from_dict(_layer)

        name = d.pop("name", UNSET)

        named = d.pop("named", UNSET)

        packages = cast(list[str], d.pop("packages", UNSET))

        java_lang_module = cls(
            annotations=annotations,
            class_loader=class_loader,
            declared_annotations=declared_annotations,
            descriptor=descriptor,
            layer=layer,
            name=name,
            named=named,
            packages=packages,
        )

        java_lang_module.additional_properties = d
        return java_lang_module

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
