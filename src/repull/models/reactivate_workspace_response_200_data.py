from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ReactivateWorkspaceResponse200Data")



@_attrs_define
class ReactivateWorkspaceResponse200Data:
    """ 
        Attributes:
            workspace_id (str | Unset):
            active (bool | Unset):
            reactivated_at (datetime.datetime | None | Unset): Null when the workspace was already active.
            already_active (bool | Unset): True when the workspace was already active — nothing was changed.
            listings_reactivated (list[str] | Unset): Listings switched back on.
            accounts_reconnect_required (bool | Unset): Accounts are never reconnected by this call.
            next_step (str | Unset): What to do next: reconnect the accounts through Connect.
     """

    workspace_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    reactivated_at: datetime.datetime | None | Unset = UNSET
    already_active: bool | Unset = UNSET
    listings_reactivated: list[str] | Unset = UNSET
    accounts_reconnect_required: bool | Unset = UNSET
    next_step: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        workspace_id = self.workspace_id

        active = self.active

        reactivated_at: None | str | Unset
        if isinstance(self.reactivated_at, Unset):
            reactivated_at = UNSET
        elif isinstance(self.reactivated_at, datetime.datetime):
            reactivated_at = self.reactivated_at.isoformat()
        else:
            reactivated_at = self.reactivated_at

        already_active = self.already_active

        listings_reactivated: list[str] | Unset = UNSET
        if not isinstance(self.listings_reactivated, Unset):
            listings_reactivated = self.listings_reactivated



        accounts_reconnect_required = self.accounts_reconnect_required

        next_step = self.next_step


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if active is not UNSET:
            field_dict["active"] = active
        if reactivated_at is not UNSET:
            field_dict["reactivatedAt"] = reactivated_at
        if already_active is not UNSET:
            field_dict["alreadyActive"] = already_active
        if listings_reactivated is not UNSET:
            field_dict["listingsReactivated"] = listings_reactivated
        if accounts_reconnect_required is not UNSET:
            field_dict["accountsReconnectRequired"] = accounts_reconnect_required
        if next_step is not UNSET:
            field_dict["nextStep"] = next_step

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        active = d.pop("active", UNSET)

        def _parse_reactivated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reactivated_at_type_0 = isoparse(data)



                return reactivated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reactivated_at = _parse_reactivated_at(d.pop("reactivatedAt", UNSET))


        already_active = d.pop("alreadyActive", UNSET)

        listings_reactivated = cast(list[str], d.pop("listingsReactivated", UNSET))


        accounts_reconnect_required = d.pop("accountsReconnectRequired", UNSET)

        next_step = d.pop("nextStep", UNSET)

        reactivate_workspace_response_200_data = cls(
            workspace_id=workspace_id,
            active=active,
            reactivated_at=reactivated_at,
            already_active=already_active,
            listings_reactivated=listings_reactivated,
            accounts_reconnect_required=accounts_reconnect_required,
            next_step=next_step,
        )


        reactivate_workspace_response_200_data.additional_properties = d
        return reactivate_workspace_response_200_data

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
