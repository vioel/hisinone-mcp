from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_account_account_info import RmErpCommonAccountAccountInfo
    from ..models.rm_erp_common_account_chapter import RmErpCommonAccountChapter
    from ..models.rm_erp_common_account_department import RmErpCommonAccountDepartment
    from ..models.rm_erp_common_account_expense_type import RmErpCommonAccountExpenseType
    from ..models.rm_erp_common_account_institution_hierarchy_level_one import (
        RmErpCommonAccountInstitutionHierarchyLevelOne,
    )
    from ..models.rm_erp_common_account_institution_hierarchy_level_three import (
        RmErpCommonAccountInstitutionHierarchyLevelThree,
    )
    from ..models.rm_erp_common_account_institution_hierarchy_level_two import (
        RmErpCommonAccountInstitutionHierarchyLevelTwo,
    )
    from ..models.rm_erp_common_account_project import RmErpCommonAccountProject
    from ..models.rm_erp_common_account_subtitle import RmErpCommonAccountSubtitle
    from ..models.rm_erp_common_account_title import RmErpCommonAccountTitle
    from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute
    from ..models.rm_erp_procurement_requisition_financing_foreigntext import (
        RmErpProcurementRequisitionFinancingForeigntext,
    )


T = TypeVar("T", bound="RmErpProcurementRequisitionFinancing")


