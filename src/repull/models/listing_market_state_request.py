from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingMarketStateRequest")



@_attrs_define
class ListingMarketStateRequest:
    """ Optional. Send no body at all unless this listing is mapped to more than one Booking.com property.

        Attributes:
            hotel_id (str | Unset): Booking.com property to act on, for a listing mapped to more than one. Without it the
                Booking.com item comes back refused with `ambiguous_booking_mapping` — closing the wrong property's availability
                takes real inventory off sale, so it is never guessed. The Airbnb items are unaffected and still run. `GET
                /v1/channels/booking/properties` lists every property in the workspace with the listings mapped under it.
                `?hotel_id=` in the query string means the same thing; the body wins if you send both.
     """

    hotel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hotel_id = self.hotel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hotel_id = d.pop("hotelId", UNSET)

        listing_market_state_request = cls(
            hotel_id=hotel_id,
        )


        listing_market_state_request.additional_properties = d
        return listing_market_state_request

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
