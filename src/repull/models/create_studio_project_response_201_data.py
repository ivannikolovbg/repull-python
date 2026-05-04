from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_studio_project_response_201_data_status import CreateStudioProjectResponse201DataStatus
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="CreateStudioProjectResponse201Data")



@_attrs_define
class CreateStudioProjectResponse201Data:
    """ 
        Attributes:
            id (UUID | Unset):
            slug (str | Unset):
            status (CreateStudioProjectResponse201DataStatus | Unset):
     """

    id: UUID | Unset = UNSET
    slug: str | Unset = UNSET
    status: CreateStudioProjectResponse201DataStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        slug = self.slug

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if status is not UNSET:
            field_dict["status"] = status

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

        _status = d.pop("status", UNSET)
        status: CreateStudioProjectResponse201DataStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = CreateStudioProjectResponse201DataStatus(_status)




        create_studio_project_response_201_data = cls(
            id=id,
            slug=slug,
            status=status,
        )


        create_studio_project_response_201_data.additional_properties = d
        return create_studio_project_response_201_data

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
