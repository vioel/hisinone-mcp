from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cs_psv_person_rest import CsPsvPersonRest
    from ..models.fs_res_publication_publication_creator_foreigntext_type_0 import (
        FsResPublicationPublicationCreatorForeigntextType0,
    )
    from ..models.fs_res_publication_publication_creator_orgunit import FsResPublicationPublicationCreatorOrgunit


T = TypeVar("T", bound="FsResPublicationPublicationCreator")


@_attrs_define
class FsResPublicationPublicationCreator:
    """
    Attributes:
        field_foreigntext (FsResPublicationPublicationCreatorForeigntextType0 | None | Unset):
        creator_organizations (list[FsResPublicationPublicationCreatorOrgunit] | Unset):
        creatorname (str | Unset):
        email (None | str | Unset):
        firstname (str | Unset):
        has_visible_affiliations (bool | Unset):
        id (int | Unset):
        is_publication_contact (bool | None | Unset):
        lock_version (int | Unset):
        nameprefix (str | Unset):
        namesuffix (str | Unset):
        obj_guid (None | str | Unset):
        orcid (list[str] | None | Unset):
        person (CsPsvPersonRest | Unset):
        sortorder (int | Unset):
    """

    field_foreigntext: FsResPublicationPublicationCreatorForeigntextType0 | None | Unset = UNSET
    creator_organizations: list[FsResPublicationPublicationCreatorOrgunit] | Unset = UNSET
    creatorname: str | Unset = UNSET
    email: None | str | Unset = UNSET
    firstname: str | Unset = UNSET
    has_visible_affiliations: bool | Unset = UNSET
    id: int | Unset = UNSET
    is_publication_contact: bool | None | Unset = UNSET
    lock_version: int | Unset = UNSET
    nameprefix: str | Unset = UNSET
    namesuffix: str | Unset = UNSET
    obj_guid: None | str | Unset = UNSET
    orcid: list[str] | None | Unset = UNSET
    person: CsPsvPersonRest | Unset = UNSET
    sortorder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict[str, Any])

    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_res_publication_publication_creator_foreigntext_type_0 import (
            FsResPublicationPublicationCreatorForeigntextType0,  # noqa: PLC0415
        )

        field_foreigntext: dict[str, Any] | None | Unset
        if isinstance(self.field_foreigntext, Unset):
            field_foreigntext = UNSET
        elif isinstance(self.field_foreigntext, FsResPublicationPublicationCreatorForeigntextType0):
            field_foreigntext = self.field_foreigntext.to_dict()
        else:
            field_foreigntext = self.field_foreigntext

        creator_organizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator_organizations, Unset):
            creator_organizations = []
            for creator_organizations_item_data in self.creator_organizations:
                creator_organizations_item = creator_organizations_item_data.to_dict()
                creator_organizations.append(creator_organizations_item)

        creatorname = self.creatorname

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        firstname = self.firstname

        has_visible_affiliations = self.has_visible_affiliations

        id = self.id

        is_publication_contact: bool | None | Unset
        if isinstance(self.is_publication_contact, Unset):
            is_publication_contact = UNSET
        else:
            is_publication_contact = self.is_publication_contact

        lock_version = self.lock_version

        nameprefix = self.nameprefix

        namesuffix = self.namesuffix

        obj_guid: None | str | Unset
        if isinstance(self.obj_guid, Unset):
            obj_guid = UNSET
        else:
            obj_guid = self.obj_guid

        orcid: list[str] | None | Unset
        if isinstance(self.orcid, Unset):
            orcid = UNSET
        elif isinstance(self.orcid, list):
            orcid = self.orcid

        else:
            orcid = self.orcid

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        sortorder = self.sortorder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_foreigntext is not UNSET:
            field_dict["_foreigntext"] = field_foreigntext
        if creator_organizations is not UNSET:
            field_dict["creatorOrganizations"] = creator_organizations
        if creatorname is not UNSET:
            field_dict["creatorname"] = creatorname
        if email is not UNSET:
            field_dict["email"] = email
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if has_visible_affiliations is not UNSET:
            field_dict["hasVisibleAffiliations"] = has_visible_affiliations
        if id is not UNSET:
            field_dict["id"] = id
        if is_publication_contact is not UNSET:
            field_dict["isPublicationContact"] = is_publication_contact
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if nameprefix is not UNSET:
            field_dict["nameprefix"] = nameprefix
        if namesuffix is not UNSET:
            field_dict["namesuffix"] = namesuffix
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if orcid is not UNSET:
            field_dict["orcid"] = orcid
        if person is not UNSET:
            field_dict["person"] = person
        if sortorder is not UNSET:
            field_dict["sortorder"] = sortorder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cs_psv_person_rest import CsPsvPersonRest  # noqa: PLC0415
        from ..models.fs_res_publication_publication_creator_foreigntext_type_0 import (
            FsResPublicationPublicationCreatorForeigntextType0,  # noqa: PLC0415
        )
        from ..models.fs_res_publication_publication_creator_orgunit import FsResPublicationPublicationCreatorOrgunit  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_field_foreigntext(data: object) -> FsResPublicationPublicationCreatorForeigntextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            field_foreigntext_type_0 = FsResPublicationPublicationCreatorForeigntextType0.from_dict(
                cast(dict[str, Any], data)
            )

            return field_foreigntext_type_0

        field_foreigntext = _parse_field_foreigntext(d.pop("_foreigntext", UNSET))

        _creator_organizations = d.pop("creatorOrganizations", UNSET)
        creator_organizations: list[FsResPublicationPublicationCreatorOrgunit] | Unset = UNSET
        if _creator_organizations is not UNSET:
            creator_organizations = []
            for creator_organizations_item_data in _creator_organizations:
                creator_organizations_item = FsResPublicationPublicationCreatorOrgunit.from_dict(
                    creator_organizations_item_data
                )

                creator_organizations.append(creator_organizations_item)

        creatorname = d.pop("creatorname", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        firstname = d.pop("firstname", UNSET)

        has_visible_affiliations = d.pop("hasVisibleAffiliations", UNSET)

        id = d.pop("id", UNSET)

        def _parse_is_publication_contact(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_publication_contact = _parse_is_publication_contact(d.pop("isPublicationContact", UNSET))

        lock_version = d.pop("lockVersion", UNSET)

        nameprefix = d.pop("nameprefix", UNSET)

        namesuffix = d.pop("namesuffix", UNSET)

        def _parse_obj_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_guid = _parse_obj_guid(d.pop("objGuid", UNSET))

        def _parse_orcid(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            if not isinstance(data, list):
                raise TypeError()
            orcid_type_0 = cast(list[str], data)

            return orcid_type_0

        orcid = _parse_orcid(d.pop("orcid", UNSET))

        _person = d.pop("person", UNSET)
        person: CsPsvPersonRest | Unset
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CsPsvPersonRest.from_dict(_person)

        sortorder = d.pop("sortorder", UNSET)

        fs_res_publication_publication_creator = cls(
            field_foreigntext=field_foreigntext,
            creator_organizations=creator_organizations,
            creatorname=creatorname,
            email=email,
            firstname=firstname,
            has_visible_affiliations=has_visible_affiliations,
            id=id,
            is_publication_contact=is_publication_contact,
            lock_version=lock_version,
            nameprefix=nameprefix,
            namesuffix=namesuffix,
            obj_guid=obj_guid,
            orcid=orcid,
            person=person,
            sortorder=sortorder,
        )

        fs_res_publication_publication_creator.additional_properties = d
        return fs_res_publication_publication_creator

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
