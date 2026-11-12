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

if TYPE_CHECKING:
  from ..models.deactivate_workspace_response_200_data_disconnected_item import DeactivateWorkspaceResponse200DataDisconnectedItem





T = TypeVar("T", bound="DeactivateWorkspaceResponse200Data")



@_attrs_define
class DeactivateWorkspaceResponse200Data:
    """ 
        Attributes:
            workspace_id (str | Unset):
            active (bool | Unset):
            deactivated_at (datetime.datetime | Unset):
            already_inactive (bool | Unset): True when the workspace was already inactive before this call.
            disconnected (list[DeactivateWorkspaceResponse200DataDisconnectedItem] | Unset): Accounts that were still
                connected and are now disconnected.
            listings_deactivated (list[str] | Unset): Listings this call switched off. `reactivate` switches these back on.
     """

    workspace_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    deactivated_at: datetime.datetime | Unset = UNSET
    already_inactive: bool | Unset = UNSET
    disconnected: list[DeactivateWorkspaceResponse200DataDisconnectedItem] | Unset = UNSET
    listings_deactivated: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.deactivate_workspace_response_200_data_disconnected_item import DeactivateWorkspaceResponse200DataDisconnectedItem
        workspace_id = self.workspace_id

        active = self.active

        deactivated_at: str | Unset = UNSET
        if not isinstance(self.deactivated_at, Unset):
            deactivated_at = self.deactivated_at.isoformat()

        already_inactive = self.already_inactive

        disconnected: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disconnected, Unset):
            disconnected = []
            for disconnected_item_data in self.disconnected:
                disconnected_item = disconnected_item_data.to_dict()
                disconnected.append(disconnected_item)



        listings_deactivated: list[str] | Unset = UNSET
        if not isinstance(self.listings_deactivated, Unset):
            listings_deactivated = self.listings_deactivated




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if active is not UNSET:
            field_dict["active"] = active
        if deactivated_at is not UNSET:
            field_dict["deactivatedAt"] = deactivated_at
        if already_inactive is not UNSET:
            field_dict["alreadyInactive"] = already_inactive
        if disconnected is not UNSET:
            field_dict["disconnected"] = disconnected
        if listings_deactivated is not UNSET:
            field_dict["listingsDeactivated"] = listings_deactivated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deactivate_workspace_response_200_data_disconnected_item import DeactivateWorkspaceResponse200DataDisconnectedItem
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId", UNSET)

        active = d.pop("active", UNSET)

        _deactivated_at = d.pop("deactivatedAt", UNSET)
        deactivated_at: datetime.datetime | Unset
        if isinstance(_deactivated_at,  Unset):
            deactivated_at = UNSET
        else:
            deactivated_at = isoparse(_deactivated_at)




        already_inactive = d.pop("alreadyInactive", UNSET)

        _disconnected = d.pop("disconnected", UNSET)
        disconnected: list[DeactivateWorkspaceResponse200DataDisconnectedItem] | Unset = UNSET
        if _disconnected is not UNSET:
            disconnected = []
            for disconnected_item_data in _disconnected:
                disconnected_item = DeactivateWorkspaceResponse200DataDisconnectedItem.from_dict(disconnected_item_data)



                disconnected.append(disconnected_item)


        listings_deactivated = cast(list[str], d.pop("listingsDeactivated", UNSET))


        deactivate_workspace_response_200_data = cls(
            workspace_id=workspace_id,
            active=active,
            deactivated_at=deactivated_at,
            already_inactive=already_inactive,
            disconnected=disconnected,
            listings_deactivated=listings_deactivated,
        )


        deactivate_workspace_response_200_data.additional_properties = d
        return deactivate_workspace_response_200_data

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
