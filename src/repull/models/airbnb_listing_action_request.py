from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_listing_action_request_action import AirbnbListingActionRequestAction
from ..types import UNSET, Unset






T = TypeVar("T", bound="AirbnbListingActionRequest")



@_attrs_define
class AirbnbListingActionRequest:
    """ Body for `POST /v1/channels/airbnb/listings/{id}`.

        Attributes:
            action (AirbnbListingActionRequestAction): `delete` deactivates the Repull record. `push`/`publish` push content
                to Airbnb.
            airbnb_connection_id (str | Unset): For `push`/`publish`: the Airbnb connection to update (from `GET
                /v1/channels/airbnb/listings/{id}`). Pass this OR `hostId`.
            host_id (str | Unset): For `push`/`publish`: create + publish a new Airbnb listing under this host. Pass this OR
                `airbnbConnectionId`.
            force (bool | Unset): For `push`/`publish`: re-push every field, ignoring dirty-field tracking. Default: False.
     """

    action: AirbnbListingActionRequestAction
    airbnb_connection_id: str | Unset = UNSET
    host_id: str | Unset = UNSET
    force: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        airbnb_connection_id = self.airbnb_connection_id

        host_id = self.host_id

        force = self.force


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action": action,
        })
        if airbnb_connection_id is not UNSET:
            field_dict["airbnbConnectionId"] = airbnb_connection_id
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if force is not UNSET:
            field_dict["force"] = force

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = AirbnbListingActionRequestAction(d.pop("action"))




        airbnb_connection_id = d.pop("airbnbConnectionId", UNSET)

        host_id = d.pop("hostId", UNSET)

        force = d.pop("force", UNSET)

        airbnb_listing_action_request = cls(
            action=action,
            airbnb_connection_id=airbnb_connection_id,
            host_id=host_id,
            force=force,
        )


        airbnb_listing_action_request.additional_properties = d
        return airbnb_listing_action_request

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
