from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fs_res_publication_universal_import_publication_import_import_run import (
        FsResPublicationUniversalImportPublicationImportImportRun,
    )
    from ..models.fs_res_publication_universal_import_publication_to_import import (
        FsResPublicationUniversalImportPublicationToImport,
    )


T = TypeVar("T", bound="FsResPublicationUniversalImportPublicationImport")


@_attrs_define
class FsResPublicationUniversalImportPublicationImport:
    """
    Attributes:
        import_run (FsResPublicationUniversalImportPublicationImportImportRun | Unset):
        interface_name (str | Unset):
        person_id (int | Unset):
        publications (list[FsResPublicationUniversalImportPublicationToImport] | Unset):
    """

    import_run: FsResPublicationUniversalImportPublicationImportImportRun | Unset = UNSET
    interface_name: str | Unset = UNSET
    person_id: int | Unset = UNSET
    publications: list[FsResPublicationUniversalImportPublicationToImport] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        import_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.import_run, Unset):
            import_run = self.import_run.to_dict()

        interface_name = self.interface_name

        person_id = self.person_id

        publications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publications, Unset):
            publications = []
            for publications_item_data in self.publications:
                publications_item = publications_item_data.to_dict()
                publications.append(publications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if import_run is not UNSET:
            field_dict["importRun"] = import_run
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if publications is not UNSET:
            field_dict["publications"] = publications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_res_publication_universal_import_publication_import_import_run import (
            FsResPublicationUniversalImportPublicationImportImportRun,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_universal_import_publication_to_import import (
            FsResPublicationUniversalImportPublicationToImport,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _import_run = d.pop("importRun", UNSET)
        import_run: FsResPublicationUniversalImportPublicationImportImportRun | Unset
        if isinstance(_import_run, Unset):
            import_run = UNSET
        else:
            import_run = FsResPublicationUniversalImportPublicationImportImportRun.from_dict(_import_run)

        interface_name = d.pop("interfaceName", UNSET)

        person_id = d.pop("personId", UNSET)

        _publications = d.pop("publications", UNSET)
        publications: list[FsResPublicationUniversalImportPublicationToImport] | Unset = UNSET
        if _publications is not UNSET:
            publications = []
            for publications_item_data in _publications:
                publications_item = FsResPublicationUniversalImportPublicationToImport.from_dict(publications_item_data)

                publications.append(publications_item)

        fs_res_publication_universal_import_publication_import = cls(
            import_run=import_run,
            interface_name=interface_name,
            person_id=person_id,
            publications=publications,
        )

        fs_res_publication_universal_import_publication_import.additional_properties = d
        return fs_res_publication_universal_import_publication_import

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
