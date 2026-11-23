from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_account_info_foreigntext import RmErpCommonAccountAccountInfoForeigntext


T = TypeVar("T", bound="RmErpCommonAccountAccountInfo")


@_attrs_define
class RmErpCommonAccountAccountInfo:
    """
    Attributes:
        field_foreigntext (RmErpCommonAccountAccountInfoForeigntext | Unset):
        chapter (str | Unset):
        department (str | Unset):
        expense_type (str | Unset):
        fiscal_year (str | Unset):
        id (int | Unset):
        institute (str | Unset):
        institution_hierarchy_level_one (str | Unset):
        institution_hierarchy_level_three (str | Unset):
        institution_hierarchy_level_two (str | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        project (str | Unset):
        subtitle (str | Unset):
        title (str | Unset):
    """

    field_foreigntext: RmErpCommonAccountAccountInfoForeigntext | Unset = UNSET
    chapter: str | Unset = UNSET
    department: str | Unset = UNSET
    expense_type: str | Unset = UNSET
    fiscal_year: str | Unset = UNSET
    id: int | Unset = UNSET
    institute: str | Unset = UNSET
    institution_hierarchy_level_one: str | Unset = UNSET
    institution_hierarchy_level_three: str | Unset = UNSET
    institution_hierarchy_level_two: str | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    project: str | Unset = UNSET
    subtitle: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        chapter = self.chapter

        department = self.department

        expense_type = self.expense_type

        fiscal_year = self.fiscal_year

        id = self.id

        institute = self.institute

        institution_hierarchy_level_one = self.institution_hierarchy_level_one

        institution_hierarchy_level_three = self.institution_hierarchy_level_three

        institution_hierarchy_level_two = self.institution_hierarchy_level_two

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        project = self.project

        subtitle = self.subtitle

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if department is not UNSET:
            field_dict["department"] = department
        if expense_type is not UNSET:
            field_dict["expenseType"] = expense_type
        if fiscal_year is not UNSET:
            field_dict["fiscalYear"] = fiscal_year
        if id is not UNSET:
            field_dict["id"] = id
        if institute is not UNSET:
            field_dict["institute"] = institute
        if institution_hierarchy_level_one is not UNSET:
            field_dict["institutionHierarchyLevelOne"] = institution_hierarchy_level_one
        if institution_hierarchy_level_three is not UNSET:
            field_dict["institutionHierarchyLevelThree"] = institution_hierarchy_level_three
        if institution_hierarchy_level_two is not UNSET:
            field_dict["institutionHierarchyLevelTwo"] = institution_hierarchy_level_two
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if project is not UNSET:
            field_dict["project"] = project
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_account_info_foreigntext import RmErpCommonAccountAccountInfoForeigntext  # noqa: PLC0415

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpCommonAccountAccountInfoForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpCommonAccountAccountInfoForeigntext.from_dict(_field_foreigntext)

        chapter = d.pop("chapter", UNSET)

        department = d.pop("department", UNSET)

        expense_type = d.pop("expenseType", UNSET)

        fiscal_year = d.pop("fiscalYear", UNSET)

        id = d.pop("id", UNSET)

        institute = d.pop("institute", UNSET)

        institution_hierarchy_level_one = d.pop("institutionHierarchyLevelOne", UNSET)

        institution_hierarchy_level_three = d.pop("institutionHierarchyLevelThree", UNSET)

        institution_hierarchy_level_two = d.pop("institutionHierarchyLevelTwo", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        project = d.pop("project", UNSET)

        subtitle = d.pop("subtitle", UNSET)

        title = d.pop("title", UNSET)

        rm_erp_common_account_account_info = cls(
            field_foreigntext=field_foreigntext,
            chapter=chapter,
            department=department,
            expense_type=expense_type,
            fiscal_year=fiscal_year,
            id=id,
            institute=institute,
            institution_hierarchy_level_one=institution_hierarchy_level_one,
            institution_hierarchy_level_three=institution_hierarchy_level_three,
            institution_hierarchy_level_two=institution_hierarchy_level_two,
            lock_version=lock_version,
            obj_guid=obj_guid,
            project=project,
            subtitle=subtitle,
            title=title,
        )

        rm_erp_common_account_account_info.additional_properties = d
        return rm_erp_common_account_account_info

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
