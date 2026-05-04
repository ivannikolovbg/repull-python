from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.studio_deployment_status import StudioDeploymentStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="StudioDeployment")



@_attrs_define
class StudioDeployment:
    """ A deployed instance of a Studio project, served from a `*.studio.repull.dev` subdomain.

        Attributes:
            deployment_id (UUID | Unset):
            project_id (UUID | Unset):
            subdomain (str | Unset): Subdomain assigned to this deployment (e.g. `my-app-a1b2c3`).
            status (StudioDeploymentStatus | Unset): Current deployment lifecycle status.
            url (str | Unset): Fully-qualified URL where the deployment is reachable when `status` is `live`.
            created_at (datetime.datetime | Unset):
            suspended_at (datetime.datetime | None | Unset): Set when the deployment is paused via `/suspend`.
     """

    deployment_id: UUID | Unset = UNSET
    project_id: UUID | Unset = UNSET
    subdomain: str | Unset = UNSET
    status: StudioDeploymentStatus | Unset = UNSET
    url: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    suspended_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        deployment_id: str | Unset = UNSET
        if not isinstance(self.deployment_id, Unset):
            deployment_id = str(self.deployment_id)

        project_id: str | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = str(self.project_id)

        subdomain = self.subdomain

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        url = self.url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        suspended_at: None | str | Unset
        if isinstance(self.suspended_at, Unset):
            suspended_at = UNSET
        elif isinstance(self.suspended_at, datetime.datetime):
            suspended_at = self.suspended_at.isoformat()
        else:
            suspended_at = self.suspended_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if deployment_id is not UNSET:
            field_dict["deployment_id"] = deployment_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if suspended_at is not UNSET:
            field_dict["suspended_at"] = suspended_at

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




        _project_id = d.pop("project_id", UNSET)
        project_id: UUID | Unset
        if isinstance(_project_id,  Unset):
            project_id = UNSET
        else:
            project_id = UUID(_project_id)




        subdomain = d.pop("subdomain", UNSET)

        _status = d.pop("status", UNSET)
        status: StudioDeploymentStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = StudioDeploymentStatus(_status)




        url = d.pop("url", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        def _parse_suspended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_at_type_0 = isoparse(data)



                return suspended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        suspended_at = _parse_suspended_at(d.pop("suspended_at", UNSET))


        studio_deployment = cls(
            deployment_id=deployment_id,
            project_id=project_id,
            subdomain=subdomain,
            status=status,
            url=url,
            created_at=created_at,
            suspended_at=suspended_at,
        )


        studio_deployment.additional_properties = d
        return studio_deployment

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
