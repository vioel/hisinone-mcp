from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_travelmanagement_businesstripapplication_businesstrip_application import (
        RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication,
    )
    from ..models.rm_erp_travelmanagement_businesstripapplication_businesstrip_application_validation_foreigntext import (
        RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidationForeigntext,
    )


T = TypeVar("T", bound="RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidation")


@_attrs_define
class RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidation:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidationForeigntext |
            Unset):
        id (int | Unset):
        is_additional_meal_expenses_tax_free (bool | Unset):
        list_businesstrip_application_over_same_travel_period
            (list[RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication] | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
    """

    field_foreigntext: (
        RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidationForeigntext | Unset
    ) = UNSET
    id: int | Unset = UNSET
    is_additional_meal_expenses_tax_free: bool | Unset = UNSET
    list_businesstrip_application_over_same_travel_period: (
        list[RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication] | Unset
    ) = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        id = self.id

        is_additional_meal_expenses_tax_free = self.is_additional_meal_expenses_tax_free

        list_businesstrip_application_over_same_travel_period: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_businesstrip_application_over_same_travel_period, Unset):
            list_businesstrip_application_over_same_travel_period = []
            for (
                list_businesstrip_application_over_same_travel_period_item_data
            ) in self.list_businesstrip_application_over_same_travel_period:
                list_businesstrip_application_over_same_travel_period_item = (
                    list_businesstrip_application_over_same_travel_period_item_data.to_dict()
                )
                list_businesstrip_application_over_same_travel_period.append(
                    list_businesstrip_application_over_same_travel_period_item
                )

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if id is not UNSET:
            field_dict["id"] = id
        if is_additional_meal_expenses_tax_free is not UNSET:
            field_dict["isAdditionalMealExpensesTaxFree"] = is_additional_meal_expenses_tax_free
        if list_businesstrip_application_over_same_travel_period is not UNSET:
            field_dict["listBusinesstripApplicationOverSameTravelPeriod"] = (
                list_businesstrip_application_over_same_travel_period
            )
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_travelmanagement_businesstripapplication_businesstrip_application import (
            RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_businesstripapplication_businesstrip_application_validation_foreigntext import (
            RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidationForeigntext,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: (
            RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidationForeigntext | Unset
        )
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationValidationForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        id = d.pop("id", UNSET)

        is_additional_meal_expenses_tax_free = d.pop("isAdditionalMealExpensesTaxFree", UNSET)

        _list_businesstrip_application_over_same_travel_period = d.pop(
            "listBusinesstripApplicationOverSameTravelPeriod", UNSET
        )
        list_businesstrip_application_over_same_travel_period: (
            list[RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication] | Unset
        ) = UNSET
        if _list_businesstrip_application_over_same_travel_period is not UNSET:
            list_businesstrip_application_over_same_travel_period = []
            for (
                list_businesstrip_application_over_same_travel_period_item_data
            ) in _list_businesstrip_application_over_same_travel_period:
                list_businesstrip_application_over_same_travel_period_item = (
                    RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication.from_dict(
                        list_businesstrip_application_over_same_travel_period_item_data
                    )
                )

                list_businesstrip_application_over_same_travel_period.append(
                    list_businesstrip_application_over_same_travel_period_item
                )

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        rm_erp_travelmanagement_businesstripapplication_businesstrip_application_validation = cls(
            field_foreigntext=field_foreigntext,
            id=id,
            is_additional_meal_expenses_tax_free=is_additional_meal_expenses_tax_free,
            list_businesstrip_application_over_same_travel_period=list_businesstrip_application_over_same_travel_period,
            lock_version=lock_version,
            obj_guid=obj_guid,
        )

        rm_erp_travelmanagement_businesstripapplication_businesstrip_application_validation.additional_properties = d
        return rm_erp_travelmanagement_businesstripapplication_businesstrip_application_validation

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
