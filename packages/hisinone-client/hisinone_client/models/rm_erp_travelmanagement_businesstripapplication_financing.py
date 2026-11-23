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
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_financialoperating_payment_partner import RmErpCommonFinancialoperatingPaymentPartner
    from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute
    from ..models.rm_erp_travelmanagement_businesstripapplication_financing_foreigntext import (
        RmErpTravelmanagementBusinesstripapplicationFinancingForeigntext,
    )


T = TypeVar("T", bound="RmErpTravelmanagementBusinesstripapplicationFinancing")


@_attrs_define
class RmErpTravelmanagementBusinesstripapplicationFinancing:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementBusinesstripapplicationFinancingForeigntext | Unset):
        account_info (RmErpCommonAccountAccountInfo | Unset):
        amount (float | Unset):
        amount_to_be_distributed (float | Unset):
        amount_to_be_distributed_in_percent (float | Unset):
        chapter (RmErpCommonAccountChapter | Unset):
        corporate_credit_card (RmErpCommonErpGenericValue | Unset):
        department (RmErpCommonAccountDepartment | Unset):
        description (str | Unset):
        erp_institute (RmErpCommonInstituteErpInstitute | Unset):
        expense_type (RmErpCommonAccountExpenseType | Unset):
        fiscalyear (str | Unset):
        id (int | Unset):
        institution_hierarchy_level_one (RmErpCommonAccountInstitutionHierarchyLevelOne | Unset):
        institution_hierarchy_level_three (RmErpCommonAccountInstitutionHierarchyLevelThree | Unset):
        institution_hierarchy_level_two (RmErpCommonAccountInstitutionHierarchyLevelTwo | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        payment_partner (RmErpCommonFinancialoperatingPaymentPartner | Unset):
        project (RmErpCommonAccountProject | Unset):
        serialversionuid (int | Unset):
        subtitle (RmErpCommonAccountSubtitle | Unset):
        title (RmErpCommonAccountTitle | Unset):
    """

    field_foreigntext: RmErpTravelmanagementBusinesstripapplicationFinancingForeigntext | Unset = UNSET
    account_info: RmErpCommonAccountAccountInfo | Unset = UNSET
    amount: float | Unset = UNSET
    amount_to_be_distributed: float | Unset = UNSET
    amount_to_be_distributed_in_percent: float | Unset = UNSET
    chapter: RmErpCommonAccountChapter | Unset = UNSET
    corporate_credit_card: RmErpCommonErpGenericValue | Unset = UNSET
    department: RmErpCommonAccountDepartment | Unset = UNSET
    description: str | Unset = UNSET
    erp_institute: RmErpCommonInstituteErpInstitute | Unset = UNSET
    expense_type: RmErpCommonAccountExpenseType | Unset = UNSET
    fiscalyear: str | Unset = UNSET
    id: int | Unset = UNSET
    institution_hierarchy_level_one: RmErpCommonAccountInstitutionHierarchyLevelOne | Unset = UNSET
    institution_hierarchy_level_three: RmErpCommonAccountInstitutionHierarchyLevelThree | Unset = UNSET
    institution_hierarchy_level_two: RmErpCommonAccountInstitutionHierarchyLevelTwo | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    payment_partner: RmErpCommonFinancialoperatingPaymentPartner | Unset = UNSET
    project: RmErpCommonAccountProject | Unset = UNSET
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

        amount_to_be_distributed = self.amount_to_be_distributed

        amount_to_be_distributed_in_percent = self.amount_to_be_distributed_in_percent

        chapter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chapter, Unset):
            chapter = self.chapter.to_dict()

        corporate_credit_card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.corporate_credit_card, Unset):
            corporate_credit_card = self.corporate_credit_card.to_dict()

        department: dict[str, Any] | Unset = UNSET
        if not isinstance(self.department, Unset):
            department = self.department.to_dict()

        description = self.description

        erp_institute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.erp_institute, Unset):
            erp_institute = self.erp_institute.to_dict()

        expense_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expense_type, Unset):
            expense_type = self.expense_type.to_dict()

        fiscalyear = self.fiscalyear

        id = self.id

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

        payment_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment_partner, Unset):
            payment_partner = self.payment_partner.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

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
        if amount_to_be_distributed is not UNSET:
            field_dict["amountToBeDistributed"] = amount_to_be_distributed
        if amount_to_be_distributed_in_percent is not UNSET:
            field_dict["amountToBeDistributedInPercent"] = amount_to_be_distributed_in_percent
        if chapter is not UNSET:
            field_dict["chapter"] = chapter
        if corporate_credit_card is not UNSET:
            field_dict["corporateCreditCard"] = corporate_credit_card
        if department is not UNSET:
            field_dict["department"] = department
        if description is not UNSET:
            field_dict["description"] = description
        if erp_institute is not UNSET:
            field_dict["erpInstitute"] = erp_institute
        if expense_type is not UNSET:
            field_dict["expenseType"] = expense_type
        if fiscalyear is not UNSET:
            field_dict["fiscalyear"] = fiscalyear
        if id is not UNSET:
            field_dict["id"] = id
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
        if payment_partner is not UNSET:
            field_dict["paymentPartner"] = payment_partner
        if project is not UNSET:
            field_dict["project"] = project
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
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_financialoperating_payment_partner import (
            RmErpCommonFinancialoperatingPaymentPartner,  # noqa: PLC0415
        )
        from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute  # noqa: PLC0415
        from ..models.rm_erp_travelmanagement_businesstripapplication_financing_foreigntext import (
            RmErpTravelmanagementBusinesstripapplicationFinancingForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTravelmanagementBusinesstripapplicationFinancingForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = RmErpTravelmanagementBusinesstripapplicationFinancingForeigntext.from_dict(
                _field_foreigntext
            )

        _account_info = d.pop("accountInfo", UNSET)
        account_info: RmErpCommonAccountAccountInfo | Unset
        if isinstance(_account_info, Unset):
            account_info = UNSET
        else:
            account_info = RmErpCommonAccountAccountInfo.from_dict(_account_info)

        amount = d.pop("amount", UNSET)

        amount_to_be_distributed = d.pop("amountToBeDistributed", UNSET)

        amount_to_be_distributed_in_percent = d.pop("amountToBeDistributedInPercent", UNSET)

        _chapter = d.pop("chapter", UNSET)
        chapter: RmErpCommonAccountChapter | Unset
        if isinstance(_chapter, Unset):
            chapter = UNSET
        else:
            chapter = RmErpCommonAccountChapter.from_dict(_chapter)

        _corporate_credit_card = d.pop("corporateCreditCard", UNSET)
        corporate_credit_card: RmErpCommonErpGenericValue | Unset
        if isinstance(_corporate_credit_card, Unset):
            corporate_credit_card = UNSET
        else:
            corporate_credit_card = RmErpCommonErpGenericValue.from_dict(_corporate_credit_card)

        _department = d.pop("department", UNSET)
        department: RmErpCommonAccountDepartment | Unset
        if isinstance(_department, Unset):
            department = UNSET
        else:
            department = RmErpCommonAccountDepartment.from_dict(_department)

        description = d.pop("description", UNSET)

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

        _payment_partner = d.pop("paymentPartner", UNSET)
        payment_partner: RmErpCommonFinancialoperatingPaymentPartner | Unset
        if isinstance(_payment_partner, Unset):
            payment_partner = UNSET
        else:
            payment_partner = RmErpCommonFinancialoperatingPaymentPartner.from_dict(_payment_partner)

        _project = d.pop("project", UNSET)
        project: RmErpCommonAccountProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = RmErpCommonAccountProject.from_dict(_project)

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

        rm_erp_travelmanagement_businesstripapplication_financing = cls(
            field_foreigntext=field_foreigntext,
            account_info=account_info,
            amount=amount,
            amount_to_be_distributed=amount_to_be_distributed,
            amount_to_be_distributed_in_percent=amount_to_be_distributed_in_percent,
            chapter=chapter,
            corporate_credit_card=corporate_credit_card,
            department=department,
            description=description,
            erp_institute=erp_institute,
            expense_type=expense_type,
            fiscalyear=fiscalyear,
            id=id,
            institution_hierarchy_level_one=institution_hierarchy_level_one,
            institution_hierarchy_level_three=institution_hierarchy_level_three,
            institution_hierarchy_level_two=institution_hierarchy_level_two,
            lock_version=lock_version,
            obj_guid=obj_guid,
            payment_partner=payment_partner,
            project=project,
            serialversionuid=serialversionuid,
            subtitle=subtitle,
            title=title,
        )

        rm_erp_travelmanagement_businesstripapplication_financing.additional_properties = d
        return rm_erp_travelmanagement_businesstripapplication_financing

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
