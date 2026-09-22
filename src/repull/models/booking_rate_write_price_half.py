from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_rate_write_price_half_applied import BookingRateWritePriceHalfApplied
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_rate_write_price_half_errors_item import BookingRateWritePriceHalfErrorsItem
  from ..models.booking_rate_write_verification import BookingRateWriteVerification
  from ..models.booking_upstream_failure import BookingUpstreamFailure





T = TypeVar("T", bound="BookingRateWritePriceHalf")



@_attrs_define
class BookingRateWritePriceHalf:
    """ The prices: what was sent, what Booking.com said, and what is live now.

        Attributes:
            requested (int | Unset): How many updates carried a price.
            applied (BookingRateWritePriceHalfApplied | Unset): What is known about the amounts. Same vocabulary as the top-
                level `applied`, for this half alone.
            verification (BookingRateWriteVerification | Unset): The read-back. Booking.com's answer to a rate write is an
                acknowledgement of the request with no per-date status, so the dates are read back to find out what is actually
                live.
            errors (list[BookingRateWritePriceHalfErrorsItem] | Unset):
            rejection (BookingUpstreamFailure | Unset): Why Booking.com refused one half of a write, in their words. Present
                on the half that was refused.
     """

    requested: int | Unset = UNSET
    applied: BookingRateWritePriceHalfApplied | Unset = UNSET
    verification: BookingRateWriteVerification | Unset = UNSET
    errors: list[BookingRateWritePriceHalfErrorsItem] | Unset = UNSET
    rejection: BookingUpstreamFailure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_rate_write_price_half_errors_item import BookingRateWritePriceHalfErrorsItem
        from ..models.booking_rate_write_verification import BookingRateWriteVerification
        from ..models.booking_upstream_failure import BookingUpstreamFailure
        requested = self.requested

        applied: str | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied.value


        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



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
        if verification is not UNSET:
            field_dict["verification"] = verification
        if errors is not UNSET:
            field_dict["errors"] = errors
        if rejection is not UNSET:
            field_dict["rejection"] = rejection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_rate_write_price_half_errors_item import BookingRateWritePriceHalfErrorsItem
        from ..models.booking_rate_write_verification import BookingRateWriteVerification
        from ..models.booking_upstream_failure import BookingUpstreamFailure
        d = dict(src_dict)
        requested = d.pop("requested", UNSET)

        _applied = d.pop("applied", UNSET)
        applied: BookingRateWritePriceHalfApplied | Unset
        if isinstance(_applied,  Unset):
            applied = UNSET
        else:
            applied = BookingRateWritePriceHalfApplied(_applied)




        _verification = d.pop("verification", UNSET)
        verification: BookingRateWriteVerification | Unset
        if isinstance(_verification,  Unset):
            verification = UNSET
        else:
            verification = BookingRateWriteVerification.from_dict(_verification)




        _errors = d.pop("errors", UNSET)
        errors: list[BookingRateWritePriceHalfErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BookingRateWritePriceHalfErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        _rejection = d.pop("rejection", UNSET)
        rejection: BookingUpstreamFailure | Unset
        if isinstance(_rejection,  Unset):
            rejection = UNSET
        else:
            rejection = BookingUpstreamFailure.from_dict(_rejection)




        booking_rate_write_price_half = cls(
            requested=requested,
            applied=applied,
            verification=verification,
            errors=errors,
            rejection=rejection,
        )


        booking_rate_write_price_half.additional_properties = d
        return booking_rate_write_price_half

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
