from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_property_action_response_action import BookingPropertyActionResponseAction
from ..models.booking_property_action_response_channel import BookingPropertyActionResponseChannel
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingPropertyActionResponse")



@_attrs_define
class BookingPropertyActionResponse:
    """ 
        Attributes:
            listing_id (str):
            channel (BookingPropertyActionResponseChannel):
            action (BookingPropertyActionResponseAction):
            hotel_id (str): The Booking.com property that was acted on. Always read it back — a listing can be mapped to
                several, and this states which one changed.
            selling (bool): Whether the property is now on sale. **This is the state of the property on Booking.com, not of
                the listing in Repull** — `active` (what Repull bills and serves) is untouched by both actions and is
                deliberately not echoed here so the two can never be read as one field.
            room_booking_id (None | str | Unset): Booking.com's own room id the availability write addressed.
     """

    listing_id: str
    channel: BookingPropertyActionResponseChannel
    action: BookingPropertyActionResponseAction
    hotel_id: str
    selling: bool
    room_booking_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        channel = self.channel.value

        action = self.action.value

        hotel_id = self.hotel_id

        selling = self.selling

        room_booking_id: None | str | Unset
        if isinstance(self.room_booking_id, Unset):
            room_booking_id = UNSET
        else:
            room_booking_id = self.room_booking_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "channel": channel,
            "action": action,
            "hotelId": hotel_id,
            "selling": selling,
        })
        if room_booking_id is not UNSET:
            field_dict["roomBookingId"] = room_booking_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        channel = BookingPropertyActionResponseChannel(d.pop("channel"))




        action = BookingPropertyActionResponseAction(d.pop("action"))




        hotel_id = d.pop("hotelId")

        selling = d.pop("selling")

        def _parse_room_booking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_booking_id = _parse_room_booking_id(d.pop("roomBookingId", UNSET))


        booking_property_action_response = cls(
            listing_id=listing_id,
            channel=channel,
            action=action,
            hotel_id=hotel_id,
            selling=selling,
            room_booking_id=room_booking_id,
        )


        booking_property_action_response.additional_properties = d
        return booking_property_action_response

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
