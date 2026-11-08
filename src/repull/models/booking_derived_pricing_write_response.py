from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_derived_pricing_write_response_applied import BookingDerivedPricingWriteResponseApplied
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_derived_pricing_write_response_booking import BookingDerivedPricingWriteResponseBooking
  from ..models.booking_derived_pricing_write_response_rates_item import BookingDerivedPricingWriteResponseRatesItem
  from ..models.booking_derived_pricing_write_response_verification import BookingDerivedPricingWriteResponseVerification





T = TypeVar("T", bound="BookingDerivedPricingWriteResponse")



@_attrs_define
class BookingDerivedPricingWriteResponse:
    """ Returned by `PUT /v1/channels/booking/availability` with `type: "derived-pricing"`.

        Attributes:
            property_id (str | Unset):
            requested (int | Unset):
            applied (BookingDerivedPricingWriteResponseApplied | Unset): `verified` — read back, each rate plan holds
                exactly the rules sent. `mismatch` — read back and they differ (`verification.rows`). `unverified` — `verify:
                false`, or the read failed. A refusal is `422 booking_rejected`, not a 200.
            rates (list[BookingDerivedPricingWriteResponseRatesItem] | Unset): Per rate plan, the rules it holds now (as
                read back; as sent when unverified).
            verification (BookingDerivedPricingWriteResponseVerification | Unset):
            booking (BookingDerivedPricingWriteResponseBooking | Unset): Booking.com's answer, verbatim.
     """

    property_id: str | Unset = UNSET
    requested: int | Unset = UNSET
    applied: BookingDerivedPricingWriteResponseApplied | Unset = UNSET
    rates: list[BookingDerivedPricingWriteResponseRatesItem] | Unset = UNSET
    verification: BookingDerivedPricingWriteResponseVerification | Unset = UNSET
    booking: BookingDerivedPricingWriteResponseBooking | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_derived_pricing_write_response_booking import BookingDerivedPricingWriteResponseBooking
        from ..models.booking_derived_pricing_write_response_rates_item import BookingDerivedPricingWriteResponseRatesItem
        from ..models.booking_derived_pricing_write_response_verification import BookingDerivedPricingWriteResponseVerification
        property_id = self.property_id

        requested = self.requested

        applied: str | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied.value


        rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)



        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        booking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking, Unset):
            booking = self.booking.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if requested is not UNSET:
            field_dict["requested"] = requested
        if applied is not UNSET:
            field_dict["applied"] = applied
        if rates is not UNSET:
            field_dict["rates"] = rates
        if verification is not UNSET:
            field_dict["verification"] = verification
        if booking is not UNSET:
            field_dict["booking"] = booking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_derived_pricing_write_response_booking import BookingDerivedPricingWriteResponseBooking
        from ..models.booking_derived_pricing_write_response_rates_item import BookingDerivedPricingWriteResponseRatesItem
        from ..models.booking_derived_pricing_write_response_verification import BookingDerivedPricingWriteResponseVerification
        d = dict(src_dict)
        property_id = d.pop("propertyId", UNSET)

        requested = d.pop("requested", UNSET)

        _applied = d.pop("applied", UNSET)
        applied: BookingDerivedPricingWriteResponseApplied | Unset
        if isinstance(_applied,  Unset):
            applied = UNSET
        else:
            applied = BookingDerivedPricingWriteResponseApplied(_applied)




        _rates = d.pop("rates", UNSET)
        rates: list[BookingDerivedPricingWriteResponseRatesItem] | Unset = UNSET
        if _rates is not UNSET:
            rates = []
            for rates_item_data in _rates:
                rates_item = BookingDerivedPricingWriteResponseRatesItem.from_dict(rates_item_data)



                rates.append(rates_item)


        _verification = d.pop("verification", UNSET)
        verification: BookingDerivedPricingWriteResponseVerification | Unset
        if isinstance(_verification,  Unset):
            verification = UNSET
        else:
            verification = BookingDerivedPricingWriteResponseVerification.from_dict(_verification)




        _booking = d.pop("booking", UNSET)
        booking: BookingDerivedPricingWriteResponseBooking | Unset
        if isinstance(_booking,  Unset):
            booking = UNSET
        else:
            booking = BookingDerivedPricingWriteResponseBooking.from_dict(_booking)




        booking_derived_pricing_write_response = cls(
            property_id=property_id,
            requested=requested,
            applied=applied,
            rates=rates,
            verification=verification,
            booking=booking,
        )


        booking_derived_pricing_write_response.additional_properties = d
        return booking_derived_pricing_write_response

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
