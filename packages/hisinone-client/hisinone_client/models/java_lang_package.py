from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.java_lang_annotation_annotation import JavaLangAnnotationAnnotation


T = TypeVar("T", bound="JavaLangPackage")


@_attrs_define
class JavaLangPackage:
    """
    Attributes:
        annotations (list[JavaLangAnnotationAnnotation] | Unset):
        declared_annotations (list[JavaLangAnnotationAnnotation] | Unset):
        implementation_title (str | Unset):
        implementation_vendor (str | Unset):
        implementation_version (str | Unset):
        name (str | Unset):
        packages (list[JavaLangPackage] | Unset):
        sealed (bool | Unset):
        specification_title (str | Unset):
        specification_vendor (str | Unset):
        specification_version (str | Unset):
    """

    annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
    declared_annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
    implementation_title: str | Unset = UNSET
    implementation_vendor: str | Unset = UNSET
    implementation_version: str | Unset = UNSET
    name: str | Unset = UNSET
    packages: list[JavaLangPackage] | Unset = UNSET
    sealed: bool | Unset = UNSET
    specification_title: str | Unset = UNSET
    specification_vendor: str | Unset = UNSET
    specification_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()
                annotations.append(annotations_item)

        declared_annotations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.declared_annotations, Unset):
            declared_annotations = []
            for declared_annotations_item_data in self.declared_annotations:
                declared_annotations_item = declared_annotations_item_data.to_dict()
                declared_annotations.append(declared_annotations_item)

        implementation_title = self.implementation_title

        implementation_vendor = self.implementation_vendor

        implementation_version = self.implementation_version

        name = self.name

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        sealed = self.sealed

        specification_title = self.specification_title

        specification_vendor = self.specification_vendor

        specification_version = self.specification_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if declared_annotations is not UNSET:
            field_dict["declaredAnnotations"] = declared_annotations
        if implementation_title is not UNSET:
            field_dict["implementationTitle"] = implementation_title
        if implementation_vendor is not UNSET:
            field_dict["implementationVendor"] = implementation_vendor
        if implementation_version is not UNSET:
            field_dict["implementationVersion"] = implementation_version
        if name is not UNSET:
            field_dict["name"] = name
        if packages is not UNSET:
            field_dict["packages"] = packages
        if sealed is not UNSET:
            field_dict["sealed"] = sealed
        if specification_title is not UNSET:
            field_dict["specificationTitle"] = specification_title
        if specification_vendor is not UNSET:
            field_dict["specificationVendor"] = specification_vendor
        if specification_version is not UNSET:
            field_dict["specificationVersion"] = specification_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.java_lang_annotation_annotation import JavaLangAnnotationAnnotation  # noqa: PLC0415

        d = dict(src_dict)
        _annotations = d.pop("annotations", UNSET)
        annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
        if _annotations is not UNSET:
            annotations = []
            for annotations_item_data in _annotations:
                annotations_item = JavaLangAnnotationAnnotation.from_dict(annotations_item_data)

                annotations.append(annotations_item)

        _declared_annotations = d.pop("declaredAnnotations", UNSET)
        declared_annotations: list[JavaLangAnnotationAnnotation] | Unset = UNSET
        if _declared_annotations is not UNSET:
            declared_annotations = []
            for declared_annotations_item_data in _declared_annotations:
                declared_annotations_item = JavaLangAnnotationAnnotation.from_dict(declared_annotations_item_data)

                declared_annotations.append(declared_annotations_item)

        implementation_title = d.pop("implementationTitle", UNSET)

        implementation_vendor = d.pop("implementationVendor", UNSET)

        implementation_version = d.pop("implementationVersion", UNSET)

        name = d.pop("name", UNSET)

        _packages = d.pop("packages", UNSET)
        packages: list[JavaLangPackage] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = JavaLangPackage.from_dict(packages_item_data)

                packages.append(packages_item)

        sealed = d.pop("sealed", UNSET)

        specification_title = d.pop("specificationTitle", UNSET)

        specification_vendor = d.pop("specificationVendor", UNSET)

        specification_version = d.pop("specificationVersion", UNSET)

        java_lang_package = cls(
            annotations=annotations,
            declared_annotations=declared_annotations,
            implementation_title=implementation_title,
            implementation_vendor=implementation_vendor,
            implementation_version=implementation_version,
            name=name,
            packages=packages,
            sealed=sealed,
            specification_title=specification_title,
            specification_vendor=specification_vendor,
            specification_version=specification_version,
        )

        java_lang_package.additional_properties = d
        return java_lang_package

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
