from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.common_term_type_value_termcategory import CommonTermTypeValueTermcategory
    from ..models.cs_sys_value_term_type_value_meta import CsSysValueTermTypeValueMeta
    from ..models.java_util_locale import JavaUtilLocale


T = TypeVar("T", bound="CsSysValueTermTypeValue")


@_attrs_define
class CsSysValueTermTypeValue:
    """
    Attributes:
        applied_contexts (list[str] | Unset):
        defaultlanguage (int | Unset):
        defaultlanguage_original_value (int | Unset):
        defaultlanguage_set (bool | Unset):
        defaulttext (str | Unset):
        defaulttext_original_value (str | Unset):
        defaulttext_set (bool | Unset):
        dirty (bool | Unset):
        dto_id (str | Unset):
        i_18_n_attributes_as_list (list[str] | Unset):
        id (int | Unset):
        load_version_date (Any | Unset):
        load_version_date_original_value (Any | Unset):
        load_version_date_set (bool | Unset):
        lock_version (int | Unset):
        longtext (str | Unset):
        longtext_original_value (str | Unset):
        longtext_set (bool | Unset):
        meta (CsSysValueTermTypeValueMeta | Unset):
        metadata_possibly_customized (bool | Unset):
        obj_address (str | Unset):
        obj_guid (str | Unset):
        object_locale (JavaUtilLocale | Unset):
        object_locale_original_value (JavaUtilLocale | Unset):
        object_locale_set (bool | Unset):
        shorttext (str | Unset):
        shorttext_original_value (str | Unset):
        shorttext_set (bool | Unset):
        sortorder (int | Unset):
        sortorder_original_value (int | Unset):
        sortorder_set (bool | Unset):
        term_category (int | Unset):
        term_category_original_value (int | Unset):
        term_category_set (bool | Unset):
        term_category_value (CommonTermTypeValueTermcategory | Unset):
        term_category_value_original_value (CommonTermTypeValueTermcategory | Unset):
        term_category_value_set (bool | Unset):
        term_number (int | Unset):
        term_number_original_value (int | Unset):
        term_number_set (bool | Unset):
        uniquename (str | Unset):
        uniquename_original_value (str | Unset):
        uniquename_set (bool | Unset):
    """

    applied_contexts: list[str] | Unset = UNSET
    defaultlanguage: int | Unset = UNSET
    defaultlanguage_original_value: int | Unset = UNSET
    defaultlanguage_set: bool | Unset = UNSET
    defaulttext: str | Unset = UNSET
    defaulttext_original_value: str | Unset = UNSET
    defaulttext_set: bool | Unset = UNSET
    dirty: bool | Unset = UNSET
    dto_id: str | Unset = UNSET
    i_18_n_attributes_as_list: list[str] | Unset = UNSET
    id: int | Unset = UNSET
    load_version_date: Any | Unset = UNSET
    load_version_date_original_value: Any | Unset = UNSET
    load_version_date_set: bool | Unset = UNSET
    lock_version: int | Unset = UNSET
    longtext: str | Unset = UNSET
    longtext_original_value: str | Unset = UNSET
    longtext_set: bool | Unset = UNSET
    meta: CsSysValueTermTypeValueMeta | Unset = UNSET
    metadata_possibly_customized: bool | Unset = UNSET
    obj_address: str | Unset = UNSET
    obj_guid: str | Unset = UNSET
    object_locale: JavaUtilLocale | Unset = UNSET
    object_locale_original_value: JavaUtilLocale | Unset = UNSET
    object_locale_set: bool | Unset = UNSET
    shorttext: str | Unset = UNSET
    shorttext_original_value: str | Unset = UNSET
    shorttext_set: bool | Unset = UNSET
    sortorder: int | Unset = UNSET
    sortorder_original_value: int | Unset = UNSET
    sortorder_set: bool | Unset = UNSET
    term_category: int | Unset = UNSET
    term_category_original_value: int | Unset = UNSET
    term_category_set: bool | Unset = UNSET
    term_category_value: CommonTermTypeValueTermcategory | Unset = UNSET
    term_category_value_original_value: CommonTermTypeValueTermcategory | Unset = UNSET
    term_category_value_set: bool | Unset = UNSET
    term_number: int | Unset = UNSET
    term_number_original_value: int | Unset = UNSET
    term_number_set: bool | Unset = UNSET
    uniquename: str | Unset = UNSET
    uniquename_original_value: str | Unset = UNSET
    uniquename_set: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        applied_contexts: list[str] | Unset = UNSET
        if not isinstance(self.applied_contexts, Unset):
            applied_contexts = self.applied_contexts

        defaultlanguage = self.defaultlanguage

        defaultlanguage_original_value = self.defaultlanguage_original_value

        defaultlanguage_set = self.defaultlanguage_set

        defaulttext = self.defaulttext

        defaulttext_original_value = self.defaulttext_original_value

        defaulttext_set = self.defaulttext_set

        dirty = self.dirty

        dto_id = self.dto_id

        i_18_n_attributes_as_list: list[str] | Unset = UNSET
        if not isinstance(self.i_18_n_attributes_as_list, Unset):
            i_18_n_attributes_as_list = self.i_18_n_attributes_as_list

        id = self.id

        load_version_date = self.load_version_date

        load_version_date_original_value = self.load_version_date_original_value

        load_version_date_set = self.load_version_date_set

        lock_version = self.lock_version

        longtext = self.longtext

        longtext_original_value = self.longtext_original_value

        longtext_set = self.longtext_set

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        metadata_possibly_customized = self.metadata_possibly_customized

        obj_address = self.obj_address

        obj_guid = self.obj_guid

        object_locale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_locale, Unset):
            object_locale = self.object_locale.to_dict()

        object_locale_original_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_locale_original_value, Unset):
            object_locale_original_value = self.object_locale_original_value.to_dict()

        object_locale_set = self.object_locale_set

        shorttext = self.shorttext

        shorttext_original_value = self.shorttext_original_value

        shorttext_set = self.shorttext_set

        sortorder = self.sortorder

        sortorder_original_value = self.sortorder_original_value

        sortorder_set = self.sortorder_set

        term_category = self.term_category

        term_category_original_value = self.term_category_original_value

        term_category_set = self.term_category_set

        term_category_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.term_category_value, Unset):
            term_category_value = self.term_category_value.to_dict()

        term_category_value_original_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.term_category_value_original_value, Unset):
            term_category_value_original_value = self.term_category_value_original_value.to_dict()

        term_category_value_set = self.term_category_value_set

        term_number = self.term_number

        term_number_original_value = self.term_number_original_value

        term_number_set = self.term_number_set

        uniquename = self.uniquename

        uniquename_original_value = self.uniquename_original_value

        uniquename_set = self.uniquename_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied_contexts is not UNSET:
            field_dict["appliedContexts"] = applied_contexts
        if defaultlanguage is not UNSET:
            field_dict["defaultlanguage"] = defaultlanguage
        if defaultlanguage_original_value is not UNSET:
            field_dict["defaultlanguageOriginalValue"] = defaultlanguage_original_value
        if defaultlanguage_set is not UNSET:
            field_dict["defaultlanguageSet"] = defaultlanguage_set
        if defaulttext is not UNSET:
            field_dict["defaulttext"] = defaulttext
        if defaulttext_original_value is not UNSET:
            field_dict["defaulttextOriginalValue"] = defaulttext_original_value
        if defaulttext_set is not UNSET:
            field_dict["defaulttextSet"] = defaulttext_set
        if dirty is not UNSET:
            field_dict["dirty"] = dirty
        if dto_id is not UNSET:
            field_dict["dtoId"] = dto_id
        if i_18_n_attributes_as_list is not UNSET:
            field_dict["i18nAttributesAsList"] = i_18_n_attributes_as_list
        if id is not UNSET:
            field_dict["id"] = id
        if load_version_date is not UNSET:
            field_dict["loadVersionDate"] = load_version_date
        if load_version_date_original_value is not UNSET:
            field_dict["loadVersionDateOriginalValue"] = load_version_date_original_value
        if load_version_date_set is not UNSET:
            field_dict["loadVersionDateSet"] = load_version_date_set
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if longtext is not UNSET:
            field_dict["longtext"] = longtext
        if longtext_original_value is not UNSET:
            field_dict["longtextOriginalValue"] = longtext_original_value
        if longtext_set is not UNSET:
            field_dict["longtextSet"] = longtext_set
        if meta is not UNSET:
            field_dict["meta"] = meta
        if metadata_possibly_customized is not UNSET:
            field_dict["metadataPossiblyCustomized"] = metadata_possibly_customized
        if obj_address is not UNSET:
            field_dict["objAddress"] = obj_address
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if object_locale is not UNSET:
            field_dict["objectLocale"] = object_locale
        if object_locale_original_value is not UNSET:
            field_dict["objectLocaleOriginalValue"] = object_locale_original_value
        if object_locale_set is not UNSET:
            field_dict["objectLocaleSet"] = object_locale_set
        if shorttext is not UNSET:
            field_dict["shorttext"] = shorttext
        if shorttext_original_value is not UNSET:
            field_dict["shorttextOriginalValue"] = shorttext_original_value
        if shorttext_set is not UNSET:
            field_dict["shorttextSet"] = shorttext_set
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder
        if sortorder_original_value is not UNSET:
            field_dict["sortorderOriginalValue"] = sortorder_original_value
        if sortorder_set is not UNSET:
            field_dict["sortorderSet"] = sortorder_set
        if term_category is not UNSET:
            field_dict["termCategory"] = term_category
        if term_category_original_value is not UNSET:
            field_dict["termCategoryOriginalValue"] = term_category_original_value
        if term_category_set is not UNSET:
            field_dict["termCategorySet"] = term_category_set
        if term_category_value is not UNSET:
            field_dict["termCategoryValue"] = term_category_value
        if term_category_value_original_value is not UNSET:
            field_dict["termCategoryValueOriginalValue"] = term_category_value_original_value
        if term_category_value_set is not UNSET:
            field_dict["termCategoryValueSet"] = term_category_value_set
        if term_number is not UNSET:
            field_dict["termNumber"] = term_number
        if term_number_original_value is not UNSET:
            field_dict["termNumberOriginalValue"] = term_number_original_value
        if term_number_set is not UNSET:
            field_dict["termNumberSet"] = term_number_set
        if uniquename is not UNSET:
            field_dict["uniquename"] = uniquename
        if uniquename_original_value is not UNSET:
            field_dict["uniquenameOriginalValue"] = uniquename_original_value
        if uniquename_set is not UNSET:
            field_dict["uniquenameSet"] = uniquename_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.common_term_type_value_termcategory import CommonTermTypeValueTermcategory  # noqa: PLC0415
        from ..models.cs_sys_value_term_type_value_meta import CsSysValueTermTypeValueMeta  # noqa: PLC0415
        from ..models.java_util_locale import JavaUtilLocale  # noqa: PLC0415

        d = dict(src_dict)
        applied_contexts = cast(list[str], d.pop("appliedContexts", UNSET))

        defaultlanguage = d.pop("defaultlanguage", UNSET)

        defaultlanguage_original_value = d.pop("defaultlanguageOriginalValue", UNSET)

        defaultlanguage_set = d.pop("defaultlanguageSet", UNSET)

        defaulttext = d.pop("defaulttext", UNSET)

        defaulttext_original_value = d.pop("defaulttextOriginalValue", UNSET)

        defaulttext_set = d.pop("defaulttextSet", UNSET)

        dirty = d.pop("dirty", UNSET)

        dto_id = d.pop("dtoId", UNSET)

        i_18_n_attributes_as_list = cast(list[str], d.pop("i18nAttributesAsList", UNSET))

        id = d.pop("id", UNSET)

        load_version_date = d.pop("loadVersionDate", UNSET)

        load_version_date_original_value = d.pop("loadVersionDateOriginalValue", UNSET)

        load_version_date_set = d.pop("loadVersionDateSet", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        longtext = d.pop("longtext", UNSET)

        longtext_original_value = d.pop("longtextOriginalValue", UNSET)

        longtext_set = d.pop("longtextSet", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: CsSysValueTermTypeValueMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = CsSysValueTermTypeValueMeta.from_dict(_meta)

        metadata_possibly_customized = d.pop("metadataPossiblyCustomized", UNSET)

        obj_address = d.pop("objAddress", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        _object_locale = d.pop("objectLocale", UNSET)
        object_locale: JavaUtilLocale | Unset
        if isinstance(_object_locale, Unset):
            object_locale = UNSET
        else:
            object_locale = JavaUtilLocale.from_dict(_object_locale)

        _object_locale_original_value = d.pop("objectLocaleOriginalValue", UNSET)
        object_locale_original_value: JavaUtilLocale | Unset
        if isinstance(_object_locale_original_value, Unset):
            object_locale_original_value = UNSET
        else:
            object_locale_original_value = JavaUtilLocale.from_dict(_object_locale_original_value)

        object_locale_set = d.pop("objectLocaleSet", UNSET)

        shorttext = d.pop("shorttext", UNSET)

        shorttext_original_value = d.pop("shorttextOriginalValue", UNSET)

        shorttext_set = d.pop("shorttextSet", UNSET)

        sortorder = d.pop("sortorder", UNSET)

        sortorder_original_value = d.pop("sortorderOriginalValue", UNSET)

        sortorder_set = d.pop("sortorderSet", UNSET)

        term_category = d.pop("termCategory", UNSET)

        term_category_original_value = d.pop("termCategoryOriginalValue", UNSET)

        term_category_set = d.pop("termCategorySet", UNSET)

        _term_category_value = d.pop("termCategoryValue", UNSET)
        term_category_value: CommonTermTypeValueTermcategory | Unset
        if isinstance(_term_category_value, Unset):
            term_category_value = UNSET
        else:
            term_category_value = CommonTermTypeValueTermcategory.from_dict(_term_category_value)

        _term_category_value_original_value = d.pop("termCategoryValueOriginalValue", UNSET)
        term_category_value_original_value: CommonTermTypeValueTermcategory | Unset
        if isinstance(_term_category_value_original_value, Unset):
            term_category_value_original_value = UNSET
        else:
            term_category_value_original_value = CommonTermTypeValueTermcategory.from_dict(
                _term_category_value_original_value
            )

        term_category_value_set = d.pop("termCategoryValueSet", UNSET)

        term_number = d.pop("termNumber", UNSET)

        term_number_original_value = d.pop("termNumberOriginalValue", UNSET)

        term_number_set = d.pop("termNumberSet", UNSET)

        uniquename = d.pop("uniquename", UNSET)

        uniquename_original_value = d.pop("uniquenameOriginalValue", UNSET)

        uniquename_set = d.pop("uniquenameSet", UNSET)

        cs_sys_value_term_type_value = cls(
            applied_contexts=applied_contexts,
            defaultlanguage=defaultlanguage,
            defaultlanguage_original_value=defaultlanguage_original_value,
            defaultlanguage_set=defaultlanguage_set,
            defaulttext=defaulttext,
            defaulttext_original_value=defaulttext_original_value,
            defaulttext_set=defaulttext_set,
            dirty=dirty,
            dto_id=dto_id,
            i_18_n_attributes_as_list=i_18_n_attributes_as_list,
            id=id,
            load_version_date=load_version_date,
            load_version_date_original_value=load_version_date_original_value,
            load_version_date_set=load_version_date_set,
            lock_version=lock_version,
            longtext=longtext,
            longtext_original_value=longtext_original_value,
            longtext_set=longtext_set,
            meta=meta,
            metadata_possibly_customized=metadata_possibly_customized,
            obj_address=obj_address,
            obj_guid=obj_guid,
            object_locale=object_locale,
            object_locale_original_value=object_locale_original_value,
            object_locale_set=object_locale_set,
            shorttext=shorttext,
            shorttext_original_value=shorttext_original_value,
            shorttext_set=shorttext_set,
            sortorder=sortorder,
            sortorder_original_value=sortorder_original_value,
            sortorder_set=sortorder_set,
            term_category=term_category,
            term_category_original_value=term_category_original_value,
            term_category_set=term_category_set,
            term_category_value=term_category_value,
            term_category_value_original_value=term_category_value_original_value,
            term_category_value_set=term_category_value_set,
            term_number=term_number,
            term_number_original_value=term_number_original_value,
            term_number_set=term_number_set,
            uniquename=uniquename,
            uniquename_original_value=uniquename_original_value,
            uniquename_set=uniquename_set,
        )

        cs_sys_value_term_type_value.additional_properties = d
        return cs_sys_value_term_type_value

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
