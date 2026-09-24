from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MapBookingRoomRequest")



@_attrs_define
class MapBookingRoomRequest:
    """ Body for `POST /v1/channels/booking/listings/map`.

        Attributes:
            room_booking_id (str): Booking.com's own room id. Discover it via `GET
                /v1/channels/booking/properties/{id}/rooms` (`rooms[].roomId`). A number is also accepted.
            listing_id (int | None): Canonical Repull listing id to link the room to. Must belong to your workspace and be
                active. `null` unmaps the room and removes its channel link. The field is required — omitting it is a 422, not
                an unmap.
            hotel_id (str | Unset): Optional. When present, must be the Booking.com property the room belongs to — guards
                against mapping a room of the wrong property when looping over several.
            sync_enabled (bool | Unset): Whether the resulting channel link has sync enabled. Default: True.
     """

    room_booking_id: str
    listing_id: int | None
    hotel_id: str | Unset = UNSET
    sync_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_booking_id = self.room_booking_id

        listing_id: int | None
        listing_id = self.listing_id

        hotel_id = self.hotel_id

        sync_enabled = self.sync_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomBookingId": room_booking_id,
            "listingId": listing_id,
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_booking_id = d.pop("roomBookingId")

        def _parse_listing_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        listing_id = _parse_listing_id(d.pop("listingId"))


        hotel_id = d.pop("hotelId", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        map_booking_room_request = cls(
            room_booking_id=room_booking_id,
            listing_id=listing_id,
            hotel_id=hotel_id,
            sync_enabled=sync_enabled,
        )


        map_booking_room_request.additional_properties = d
        return map_booking_room_request

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
