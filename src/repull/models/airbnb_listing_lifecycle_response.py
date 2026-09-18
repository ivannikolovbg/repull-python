from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_listing_lifecycle_response_action import AirbnbListingLifecycleResponseAction
from ..models.airbnb_listing_lifecycle_response_channel import AirbnbListingLifecycleResponseChannel
from ..types import UNSET, Unset






T = TypeVar("T", bound="AirbnbListingLifecycleResponse")



@_attrs_define
class AirbnbListingLifecycleResponse:
    """ Result of `unlist` / `relist`. Reports the state of the LIVE Airbnb listing. The Repull record's own `active` flag
    is untouched by both and is deliberately not echoed here, so the two ideas cannot be read as one field.

        Attributes:
            id (str | Unset): Repull listing id.
            action (AirbnbListingLifecycleResponseAction | Unset):
            channel (AirbnbListingLifecycleResponseChannel | Unset):
            airbnb_connection_id (str | Unset):
            live (bool | Unset): Whether the Airbnb listing is taking bookings after this call. `false` after `unlist`,
                `true` after `relist`.
            verified (bool | Unset): True when the result was confirmed by reading the listing back from Airbnb (done on
                `unlist`: Airbnb accepting the call is not proof the listing came down).
     """

    id: str | Unset = UNSET
    action: AirbnbListingLifecycleResponseAction | Unset = UNSET
    channel: AirbnbListingLifecycleResponseChannel | Unset = UNSET
    airbnb_connection_id: str | Unset = UNSET
    live: bool | Unset = UNSET
    verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value


        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        airbnb_connection_id = self.airbnb_connection_id

        live = self.live

        verified = self.verified


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if action is not UNSET:
            field_dict["action"] = action
        if channel is not UNSET:
            field_dict["channel"] = channel
        if airbnb_connection_id is not UNSET:
            field_dict["airbnbConnectionId"] = airbnb_connection_id
        if live is not UNSET:
            field_dict["live"] = live
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _action = d.pop("action", UNSET)
        action: AirbnbListingLifecycleResponseAction | Unset
        if isinstance(_action,  Unset):
            action = UNSET
        else:
            action = AirbnbListingLifecycleResponseAction(_action)




        _channel = d.pop("channel", UNSET)
        channel: AirbnbListingLifecycleResponseChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = AirbnbListingLifecycleResponseChannel(_channel)




        airbnb_connection_id = d.pop("airbnbConnectionId", UNSET)

        live = d.pop("live", UNSET)

        verified = d.pop("verified", UNSET)

        airbnb_listing_lifecycle_response = cls(
            id=id,
            action=action,
            channel=channel,
            airbnb_connection_id=airbnb_connection_id,
            live=live,
            verified=verified,
        )


        airbnb_listing_lifecycle_response.additional_properties = d
        return airbnb_listing_lifecycle_response

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
