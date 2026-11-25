from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TiketConnectRoomsResponseRoomsItem")



@_attrs_define
class TiketConnectRoomsResponseRoomsItem:
    """ 
        Attributes:
            room_id (str | Unset): Pass this back in `POST /v1/connect/tiket/map-rooms`.
            room_name (None | str | Unset):
            max_guests (int | None | Unset):
            number_of_rooms (int | None | Unset):
            current_listing_id (None | str | Unset):
            room_booking_id (None | str | Unset): tiket.com room type code (`roomTypeCode` on `GET
                /v1/channels/tiket/properties/{id}/rooms`), exactly as tiket.com sends it. Free-form text such as `DLX-KING`, so
                always a string — never parse it as a number.
     """

    room_id: str | Unset = UNSET
    room_name: None | str | Unset = UNSET
    max_guests: int | None | Unset = UNSET
    number_of_rooms: int | None | Unset = UNSET
    current_listing_id: None | str | Unset = UNSET
    room_booking_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        room_name: None | str | Unset
        if isinstance(self.room_name, Unset):
            room_name = UNSET
        else:
            room_name = self.room_name

        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        number_of_rooms: int | None | Unset
        if isinstance(self.number_of_rooms, Unset):
            number_of_rooms = UNSET
        else:
            number_of_rooms = self.number_of_rooms

        current_listing_id: None | str | Unset
        if isinstance(self.current_listing_id, Unset):
            current_listing_id = UNSET
        else:
            current_listing_id = self.current_listing_id

        room_booking_id: None | str | Unset
        if isinstance(self.room_booking_id, Unset):
            room_booking_id = UNSET
        else:
            room_booking_id = self.room_booking_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room_name is not UNSET:
            field_dict["roomName"] = room_name
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if number_of_rooms is not UNSET:
            field_dict["numberOfRooms"] = number_of_rooms
        if current_listing_id is not UNSET:
            field_dict["currentListingId"] = current_listing_id
        if room_booking_id is not UNSET:
            field_dict["roomBookingId"] = room_booking_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_id = d.pop("roomId", UNSET)

        def _parse_room_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_name = _parse_room_name(d.pop("roomName", UNSET))


        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("maxGuests", UNSET))


        def _parse_number_of_rooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_rooms = _parse_number_of_rooms(d.pop("numberOfRooms", UNSET))


        def _parse_current_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_listing_id = _parse_current_listing_id(d.pop("currentListingId", UNSET))


        def _parse_room_booking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_booking_id = _parse_room_booking_id(d.pop("roomBookingId", UNSET))


        tiket_connect_rooms_response_rooms_item = cls(
            room_id=room_id,
            room_name=room_name,
            max_guests=max_guests,
            number_of_rooms=number_of_rooms,
            current_listing_id=current_listing_id,
            room_booking_id=room_booking_id,
        )


        tiket_connect_rooms_response_rooms_item.additional_properties = d
        return tiket_connect_rooms_response_rooms_item

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
