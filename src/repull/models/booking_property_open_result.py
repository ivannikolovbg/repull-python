from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_property_open_result_outcome import BookingPropertyOpenResultOutcome
from typing import cast






T = TypeVar("T", bound="BookingPropertyOpenResult")



@_attrs_define
class BookingPropertyOpenResult:
    """ What happened to one Booking.com property when its listing was activated. Repull opens a Booking.com property
    automatically only while every listing mapped to it is active. Keep a listing that is not ready inactive and its
    property is never opened; activate it and Repull opens the property, provided Booking.com's own readiness check
    passes.

        Attributes:
            hotel_id (str): The Booking.com property (hotel id).
            listing_ids (list[str]): The listings in this request that are mapped to the property.
            outcome (BookingPropertyOpenResultOutcome): `opened`: Booking.com's check passed and the property is now open.
                `refused`: Booking.com's check did not pass — `blockers` has its own reasons — and nothing changed.
                `not_needed`: Booking.com already has the property past its build stage (open, or closed by you), so it was left
                alone; use the `open` action on `POST /v1/channels/booking/properties/{id}` to reopen a closed property.
                `listing_inactive`: another listing on the same property is still inactive. `no_listing`: no listing is mapped
                to the property. `failed`: Booking.com did not answer; nothing changed — send the request again.
            booking_status (None | str): Booking.com's status for the property before anything was sent, e.g. `XML: Ready to
                open`, when it was read.
            blockers (list[str]): Booking.com's own reasons it will not open the property, e.g. "Room 1554900501 does not
                have kitchen or kitchenette". Empty unless `outcome` is `refused`.
     """

    hotel_id: str
    listing_ids: list[str]
    outcome: BookingPropertyOpenResultOutcome
    booking_status: None | str
    blockers: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hotel_id = self.hotel_id

        listing_ids = self.listing_ids



        outcome = self.outcome.value

        booking_status: None | str
        booking_status = self.booking_status

        blockers = self.blockers




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "hotelId": hotel_id,
            "listingIds": listing_ids,
            "outcome": outcome,
            "bookingStatus": booking_status,
            "blockers": blockers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hotel_id = d.pop("hotelId")

        listing_ids = cast(list[str], d.pop("listingIds"))


        outcome = BookingPropertyOpenResultOutcome(d.pop("outcome"))




        def _parse_booking_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        booking_status = _parse_booking_status(d.pop("bookingStatus"))


        blockers = cast(list[str], d.pop("blockers"))


        booking_property_open_result = cls(
            hotel_id=hotel_id,
            listing_ids=listing_ids,
            outcome=outcome,
            booking_status=booking_status,
            blockers=blockers,
        )


        booking_property_open_result.additional_properties = d
        return booking_property_open_result

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
