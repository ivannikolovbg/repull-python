from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.studio_project_status import StudioProjectStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="StudioProject")



@_attrs_define
class StudioProject:
    """ A single Repull Studio project — a vibe-coded app generated from a prompt. Each project has its own files,
    generations, and deployments.

        Attributes:
            id (UUID | Unset): Project UUID.
            slug (str | Unset): URL-safe slug (unique within your account). Used for the deployment subdomain.
            name (str | Unset): Human-readable project name.
            prompt (None | str | Unset): Initial prompt that seeded the project.
            template_id (None | str | Unset): Template the project was scaffolded from, if any.
            status (StudioProjectStatus | Unset): Current project lifecycle status.
            customer_id (int | Unset): Owning Repull account ID.
            created_at (datetime.datetime | Unset):
            last_active_at (datetime.datetime | Unset): Updated whenever a file, generation, or deployment is touched.
            deleted_at (datetime.datetime | None | Unset): Soft-delete timestamp. `null` for live projects.
     """

    id: UUID | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    prompt: None | str | Unset = UNSET
    template_id: None | str | Unset = UNSET
    status: StudioProjectStatus | Unset = UNSET
    customer_id: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    last_active_at: datetime.datetime | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        slug = self.slug

        name = self.name

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        template_id: None | str | Unset
        if isinstance(self.template_id, Unset):
            template_id = UNSET
        else:
            template_id = self.template_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        customer_id = self.customer_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        last_active_at: str | Unset = UNSET
        if not isinstance(self.last_active_at, Unset):
            last_active_at = self.last_active_at.isoformat()

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if status is not UNSET:
            field_dict["status"] = status
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_active_at is not UNSET:
            field_dict["last_active_at"] = last_active_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))


        def _parse_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_id = _parse_template_id(d.pop("template_id", UNSET))


        _status = d.pop("status", UNSET)
        status: StudioProjectStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = StudioProjectStatus(_status)




        customer_id = d.pop("customer_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _last_active_at = d.pop("last_active_at", UNSET)
        last_active_at: datetime.datetime | Unset
        if isinstance(_last_active_at,  Unset):
            last_active_at = UNSET
        else:
            last_active_at = isoparse(_last_active_at)




        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)



                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))


        studio_project = cls(
            id=id,
            slug=slug,
            name=name,
            prompt=prompt,
            template_id=template_id,
            status=status,
            customer_id=customer_id,
            created_at=created_at,
            last_active_at=last_active_at,
            deleted_at=deleted_at,
        )


        studio_project.additional_properties = d
        return studio_project

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
