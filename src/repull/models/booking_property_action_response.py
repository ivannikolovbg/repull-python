from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_property_action_response_action import BookingPropertyActionResponseAction
from ..models.booking_property_action_response_channel import BookingPropertyActionResponseChannel
from ..models.booking_property_action_response_property_status import BookingPropertyActionResponsePropertyStatus
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
            property_status (BookingPropertyActionResponsePropertyStatus | Unset): `open` / `close` only: the property's
                state on Booking.com after the call.
            changed (bool | Unset): `open` / `close` only: false when the property was already in that state, so nothing was
                sent.
            booking_status (None | str | Unset): `open` / `close` only: Booking.com's status for the property before the
                call, e.g. `XML: Ready to open`.
            room_booking_id (None | str | Unset): Booking.com's own room id the availability write addressed.
            selling (bool | Unset): `unlist` / `relist` only. Whether the property is now on sale. **This is the state of
                the property on Booking.com, not of the listing in Repull** — `active` (what Repull bills and serves) is
                untouched by both actions and is deliberately not echoed here so the two can never be read as one field.
     """

    listing_id: str
    channel: BookingPropertyActionResponseChannel
    action: BookingPropertyActionResponseAction
    hotel_id: str
    property_status: BookingPropertyActionResponsePropertyStatus | Unset = UNSET
    changed: bool | Unset = UNSET
    booking_status: None | str | Unset = UNSET
    room_booking_id: None | str | Unset = UNSET
    selling: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        channel = self.channel.value

        action = self.action.value

        hotel_id = self.hotel_id

        property_status: str | Unset = UNSET
        if not isinstance(self.property_status, Unset):
            property_status = self.property_status.value


        changed = self.changed

        booking_status: None | str | Unset
        if isinstance(self.booking_status, Unset):
            booking_status = UNSET
        else:
            booking_status = self.booking_status

        room_booking_id: None | str | Unset
        if isinstance(self.room_booking_id, Unset):
            room_booking_id = UNSET
        else:
            room_booking_id = self.room_booking_id

        selling = self.selling


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "channel": channel,
            "action": action,
            "hotelId": hotel_id,
        })
        if property_status is not UNSET:
            field_dict["propertyStatus"] = property_status
        if changed is not UNSET:
            field_dict["changed"] = changed
        if booking_status is not UNSET:
            field_dict["bookingStatus"] = booking_status
        if room_booking_id is not UNSET:
            field_dict["roomBookingId"] = room_booking_id
        if selling is not UNSET:
            field_dict["selling"] = selling

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        channel = BookingPropertyActionResponseChannel(d.pop("channel"))




        action = BookingPropertyActionResponseAction(d.pop("action"))




        hotel_id = d.pop("hotelId")

        _property_status = d.pop("propertyStatus", UNSET)
        property_status: BookingPropertyActionResponsePropertyStatus | Unset
        if isinstance(_property_status,  Unset):
            property_status = UNSET
        else:
            property_status = BookingPropertyActionResponsePropertyStatus(_property_status)




        changed = d.pop("changed", UNSET)

        def _parse_booking_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_status = _parse_booking_status(d.pop("bookingStatus", UNSET))


        def _parse_room_booking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_booking_id = _parse_room_booking_id(d.pop("roomBookingId", UNSET))


        selling = d.pop("selling", UNSET)

        booking_property_action_response = cls(
            listing_id=listing_id,
            channel=channel,
            action=action,
            hotel_id=hotel_id,
            property_status=property_status,
            changed=changed,
            booking_status=booking_status,
            room_booking_id=room_booking_id,
            selling=selling,
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
