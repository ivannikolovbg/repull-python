from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MapBookingRoomResponse")



@_attrs_define
class MapBookingRoomResponse:
    """ Id fields are strings (API-wide convention — bigint ids are stringified to avoid 53-bit JS-number precision loss).

        Attributes:
            success (bool):  Example: True.
            already_mapped (bool): True when the room already pointed at this listing (or was already unmapped) and its
                channel link agreed. Nothing was written.
            room_booking_id (None | str): Booking.com's room id, as recorded for this room.
            listing_id (None | str): The listing the room now points at. Null after an unmap.
            hotel_id (str): The Booking.com property the room belongs to.
            room_id (str): Repull-side id of the room record — the `roomId` the Connect room-mapping flow takes.
            previous_listing_id (None | str | Unset): The listing the room pointed at before this call; null when it was
                unmapped. Omitted on a no-op.
            room_name (None | str | Unset):
            platform_link_id (None | str | Unset): Id of the resulting channel-link row. Null after an unmap, and for a room
                Booking.com has given us no room id for.
            reservations_imported (int | None | Unset): Reservations Booking.com returned for the property and ran through
                the import after the room was mapped — the property's active bookings, which would otherwise never reach the
                listing. A reservation already present is left as it is, so this counts what was processed, not what was new,
                and re-sending never duplicates. Runs on every successful map, including a re-map to the same listing, so re-
                sending retries an import that did not run. `null` means the mapping succeeded but the import could not run; the
                room is still mapped. Absent after an unmap, when there is nothing to pull.
     """

    success: bool
    already_mapped: bool
    room_booking_id: None | str
    listing_id: None | str
    hotel_id: str
    room_id: str
    previous_listing_id: None | str | Unset = UNSET
    room_name: None | str | Unset = UNSET
    platform_link_id: None | str | Unset = UNSET
    reservations_imported: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        already_mapped = self.already_mapped

        room_booking_id: None | str
        room_booking_id = self.room_booking_id

        listing_id: None | str
        listing_id = self.listing_id

        hotel_id = self.hotel_id

        room_id = self.room_id

        previous_listing_id: None | str | Unset
        if isinstance(self.previous_listing_id, Unset):
            previous_listing_id = UNSET
        else:
            previous_listing_id = self.previous_listing_id

        room_name: None | str | Unset
        if isinstance(self.room_name, Unset):
            room_name = UNSET
        else:
            room_name = self.room_name

        platform_link_id: None | str | Unset
        if isinstance(self.platform_link_id, Unset):
            platform_link_id = UNSET
        else:
            platform_link_id = self.platform_link_id

        reservations_imported: int | None | Unset
        if isinstance(self.reservations_imported, Unset):
            reservations_imported = UNSET
        else:
            reservations_imported = self.reservations_imported


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "alreadyMapped": already_mapped,
            "roomBookingId": room_booking_id,
            "listingId": listing_id,
            "hotelId": hotel_id,
            "roomId": room_id,
        })
        if previous_listing_id is not UNSET:
            field_dict["previousListingId"] = previous_listing_id
        if room_name is not UNSET:
            field_dict["roomName"] = room_name
        if platform_link_id is not UNSET:
            field_dict["platformLinkId"] = platform_link_id
        if reservations_imported is not UNSET:
            field_dict["reservationsImported"] = reservations_imported

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        already_mapped = d.pop("alreadyMapped")

        def _parse_room_booking_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        room_booking_id = _parse_room_booking_id(d.pop("roomBookingId"))


        def _parse_listing_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        listing_id = _parse_listing_id(d.pop("listingId"))


        hotel_id = d.pop("hotelId")

        room_id = d.pop("roomId")

        def _parse_previous_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous_listing_id = _parse_previous_listing_id(d.pop("previousListingId", UNSET))


        def _parse_room_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_name = _parse_room_name(d.pop("roomName", UNSET))


        def _parse_platform_link_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform_link_id = _parse_platform_link_id(d.pop("platformLinkId", UNSET))


        def _parse_reservations_imported(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservations_imported = _parse_reservations_imported(d.pop("reservationsImported", UNSET))


        map_booking_room_response = cls(
            success=success,
            already_mapped=already_mapped,
            room_booking_id=room_booking_id,
            listing_id=listing_id,
            hotel_id=hotel_id,
            room_id=room_id,
            previous_listing_id=previous_listing_id,
            room_name=room_name,
            platform_link_id=platform_link_id,
            reservations_imported=reservations_imported,
        )


        map_booking_room_response.additional_properties = d
        return map_booking_room_response

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
