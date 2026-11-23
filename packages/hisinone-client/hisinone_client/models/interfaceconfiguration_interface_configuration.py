from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceconfigurationInterfaceConfiguration")


@_attrs_define
class InterfaceconfigurationInterfaceConfiguration:
    """
    Attributes:
        add_non_zdb_journals (bool | Unset):
        apikey (str | Unset):
        class_name (str | Unset):
        conf_source (str | Unset):
        database_identifier (str | Unset):
        default_import_status_id (int | Unset):
        default_visibility_id (int | Unset):
        doi_lookup (bool | Unset):
        duplicate_check (bool | Unset):
        his_repo_type (str | Unset):
        id_only_search (bool | Unset):
        import_kettle_job_name (str | Unset):
        import_keywords (bool | Unset):
        import_modus_initial (bool | Unset):
        interface_identifier (str | Unset):
        interface_name (str | Unset):
        load_time_span (str | Unset):
        max_count_per_db (int | Unset):
        only_public (bool | Unset):
        override_openaccess_id (int | Unset):
        password_value (str | Unset):
        searchterm (str | Unset):
        time_between_requests (int | Unset):
        updateifstatus (str | Unset):
        url (str | Unset):
        username (str | Unset):
        yearlyimportstartyear (int | Unset):
        zdb_title_without_additions (bool | Unset):
    """

    add_non_zdb_journals: bool | Unset = UNSET
    apikey: str | Unset = UNSET
    class_name: str | Unset = UNSET
    conf_source: str | Unset = UNSET
    database_identifier: str | Unset = UNSET
    default_import_status_id: int | Unset = UNSET
    default_visibility_id: int | Unset = UNSET
    doi_lookup: bool | Unset = UNSET
    duplicate_check: bool | Unset = UNSET
    his_repo_type: str | Unset = UNSET
    id_only_search: bool | Unset = UNSET
    import_kettle_job_name: str | Unset = UNSET
    import_keywords: bool | Unset = UNSET
    import_modus_initial: bool | Unset = UNSET
    interface_identifier: str | Unset = UNSET
    interface_name: str | Unset = UNSET
    load_time_span: str | Unset = UNSET
    max_count_per_db: int | Unset = UNSET
    only_public: bool | Unset = UNSET
    override_openaccess_id: int | Unset = UNSET
    password_value: str | Unset = UNSET
    searchterm: str | Unset = UNSET
    time_between_requests: int | Unset = UNSET
    updateifstatus: str | Unset = UNSET
    url: str | Unset = UNSET
    username: str | Unset = UNSET
    yearlyimportstartyear: int | Unset = UNSET
    zdb_title_without_additions: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        add_non_zdb_journals = self.add_non_zdb_journals

        apikey = self.apikey

        class_name = self.class_name

        conf_source = self.conf_source

        database_identifier = self.database_identifier

        default_import_status_id = self.default_import_status_id

        default_visibility_id = self.default_visibility_id

        doi_lookup = self.doi_lookup

        duplicate_check = self.duplicate_check

        his_repo_type = self.his_repo_type

        id_only_search = self.id_only_search

        import_kettle_job_name = self.import_kettle_job_name

        import_keywords = self.import_keywords

        import_modus_initial = self.import_modus_initial

        interface_identifier = self.interface_identifier

        interface_name = self.interface_name

        load_time_span = self.load_time_span

        max_count_per_db = self.max_count_per_db

        only_public = self.only_public

        override_openaccess_id = self.override_openaccess_id

        password_value = self.password_value

        searchterm = self.searchterm

        time_between_requests = self.time_between_requests

        updateifstatus = self.updateifstatus

        url = self.url

        username = self.username

        yearlyimportstartyear = self.yearlyimportstartyear

        zdb_title_without_additions = self.zdb_title_without_additions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_non_zdb_journals is not UNSET:
            field_dict["addNonZdbJournals"] = add_non_zdb_journals
        if apikey is not UNSET:
            field_dict["apikey"] = apikey
        if class_name is not UNSET:
            field_dict["className"] = class_name
        if conf_source is not UNSET:
            field_dict["confSource"] = conf_source
        if database_identifier is not UNSET:
            field_dict["databaseIdentifier"] = database_identifier
        if default_import_status_id is not UNSET:
            field_dict["defaultImportStatusId"] = default_import_status_id
        if default_visibility_id is not UNSET:
            field_dict["defaultVisibilityId"] = default_visibility_id
        if doi_lookup is not UNSET:
            field_dict["doiLookup"] = doi_lookup
        if duplicate_check is not UNSET:
            field_dict["duplicateCheck"] = duplicate_check
        if his_repo_type is not UNSET:
            field_dict["hisRepoType"] = his_repo_type
        if id_only_search is not UNSET:
            field_dict["idOnlySearch"] = id_only_search
        if import_kettle_job_name is not UNSET:
            field_dict["importKettleJobName"] = import_kettle_job_name
        if import_keywords is not UNSET:
            field_dict["importKeywords"] = import_keywords
        if import_modus_initial is not UNSET:
            field_dict["importModusInitial"] = import_modus_initial
        if interface_identifier is not UNSET:
            field_dict["interfaceIdentifier"] = interface_identifier
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if load_time_span is not UNSET:
            field_dict["loadTimeSpan"] = load_time_span
        if max_count_per_db is not UNSET:
            field_dict["maxCountPerDB"] = max_count_per_db
        if only_public is not UNSET:
            field_dict["onlyPublic"] = only_public
        if override_openaccess_id is not UNSET:
            field_dict["overrideOpenaccessId"] = override_openaccess_id
        if password_value is not UNSET:
            field_dict["passwordValue"] = password_value
        if searchterm is not UNSET:
            field_dict["searchterm"] = searchterm
        if time_between_requests is not UNSET:
            field_dict["timeBetweenRequests"] = time_between_requests
        if updateifstatus is not UNSET:
            field_dict["updateifstatus"] = updateifstatus
        if url is not UNSET:
            field_dict["url"] = url
        if username is not UNSET:
            field_dict["username"] = username
        if yearlyimportstartyear is not UNSET:
            field_dict["yearlyimportstartyear"] = yearlyimportstartyear
        if zdb_title_without_additions is not UNSET:
            field_dict["zdbTitleWithoutAdditions"] = zdb_title_without_additions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add_non_zdb_journals = d.pop("addNonZdbJournals", UNSET)

        apikey = d.pop("apikey", UNSET)

        class_name = d.pop("className", UNSET)

        conf_source = d.pop("confSource", UNSET)

        database_identifier = d.pop("databaseIdentifier", UNSET)

        default_import_status_id = d.pop("defaultImportStatusId", UNSET)

        default_visibility_id = d.pop("defaultVisibilityId", UNSET)

        doi_lookup = d.pop("doiLookup", UNSET)

        duplicate_check = d.pop("duplicateCheck", UNSET)

        his_repo_type = d.pop("hisRepoType", UNSET)

        id_only_search = d.pop("idOnlySearch", UNSET)

        import_kettle_job_name = d.pop("importKettleJobName", UNSET)

        import_keywords = d.pop("importKeywords", UNSET)

        import_modus_initial = d.pop("importModusInitial", UNSET)

        interface_identifier = d.pop("interfaceIdentifier", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        load_time_span = d.pop("loadTimeSpan", UNSET)

        max_count_per_db = d.pop("maxCountPerDB", UNSET)

        only_public = d.pop("onlyPublic", UNSET)

        override_openaccess_id = d.pop("overrideOpenaccessId", UNSET)

        password_value = d.pop("passwordValue", UNSET)

        searchterm = d.pop("searchterm", UNSET)

        time_between_requests = d.pop("timeBetweenRequests", UNSET)

        updateifstatus = d.pop("updateifstatus", UNSET)

        url = d.pop("url", UNSET)

        username = d.pop("username", UNSET)

        yearlyimportstartyear = d.pop("yearlyimportstartyear", UNSET)

        zdb_title_without_additions = d.pop("zdbTitleWithoutAdditions", UNSET)

        interfaceconfiguration_interface_configuration = cls(
            add_non_zdb_journals=add_non_zdb_journals,
            apikey=apikey,
            class_name=class_name,
            conf_source=conf_source,
            database_identifier=database_identifier,
            default_import_status_id=default_import_status_id,
            default_visibility_id=default_visibility_id,
            doi_lookup=doi_lookup,
            duplicate_check=duplicate_check,
            his_repo_type=his_repo_type,
            id_only_search=id_only_search,
            import_kettle_job_name=import_kettle_job_name,
            import_keywords=import_keywords,
            import_modus_initial=import_modus_initial,
            interface_identifier=interface_identifier,
            interface_name=interface_name,
            load_time_span=load_time_span,
            max_count_per_db=max_count_per_db,
            only_public=only_public,
            override_openaccess_id=override_openaccess_id,
            password_value=password_value,
            searchterm=searchterm,
            time_between_requests=time_between_requests,
            updateifstatus=updateifstatus,
            url=url,
            username=username,
            yearlyimportstartyear=yearlyimportstartyear,
            zdb_title_without_additions=zdb_title_without_additions,
        )

        interfaceconfiguration_interface_configuration.additional_properties = d
        return interfaceconfiguration_interface_configuration

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
