from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rm_erp_common_document_document import RmErpCommonDocumentDocument
    from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue
    from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute
    from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue
    from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData
    from ..models.rm_erp_travelmanagement_businesstripapplication_assets import (
        RmErpTravelmanagementBusinesstripapplicationAssets,
    )
    from ..models.rm_erp_travelmanagement_businesstripapplication_businesstrip_application_foreigntext import (
        RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationForeigntext,
    )
    from ..models.rm_erp_travelmanagement_businesstripapplication_financing import (
        RmErpTravelmanagementBusinesstripapplicationFinancing,
    )
    from ..models.rm_erp_travelmanagement_businesstripapplication_travel_abroad import (
        RmErpTravelmanagementBusinesstripapplicationTravelAbroad,
    )
    from ..models.rm_erp_travelmanagement_businesstripapplication_travel_itinerary import (
        RmErpTravelmanagementBusinesstripapplicationTravelItinerary,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_arrival_value import RmErpTravelmanagementSharedErpArrivalValue
    from ..models.rm_erp_travelmanagement_shared_erp_billingbasis_value import (
        RmErpTravelmanagementSharedErpBillingbasisValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_health_insurance_value import (
        RmErpTravelmanagementSharedErpHealthInsuranceValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_return_trip_value import (
        RmErpTravelmanagementSharedErpReturnTripValue,
    )
    from ..models.rm_erp_travelmanagement_shared_erp_travel_management_notes_value import (
        RmErpTravelmanagementSharedErpTravelManagementNotesValue,
    )


T = TypeVar("T", bound="RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication")


@_attrs_define
class RmErpTravelmanagementBusinesstripapplicationBusinesstripApplication:
    """
    Attributes:
        field_foreigntext (RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationForeigntext | Unset):
        accident_care (RmErpCommonErpGenericValue | Unset):
        accommodation_expenses (float | Unset):
        account_bic (str | Unset):
        account_iban (str | Unset):
        address_travel_destination (str | Unset):
        application_date (int | Unset):
        application_related_person (RmErpCommonPersonPersonBasicDataCoreData | Unset):
        application_related_person_id (int | Unset):
        arrival_selected (RmErpTravelmanagementSharedErpArrivalValue | Unset):
        assets (RmErpTravelmanagementBusinesstripapplicationAssets | Unset):
        availability_freetext (str | Unset):
        billingbasis_selected (RmErpTravelmanagementSharedErpBillingbasisValue | Unset):
        business_begin_date (int | Unset):
        business_end_date (int | Unset):
        businesstrip_application_identifier (int | Unset):
        change_account_new_bic (str | Unset):
        change_account_new_iban (str | Unset):
        change_bank_details (RmErpCommonErpGenericValue | Unset):
        conference_fee (float | Unset):
        costs_higher_staedtekatalog (RmErpCommonErpGenericValue | Unset):
        country (str | Unset):
        country_selected (RmErpCommonPersonErpCountryValue | Unset):
        destination (str | Unset):
        destination_details (str | Unset):
        destination_freetext (str | Unset):
        destinations_of_the_last_years (str | Unset):
        documents (list[RmErpCommonDocumentDocument] | Unset):
        forego_accommodation_allowance (RmErpCommonErpGenericValue | Unset):
        forego_daily_allowance (RmErpCommonErpGenericValue | Unset):
        forego_participation_fees (RmErpCommonErpGenericValue | Unset):
        forego_travel_costs (RmErpCommonErpGenericValue | Unset):
        full_reimbursement (RmErpCommonErpGenericValue | Unset):
        health_insurance_selected (RmErpTravelmanagementSharedErpHealthInsuranceValue | Unset):
        id (int | Unset):
        institute_first_selected (RmErpCommonInstituteErpInstitute | Unset):
        institute_second_selected (RmErpCommonInstituteErpInstitute | Unset):
        is_foreign_country (bool | Unset):
        is_private_trip (RmErpCommonErpGenericValue | Unset):
        large_mileage_allowance (RmErpCommonErpGenericValue | Unset):
        large_mileage_allowance_explanation (str | Unset):
        list_financing (list[RmErpTravelmanagementBusinesstripapplicationFinancing] | Unset):
        list_travel_abroad (list[RmErpTravelmanagementBusinesstripapplicationTravelAbroad] | Unset):
        list_travel_itinerary (list[RmErpTravelmanagementBusinesstripapplicationTravelItinerary] | Unset):
        lock_version (int | Unset):
        notes (str | Unset):
        notes_selected (RmErpTravelmanagementSharedErpTravelManagementNotesValue | Unset):
        obj_guid (str | Unset):
        other_estimated_costs (float | Unset):
        private_trip_address (str | Unset):
        private_trip_begin_date (int | Unset):
        private_trip_end_date (int | Unset):
        private_trip_explanation (str | Unset):
        private_trip_residence (str | Unset):
        provide_compensation_amount (RmErpCommonErpGenericValue | Unset):
        reason_costs_higher_staedtekatalog (str | Unset):
        reduction_of_estimated_costs (float | Unset):
        return_trip_selected (RmErpTravelmanagementSharedErpReturnTripValue | Unset):
        small_mileage_allowance (RmErpCommonErpGenericValue | Unset):
        social_insurance_number (str | Unset):
        status (int | Unset):
        sum_of_estimated_costs (float | Unset):
        teaching_activity_in_curriculum (RmErpCommonErpGenericValue | Unset):
        transportation_airplane (RmErpCommonErpGenericValue | Unset):
        transportation_bicycle (RmErpCommonErpGenericValue | Unset):
        transportation_company_car (RmErpCommonErpGenericValue | Unset):
        transportation_costs (float | Unset):
        transportation_long_distance_bus (RmErpCommonErpGenericValue | Unset):
        transportation_motorcycle (RmErpCommonErpGenericValue | Unset):
        transportation_other (RmErpCommonErpGenericValue | Unset):
        transportation_other_explanation (str | Unset):
        transportation_own_car (RmErpCommonErpGenericValue | Unset):
        transportation_public_transport (RmErpCommonErpGenericValue | Unset):
        transportation_rental_car (RmErpCommonErpGenericValue | Unset):
        transportation_reservation (RmErpCommonErpGenericValue | Unset):
        transportation_reservation_explanation (str | Unset):
        transportation_train (RmErpCommonErpGenericValue | Unset):
        travel_allowance_amount (float | Unset):
        travel_companion_explanation_freetext (str | Unset):
        travel_companion_freetext (str | Unset):
        travel_management_purpose (str | Unset):
        trip_begin_date (int | Unset):
        trip_end_date (int | Unset):
        valueable_consideration_for_teaching (RmErpCommonErpGenericValue | Unset):
    """

    field_foreigntext: RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationForeigntext | Unset = UNSET
    accident_care: RmErpCommonErpGenericValue | Unset = UNSET
    accommodation_expenses: float | Unset = UNSET
    account_bic: str | Unset = UNSET
    account_iban: str | Unset = UNSET
    address_travel_destination: str | Unset = UNSET
    application_date: int | Unset = UNSET
    application_related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset = UNSET
    application_related_person_id: int | Unset = UNSET
    arrival_selected: RmErpTravelmanagementSharedErpArrivalValue | Unset = UNSET
    assets: RmErpTravelmanagementBusinesstripapplicationAssets | Unset = UNSET
    availability_freetext: str | Unset = UNSET
    billingbasis_selected: RmErpTravelmanagementSharedErpBillingbasisValue | Unset = UNSET
    business_begin_date: int | Unset = UNSET
    business_end_date: int | Unset = UNSET
    businesstrip_application_identifier: int | Unset = UNSET
    change_account_new_bic: str | Unset = UNSET
    change_account_new_iban: str | Unset = UNSET
    change_bank_details: RmErpCommonErpGenericValue | Unset = UNSET
    conference_fee: float | Unset = UNSET
    costs_higher_staedtekatalog: RmErpCommonErpGenericValue | Unset = UNSET
    country: str | Unset = UNSET
    country_selected: RmErpCommonPersonErpCountryValue | Unset = UNSET
    destination: str | Unset = UNSET
    destination_details: str | Unset = UNSET
    destination_freetext: str | Unset = UNSET
    destinations_of_the_last_years: str | Unset = UNSET
    documents: list[RmErpCommonDocumentDocument] | Unset = UNSET
    forego_accommodation_allowance: RmErpCommonErpGenericValue | Unset = UNSET
    forego_daily_allowance: RmErpCommonErpGenericValue | Unset = UNSET
    forego_participation_fees: RmErpCommonErpGenericValue | Unset = UNSET
    forego_travel_costs: RmErpCommonErpGenericValue | Unset = UNSET
    full_reimbursement: RmErpCommonErpGenericValue | Unset = UNSET
    health_insurance_selected: RmErpTravelmanagementSharedErpHealthInsuranceValue | Unset = UNSET
    id: int | Unset = UNSET
    institute_first_selected: RmErpCommonInstituteErpInstitute | Unset = UNSET
    institute_second_selected: RmErpCommonInstituteErpInstitute | Unset = UNSET
    is_foreign_country: bool | Unset = UNSET
    is_private_trip: RmErpCommonErpGenericValue | Unset = UNSET
    large_mileage_allowance: RmErpCommonErpGenericValue | Unset = UNSET
    large_mileage_allowance_explanation: str | Unset = UNSET
    list_financing: list[RmErpTravelmanagementBusinesstripapplicationFinancing] | Unset = UNSET
    list_travel_abroad: list[RmErpTravelmanagementBusinesstripapplicationTravelAbroad] | Unset = UNSET
    list_travel_itinerary: list[RmErpTravelmanagementBusinesstripapplicationTravelItinerary] | Unset = UNSET
    lock_version: int | Unset = UNSET
    notes: str | Unset = UNSET
    notes_selected: RmErpTravelmanagementSharedErpTravelManagementNotesValue | Unset = UNSET
    obj_guid: str | Unset = UNSET
    other_estimated_costs: float | Unset = UNSET
    private_trip_address: str | Unset = UNSET
    private_trip_begin_date: int | Unset = UNSET
    private_trip_end_date: int | Unset = UNSET
    private_trip_explanation: str | Unset = UNSET
    private_trip_residence: str | Unset = UNSET
    provide_compensation_amount: RmErpCommonErpGenericValue | Unset = UNSET
    reason_costs_higher_staedtekatalog: str | Unset = UNSET
    reduction_of_estimated_costs: float | Unset = UNSET
    return_trip_selected: RmErpTravelmanagementSharedErpReturnTripValue | Unset = UNSET
    small_mileage_allowance: RmErpCommonErpGenericValue | Unset = UNSET
    social_insurance_number: str | Unset = UNSET
    status: int | Unset = UNSET
    sum_of_estimated_costs: float | Unset = UNSET
    teaching_activity_in_curriculum: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_airplane: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_bicycle: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_company_car: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_costs: float | Unset = UNSET
    transportation_long_distance_bus: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_motorcycle: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_other: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_other_explanation: str | Unset = UNSET
    transportation_own_car: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_public_transport: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_rental_car: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_reservation: RmErpCommonErpGenericValue | Unset = UNSET
    transportation_reservation_explanation: str | Unset = UNSET
    transportation_train: RmErpCommonErpGenericValue | Unset = UNSET
    travel_allowance_amount: float | Unset = UNSET
    travel_companion_explanation_freetext: str | Unset = UNSET
    travel_companion_freetext: str | Unset = UNSET
    travel_management_purpose: str | Unset = UNSET
    trip_begin_date: int | Unset = UNSET
    trip_end_date: int | Unset = UNSET
    valueable_consideration_for_teaching: RmErpCommonErpGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        accident_care: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accident_care, Unset):
            accident_care = self.accident_care.to_dict()

        accommodation_expenses = self.accommodation_expenses

        account_bic = self.account_bic

        account_iban = self.account_iban

        address_travel_destination = self.address_travel_destination

        application_date = self.application_date

        application_related_person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application_related_person, Unset):
            application_related_person = self.application_related_person.to_dict()

        application_related_person_id = self.application_related_person_id

        arrival_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.arrival_selected, Unset):
            arrival_selected = self.arrival_selected.to_dict()

        assets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assets, Unset):
            assets = self.assets.to_dict()

        availability_freetext = self.availability_freetext

        billingbasis_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billingbasis_selected, Unset):
            billingbasis_selected = self.billingbasis_selected.to_dict()

        business_begin_date = self.business_begin_date

        business_end_date = self.business_end_date

        businesstrip_application_identifier = self.businesstrip_application_identifier

        change_account_new_bic = self.change_account_new_bic

        change_account_new_iban = self.change_account_new_iban

        change_bank_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_bank_details, Unset):
            change_bank_details = self.change_bank_details.to_dict()

        conference_fee = self.conference_fee

        costs_higher_staedtekatalog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.costs_higher_staedtekatalog, Unset):
            costs_higher_staedtekatalog = self.costs_higher_staedtekatalog.to_dict()

        country = self.country

        country_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country_selected, Unset):
            country_selected = self.country_selected.to_dict()

        destination = self.destination

        destination_details = self.destination_details

        destination_freetext = self.destination_freetext

        destinations_of_the_last_years = self.destinations_of_the_last_years

        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        forego_accommodation_allowance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forego_accommodation_allowance, Unset):
            forego_accommodation_allowance = self.forego_accommodation_allowance.to_dict()

        forego_daily_allowance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forego_daily_allowance, Unset):
            forego_daily_allowance = self.forego_daily_allowance.to_dict()

        forego_participation_fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forego_participation_fees, Unset):
            forego_participation_fees = self.forego_participation_fees.to_dict()

        forego_travel_costs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forego_travel_costs, Unset):
            forego_travel_costs = self.forego_travel_costs.to_dict()

        full_reimbursement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_reimbursement, Unset):
            full_reimbursement = self.full_reimbursement.to_dict()

        health_insurance_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_insurance_selected, Unset):
            health_insurance_selected = self.health_insurance_selected.to_dict()

        id = self.id

        institute_first_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.institute_first_selected, Unset):
            institute_first_selected = self.institute_first_selected.to_dict()

        institute_second_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.institute_second_selected, Unset):
            institute_second_selected = self.institute_second_selected.to_dict()

        is_foreign_country = self.is_foreign_country

        is_private_trip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.is_private_trip, Unset):
            is_private_trip = self.is_private_trip.to_dict()

        large_mileage_allowance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.large_mileage_allowance, Unset):
            large_mileage_allowance = self.large_mileage_allowance.to_dict()

        large_mileage_allowance_explanation = self.large_mileage_allowance_explanation

        list_financing: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_financing, Unset):
            list_financing = []
            for list_financing_item_data in self.list_financing:
                list_financing_item = list_financing_item_data.to_dict()
                list_financing.append(list_financing_item)

        list_travel_abroad: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_travel_abroad, Unset):
            list_travel_abroad = []
            for list_travel_abroad_item_data in self.list_travel_abroad:
                list_travel_abroad_item = list_travel_abroad_item_data.to_dict()
                list_travel_abroad.append(list_travel_abroad_item)

        list_travel_itinerary: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_travel_itinerary, Unset):
            list_travel_itinerary = []
            for list_travel_itinerary_item_data in self.list_travel_itinerary:
                list_travel_itinerary_item = list_travel_itinerary_item_data.to_dict()
                list_travel_itinerary.append(list_travel_itinerary_item)

        lock_version = self.lock_version

        notes = self.notes

        notes_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notes_selected, Unset):
            notes_selected = self.notes_selected.to_dict()

        obj_guid = self.obj_guid

        other_estimated_costs = self.other_estimated_costs

        private_trip_address = self.private_trip_address

        private_trip_begin_date = self.private_trip_begin_date

        private_trip_end_date = self.private_trip_end_date

        private_trip_explanation = self.private_trip_explanation

        private_trip_residence = self.private_trip_residence

        provide_compensation_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provide_compensation_amount, Unset):
            provide_compensation_amount = self.provide_compensation_amount.to_dict()

        reason_costs_higher_staedtekatalog = self.reason_costs_higher_staedtekatalog

        reduction_of_estimated_costs = self.reduction_of_estimated_costs

        return_trip_selected: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_trip_selected, Unset):
            return_trip_selected = self.return_trip_selected.to_dict()

        small_mileage_allowance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.small_mileage_allowance, Unset):
            small_mileage_allowance = self.small_mileage_allowance.to_dict()

        social_insurance_number = self.social_insurance_number

        status = self.status

        sum_of_estimated_costs = self.sum_of_estimated_costs

        teaching_activity_in_curriculum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.teaching_activity_in_curriculum, Unset):
            teaching_activity_in_curriculum = self.teaching_activity_in_curriculum.to_dict()

        transportation_airplane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_airplane, Unset):
            transportation_airplane = self.transportation_airplane.to_dict()

        transportation_bicycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_bicycle, Unset):
            transportation_bicycle = self.transportation_bicycle.to_dict()

        transportation_company_car: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_company_car, Unset):
            transportation_company_car = self.transportation_company_car.to_dict()

        transportation_costs = self.transportation_costs

        transportation_long_distance_bus: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_long_distance_bus, Unset):
            transportation_long_distance_bus = self.transportation_long_distance_bus.to_dict()

        transportation_motorcycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_motorcycle, Unset):
            transportation_motorcycle = self.transportation_motorcycle.to_dict()

        transportation_other: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_other, Unset):
            transportation_other = self.transportation_other.to_dict()

        transportation_other_explanation = self.transportation_other_explanation

        transportation_own_car: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_own_car, Unset):
            transportation_own_car = self.transportation_own_car.to_dict()

        transportation_public_transport: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_public_transport, Unset):
            transportation_public_transport = self.transportation_public_transport.to_dict()

        transportation_rental_car: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_rental_car, Unset):
            transportation_rental_car = self.transportation_rental_car.to_dict()

        transportation_reservation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_reservation, Unset):
            transportation_reservation = self.transportation_reservation.to_dict()

        transportation_reservation_explanation = self.transportation_reservation_explanation

        transportation_train: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transportation_train, Unset):
            transportation_train = self.transportation_train.to_dict()

        travel_allowance_amount = self.travel_allowance_amount

        travel_companion_explanation_freetext = self.travel_companion_explanation_freetext

        travel_companion_freetext = self.travel_companion_freetext

        travel_management_purpose = self.travel_management_purpose

        trip_begin_date = self.trip_begin_date

        trip_end_date = self.trip_end_date

        valueable_consideration_for_teaching: dict[str, Any] | Unset = UNSET
        if not isinstance(self.valueable_consideration_for_teaching, Unset):
            valueable_consideration_for_teaching = self.valueable_consideration_for_teaching.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if accident_care is not UNSET:
            field_dict["accidentCare"] = accident_care
        if accommodation_expenses is not UNSET:
            field_dict["accommodationExpenses"] = accommodation_expenses
        if account_bic is not UNSET:
            field_dict["accountBic"] = account_bic
        if account_iban is not UNSET:
            field_dict["accountIban"] = account_iban
        if address_travel_destination is not UNSET:
            field_dict["addressTravelDestination"] = address_travel_destination
        if application_date is not UNSET:
            field_dict["applicationDate"] = application_date
        if application_related_person is not UNSET:
            field_dict["applicationRelatedPerson"] = application_related_person
        if application_related_person_id is not UNSET:
            field_dict["applicationRelatedPersonId"] = application_related_person_id
        if arrival_selected is not UNSET:
            field_dict["arrivalSelected"] = arrival_selected
        if assets is not UNSET:
            field_dict["assets"] = assets
        if availability_freetext is not UNSET:
            field_dict["availabilityFreetext"] = availability_freetext
        if billingbasis_selected is not UNSET:
            field_dict["billingbasisSelected"] = billingbasis_selected
        if business_begin_date is not UNSET:
            field_dict["businessBeginDate"] = business_begin_date
        if business_end_date is not UNSET:
            field_dict["businessEndDate"] = business_end_date
        if businesstrip_application_identifier is not UNSET:
            field_dict["businesstripApplicationIdentifier"] = businesstrip_application_identifier
        if change_account_new_bic is not UNSET:
            field_dict["changeAccountNewBic"] = change_account_new_bic
        if change_account_new_iban is not UNSET:
            field_dict["changeAccountNewIban"] = change_account_new_iban
        if change_bank_details is not UNSET:
            field_dict["changeBankDetails"] = change_bank_details
        if conference_fee is not UNSET:
            field_dict["conferenceFee"] = conference_fee
        if costs_higher_staedtekatalog is not UNSET:
            field_dict["costsHigherStaedtekatalog"] = costs_higher_staedtekatalog
        if country is not UNSET:
            field_dict["country"] = country
        if country_selected is not UNSET:
            field_dict["countrySelected"] = country_selected
        if destination is not UNSET:
            field_dict["destination"] = destination
        if destination_details is not UNSET:
            field_dict["destinationDetails"] = destination_details
        if destination_freetext is not UNSET:
            field_dict["destinationFreetext"] = destination_freetext
        if destinations_of_the_last_years is not UNSET:
            field_dict["destinationsOfTheLastYears"] = destinations_of_the_last_years
        if documents is not UNSET:
            field_dict["documents"] = documents
        if forego_accommodation_allowance is not UNSET:
            field_dict["foregoAccommodationAllowance"] = forego_accommodation_allowance
        if forego_daily_allowance is not UNSET:
            field_dict["foregoDailyAllowance"] = forego_daily_allowance
        if forego_participation_fees is not UNSET:
            field_dict["foregoParticipationFees"] = forego_participation_fees
        if forego_travel_costs is not UNSET:
            field_dict["foregoTravelCosts"] = forego_travel_costs
        if full_reimbursement is not UNSET:
            field_dict["fullReimbursement"] = full_reimbursement
        if health_insurance_selected is not UNSET:
            field_dict["healthInsuranceSelected"] = health_insurance_selected
        if id is not UNSET:
            field_dict["id"] = id
        if institute_first_selected is not UNSET:
            field_dict["instituteFirstSelected"] = institute_first_selected
        if institute_second_selected is not UNSET:
            field_dict["instituteSecondSelected"] = institute_second_selected
        if is_foreign_country is not UNSET:
            field_dict["isForeignCountry"] = is_foreign_country
        if is_private_trip is not UNSET:
            field_dict["isPrivateTrip"] = is_private_trip
        if large_mileage_allowance is not UNSET:
            field_dict["largeMileageAllowance"] = large_mileage_allowance
        if large_mileage_allowance_explanation is not UNSET:
            field_dict["largeMileageAllowanceExplanation"] = large_mileage_allowance_explanation
        if list_financing is not UNSET:
            field_dict["listFinancing"] = list_financing
        if list_travel_abroad is not UNSET:
            field_dict["listTravelAbroad"] = list_travel_abroad
        if list_travel_itinerary is not UNSET:
            field_dict["listTravelItinerary"] = list_travel_itinerary
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if notes is not UNSET:
            field_dict["notes"] = notes
        if notes_selected is not UNSET:
            field_dict["notesSelected"] = notes_selected
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if other_estimated_costs is not UNSET:
            field_dict["otherEstimatedCosts"] = other_estimated_costs
        if private_trip_address is not UNSET:
            field_dict["privateTripAddress"] = private_trip_address
        if private_trip_begin_date is not UNSET:
            field_dict["privateTripBeginDate"] = private_trip_begin_date
        if private_trip_end_date is not UNSET:
            field_dict["privateTripEndDate"] = private_trip_end_date
        if private_trip_explanation is not UNSET:
            field_dict["privateTripExplanation"] = private_trip_explanation
        if private_trip_residence is not UNSET:
            field_dict["privateTripResidence"] = private_trip_residence
        if provide_compensation_amount is not UNSET:
            field_dict["provideCompensationAmount"] = provide_compensation_amount
        if reason_costs_higher_staedtekatalog is not UNSET:
            field_dict["reasonCostsHigherStaedtekatalog"] = reason_costs_higher_staedtekatalog
        if reduction_of_estimated_costs is not UNSET:
            field_dict["reductionOfEstimatedCosts"] = reduction_of_estimated_costs
        if return_trip_selected is not UNSET:
            field_dict["returnTripSelected"] = return_trip_selected
        if small_mileage_allowance is not UNSET:
            field_dict["smallMileageAllowance"] = small_mileage_allowance
        if social_insurance_number is not UNSET:
            field_dict["socialInsuranceNumber"] = social_insurance_number
        if status is not UNSET:
            field_dict["status"] = status
        if sum_of_estimated_costs is not UNSET:
            field_dict["sumOfEstimatedCosts"] = sum_of_estimated_costs
        if teaching_activity_in_curriculum is not UNSET:
            field_dict["teachingActivityInCurriculum"] = teaching_activity_in_curriculum
        if transportation_airplane is not UNSET:
            field_dict["transportationAirplane"] = transportation_airplane
        if transportation_bicycle is not UNSET:
            field_dict["transportationBicycle"] = transportation_bicycle
        if transportation_company_car is not UNSET:
            field_dict["transportationCompanyCar"] = transportation_company_car
        if transportation_costs is not UNSET:
            field_dict["transportationCosts"] = transportation_costs
        if transportation_long_distance_bus is not UNSET:
            field_dict["transportationLongDistanceBus"] = transportation_long_distance_bus
        if transportation_motorcycle is not UNSET:
            field_dict["transportationMotorcycle"] = transportation_motorcycle
        if transportation_other is not UNSET:
            field_dict["transportationOther"] = transportation_other
        if transportation_other_explanation is not UNSET:
            field_dict["transportationOtherExplanation"] = transportation_other_explanation
        if transportation_own_car is not UNSET:
            field_dict["transportationOwnCar"] = transportation_own_car
        if transportation_public_transport is not UNSET:
            field_dict["transportationPublicTransport"] = transportation_public_transport
        if transportation_rental_car is not UNSET:
            field_dict["transportationRentalCar"] = transportation_rental_car
        if transportation_reservation is not UNSET:
            field_dict["transportationReservation"] = transportation_reservation
        if transportation_reservation_explanation is not UNSET:
            field_dict["transportationReservationExplanation"] = transportation_reservation_explanation
        if transportation_train is not UNSET:
            field_dict["transportationTrain"] = transportation_train
        if travel_allowance_amount is not UNSET:
            field_dict["travelAllowanceAmount"] = travel_allowance_amount
        if travel_companion_explanation_freetext is not UNSET:
            field_dict["travelCompanionExplanationFreetext"] = travel_companion_explanation_freetext
        if travel_companion_freetext is not UNSET:
            field_dict["travelCompanionFreetext"] = travel_companion_freetext
        if travel_management_purpose is not UNSET:
            field_dict["travelManagementPurpose"] = travel_management_purpose
        if trip_begin_date is not UNSET:
            field_dict["tripBeginDate"] = trip_begin_date
        if trip_end_date is not UNSET:
            field_dict["tripEndDate"] = trip_end_date
        if valueable_consideration_for_teaching is not UNSET:
            field_dict["valueableConsiderationForTeaching"] = valueable_consideration_for_teaching

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rm_erp_common_document_document import RmErpCommonDocumentDocument  # noqa: PLC0415
        from ..models.rm_erp_common_erp_generic_value import RmErpCommonErpGenericValue  # noqa: PLC0415
        from ..models.rm_erp_common_institute_erp_institute import RmErpCommonInstituteErpInstitute  # noqa: PLC0415
        from ..models.rm_erp_common_person_erp_country_value import RmErpCommonPersonErpCountryValue  # noqa: PLC0415
        from ..models.rm_erp_common_person_person_basic_data_core_data import RmErpCommonPersonPersonBasicDataCoreData  # noqa: PLC0415
        from ..models.rm_erp_travelmanagement_businesstripapplication_assets import (
            RmErpTravelmanagementBusinesstripapplicationAssets,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_businesstripapplication_businesstrip_application_foreigntext import (
            RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationForeigntext,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_businesstripapplication_financing import (
            RmErpTravelmanagementBusinesstripapplicationFinancing,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_businesstripapplication_travel_abroad import (
            RmErpTravelmanagementBusinesstripapplicationTravelAbroad,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_businesstripapplication_travel_itinerary import (
            RmErpTravelmanagementBusinesstripapplicationTravelItinerary,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_arrival_value import RmErpTravelmanagementSharedErpArrivalValue  # noqa: PLC0415
        from ..models.rm_erp_travelmanagement_shared_erp_billingbasis_value import (
            RmErpTravelmanagementSharedErpBillingbasisValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_health_insurance_value import (
            RmErpTravelmanagementSharedErpHealthInsuranceValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_return_trip_value import (
            RmErpTravelmanagementSharedErpReturnTripValue,  # noqa: PLC0415
        )
        from ..models.rm_erp_travelmanagement_shared_erp_travel_management_notes_value import (
            RmErpTravelmanagementSharedErpTravelManagementNotesValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = (
                RmErpTravelmanagementBusinesstripapplicationBusinesstripApplicationForeigntext.from_dict(
                    _field_foreigntext
                )
            )

        _accident_care = d.pop("accidentCare", UNSET)
        accident_care: RmErpCommonErpGenericValue | Unset
        if isinstance(_accident_care, Unset):
            accident_care = UNSET
        else:
            accident_care = RmErpCommonErpGenericValue.from_dict(_accident_care)

        accommodation_expenses = d.pop("accommodationExpenses", UNSET)

        account_bic = d.pop("accountBic", UNSET)

        account_iban = d.pop("accountIban", UNSET)

        address_travel_destination = d.pop("addressTravelDestination", UNSET)

        application_date = d.pop("applicationDate", UNSET)

        _application_related_person = d.pop("applicationRelatedPerson", UNSET)
        application_related_person: RmErpCommonPersonPersonBasicDataCoreData | Unset
        if isinstance(_application_related_person, Unset):
            application_related_person = UNSET
        else:
            application_related_person = RmErpCommonPersonPersonBasicDataCoreData.from_dict(_application_related_person)

        application_related_person_id = d.pop("applicationRelatedPersonId", UNSET)

        _arrival_selected = d.pop("arrivalSelected", UNSET)
        arrival_selected: RmErpTravelmanagementSharedErpArrivalValue | Unset
        if isinstance(_arrival_selected, Unset):
            arrival_selected = UNSET
        else:
            arrival_selected = RmErpTravelmanagementSharedErpArrivalValue.from_dict(_arrival_selected)

        _assets = d.pop("assets", UNSET)
        assets: RmErpTravelmanagementBusinesstripapplicationAssets | Unset
        if isinstance(_assets, Unset):
            assets = UNSET
        else:
            assets = RmErpTravelmanagementBusinesstripapplicationAssets.from_dict(_assets)

        availability_freetext = d.pop("availabilityFreetext", UNSET)

        _billingbasis_selected = d.pop("billingbasisSelected", UNSET)
        billingbasis_selected: RmErpTravelmanagementSharedErpBillingbasisValue | Unset
        if isinstance(_billingbasis_selected, Unset):
            billingbasis_selected = UNSET
        else:
            billingbasis_selected = RmErpTravelmanagementSharedErpBillingbasisValue.from_dict(_billingbasis_selected)

        business_begin_date = d.pop("businessBeginDate", UNSET)

        business_end_date = d.pop("businessEndDate", UNSET)

        businesstrip_application_identifier = d.pop("businesstripApplicationIdentifier", UNSET)

        change_account_new_bic = d.pop("changeAccountNewBic", UNSET)

        change_account_new_iban = d.pop("changeAccountNewIban", UNSET)

        _change_bank_details = d.pop("changeBankDetails", UNSET)
        change_bank_details: RmErpCommonErpGenericValue | Unset
        if isinstance(_change_bank_details, Unset):
            change_bank_details = UNSET
        else:
            change_bank_details = RmErpCommonErpGenericValue.from_dict(_change_bank_details)

        conference_fee = d.pop("conferenceFee", UNSET)

        _costs_higher_staedtekatalog = d.pop("costsHigherStaedtekatalog", UNSET)
        costs_higher_staedtekatalog: RmErpCommonErpGenericValue | Unset
        if isinstance(_costs_higher_staedtekatalog, Unset):
            costs_higher_staedtekatalog = UNSET
        else:
            costs_higher_staedtekatalog = RmErpCommonErpGenericValue.from_dict(_costs_higher_staedtekatalog)

        country = d.pop("country", UNSET)

        _country_selected = d.pop("countrySelected", UNSET)
        country_selected: RmErpCommonPersonErpCountryValue | Unset
        if isinstance(_country_selected, Unset):
            country_selected = UNSET
        else:
            country_selected = RmErpCommonPersonErpCountryValue.from_dict(_country_selected)

        destination = d.pop("destination", UNSET)

        destination_details = d.pop("destinationDetails", UNSET)

        destination_freetext = d.pop("destinationFreetext", UNSET)

        destinations_of_the_last_years = d.pop("destinationsOfTheLastYears", UNSET)

        _documents = d.pop("documents", UNSET)
        documents: list[RmErpCommonDocumentDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RmErpCommonDocumentDocument.from_dict(documents_item_data)

                documents.append(documents_item)

        _forego_accommodation_allowance = d.pop("foregoAccommodationAllowance", UNSET)
        forego_accommodation_allowance: RmErpCommonErpGenericValue | Unset
        if isinstance(_forego_accommodation_allowance, Unset):
            forego_accommodation_allowance = UNSET
        else:
            forego_accommodation_allowance = RmErpCommonErpGenericValue.from_dict(_forego_accommodation_allowance)

        _forego_daily_allowance = d.pop("foregoDailyAllowance", UNSET)
        forego_daily_allowance: RmErpCommonErpGenericValue | Unset
        if isinstance(_forego_daily_allowance, Unset):
            forego_daily_allowance = UNSET
        else:
            forego_daily_allowance = RmErpCommonErpGenericValue.from_dict(_forego_daily_allowance)

        _forego_participation_fees = d.pop("foregoParticipationFees", UNSET)
        forego_participation_fees: RmErpCommonErpGenericValue | Unset
        if isinstance(_forego_participation_fees, Unset):
            forego_participation_fees = UNSET
        else:
            forego_participation_fees = RmErpCommonErpGenericValue.from_dict(_forego_participation_fees)

        _forego_travel_costs = d.pop("foregoTravelCosts", UNSET)
        forego_travel_costs: RmErpCommonErpGenericValue | Unset
        if isinstance(_forego_travel_costs, Unset):
            forego_travel_costs = UNSET
        else:
            forego_travel_costs = RmErpCommonErpGenericValue.from_dict(_forego_travel_costs)

        _full_reimbursement = d.pop("fullReimbursement", UNSET)
        full_reimbursement: RmErpCommonErpGenericValue | Unset
        if isinstance(_full_reimbursement, Unset):
            full_reimbursement = UNSET
        else:
            full_reimbursement = RmErpCommonErpGenericValue.from_dict(_full_reimbursement)

        _health_insurance_selected = d.pop("healthInsuranceSelected", UNSET)
        health_insurance_selected: RmErpTravelmanagementSharedErpHealthInsuranceValue | Unset
        if isinstance(_health_insurance_selected, Unset):
            health_insurance_selected = UNSET
        else:
            health_insurance_selected = RmErpTravelmanagementSharedErpHealthInsuranceValue.from_dict(
                _health_insurance_selected
            )

        id = d.pop("id", UNSET)

        _institute_first_selected = d.pop("instituteFirstSelected", UNSET)
        institute_first_selected: RmErpCommonInstituteErpInstitute | Unset
        if isinstance(_institute_first_selected, Unset):
            institute_first_selected = UNSET
        else:
            institute_first_selected = RmErpCommonInstituteErpInstitute.from_dict(_institute_first_selected)

        _institute_second_selected = d.pop("instituteSecondSelected", UNSET)
        institute_second_selected: RmErpCommonInstituteErpInstitute | Unset
        if isinstance(_institute_second_selected, Unset):
            institute_second_selected = UNSET
        else:
            institute_second_selected = RmErpCommonInstituteErpInstitute.from_dict(_institute_second_selected)

        is_foreign_country = d.pop("isForeignCountry", UNSET)

        _is_private_trip = d.pop("isPrivateTrip", UNSET)
        is_private_trip: RmErpCommonErpGenericValue | Unset
        if isinstance(_is_private_trip, Unset):
            is_private_trip = UNSET
        else:
            is_private_trip = RmErpCommonErpGenericValue.from_dict(_is_private_trip)

        _large_mileage_allowance = d.pop("largeMileageAllowance", UNSET)
        large_mileage_allowance: RmErpCommonErpGenericValue | Unset
        if isinstance(_large_mileage_allowance, Unset):
            large_mileage_allowance = UNSET
        else:
            large_mileage_allowance = RmErpCommonErpGenericValue.from_dict(_large_mileage_allowance)

        large_mileage_allowance_explanation = d.pop("largeMileageAllowanceExplanation", UNSET)

        _list_financing = d.pop("listFinancing", UNSET)
        list_financing: list[RmErpTravelmanagementBusinesstripapplicationFinancing] | Unset = UNSET
        if _list_financing is not UNSET:
            list_financing = []
            for list_financing_item_data in _list_financing:
                list_financing_item = RmErpTravelmanagementBusinesstripapplicationFinancing.from_dict(
                    list_financing_item_data
                )

                list_financing.append(list_financing_item)

        _list_travel_abroad = d.pop("listTravelAbroad", UNSET)
        list_travel_abroad: list[RmErpTravelmanagementBusinesstripapplicationTravelAbroad] | Unset = UNSET
        if _list_travel_abroad is not UNSET:
            list_travel_abroad = []
            for list_travel_abroad_item_data in _list_travel_abroad:
                list_travel_abroad_item = RmErpTravelmanagementBusinesstripapplicationTravelAbroad.from_dict(
                    list_travel_abroad_item_data
                )

                list_travel_abroad.append(list_travel_abroad_item)

        _list_travel_itinerary = d.pop("listTravelItinerary", UNSET)
        list_travel_itinerary: list[RmErpTravelmanagementBusinesstripapplicationTravelItinerary] | Unset = UNSET
        if _list_travel_itinerary is not UNSET:
            list_travel_itinerary = []
            for list_travel_itinerary_item_data in _list_travel_itinerary:
                list_travel_itinerary_item = RmErpTravelmanagementBusinesstripapplicationTravelItinerary.from_dict(
                    list_travel_itinerary_item_data
                )

                list_travel_itinerary.append(list_travel_itinerary_item)

        lock_version = d.pop("lockVersion", UNSET)

        notes = d.pop("notes", UNSET)

        _notes_selected = d.pop("notesSelected", UNSET)
        notes_selected: RmErpTravelmanagementSharedErpTravelManagementNotesValue | Unset
        if isinstance(_notes_selected, Unset):
            notes_selected = UNSET
        else:
            notes_selected = RmErpTravelmanagementSharedErpTravelManagementNotesValue.from_dict(_notes_selected)

        obj_guid = d.pop("objGuid", UNSET)

        other_estimated_costs = d.pop("otherEstimatedCosts", UNSET)

        private_trip_address = d.pop("privateTripAddress", UNSET)

        private_trip_begin_date = d.pop("privateTripBeginDate", UNSET)

        private_trip_end_date = d.pop("privateTripEndDate", UNSET)

        private_trip_explanation = d.pop("privateTripExplanation", UNSET)

        private_trip_residence = d.pop("privateTripResidence", UNSET)

        _provide_compensation_amount = d.pop("provideCompensationAmount", UNSET)
        provide_compensation_amount: RmErpCommonErpGenericValue | Unset
        if isinstance(_provide_compensation_amount, Unset):
            provide_compensation_amount = UNSET
        else:
            provide_compensation_amount = RmErpCommonErpGenericValue.from_dict(_provide_compensation_amount)

        reason_costs_higher_staedtekatalog = d.pop("reasonCostsHigherStaedtekatalog", UNSET)

        reduction_of_estimated_costs = d.pop("reductionOfEstimatedCosts", UNSET)

        _return_trip_selected = d.pop("returnTripSelected", UNSET)
        return_trip_selected: RmErpTravelmanagementSharedErpReturnTripValue | Unset
        if isinstance(_return_trip_selected, Unset):
            return_trip_selected = UNSET
        else:
            return_trip_selected = RmErpTravelmanagementSharedErpReturnTripValue.from_dict(_return_trip_selected)

        _small_mileage_allowance = d.pop("smallMileageAllowance", UNSET)
        small_mileage_allowance: RmErpCommonErpGenericValue | Unset
        if isinstance(_small_mileage_allowance, Unset):
            small_mileage_allowance = UNSET
        else:
            small_mileage_allowance = RmErpCommonErpGenericValue.from_dict(_small_mileage_allowance)

        social_insurance_number = d.pop("socialInsuranceNumber", UNSET)

        status = d.pop("status", UNSET)

        sum_of_estimated_costs = d.pop("sumOfEstimatedCosts", UNSET)

        _teaching_activity_in_curriculum = d.pop("teachingActivityInCurriculum", UNSET)
        teaching_activity_in_curriculum: RmErpCommonErpGenericValue | Unset
        if isinstance(_teaching_activity_in_curriculum, Unset):
            teaching_activity_in_curriculum = UNSET
        else:
            teaching_activity_in_curriculum = RmErpCommonErpGenericValue.from_dict(_teaching_activity_in_curriculum)

        _transportation_airplane = d.pop("transportationAirplane", UNSET)
        transportation_airplane: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_airplane, Unset):
            transportation_airplane = UNSET
        else:
            transportation_airplane = RmErpCommonErpGenericValue.from_dict(_transportation_airplane)

        _transportation_bicycle = d.pop("transportationBicycle", UNSET)
        transportation_bicycle: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_bicycle, Unset):
            transportation_bicycle = UNSET
        else:
            transportation_bicycle = RmErpCommonErpGenericValue.from_dict(_transportation_bicycle)

        _transportation_company_car = d.pop("transportationCompanyCar", UNSET)
        transportation_company_car: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_company_car, Unset):
            transportation_company_car = UNSET
        else:
            transportation_company_car = RmErpCommonErpGenericValue.from_dict(_transportation_company_car)

        transportation_costs = d.pop("transportationCosts", UNSET)

        _transportation_long_distance_bus = d.pop("transportationLongDistanceBus", UNSET)
        transportation_long_distance_bus: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_long_distance_bus, Unset):
            transportation_long_distance_bus = UNSET
        else:
            transportation_long_distance_bus = RmErpCommonErpGenericValue.from_dict(_transportation_long_distance_bus)

        _transportation_motorcycle = d.pop("transportationMotorcycle", UNSET)
        transportation_motorcycle: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_motorcycle, Unset):
            transportation_motorcycle = UNSET
        else:
            transportation_motorcycle = RmErpCommonErpGenericValue.from_dict(_transportation_motorcycle)

        _transportation_other = d.pop("transportationOther", UNSET)
        transportation_other: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_other, Unset):
            transportation_other = UNSET
        else:
            transportation_other = RmErpCommonErpGenericValue.from_dict(_transportation_other)

        transportation_other_explanation = d.pop("transportationOtherExplanation", UNSET)

        _transportation_own_car = d.pop("transportationOwnCar", UNSET)
        transportation_own_car: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_own_car, Unset):
            transportation_own_car = UNSET
        else:
            transportation_own_car = RmErpCommonErpGenericValue.from_dict(_transportation_own_car)

        _transportation_public_transport = d.pop("transportationPublicTransport", UNSET)
        transportation_public_transport: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_public_transport, Unset):
            transportation_public_transport = UNSET
        else:
            transportation_public_transport = RmErpCommonErpGenericValue.from_dict(_transportation_public_transport)

        _transportation_rental_car = d.pop("transportationRentalCar", UNSET)
        transportation_rental_car: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_rental_car, Unset):
            transportation_rental_car = UNSET
        else:
            transportation_rental_car = RmErpCommonErpGenericValue.from_dict(_transportation_rental_car)

        _transportation_reservation = d.pop("transportationReservation", UNSET)
        transportation_reservation: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_reservation, Unset):
            transportation_reservation = UNSET
        else:
            transportation_reservation = RmErpCommonErpGenericValue.from_dict(_transportation_reservation)

        transportation_reservation_explanation = d.pop("transportationReservationExplanation", UNSET)

        _transportation_train = d.pop("transportationTrain", UNSET)
        transportation_train: RmErpCommonErpGenericValue | Unset
        if isinstance(_transportation_train, Unset):
            transportation_train = UNSET
        else:
            transportation_train = RmErpCommonErpGenericValue.from_dict(_transportation_train)

        travel_allowance_amount = d.pop("travelAllowanceAmount", UNSET)

        travel_companion_explanation_freetext = d.pop("travelCompanionExplanationFreetext", UNSET)

        travel_companion_freetext = d.pop("travelCompanionFreetext", UNSET)

        travel_management_purpose = d.pop("travelManagementPurpose", UNSET)

        trip_begin_date = d.pop("tripBeginDate", UNSET)

        trip_end_date = d.pop("tripEndDate", UNSET)

        _valueable_consideration_for_teaching = d.pop("valueableConsiderationForTeaching", UNSET)
        valueable_consideration_for_teaching: RmErpCommonErpGenericValue | Unset
        if isinstance(_valueable_consideration_for_teaching, Unset):
            valueable_consideration_for_teaching = UNSET
        else:
            valueable_consideration_for_teaching = RmErpCommonErpGenericValue.from_dict(
                _valueable_consideration_for_teaching
            )

        rm_erp_travelmanagement_businesstripapplication_businesstrip_application = cls(
            field_foreigntext=field_foreigntext,
            accident_care=accident_care,
            accommodation_expenses=accommodation_expenses,
            account_bic=account_bic,
            account_iban=account_iban,
            address_travel_destination=address_travel_destination,
            application_date=application_date,
            application_related_person=application_related_person,
            application_related_person_id=application_related_person_id,
            arrival_selected=arrival_selected,
            assets=assets,
            availability_freetext=availability_freetext,
            billingbasis_selected=billingbasis_selected,
            business_begin_date=business_begin_date,
            business_end_date=business_end_date,
            businesstrip_application_identifier=businesstrip_application_identifier,
            change_account_new_bic=change_account_new_bic,
            change_account_new_iban=change_account_new_iban,
            change_bank_details=change_bank_details,
            conference_fee=conference_fee,
            costs_higher_staedtekatalog=costs_higher_staedtekatalog,
            country=country,
            country_selected=country_selected,
            destination=destination,
            destination_details=destination_details,
            destination_freetext=destination_freetext,
            destinations_of_the_last_years=destinations_of_the_last_years,
            documents=documents,
            forego_accommodation_allowance=forego_accommodation_allowance,
            forego_daily_allowance=forego_daily_allowance,
            forego_participation_fees=forego_participation_fees,
            forego_travel_costs=forego_travel_costs,
            full_reimbursement=full_reimbursement,
            health_insurance_selected=health_insurance_selected,
            id=id,
            institute_first_selected=institute_first_selected,
            institute_second_selected=institute_second_selected,
            is_foreign_country=is_foreign_country,
            is_private_trip=is_private_trip,
            large_mileage_allowance=large_mileage_allowance,
            large_mileage_allowance_explanation=large_mileage_allowance_explanation,
            list_financing=list_financing,
            list_travel_abroad=list_travel_abroad,
            list_travel_itinerary=list_travel_itinerary,
            lock_version=lock_version,
            notes=notes,
            notes_selected=notes_selected,
            obj_guid=obj_guid,
            other_estimated_costs=other_estimated_costs,
            private_trip_address=private_trip_address,
            private_trip_begin_date=private_trip_begin_date,
            private_trip_end_date=private_trip_end_date,
            private_trip_explanation=private_trip_explanation,
            private_trip_residence=private_trip_residence,
            provide_compensation_amount=provide_compensation_amount,
            reason_costs_higher_staedtekatalog=reason_costs_higher_staedtekatalog,
            reduction_of_estimated_costs=reduction_of_estimated_costs,
            return_trip_selected=return_trip_selected,
            small_mileage_allowance=small_mileage_allowance,
            social_insurance_number=social_insurance_number,
            status=status,
            sum_of_estimated_costs=sum_of_estimated_costs,
            teaching_activity_in_curriculum=teaching_activity_in_curriculum,
            transportation_airplane=transportation_airplane,
            transportation_bicycle=transportation_bicycle,
            transportation_company_car=transportation_company_car,
            transportation_costs=transportation_costs,
            transportation_long_distance_bus=transportation_long_distance_bus,
            transportation_motorcycle=transportation_motorcycle,
            transportation_other=transportation_other,
            transportation_other_explanation=transportation_other_explanation,
            transportation_own_car=transportation_own_car,
            transportation_public_transport=transportation_public_transport,
            transportation_rental_car=transportation_rental_car,
            transportation_reservation=transportation_reservation,
            transportation_reservation_explanation=transportation_reservation_explanation,
            transportation_train=transportation_train,
            travel_allowance_amount=travel_allowance_amount,
            travel_companion_explanation_freetext=travel_companion_explanation_freetext,
            travel_companion_freetext=travel_companion_freetext,
            travel_management_purpose=travel_management_purpose,
            trip_begin_date=trip_begin_date,
            trip_end_date=trip_end_date,
            valueable_consideration_for_teaching=valueable_consideration_for_teaching,
        )

        rm_erp_travelmanagement_businesstripapplication_businesstrip_application.additional_properties = d
        return rm_erp_travelmanagement_businesstripapplication_businesstrip_application

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
