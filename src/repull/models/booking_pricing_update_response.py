from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_pricing_update_response_applied import BookingPricingUpdateResponseApplied
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_pricing_update_response_booking import BookingPricingUpdateResponseBooking
  from ..models.booking_pricing_update_response_errors_item import BookingPricingUpdateResponseErrorsItem
  from ..models.booking_rate_write_occupancy import BookingRateWriteOccupancy
  from ..models.booking_rate_write_price_half import BookingRateWritePriceHalf
  from ..models.booking_rate_write_restriction_half import BookingRateWriteRestrictionHalf
  from ..models.booking_rate_write_verification import BookingRateWriteVerification





T = TypeVar("T", bound="BookingPricingUpdateResponse")



@_attrs_define
class BookingPricingUpdateResponse:
    """ What a Booking.com rate write actually did. Returned by `PUT /v1/channels/booking/listings/{id}/pricing` and by `PUT
    /v1/channels/booking/availability` with `type: "rates"`.

    Prices and restrictions are two writes on two of Booking.com's wires, and Booking.com can take one and refuse the
    other. The response says so: `price` and `restrictions` each carry their own state, their own read-back and — when
    refused — Booking.com's own reason. The top-level `applied` summarises them, and is `partial` when they disagree. A
    half that landed is never reported as a failure.

        Attributes:
            hotel_id (None | str | Unset):
            listing_id (None | str | Unset):
            property_id (None | str | Unset): Echoed back by `PUT /v1/channels/booking/availability`.
            requested (int | Unset): How many updates were sent.
            occupancy (list[BookingRateWriteOccupancy] | Unset):
            applied (BookingPricingUpdateResponseApplied | Unset): What is known about the nights now. `verified` — read
                back, every night carries what was sent. `mismatch` — read back, some do not (`verification.rows` /
                `restrictions.verification.rows` name them). `rejected` — Booking.com refused everything that was sent.
                `partial` — one half landed and the other did not; read `price.applied` and `restrictions.applied` to see which,
                and `restrictions.rejection.message` for Booking.com's reason. `unverified` — Booking.com acknowledged the
                request and no read-back ran: an unknown, not a success. A bare acknowledgement is never reported as "all
                applied".
            price (BookingRateWritePriceHalf | Unset): The prices: what was sent, what Booking.com said, and what is live
                now.
            restrictions (BookingRateWriteRestrictionHalf | Unset): The restrictions: the same report as the price half, for
                the other write.
            verification (BookingRateWriteVerification | Unset): The read-back. Booking.com's answer to a rate write is an
                acknowledgement of the request with no per-date status, so the dates are read back to find out what is actually
                live.
            booking (BookingPricingUpdateResponseBooking | Unset): Booking.com's own answers, verbatim: `rates` (the rate-
                amount notification) and `restrictions` (the availability notification, when the updates carried any
                restriction).
            errors (list[BookingPricingUpdateResponseErrorsItem] | Unset): Failures Booking.com named, across both wires.
                Empty means Booking.com named none — not that the nights changed; that is what `applied` is for.
            rate_plan_read_error (None | str | Unset): Present when Booking.com's rate-plan read did not complete, so an
                occupancy fell back to the room definition.
     """

    hotel_id: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    property_id: None | str | Unset = UNSET
    requested: int | Unset = UNSET
    occupancy: list[BookingRateWriteOccupancy] | Unset = UNSET
    applied: BookingPricingUpdateResponseApplied | Unset = UNSET
    price: BookingRateWritePriceHalf | Unset = UNSET
    restrictions: BookingRateWriteRestrictionHalf | Unset = UNSET
    verification: BookingRateWriteVerification | Unset = UNSET
    booking: BookingPricingUpdateResponseBooking | Unset = UNSET
    errors: list[BookingPricingUpdateResponseErrorsItem] | Unset = UNSET
    rate_plan_read_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_pricing_update_response_booking import BookingPricingUpdateResponseBooking
        from ..models.booking_pricing_update_response_errors_item import BookingPricingUpdateResponseErrorsItem
        from ..models.booking_rate_write_occupancy import BookingRateWriteOccupancy
        from ..models.booking_rate_write_price_half import BookingRateWritePriceHalf
        from ..models.booking_rate_write_restriction_half import BookingRateWriteRestrictionHalf
        from ..models.booking_rate_write_verification import BookingRateWriteVerification
        hotel_id: None | str | Unset
        if isinstance(self.hotel_id, Unset):
            hotel_id = UNSET
        else:
            hotel_id = self.hotel_id

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        property_id: None | str | Unset
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        requested = self.requested

        occupancy: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occupancy, Unset):
            occupancy = []
            for occupancy_item_data in self.occupancy:
                occupancy_item = occupancy_item_data.to_dict()
                occupancy.append(occupancy_item)



        applied: str | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied.value


        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        booking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking, Unset):
            booking = self.booking.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        rate_plan_read_error: None | str | Unset
        if isinstance(self.rate_plan_read_error, Unset):
            rate_plan_read_error = UNSET
        else:
            rate_plan_read_error = self.rate_plan_read_error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if requested is not UNSET:
            field_dict["requested"] = requested
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if applied is not UNSET:
            field_dict["applied"] = applied
        if price is not UNSET:
            field_dict["price"] = price
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if verification is not UNSET:
            field_dict["verification"] = verification
        if booking is not UNSET:
            field_dict["booking"] = booking
        if errors is not UNSET:
            field_dict["errors"] = errors
        if rate_plan_read_error is not UNSET:
            field_dict["ratePlanReadError"] = rate_plan_read_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_pricing_update_response_booking import BookingPricingUpdateResponseBooking
        from ..models.booking_pricing_update_response_errors_item import BookingPricingUpdateResponseErrorsItem
        from ..models.booking_rate_write_occupancy import BookingRateWriteOccupancy
        from ..models.booking_rate_write_price_half import BookingRateWritePriceHalf
        from ..models.booking_rate_write_restriction_half import BookingRateWriteRestrictionHalf
        from ..models.booking_rate_write_verification import BookingRateWriteVerification
        d = dict(src_dict)
        def _parse_hotel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hotel_id = _parse_hotel_id(d.pop("hotelId", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))


        requested = d.pop("requested", UNSET)

        _occupancy = d.pop("occupancy", UNSET)
        occupancy: list[BookingRateWriteOccupancy] | Unset = UNSET
        if _occupancy is not UNSET:
            occupancy = []
            for occupancy_item_data in _occupancy:
                occupancy_item = BookingRateWriteOccupancy.from_dict(occupancy_item_data)



                occupancy.append(occupancy_item)


        _applied = d.pop("applied", UNSET)
        applied: BookingPricingUpdateResponseApplied | Unset
        if isinstance(_applied,  Unset):
            applied = UNSET
        else:
            applied = BookingPricingUpdateResponseApplied(_applied)




        _price = d.pop("price", UNSET)
        price: BookingRateWritePriceHalf | Unset
        if isinstance(_price,  Unset):
            price = UNSET
        else:
            price = BookingRateWritePriceHalf.from_dict(_price)




        _restrictions = d.pop("restrictions", UNSET)
        restrictions: BookingRateWriteRestrictionHalf | Unset
        if isinstance(_restrictions,  Unset):
            restrictions = UNSET
        else:
            restrictions = BookingRateWriteRestrictionHalf.from_dict(_restrictions)




        _verification = d.pop("verification", UNSET)
        verification: BookingRateWriteVerification | Unset
        if isinstance(_verification,  Unset):
            verification = UNSET
        else:
            verification = BookingRateWriteVerification.from_dict(_verification)




        _booking = d.pop("booking", UNSET)
        booking: BookingPricingUpdateResponseBooking | Unset
        if isinstance(_booking,  Unset):
            booking = UNSET
        else:
            booking = BookingPricingUpdateResponseBooking.from_dict(_booking)




        _errors = d.pop("errors", UNSET)
        errors: list[BookingPricingUpdateResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BookingPricingUpdateResponseErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        def _parse_rate_plan_read_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rate_plan_read_error = _parse_rate_plan_read_error(d.pop("ratePlanReadError", UNSET))


        booking_pricing_update_response = cls(
            hotel_id=hotel_id,
            listing_id=listing_id,
            property_id=property_id,
            requested=requested,
            occupancy=occupancy,
            applied=applied,
            price=price,
            restrictions=restrictions,
            verification=verification,
            booking=booking,
            errors=errors,
            rate_plan_read_error=rate_plan_read_error,
        )


        booking_pricing_update_response.additional_properties = d
        return booking_pricing_update_response

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
