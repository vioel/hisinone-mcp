from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eu_emrex_elmo_country_code import EuEmrexElmoCountryCode
    from ..models.eu_emrex_elmo_elmo_learner_identifier import EuEmrexElmoElmoLearnerIdentifier
    from ..models.eu_emrex_elmo_flexible_address import EuEmrexElmoFlexibleAddress
    from ..models.java_math_big_integer import JavaMathBigInteger
    from ..models.java_util_calendar import JavaUtilCalendar


T = TypeVar("T", bound="EuEmrexElmoElmoLearner")


@_attrs_define
class EuEmrexElmoElmoLearner:
    """
    Attributes:
        bday (JavaUtilCalendar | Unset):
        birth_name (str | Unset):
        citizenship (EuEmrexElmoCountryCode | Unset):
        current_address (EuEmrexElmoFlexibleAddress | Unset):
        family_name (str | Unset):
        gender (JavaMathBigInteger | Unset):
        given_names (str | Unset):
        identifier (list[EuEmrexElmoElmoLearnerIdentifier] | Unset):
        place_of_birth (str | Unset):
    """

    bday: JavaUtilCalendar | Unset = UNSET
    birth_name: str | Unset = UNSET
    citizenship: EuEmrexElmoCountryCode | Unset = UNSET
    current_address: EuEmrexElmoFlexibleAddress | Unset = UNSET
    family_name: str | Unset = UNSET
    gender: JavaMathBigInteger | Unset = UNSET
    given_names: str | Unset = UNSET
    identifier: list[EuEmrexElmoElmoLearnerIdentifier] | Unset = UNSET
    place_of_birth: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        bday: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bday, Unset):
            bday = self.bday.to_dict()

        birth_name = self.birth_name

        citizenship: dict[str, Any] | Unset = UNSET
        if not isinstance(self.citizenship, Unset):
            citizenship = self.citizenship.to_dict()

        current_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_address, Unset):
            current_address = self.current_address.to_dict()

        family_name = self.family_name

        gender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        given_names = self.given_names

        identifier: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = []
            for identifier_item_data in self.identifier:
                identifier_item = identifier_item_data.to_dict()
                identifier.append(identifier_item)

        place_of_birth = self.place_of_birth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bday is not UNSET:
            field_dict["bday"] = bday
        if birth_name is not UNSET:
            field_dict["birthName"] = birth_name
        if citizenship is not UNSET:
            field_dict["citizenship"] = citizenship
        if current_address is not UNSET:
            field_dict["currentAddress"] = current_address
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if given_names is not UNSET:
            field_dict["givenNames"] = given_names
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if place_of_birth is not UNSET:
            field_dict["placeOfBirth"] = place_of_birth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.eu_emrex_elmo_country_code import EuEmrexElmoCountryCode  # noqa: PLC0415
        from ..models.eu_emrex_elmo_elmo_learner_identifier import EuEmrexElmoElmoLearnerIdentifier  # noqa: PLC0415
        from ..models.eu_emrex_elmo_flexible_address import EuEmrexElmoFlexibleAddress  # noqa: PLC0415
        from ..models.java_math_big_integer import JavaMathBigInteger  # noqa: PLC0415
        from ..models.java_util_calendar import JavaUtilCalendar  # noqa: PLC0415

        d = dict(src_dict)
        _bday = d.pop("bday", UNSET)
        bday: JavaUtilCalendar | Unset
        if isinstance(_bday, Unset):
            bday = UNSET
        else:
            bday = JavaUtilCalendar.from_dict(_bday)

        birth_name = d.pop("birthName", UNSET)

        _citizenship = d.pop("citizenship", UNSET)
        citizenship: EuEmrexElmoCountryCode | Unset
        if isinstance(_citizenship, Unset):
            citizenship = UNSET
        else:
            citizenship = EuEmrexElmoCountryCode.from_dict(_citizenship)

        _current_address = d.pop("currentAddress", UNSET)
        current_address: EuEmrexElmoFlexibleAddress | Unset
        if isinstance(_current_address, Unset):
            current_address = UNSET
        else:
            current_address = EuEmrexElmoFlexibleAddress.from_dict(_current_address)

        family_name = d.pop("familyName", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: JavaMathBigInteger | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = JavaMathBigInteger.from_dict(_gender)

        given_names = d.pop("givenNames", UNSET)

        _identifier = d.pop("identifier", UNSET)
        identifier: list[EuEmrexElmoElmoLearnerIdentifier] | Unset = UNSET
        if _identifier is not UNSET:
            identifier = []
            for identifier_item_data in _identifier:
                identifier_item = EuEmrexElmoElmoLearnerIdentifier.from_dict(identifier_item_data)

                identifier.append(identifier_item)

        place_of_birth = d.pop("placeOfBirth", UNSET)

        eu_emrex_elmo_elmo_learner = cls(
            bday=bday,
            birth_name=birth_name,
            citizenship=citizenship,
            current_address=current_address,
            family_name=family_name,
            gender=gender,
            given_names=given_names,
            identifier=identifier,
            place_of_birth=place_of_birth,
        )

        eu_emrex_elmo_elmo_learner.additional_properties = d
        return eu_emrex_elmo_elmo_learner

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
