from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_connect_rooms_response_status import TiketConnectRoomsResponseStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_connect_listing_option import BookingConnectListingOption
  from ..models.tiket_connect_rooms_response_rooms_item import TiketConnectRoomsResponseRoomsItem





T = TypeVar("T", bound="TiketConnectRoomsResponse")



@_attrs_define
class TiketConnectRoomsResponse:
    """ Returned by `GET /v1/connect/tiket/rooms`. Same shape as `GET /v1/connect/booking/rooms`.

        Attributes:
            status (TiketConnectRoomsResponseStatus): `importing` — room types are still being read; `ready` — awaiting
                mapping; `completed` — the session is finished.
            session_id (str):
            hotel_id (str):
            rooms (list[TiketConnectRoomsResponseRoomsItem]):
            listing_options (list[BookingConnectListingOption]):
            listing_options_total (int | Unset):
            missing_capabilities (list[str] | Unset): Always empty for tiket.com.
     """

    status: TiketConnectRoomsResponseStatus
    session_id: str
    hotel_id: str
    rooms: list[TiketConnectRoomsResponseRoomsItem]
    listing_options: list[BookingConnectListingOption]
    listing_options_total: int | Unset = UNSET
    missing_capabilities: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_connect_listing_option import BookingConnectListingOption
        from ..models.tiket_connect_rooms_response_rooms_item import TiketConnectRoomsResponseRoomsItem
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



        listing_options_total = self.listing_options_total

        missing_capabilities: list[str] | Unset = UNSET
        if not isinstance(self.missing_capabilities, Unset):
            missing_capabilities = self.missing_capabilities




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "sessionId": session_id,
            "hotelId": hotel_id,
            "rooms": rooms,
            "listingOptions": listing_options,
        })
        if listing_options_total is not UNSET:
            field_dict["listingOptionsTotal"] = listing_options_total
        if missing_capabilities is not UNSET:
            field_dict["missingCapabilities"] = missing_capabilities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_connect_listing_option import BookingConnectListingOption
        from ..models.tiket_connect_rooms_response_rooms_item import TiketConnectRoomsResponseRoomsItem
        d = dict(src_dict)
        status = TiketConnectRoomsResponseStatus(d.pop("status"))




        session_id = d.pop("sessionId")

        hotel_id = d.pop("hotelId")

        rooms = []
        _rooms = d.pop("rooms")
        for rooms_item_data in (_rooms):
            rooms_item = TiketConnectRoomsResponseRoomsItem.from_dict(rooms_item_data)



            rooms.append(rooms_item)


        listing_options = []
        _listing_options = d.pop("listingOptions")
        for listing_options_item_data in (_listing_options):
            listing_options_item = BookingConnectListingOption.from_dict(listing_options_item_data)



            listing_options.append(listing_options_item)


        listing_options_total = d.pop("listingOptionsTotal", UNSET)

        missing_capabilities = cast(list[str], d.pop("missingCapabilities", UNSET))


        tiket_connect_rooms_response = cls(
            status=status,
            session_id=session_id,
            hotel_id=hotel_id,
            rooms=rooms,
            listing_options=listing_options,
            listing_options_total=listing_options_total,
            missing_capabilities=missing_capabilities,
        )


        tiket_connect_rooms_response.additional_properties = d
        return tiket_connect_rooms_response

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
