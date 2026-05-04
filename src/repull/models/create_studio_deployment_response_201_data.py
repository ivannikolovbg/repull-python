from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_studio_deployment_response_201_data_status import CreateStudioDeploymentResponse201DataStatus
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="CreateStudioDeploymentResponse201Data")



@_attrs_define
class CreateStudioDeploymentResponse201Data:
    """ 
        Attributes:
            deployment_id (UUID | Unset):
            subdomain (str | Unset):
            status (CreateStudioDeploymentResponse201DataStatus | Unset):
     """

    deployment_id: UUID | Unset = UNSET
    subdomain: str | Unset = UNSET
    status: CreateStudioDeploymentResponse201DataStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deployment_id: str | Unset = UNSET
        if not isinstance(self.deployment_id, Unset):
            deployment_id = str(self.deployment_id)

        subdomain = self.subdomain

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if deployment_id is not UNSET:
            field_dict["deployment_id"] = deployment_id
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _deployment_id = d.pop("deployment_id", UNSET)
        deployment_id: UUID | Unset
        if isinstance(_deployment_id,  Unset):
            deployment_id = UNSET
        else:
            deployment_id = UUID(_deployment_id)




        subdomain = d.pop("subdomain", UNSET)

        _status = d.pop("status", UNSET)
        status: CreateStudioDeploymentResponse201DataStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = CreateStudioDeploymentResponse201DataStatus(_status)




        create_studio_deployment_response_201_data = cls(
            deployment_id=deployment_id,
            subdomain=subdomain,
            status=status,
        )


        create_studio_deployment_response_201_data.additional_properties = d
        return create_studio_deployment_response_201_data

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
