from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workspace_created_via import WorkspaceCreatedVia
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Workspace")



@_attrs_define
class Workspace:
    """ A sub-workspace: one customer of yours, with its own connections, listings and data. Send its `workspaceId` as
    `X-Workspace-Id` to act on it.

        Attributes:
            workspace_id (str):  Example: 1204.
            name (str):  Example: Seaside Rentals.
            active (bool): `false` once the workspace was deactivated (`POST /v1/workspaces/{workspaceId}/deactivate`, or a
                deleted migration). Its data is kept.
            created_at (datetime.datetime):
            external_ref (None | str | Unset): Your own id for this customer, as you sent it. Example: acct_8812.
            created_via (WorkspaceCreatedVia | Unset): `connect` — opened by a Connect session; `migrate` — opened by Repull
                Migrate.
            deactivated_at (datetime.datetime | None | Unset): When the workspace was deactivated; null while active.
     """

    workspace_id: str
    name: str
    active: bool
    created_at: datetime.datetime
    external_ref: None | str | Unset = UNSET
    created_via: WorkspaceCreatedVia | Unset = UNSET
    deactivated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        name = self.name

        active = self.active

        created_at = self.created_at.isoformat()

        external_ref: None | str | Unset
        if isinstance(self.external_ref, Unset):
            external_ref = UNSET
        else:
            external_ref = self.external_ref

        created_via: str | Unset = UNSET
        if not isinstance(self.created_via, Unset):
            created_via = self.created_via.value


        deactivated_at: None | str | Unset
        if isinstance(self.deactivated_at, Unset):
            deactivated_at = UNSET
        elif isinstance(self.deactivated_at, datetime.datetime):
            deactivated_at = self.deactivated_at.isoformat()
        else:
            deactivated_at = self.deactivated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workspaceId": workspace_id,
            "name": name,
            "active": active,
            "createdAt": created_at,
        })
        if external_ref is not UNSET:
            field_dict["externalRef"] = external_ref
        if created_via is not UNSET:
            field_dict["createdVia"] = created_via
        if deactivated_at is not UNSET:
            field_dict["deactivatedAt"] = deactivated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        name = d.pop("name")

        active = d.pop("active")

        created_at = isoparse(d.pop("createdAt"))




        def _parse_external_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_ref = _parse_external_ref(d.pop("externalRef", UNSET))


        _created_via = d.pop("createdVia", UNSET)
        created_via: WorkspaceCreatedVia | Unset
        if isinstance(_created_via,  Unset):
            created_via = UNSET
        else:
            created_via = WorkspaceCreatedVia(_created_via)




        def _parse_deactivated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deactivated_at_type_0 = isoparse(data)



                return deactivated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deactivated_at = _parse_deactivated_at(d.pop("deactivatedAt", UNSET))


        workspace = cls(
            workspace_id=workspace_id,
            name=name,
            active=active,
            created_at=created_at,
            external_ref=external_ref,
            created_via=created_via,
            deactivated_at=deactivated_at,
        )


        workspace.additional_properties = d
        return workspace

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
