from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_prize_nomination_prize_foreigntext import FsResPrizeNominationPrizeForeigntext
    from ..models.fs_res_prize_nomination_prize_orgunit import FsResPrizeNominationPrizeOrgunit
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResPrizeNominationPrize")


@_attrs_define
class FsResPrizeNominationPrize:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResPrizeNominationPrizeForeigntext | Unset):
        category (CsSysValueGenericValue | Unset):
        description (str | Unset):
        endowed (CsSysValueGenericValue | Unset):
        entry_date (int | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        lock_version (int | Unset):
        obj_guid (str | Unset):
        organizations (list[FsResPrizeNominationPrizeOrgunit] | Unset):
        status (CsSysValueGenericValue | Unset):
        subcategory (CsSysValueGenericValue | Unset):
        title (str | Unset):
        type_ (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResPrizeNominationPrizeForeigntext | Unset = UNSET
    category: CsSysValueGenericValue | Unset = UNSET
    description: str | Unset = UNSET
    endowed: CsSysValueGenericValue | Unset = UNSET
    entry_date: int | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: str | Unset = UNSET
    organizations: list[FsResPrizeNominationPrizeOrgunit] | Unset = UNSET
    status: CsSysValueGenericValue | Unset = UNSET
    subcategory: CsSysValueGenericValue | Unset = UNSET
    title: str | Unset = UNSET
    type_: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_foreigntext, Unset):
            field_foreigntext = self.field_foreigntext.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        description = self.description

        endowed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endowed, Unset):
            endowed = self.endowed.to_dict()

        entry_date = self.entry_date

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        lock_version = self.lock_version

        obj_guid = self.obj_guid

        organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        subcategory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subcategory, Unset):
            subcategory = self.subcategory.to_dict()

        title = self.title

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if endowed is not UNSET:
            field_dict["endowed"] = endowed
        if entry_date is not UNSET:
            field_dict["entryDate"] = entry_date
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if status is not UNSET:
            field_dict["status"] = status
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_prize_foreigntext import FsResPrizeNominationPrizeForeigntext  # noqa: PLC0415
        from ..models.fs_res_prize_nomination_prize_orgunit import FsResPrizeNominationPrizeOrgunit  # noqa: PLC0415
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        _field_foreigntext = d.pop("_foreigntext", UNSET)
        field_foreigntext: FsResPrizeNominationPrizeForeigntext | Unset
        if isinstance(_field_foreigntext, Unset):
            field_foreigntext = UNSET
        else:
            field_foreigntext = FsResPrizeNominationPrizeForeigntext.from_dict(_field_foreigntext)

        _category = d.pop("category", UNSET)
        category: CsSysValueGenericValue | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CsSysValueGenericValue.from_dict(_category)

        description = d.pop("description", UNSET)

        _endowed = d.pop("endowed", UNSET)
        endowed: CsSysValueGenericValue | Unset
        if isinstance(_endowed, Unset):
            endowed = UNSET
        else:
            endowed = CsSysValueGenericValue.from_dict(_endowed)

        entry_date = d.pop("entryDate", UNSET)

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        lock_version = d.pop("lockVersion", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _organizations = d.pop("organizations", UNSET)
        organizations: list[FsResPrizeNominationPrizeOrgunit] | Unset = UNSET
        if _organizations is not UNSET:
            organizations = []
            for organizations_item_data in _organizations:
                organizations_item = FsResPrizeNominationPrizeOrgunit.from_dict(organizations_item_data)

                organizations.append(organizations_item)

        _status = d.pop("status", UNSET)
        status: CsSysValueGenericValue | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CsSysValueGenericValue.from_dict(_status)

        _subcategory = d.pop("subcategory", UNSET)
        subcategory: CsSysValueGenericValue | Unset
        if isinstance(_subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = CsSysValueGenericValue.from_dict(_subcategory)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CsSysValueGenericValue | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CsSysValueGenericValue.from_dict(_type_)

        fs_res_prize_nomination_prize = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            category=category,
            description=description,
            endowed=endowed,
            entry_date=entry_date,
            id=id,
            language=language,
            lock_version=lock_version,
            obj_guid=obj_guid,
            organizations=organizations,
            status=status,
            subcategory=subcategory,
            title=title,
            type_=type_,
        )

        fs_res_prize_nomination_prize.additional_properties = d
        return fs_res_prize_nomination_prize

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
