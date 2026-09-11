from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_rooms_rates_response_rooms_item import BookingRoomsRatesResponseRoomsItem





T = TypeVar("T", bound="BookingRoomsRatesResponse")



@_attrs_define
class BookingRoomsRatesResponse:
    """ Returned by `GET /v1/channels/booking/properties/{id}/rooms`. Exposes the Booking.com room + rate-plan mapping ids
    for a listing so a caller can assemble a `PUT /v1/channels/booking/availability` restriction write (which requires
    `roomId` + `rateId` on every update). Sourced from Booking's B.XML roomrates feed.

        Attributes:
            hotel_id (str | Unset): Booking.com hotel/property id the rooms belong to.
            listing_id (int | Unset): Vanio listing id echoed back.
            rooms (list[BookingRoomsRatesResponseRoomsItem] | Unset):
     """

    hotel_id: str | Unset = UNSET
    listing_id: int | Unset = UNSET
    rooms: list[BookingRoomsRatesResponseRoomsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_rooms_rates_response_rooms_item import BookingRoomsRatesResponseRoomsItem
        hotel_id = self.hotel_id

        listing_id = self.listing_id

        rooms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rooms, Unset):
            rooms = []
            for rooms_item_data in self.rooms:
                rooms_item = rooms_item_data.to_dict()
                rooms.append(rooms_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotel_id"] = hotel_id
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if rooms is not UNSET:
            field_dict["rooms"] = rooms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_rooms_rates_response_rooms_item import BookingRoomsRatesResponseRoomsItem
        d = dict(src_dict)
        hotel_id = d.pop("hotel_id", UNSET)

        listing_id = d.pop("listing_id", UNSET)

        _rooms = d.pop("rooms", UNSET)
        rooms: list[BookingRoomsRatesResponseRoomsItem] | Unset = UNSET
        if _rooms is not UNSET:
            rooms = []
            for rooms_item_data in _rooms:
                rooms_item = BookingRoomsRatesResponseRoomsItem.from_dict(rooms_item_data)



                rooms.append(rooms_item)


        booking_rooms_rates_response = cls(
            hotel_id=hotel_id,
            listing_id=listing_id,
            rooms=rooms,
        )


        booking_rooms_rates_response.additional_properties = d
        return booking_rooms_rates_response

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
