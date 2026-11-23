from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_sys_value_generic_value import CsSysValueGenericValue
    from ..models.fs_res_publication_publication import FsResPublicationPublication
    from ..models.fs_res_research_infrastructure_research_infrastructure_employment import (
        FsResResearchInfrastructureResearchInfrastructureEmployment,
    )
    from ..models.fs_res_research_infrastructure_research_infrastructure_foreigntext_type_0 import (
        FsResResearchInfrastructureResearchInfrastructureForeigntextType0,
    )
    from ..models.fs_res_research_infrastructure_research_infrastructure_listviews_type_0 import (
        FsResResearchInfrastructureResearchInfrastructureListviewsType0,
    )
    from ..models.fs_res_research_infrastructure_research_infrastructure_organisation import (
        FsResResearchInfrastructureResearchInfrastructureOrganisation,
    )
    from ..models.fs_res_research_infrastructure_research_infrastructure_usage import (
        FsResResearchInfrastructureResearchInfrastructureUsage,
    )
    from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent
    from ..models.impl_fs_res_language_value import ImplFsResLanguageValue


T = TypeVar("T", bound="FsResResearchInfrastructureResearchInfrastructure")


@_attrs_define
class FsResResearchInfrastructureResearchInfrastructure:
    """
    Attributes:
        field_dynamic_component (ImplCsSysDynamicDynamicComponent | Unset):
        field_foreigntext (FsResResearchInfrastructureResearchInfrastructureForeigntextType0 | None | Unset):
        description (None | str | Unset):
        id (int | Unset):
        language (ImplFsResLanguageValue | Unset):
        listviews (FsResResearchInfrastructureResearchInfrastructureListviewsType0 | None | Unset):
        lock_version (int | Unset):
        obj_guid (None | str | Unset):
        publications (list[FsResPublicationPublication] | Unset):
        research_infrastructure_access_kinds (list[CsSysValueGenericValue] | Unset):
        research_infrastructure_employments (list[FsResResearchInfrastructureResearchInfrastructureEmployment] | Unset):
        research_infrastructure_kind (CsSysValueGenericValue | Unset):
        research_infrastructure_organisations (list[FsResResearchInfrastructureResearchInfrastructureOrganisation] |
            Unset):
        research_infrastructure_type (CsSysValueGenericValue | Unset):
        research_infrastructure_usages (list[FsResResearchInfrastructureResearchInfrastructureUsage] | Unset):
        title (str | Unset):
        visibility_value (CsSysValueGenericValue | Unset):
    """

    field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset = UNSET
    field_foreigntext: FsResResearchInfrastructureResearchInfrastructureForeigntextType0 | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: int | Unset = UNSET
    language: ImplFsResLanguageValue | Unset = UNSET
    listviews: FsResResearchInfrastructureResearchInfrastructureListviewsType0 | None | Unset = UNSET
    lock_version: int | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    publications: list[FsResPublicationPublication] | Unset = UNSET
    research_infrastructure_access_kinds: list[CsSysValueGenericValue] | Unset = UNSET
    research_infrastructure_employments: list[FsResResearchInfrastructureResearchInfrastructureEmployment] | Unset = (
        UNSET
    )
    research_infrastructure_kind: CsSysValueGenericValue | Unset = UNSET
    research_infrastructure_organisations: (
        list[FsResResearchInfrastructureResearchInfrastructureOrganisation] | Unset
    ) = UNSET
    research_infrastructure_type: CsSysValueGenericValue | Unset = UNSET
    research_infrastructure_usages: list[FsResResearchInfrastructureResearchInfrastructureUsage] | Unset = UNSET
    title: str | Unset = UNSET
    visibility_value: CsSysValueGenericValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_res_research_infrastructure_research_infrastructure_foreigntext_type_0 import (
            FsResResearchInfrastructureResearchInfrastructureForeigntextType0,  # noqa: PLC0415
        )
        from ..models.fs_res_research_infrastructure_research_infrastructure_listviews_type_0 import (
            FsResResearchInfrastructureResearchInfrastructureListviewsType0,  # noqa: PLC0415
        )

        field_dynamic_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_dynamic_component, Unset):
            field_dynamic_component = self.field_dynamic_component.to_dict()

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResResearchInfrastructureResearchInfrastructureForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id = self.id

        language: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        listviews: dict[str, Any] | None | Unset
        if isinstance(self.listviews, Unset):
            listviews = UNSET
        elif isinstance(self.listviews, FsResResearchInfrastructureResearchInfrastructureListviewsType0):
            listviews = self.listviews.to_dict()
        else:
            listviews = self.listviews

        lock_version = self.lock_version

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        publications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publications, Unset):
            publications = []
            for publications_item_data in self.publications:
                publications_item = publications_item_data.to_dict()
                publications.append(publications_item)

        research_infrastructure_access_kinds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_infrastructure_access_kinds, Unset):
            research_infrastructure_access_kinds = []
            for research_infrastructure_access_kinds_item_data in self.research_infrastructure_access_kinds:
                research_infrastructure_access_kinds_item = research_infrastructure_access_kinds_item_data.to_dict()
                research_infrastructure_access_kinds.append(research_infrastructure_access_kinds_item)

        research_infrastructure_employments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_infrastructure_employments, Unset):
            research_infrastructure_employments = []
            for research_infrastructure_employments_item_data in self.research_infrastructure_employments:
                research_infrastructure_employments_item = research_infrastructure_employments_item_data.to_dict()
                research_infrastructure_employments.append(research_infrastructure_employments_item)

        research_infrastructure_kind: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_infrastructure_kind, Unset):
            research_infrastructure_kind = self.research_infrastructure_kind.to_dict()

        research_infrastructure_organisations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_infrastructure_organisations, Unset):
            research_infrastructure_organisations = []
            for research_infrastructure_organisations_item_data in self.research_infrastructure_organisations:
                research_infrastructure_organisations_item = research_infrastructure_organisations_item_data.to_dict()
                research_infrastructure_organisations.append(research_infrastructure_organisations_item)

        research_infrastructure_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.research_infrastructure_type, Unset):
            research_infrastructure_type = self.research_infrastructure_type.to_dict()

        research_infrastructure_usages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.research_infrastructure_usages, Unset):
            research_infrastructure_usages = []
            for research_infrastructure_usages_item_data in self.research_infrastructure_usages:
                research_infrastructure_usages_item = research_infrastructure_usages_item_data.to_dict()
                research_infrastructure_usages.append(research_infrastructure_usages_item)

        title = self.title

        visibility_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_value, Unset):
            visibility_value = self.visibility_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_dynamic_component is not UNSET:
            field_dict["_dynamicComponent"] = field_dynamic_component
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if language is not UNSET:
            field_dict["language"] = language
        if listviews is not UNSET:
            field_dict["listviews"] = listviews
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if publications is not UNSET:
            field_dict["publications"] = publications
        if research_infrastructure_access_kinds is not UNSET:
            field_dict["researchInfrastructureAccessKinds"] = research_infrastructure_access_kinds
        if research_infrastructure_employments is not UNSET:
            field_dict["researchInfrastructureEmployments"] = research_infrastructure_employments
        if research_infrastructure_kind is not UNSET:
            field_dict["researchInfrastructureKind"] = research_infrastructure_kind
        if research_infrastructure_organisations is not UNSET:
            field_dict["researchInfrastructureOrganisations"] = research_infrastructure_organisations
        if research_infrastructure_type is not UNSET:
            field_dict["researchInfrastructureType"] = research_infrastructure_type
        if research_infrastructure_usages is not UNSET:
            field_dict["researchInfrastructureUsages"] = research_infrastructure_usages
        if title is not UNSET:
            field_dict["title"] = title
        if visibility_value is not UNSET:
            field_dict["visibilityValue"] = visibility_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_sys_value_generic_value import CsSysValueGenericValue  # noqa: PLC0415
        from ..models.fs_res_publication_publication import FsResPublicationPublication  # noqa: PLC0415
        from ..models.fs_res_research_infrastructure_research_infrastructure_employment import (
            FsResResearchInfrastructureResearchInfrastructureEmployment,  # noqa: PLC0415
        )
        from ..models.fs_res_research_infrastructure_research_infrastructure_foreigntext_type_0 import (
            FsResResearchInfrastructureResearchInfrastructureForeigntextType0,  # noqa: PLC0415
        )
        from ..models.fs_res_research_infrastructure_research_infrastructure_listviews_type_0 import (
            FsResResearchInfrastructureResearchInfrastructureListviewsType0,  # noqa: PLC0415
        )
        from ..models.fs_res_research_infrastructure_research_infrastructure_organisation import (
            FsResResearchInfrastructureResearchInfrastructureOrganisation,  # noqa: PLC0415
        )
        from ..models.fs_res_research_infrastructure_research_infrastructure_usage import (
            FsResResearchInfrastructureResearchInfrastructureUsage,  # noqa: PLC0415
        )
        from ..models.impl_cs_sys_dynamic_dynamic_component import ImplCsSysDynamicDynamicComponent  # noqa: PLC0415
        from ..models.impl_fs_res_language_value import ImplFsResLanguageValue  # noqa: PLC0415

        d = dict(src_dict)
        _field_dynamic_component = d.pop("_dynamicComponent", UNSET)
        field_dynamic_component: ImplCsSysDynamicDynamicComponent | Unset
        if isinstance(_field_dynamic_component, Unset):
            field_dynamic_component = UNSET
        else:
            field_dynamic_component = ImplCsSysDynamicDynamicComponent.from_dict(_field_dynamic_component)

        def _parse_field_foreigntext(
            data: object,
        ) -> FsResResearchInfrastructureResearchInfrastructureForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResResearchInfrastructureResearchInfrastructureForeigntextType0.from_dict(
                cast(dict[str, Any], data)
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        id = d.pop("id", UNSET)

        _language = d.pop("language", UNSET)
        language: ImplFsResLanguageValue | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = ImplFsResLanguageValue.from_dict(_language)

        def _parse_listviews(
            data: object,
        ) -> FsResResearchInfrastructureResearchInfrastructureListviewsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            listviews_type_0 = FsResResearchInfrastructureResearchInfrastructureListviewsType0.from_dict(
                cast(dict[str, Any], data)
            )

            return listviews_type_0

        listviews = _parse_listviews(d.pop("listviews", UNSET))

        lock_version = d.pop("lockVersion", UNSET)

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        _publications = d.pop("publications", UNSET)
        publications: list[FsResPublicationPublication] | Unset = UNSET
        if _publications is not UNSET:
            publications = []
            for publications_item_data in _publications:
                publications_item = FsResPublicationPublication.from_dict(publications_item_data)

                publications.append(publications_item)

        _research_infrastructure_access_kinds = d.pop("researchInfrastructureAccessKinds", UNSET)
        research_infrastructure_access_kinds: list[CsSysValueGenericValue] | Unset = UNSET
        if _research_infrastructure_access_kinds is not UNSET:
            research_infrastructure_access_kinds = []
            for research_infrastructure_access_kinds_item_data in _research_infrastructure_access_kinds:
                research_infrastructure_access_kinds_item = CsSysValueGenericValue.from_dict(
                    research_infrastructure_access_kinds_item_data
                )

                research_infrastructure_access_kinds.append(research_infrastructure_access_kinds_item)

        _research_infrastructure_employments = d.pop("researchInfrastructureEmployments", UNSET)
        research_infrastructure_employments: (
            list[FsResResearchInfrastructureResearchInfrastructureEmployment] | Unset
        ) = UNSET
        if _research_infrastructure_employments is not UNSET:
            research_infrastructure_employments = []
            for research_infrastructure_employments_item_data in _research_infrastructure_employments:
                research_infrastructure_employments_item = (
                    FsResResearchInfrastructureResearchInfrastructureEmployment.from_dict(
                        research_infrastructure_employments_item_data
                    )
                )

                research_infrastructure_employments.append(research_infrastructure_employments_item)

        _research_infrastructure_kind = d.pop("researchInfrastructureKind", UNSET)
        research_infrastructure_kind: CsSysValueGenericValue | Unset
        if isinstance(_research_infrastructure_kind, Unset):
            research_infrastructure_kind = UNSET
        else:
            research_infrastructure_kind = CsSysValueGenericValue.from_dict(_research_infrastructure_kind)

        _research_infrastructure_organisations = d.pop("researchInfrastructureOrganisations", UNSET)
        research_infrastructure_organisations: (
            list[FsResResearchInfrastructureResearchInfrastructureOrganisation] | Unset
        ) = UNSET
        if _research_infrastructure_organisations is not UNSET:
            research_infrastructure_organisations = []
            for research_infrastructure_organisations_item_data in _research_infrastructure_organisations:
                research_infrastructure_organisations_item = (
                    FsResResearchInfrastructureResearchInfrastructureOrganisation.from_dict(
                        research_infrastructure_organisations_item_data
                    )
                )

                research_infrastructure_organisations.append(research_infrastructure_organisations_item)

        _research_infrastructure_type = d.pop("researchInfrastructureType", UNSET)
        research_infrastructure_type: CsSysValueGenericValue | Unset
        if isinstance(_research_infrastructure_type, Unset):
            research_infrastructure_type = UNSET
        else:
            research_infrastructure_type = CsSysValueGenericValue.from_dict(_research_infrastructure_type)

        _research_infrastructure_usages = d.pop("researchInfrastructureUsages", UNSET)
        research_infrastructure_usages: list[FsResResearchInfrastructureResearchInfrastructureUsage] | Unset = UNSET
        if _research_infrastructure_usages is not UNSET:
            research_infrastructure_usages = []
            for research_infrastructure_usages_item_data in _research_infrastructure_usages:
                research_infrastructure_usages_item = FsResResearchInfrastructureResearchInfrastructureUsage.from_dict(
                    research_infrastructure_usages_item_data
                )

                research_infrastructure_usages.append(research_infrastructure_usages_item)

        title = d.pop("title", UNSET)

        _visibility_value = d.pop("visibilityValue", UNSET)
        visibility_value: CsSysValueGenericValue | Unset
        if isinstance(_visibility_value, Unset):
            visibility_value = UNSET
        else:
            visibility_value = CsSysValueGenericValue.from_dict(_visibility_value)

        fs_res_research_infrastructure_research_infrastructure = cls(
            field_dynamic_component=field_dynamic_component,
            field_foreigntext=field_foreigntext,
            description=description,
            id=id,
            language=language,
            listviews=listviews,
            lock_version=lock_version,
            obj_guid=obj_guid,
            publications=publications,
            research_infrastructure_access_kinds=research_infrastructure_access_kinds,
            research_infrastructure_employments=research_infrastructure_employments,
            research_infrastructure_kind=research_infrastructure_kind,
            research_infrastructure_organisations=research_infrastructure_organisations,
            research_infrastructure_type=research_infrastructure_type,
            research_infrastructure_usages=research_infrastructure_usages,
            title=title,
            visibility_value=visibility_value,
        )

        fs_res_research_infrastructure_research_infrastructure.additional_properties = d
        return fs_res_research_infrastructure_research_infrastructure

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
