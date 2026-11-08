from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_restriction_write_response_applied import BookingRestrictionWriteResponseApplied
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_restriction_request_row import BookingRestrictionRequestRow
  from ..models.booking_restriction_verification import BookingRestrictionVerification
  from ..models.booking_restriction_write_response_booking import BookingRestrictionWriteResponseBooking
  from ..models.booking_restriction_write_response_errors_item import BookingRestrictionWriteResponseErrorsItem
  from ..models.booking_upstream_failure import BookingUpstreamFailure





T = TypeVar("T", bound="BookingRestrictionWriteResponse")



@_attrs_define
class BookingRestrictionWriteResponse:
    """ Returned by `PUT /v1/channels/booking/availability` for a restriction-only `type: "availability"` write (and as
    `restrictions` beside `inventory` when the write also changed inventory).

        Attributes:
            requested (int | Unset): How many updates carried a restriction.
            applied (BookingRestrictionWriteResponseApplied | Unset): `verified` — read back, Booking.com holds every
                restriction sent. `mismatch` — read back, some differ (`verification.rows`). `rejected` — Booking.com refused it
                (`rejection`). `unverified` — the read-back could not run. `acknowledged` — you sent `verify: false`:
                Booking.com took the request and nothing was read back.
            fields (list[str] | Unset):
            dates (list[BookingRestrictionRequestRow] | Unset):
            verification (BookingRestrictionVerification | Unset): The restriction read-back. It runs out of the SAME call
                that reads the prices back, so proving a restriction costs no extra request.
            errors (list[BookingRestrictionWriteResponseErrorsItem] | Unset):
            booking (BookingRestrictionWriteResponseBooking | Unset): Booking.com's answer, verbatim.
            rejection (BookingUpstreamFailure | Unset): Why Booking.com refused one half of a write, in their words. Present
                on the half that was refused.
     """

    requested: int | Unset = UNSET
    applied: BookingRestrictionWriteResponseApplied | Unset = UNSET
    fields: list[str] | Unset = UNSET
    dates: list[BookingRestrictionRequestRow] | Unset = UNSET
    verification: BookingRestrictionVerification | Unset = UNSET
    errors: list[BookingRestrictionWriteResponseErrorsItem] | Unset = UNSET
    booking: BookingRestrictionWriteResponseBooking | Unset = UNSET
    rejection: BookingUpstreamFailure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_restriction_request_row import BookingRestrictionRequestRow
        from ..models.booking_restriction_verification import BookingRestrictionVerification
        from ..models.booking_restriction_write_response_booking import BookingRestrictionWriteResponseBooking
        from ..models.booking_restriction_write_response_errors_item import BookingRestrictionWriteResponseErrorsItem
        from ..models.booking_upstream_failure import BookingUpstreamFailure
        requested = self.requested

        applied: str | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied.value


        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields



        dates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.to_dict()
                dates.append(dates_item)



        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        booking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking, Unset):
            booking = self.booking.to_dict()

        rejection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rejection, Unset):
            rejection = self.rejection.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if requested is not UNSET:
            field_dict["requested"] = requested
        if applied is not UNSET:
            field_dict["applied"] = applied
        if fields is not UNSET:
            field_dict["fields"] = fields
        if dates is not UNSET:
            field_dict["dates"] = dates
        if verification is not UNSET:
            field_dict["verification"] = verification
        if errors is not UNSET:
            field_dict["errors"] = errors
        if booking is not UNSET:
            field_dict["booking"] = booking
        if rejection is not UNSET:
            field_dict["rejection"] = rejection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_restriction_request_row import BookingRestrictionRequestRow
        from ..models.booking_restriction_verification import BookingRestrictionVerification
        from ..models.booking_restriction_write_response_booking import BookingRestrictionWriteResponseBooking
        from ..models.booking_restriction_write_response_errors_item import BookingRestrictionWriteResponseErrorsItem
        from ..models.booking_upstream_failure import BookingUpstreamFailure
        d = dict(src_dict)
        requested = d.pop("requested", UNSET)

        _applied = d.pop("applied", UNSET)
        applied: BookingRestrictionWriteResponseApplied | Unset
        if isinstance(_applied,  Unset):
            applied = UNSET
        else:
            applied = BookingRestrictionWriteResponseApplied(_applied)




        fields = cast(list[str], d.pop("fields", UNSET))


        _dates = d.pop("dates", UNSET)
        dates: list[BookingRestrictionRequestRow] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = BookingRestrictionRequestRow.from_dict(dates_item_data)



                dates.append(dates_item)


        _verification = d.pop("verification", UNSET)
        verification: BookingRestrictionVerification | Unset
        if isinstance(_verification,  Unset):
            verification = UNSET
        else:
            verification = BookingRestrictionVerification.from_dict(_verification)




        _errors = d.pop("errors", UNSET)
        errors: list[BookingRestrictionWriteResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BookingRestrictionWriteResponseErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        _booking = d.pop("booking", UNSET)
        booking: BookingRestrictionWriteResponseBooking | Unset
        if isinstance(_booking,  Unset):
            booking = UNSET
        else:
            booking = BookingRestrictionWriteResponseBooking.from_dict(_booking)




        _rejection = d.pop("rejection", UNSET)
        rejection: BookingUpstreamFailure | Unset
        if isinstance(_rejection,  Unset):
            rejection = UNSET
        else:
            rejection = BookingUpstreamFailure.from_dict(_rejection)




        booking_restriction_write_response = cls(
            requested=requested,
            applied=applied,
            fields=fields,
            dates=dates,
            verification=verification,
            errors=errors,
            booking=booking,
            rejection=rejection,
        )


        booking_restriction_write_response.additional_properties = d
        return booking_restriction_write_response

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
