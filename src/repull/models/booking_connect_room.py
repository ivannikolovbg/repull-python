from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingConnectRoom")



@_attrs_define
class BookingConnectRoom:
    """ A Booking.com room imported from the claimed hotel. The customer maps each room to one of their Repull listings via
    `mapConnectBookingRooms`.

        Attributes:
            room_id (int): Repull-side `listings_booking_rooms.id`. Pass this back in the mapping submission.
            room_name (str):  Example: Deluxe King.
            number_of_rooms (int): Number of inventory units of this room type at the hotel.
            max_guests (int | None | Unset):
            current_listing_id (int | None | Unset): Currently mapped Repull listing ID, or null if not yet mapped.
            room_booking_id (int | None | Unset): Booking.com-side room ID (used internally for `listing_platform_links`).
     """

    room_id: int
    room_name: str
    number_of_rooms: int
    max_guests: int | None | Unset = UNSET
    current_listing_id: int | None | Unset = UNSET
    room_booking_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        room_name = self.room_name

        number_of_rooms = self.number_of_rooms

        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        current_listing_id: int | None | Unset
        if isinstance(self.current_listing_id, Unset):
            current_listing_id = UNSET
        else:
            current_listing_id = self.current_listing_id

        room_booking_id: int | None | Unset
        if isinstance(self.room_booking_id, Unset):
            room_booking_id = UNSET
        else:
            room_booking_id = self.room_booking_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomId": room_id,
            "roomName": room_name,
            "numberOfRooms": number_of_rooms,
        })
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if current_listing_id is not UNSET:
            field_dict["currentListingId"] = current_listing_id
        if room_booking_id is not UNSET:
            field_dict["roomBookingId"] = room_booking_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_id = d.pop("roomId")

        room_name = d.pop("roomName")

        number_of_rooms = d.pop("numberOfRooms")

        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("maxGuests", UNSET))


        def _parse_current_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current_listing_id = _parse_current_listing_id(d.pop("currentListingId", UNSET))


        def _parse_room_booking_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        room_booking_id = _parse_room_booking_id(d.pop("roomBookingId", UNSET))


        booking_connect_room = cls(
            room_id=room_id,
            room_name=room_name,
            number_of_rooms=number_of_rooms,
            max_guests=max_guests,
            current_listing_id=current_listing_id,
            room_booking_id=room_booking_id,
        )


        booking_connect_room.additional_properties = d
        return booking_connect_room

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