@_attrs_define
class RmErpProcurementRequisitionFinancing:
    """
    Attributes:
        field_foreigntext (RmErpProcurementRequisitionFinancingForeigntext | Unset):
        account_info (RmErpCommonAccountAccountInfo | Unset):
        amount (float | Unset):
        chapter (RmErpCommonAccountChapter | Unset):
        department (RmErpCommonAccountDepartment | Unset):
        erp_institute (RmErpCommonInstituteErpInstitute | Unset):
        expense_type (RmErpCommonAccountExpenseType | Unset):
        fiscalyear (str | Unset):
        id (int | Unset):
        imby_nr (str | Unset):
        institution_hierarchy_level_one (RmErpCommonAccountInstitutionHierarchyLevelOne | Unset):
        institution_hierarchy_level_three (RmErpCommonAccountInstitutionHierarchyLevelThree | Unset):
        institution_hierarchy_level_two (RmErpCommonAccountInstitutionHierarchyLevelTwo | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        position_id (int | Unset):
        project (RmErpCommonAccountProject | Unset):
        proportion (float | Unset):
        requisition_id (int | Unset):
        rest (str | Unset):
        serialversionuid (int | Unset):
        subtitle (RmErpCommonAccountSubtitle | Unset):
        title (RmErpCommonAccountTitle | Unset):
    """

    field_foreigntext: RmErpProcurementRequisitionFinancingForeigntext | Unset = UNSET
    account_info: RmErpCommonAccountAccountInfo | Unset = UNSET
    amount: float | Unset = UNSET
    chapter: RmErpCommonAccountChapter | Unset = UNSET
    department: RmErpCommonAccountDepartment | Unset = UNSET
    erp_institute: RmErpCommonInstituteErpInstitute | Unset = UNSET
    expense_type: RmErpCommonAccountExpenseType | Unset = UNSET
    fiscalyear: str | Unset = UNSET
    id: int | Unset = UNSET
    imby_nr: str | Unset = UNSET
    institution_hierarchy_level_one: RmErpCommonAccountInstitutionHierarchyLevelOne | Unset = UNSET
    institution_hierarchy_level_three: RmErpCommonAccountInstitutionHierarchyLevelThree | Unset = UNSET
    institution_hierarchy_level_two: RmErpCommonAccountInstitutionHierarchyLevelTwo | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    position_id: int | Unset = UNSET
    project: RmErpCommonAccountProject | Unset = UNSET
    proportion: float | Unset = UNSET
    requisition_id: int | Unset = UNSET
    rest: str | Unset = UNSET
    serialversionuid: int | Unset = UNSET
    subtitle: RmErpCommonAccountSubtitle | Unset = UNSET
    title: RmErpCommonAccountTitle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        account_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_info, Unset):
            account_info = self.account_info.to_dict()

        amount = self.amount

        chapter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chapter, Unset):
            chapter = self.chapter.to_dict()

        department: dict[str, Any] | Unset = UNSET
        if not isinstance(self.department, Unset):
            department = self.department.to_dict()

        erp_institute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.erp_institute, Unset):
            erp_institute = self.erp_institute.to_dict()

        expense_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expense_type, Unset):
            expense_type = self.expense_type.to_dict()

        fiscalyear = self.fiscalyear

        id = self.id

        imby_nr = self.imby_nr

        institution_hierarchy_level_one: dict[str, Any] | Unset = UNSET
        if not isinstance(self.institution_hierarchy_level_one, Unset):
            institution_hierarchy_level_one = self.institution_hierarchy_level_one.to_dict()

        institution_hierarchy_level_three: dict[str, Any] | Unset = UNSET
        if not isinstance(self.institution_hierarchy_level_three, Unset):
            institution_hierarchy_level_three = self.institution_hierarchy_level_three.to_dict()

        institution_hierarchy_level_two: dict[str, Any] | Unset = UNSET
        if not isinstance(self.institution_hierarchy_level_two, Unset):
            institution_hierarchy_level_two = self.institution_hierarchy_level_two.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        position_id = self.position_id

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        proportion = self.proportion

        requisition_id = self.requisition_id

        rest = self.rest

        serialversionuid = self.serialversionuid

        subtitle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subtitle, Unset):
            subtitle = self.subtitle.to_dict()

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if account_info is not UNSET:
            field_dict["accountInfo"] = account_info
        if amount is not UNSET:
            field_dict["amount"] = amount
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if department is not UNSET:
            field_dict["department"] = department
        if erp_institute is not UNSET:
            field_dict["erpInstitute"] = erp_institute
        if expense_type is not UNSET:
            field_dict["expenseType"] = expense_type
        if fiscalyear is not UNSET:
            field_dict["fiscalyear"] = fiscalyear
        if id is not UNSET:
            field_dict["id"] = id
        if imby_nr is not UNSET:
            field_dict["imbyNr"] = imby_nr
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
        if position_id is not UNSET:
            field_dict["positionId"] = position_id
        if project is not UNSET:
            field_dict["project"] = project
        if proportion is not UNSET:
            field_dict["proportion"] = proportion
        if requisition_id is not UNSET:
            field_dict["requisitionId"] = requisition_id
        if rest is not UNSET:
            field_dict["rest"] = rest
        if serialversionuid is not UNSET:
            field_dict["serialversionuid"] = serialversionuid
        if subtitle is not UNSET:
            field_dict["subtitle"] = subtitle
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_account_account_info import RmErpCommonAccountAccountInfo  # noqa: PLC0415
        from ..models.rm_erp_common_account_chapter import RmErpCommonAccountChapter  # noqa: PLC0415
        from ..models.rm_erp_common_account_department import RmErpCommonAccountDepartment  # noqa: PLC0415
        from ..models.rm_erp_common_account_expense_type import RmErpCommonAccountExpenseType  # noqa: PLC0415
        from ..models.rm_erp_common_account_institution_hierarchy_level_one import (
            RmErpCommonAccountInstitutionHierarchyLevelOne,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_account_institution_hierarchy_level_three import (
            RmErpCommonAccountInstitutionHierarchyLevelThree,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_account_institution_hierarchy_level_two import (
            RmErpCommonAccountInstitutionHierarchyLevelTwo,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_account_project import RmErpCommonAccountProject  # noqa: PLC0415
        from ..models.rm_erp_common_account_subtitle import RmErpCommonAccountSubtitle  # noqa: PLC0415
        from ..models.rm_erp_common_account_title import RmErpCommonAccountTitle  # noqa: PLC0415
        from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute  # noqa: PLC0415
        from ..models.rm_erp_procurement_requisition_financing_foreigntext import (
            RmErpProcurementRequisitionFinancingForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpProcurementRequisitionFinancingForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpProcurementRequisitionFinancingForeigntext.from_dict(_field_foreigntext)

        _account_info = d.pop("accountInfo", UNSET)
        account_info: RmErpCommonAccountAccountInfo | Unset
        if isinstance(_account_info, Unset):
            account_info = UNSET
        else:
            account_info = RmErpCommonAccountAccountInfo.from_dict(_account_info)

        amount = d.pop("amount", UNSET)

        _chapter = d.pop("chapter", UNSET)
        chapter: RmErpCommonAccountChapter | Unset
        if isinstance(_chapter, Unset):
            chapter = UNSET
        else:
            chapter = RmErpCommonAccountChapter.from_dict(_chapter)

        _department = d.pop("department", UNSET)
        department: RmErpCommonAccountDepartment | Unset
        if isinstance(_department, Unset):
            department = UNSET
        else:
            department = RmErpCommonAccountDepartment.from_dict(_department)

        _erp_institute = d.pop("erpInstitute", UNSET)
        erp_institute: RmErpCommonInstituteErpInstitute | Unset
        if isinstance(_erp_institute, Unset):
            erp_institute = UNSET
        else:
            erp_institute = RmErpCommonInstituteErpInstitute.from_dict(_erp_institute)

        _expense_type = d.pop("expenseType", UNSET)
        expense_type: RmErpCommonAccountExpenseType | Unset
        if isinstance(_expense_type, Unset):
            expense_type = UNSET
        else:
            expense_type = RmErpCommonAccountExpenseType.from_dict(_expense_type)

        fiscalyear = d.pop("fiscalyear", UNSET)

        id = d.pop("id", UNSET)

        imby_nr = d.pop("imbyNr", UNSET)

        _institution_hierarchy_level_one = d.pop("institutionHierarchyLevelOne", UNSET)
        institution_hierarchy_level_one: RmErpCommonAccountInstitutionHierarchyLevelOne | Unset
        if isinstance(_institution_hierarchy_level_one, Unset):
            institution_hierarchy_level_one = UNSET
        else:
            institution_hierarchy_level_one = RmErpCommonAccountInstitutionHierarchyLevelOne.from_dict(
                _institution_hierarchy_level_one
            )

        _institution_hierarchy_level_three = d.pop("institutionHierarchyLevelThree", UNSET)
        institution_hierarchy_level_three: RmErpCommonAccountInstitutionHierarchyLevelThree | Unset
        if isinstance(_institution_hierarchy_level_three, Unset):
            institution_hierarchy_level_three = UNSET
        else:
            institution_hierarchy_level_three = RmErpCommonAccountInstitutionHierarchyLevelThree.from_dict(
                _institution_hierarchy_level_three
            )

        _institution_hierarchy_level_two = d.pop("institutionHierarchyLevelTwo", UNSET)
        institution_hierarchy_level_two: RmErpCommonAccountInstitutionHierarchyLevelTwo | Unset
        if isinstance(_institution_hierarchy_level_two, Unset):
            institution_hierarchy_level_two = UNSET
        else:
            institution_hierarchy_level_two = RmErpCommonAccountInstitutionHierarchyLevelTwo.from_dict(
                _institution_hierarchy_level_two
            )

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        position_id = d.pop("positionId", UNSET)

        _project = d.pop("project", UNSET)
        project: RmErpCommonAccountProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = RmErpCommonAccountProject.from_dict(_project)

        proportion = d.pop("proportion", UNSET)

        requisition_id = d.pop("requisitionId", UNSET)

        rest = d.pop("rest", UNSET)

        serialversionuid = d.pop("serialversionuid", UNSET)

        _subtitle = d.pop("subtitle", UNSET)
        subtitle: RmErpCommonAccountSubtitle | Unset
        if isinstance(_subtitle, Unset):
            subtitle = UNSET
        else:
            subtitle = RmErpCommonAccountSubtitle.from_dict(_subtitle)

        _title = d.pop("title", UNSET)
        title: RmErpCommonAccountTitle | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = RmErpCommonAccountTitle.from_dict(_title)

        rm_erp_procurement_requisition_financing = cls(
            field_foreigntext=field_foreigntext,
            account_info=account_info,
            amount=amount,
            chapter=chapter,
            department=department,
            erp_institute=erp_institute,
            expense_type=expense_type,
            fiscalyear=fiscalyear,
            id=id,
            imby_nr=imby_nr,
            institution_hierarchy_level_one=institution_hierarchy_level_one,
            institution_hierarchy_level_three=institution_hierarchy_level_three,
            institution_hierarchy_level_two=institution_hierarchy_level_two,
            lock_version=lock_version,
            obj_guid=obj_guid,
            position_id=position_id,
            project=project,
            proportion=proportion,
            requisition_id=requisition_id,
            rest=rest,
            serialversionuid=serialversionuid,
            subtitle=subtitle,
            title=title,
        )

        rm_erp_procurement_requisition_financing.additional_properties = d
        return rm_erp_procurement_requisition_financing

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
