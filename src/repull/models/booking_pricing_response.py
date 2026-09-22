from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingPricingResponse")



@_attrs_define
class BookingPricingResponse:
    """ Returned by `GET /v1/channels/booking/listings/{id}/pricing`. Mirrors Booking's `getRoomRateAvailability` response
    with `hotelId` and `listingId` echoed back for SDK consumers.

        Attributes:
            hotel_id (str | Unset):
            listing_id (str | Unset):
            other_hotel_ids (list[str] | Unset): Other Booking.com properties this listing is also published under. Empty in
                the normal case. Pass one as `?hotel_id=` to read its pricing instead.
     """

    hotel_id: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    other_hotel_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hotel_id = self.hotel_id

        listing_id = self.listing_id

        other_hotel_ids: list[str] | Unset = UNSET
        if not isinstance(self.other_hotel_ids, Unset):
            other_hotel_ids = self.other_hotel_ids




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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hotel_id = d.pop("hotelId", UNSET)

        listing_id = d.pop("listingId", UNSET)

        other_hotel_ids = cast(list[str], d.pop("otherHotelIds", UNSET))


        booking_pricing_response = cls(
            hotel_id=hotel_id,
            listing_id=listing_id,
            other_hotel_ids=other_hotel_ids,
        )


        booking_pricing_response.additional_properties = d
        return booking_pricing_response

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
