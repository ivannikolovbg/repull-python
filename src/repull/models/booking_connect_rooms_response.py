from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_connect_rooms_response_status import BookingConnectRoomsResponseStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_connect_listing_option import BookingConnectListingOption
  from ..models.booking_connect_room import BookingConnectRoom





T = TypeVar("T", bound="BookingConnectRoomsResponse")



@_attrs_define
class BookingConnectRoomsResponse:
    """ Returned by `GET /v1/connect/booking/rooms`. The hosted picker page polls this every ~2s while the room import runs
    server-side; once `status` is `ready` it renders the mapping UI.

        Attributes:
            status (BookingConnectRoomsResponseStatus): `importing` — listings_booking row exists but rooms not yet
                imported. `ready` — rooms imported, awaiting mapping. `completed` — session already finished.
            session_id (str):
            hotel_id (str):
            rooms (list[BookingConnectRoom]):
            listing_options (list[BookingConnectListingOption]):
     """

    status: BookingConnectRoomsResponseStatus
    session_id: str
    hotel_id: str
    rooms: list[BookingConnectRoom]
    listing_options: list[BookingConnectListingOption]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_connect_listing_option import BookingConnectListingOption
        from ..models.booking_connect_room import BookingConnectRoom
        status = self.status.value

        session_id = self.session_id

        hotel_id = self.hotel_id

        rooms = []
        for rooms_item_data in self.rooms:
            rooms_item = rooms_item_data.to_dict()
            rooms.append(rooms_item)



        listing_options = []
        for listing_options_item_data in self.listing_options:
            listing_options_item = listing_options_item_data.to_dict()
            listing_options.append(listing_options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "sessionId": session_id,
            "hotelId": hotel_id,
            "rooms": rooms,
            "listingOptions": listing_options,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_connect_listing_option import BookingConnectListingOption
        from ..models.booking_connect_room import BookingConnectRoom
        d = dict(src_dict)
        status = BookingConnectRoomsResponseStatus(d.pop("status"))




        session_id = d.pop("sessionId")

        hotel_id = d.pop("hotelId")

        rooms = []
        _rooms = d.pop("rooms")
        for rooms_item_data in (_rooms):
            rooms_item = BookingConnectRoom.from_dict(rooms_item_data)



            rooms.append(rooms_item)


        listing_options = []
        _listing_options = d.pop("listingOptions")
        for listing_options_item_data in (_listing_options):
            listing_options_item = BookingConnectListingOption.from_dict(listing_options_item_data)



            listing_options.append(listing_options_item)


        booking_connect_rooms_response = cls(
            status=status,
            session_id=session_id,
            hotel_id=hotel_id,
            rooms=rooms,
            listing_options=listing_options,
        )


        booking_connect_rooms_response.additional_properties = d
        return booking_connect_rooms_response

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
