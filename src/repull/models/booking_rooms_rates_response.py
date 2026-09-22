from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_rooms_rates_response_source import BookingRoomsRatesResponseSource
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_rooms_rates_response_rooms_item import BookingRoomsRatesResponseRoomsItem





T = TypeVar("T", bound="BookingRoomsRatesResponse")



@_attrs_define
class BookingRoomsRatesResponse:
    """ Returned by `GET /v1/channels/booking/properties/{id}/rooms`. Exposes the Booking.com room + rate-plan mapping ids
    for a listing so a caller can assemble a `PUT /v1/channels/booking/availability` restriction write (which requires
    `roomId` + `rateId` on every update). Read live from Booking's B.XML roomrates feed; `source` says so, and says when
    the answer came from the last import instead.

        Attributes:
            hotel_id (str | Unset): Booking.com hotel/property id the rooms belong to — the one the mapping resolved to.
            listing_id (str | Unset): Repull listing id echoed back.
            other_hotel_ids (list[str] | Unset): Other Booking.com properties this listing is also published under. Empty in
                the normal case. Pass one as `?hotel_id=` to read its rooms instead.
            source (BookingRoomsRatesResponseSource | Unset): Where the rooms came from. `booking` — read live from
                Booking.com just now. `mirror` — Booking.com returned nothing usable, so these are the rooms and rate plans
                recorded at the last import; the ids are Booking.com's own and are safe to write against, but they can be stale
                and `maxPersons`, `policy`, `policyId`, `pricingType` and `isChildRate` come back `null` because only the live
                feed states them.
            mirror_reason (None | str | Unset): Why the live read was not used. Null when `source` is `booking`.
            rooms (list[BookingRoomsRatesResponseRoomsItem] | Unset): Empty only when Booking.com reports no rooms for this
                property AND nothing was recorded at the last import. A failed read is never an empty list — it is an error.
     """

    hotel_id: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    other_hotel_ids: list[str] | Unset = UNSET
    source: BookingRoomsRatesResponseSource | Unset = UNSET
    mirror_reason: None | str | Unset = UNSET
    rooms: list[BookingRoomsRatesResponseRoomsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_rooms_rates_response_rooms_item import BookingRoomsRatesResponseRoomsItem
        hotel_id = self.hotel_id

        listing_id = self.listing_id

        other_hotel_ids: list[str] | Unset = UNSET
        if not isinstance(self.other_hotel_ids, Unset):
            other_hotel_ids = self.other_hotel_ids



        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        mirror_reason: None | str | Unset
        if isinstance(self.mirror_reason, Unset):
            mirror_reason = UNSET
        else:
            mirror_reason = self.mirror_reason

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
            field_dict["hotelId"] = hotel_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if other_hotel_ids is not UNSET:
            field_dict["otherHotelIds"] = other_hotel_ids
        if source is not UNSET:
            field_dict["source"] = source
        if mirror_reason is not UNSET:
            field_dict["mirrorReason"] = mirror_reason
        if rooms is not UNSET:
            field_dict["rooms"] = rooms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_rooms_rates_response_rooms_item import BookingRoomsRatesResponseRoomsItem
        d = dict(src_dict)
        hotel_id = d.pop("hotelId", UNSET)

        listing_id = d.pop("listingId", UNSET)

        other_hotel_ids = cast(list[str], d.pop("otherHotelIds", UNSET))


        _source = d.pop("source", UNSET)
        source: BookingRoomsRatesResponseSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = BookingRoomsRatesResponseSource(_source)




        def _parse_mirror_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mirror_reason = _parse_mirror_reason(d.pop("mirrorReason", UNSET))


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
            other_hotel_ids=other_hotel_ids,
            source=source,
            mirror_reason=mirror_reason,
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
