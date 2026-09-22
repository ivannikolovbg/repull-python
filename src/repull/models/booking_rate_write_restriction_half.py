from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_rate_write_restriction_half_applied import BookingRateWriteRestrictionHalfApplied
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_rate_write_restriction_half_errors_item import BookingRateWriteRestrictionHalfErrorsItem
  from ..models.booking_restriction_request_row import BookingRestrictionRequestRow
  from ..models.booking_restriction_verification import BookingRestrictionVerification
  from ..models.booking_upstream_failure import BookingUpstreamFailure





T = TypeVar("T", bound="BookingRateWriteRestrictionHalf")



@_attrs_define
class BookingRateWriteRestrictionHalf:
    """ The restrictions: the same report as the price half, for the other write.

        Attributes:
            requested (int | Unset): How many updates carried a restriction. `0` when none did.
            fields (list[str] | Unset): Every restriction asked for, across all updates.
            dates (list[BookingRestrictionRequestRow] | Unset): Per update, the nights and the restrictions asked for them —
                so a partial result names exactly what did and did not change.
            applied (BookingRateWriteRestrictionHalfApplied | Unset): `not_requested` means no update carried a restriction
                and nothing was sent.
            verification (BookingRestrictionVerification | Unset): The restriction read-back. It runs out of the SAME call
                that reads the prices back, so proving a restriction costs no extra request.
            errors (list[BookingRateWriteRestrictionHalfErrorsItem] | Unset):
            rejection (BookingUpstreamFailure | Unset): Why Booking.com refused one half of a write, in their words. Present
                on the half that was refused.
     """

    requested: int | Unset = UNSET
    fields: list[str] | Unset = UNSET
    dates: list[BookingRestrictionRequestRow] | Unset = UNSET
    applied: BookingRateWriteRestrictionHalfApplied | Unset = UNSET
    verification: BookingRestrictionVerification | Unset = UNSET
    errors: list[BookingRateWriteRestrictionHalfErrorsItem] | Unset = UNSET
    rejection: BookingUpstreamFailure | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_rate_write_restriction_half_errors_item import BookingRateWriteRestrictionHalfErrorsItem
        from ..models.booking_restriction_request_row import BookingRestrictionRequestRow
        from ..models.booking_restriction_verification import BookingRestrictionVerification
        from ..models.booking_upstream_failure import BookingUpstreamFailure
        requested = self.requested

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields



        dates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = []
            for dates_item_data in self.dates:
                dates_item = dates_item_data.to_dict()
                dates.append(dates_item)



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
        if fields is not UNSET:
            field_dict["fields"] = fields
        if dates is not UNSET:
            field_dict["dates"] = dates
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
        from ..models.booking_rate_write_restriction_half_errors_item import BookingRateWriteRestrictionHalfErrorsItem
        from ..models.booking_restriction_request_row import BookingRestrictionRequestRow
        from ..models.booking_restriction_verification import BookingRestrictionVerification
        from ..models.booking_upstream_failure import BookingUpstreamFailure
        d = dict(src_dict)
        requested = d.pop("requested", UNSET)

        fields = cast(list[str], d.pop("fields", UNSET))


        _dates = d.pop("dates", UNSET)
        dates: list[BookingRestrictionRequestRow] | Unset = UNSET
        if _dates is not UNSET:
            dates = []
            for dates_item_data in _dates:
                dates_item = BookingRestrictionRequestRow.from_dict(dates_item_data)



                dates.append(dates_item)


        _applied = d.pop("applied", UNSET)
        applied: BookingRateWriteRestrictionHalfApplied | Unset
        if isinstance(_applied,  Unset):
            applied = UNSET
        else:
            applied = BookingRateWriteRestrictionHalfApplied(_applied)




        _verification = d.pop("verification", UNSET)
        verification: BookingRestrictionVerification | Unset
        if isinstance(_verification,  Unset):
            verification = UNSET
        else:
            verification = BookingRestrictionVerification.from_dict(_verification)




        _errors = d.pop("errors", UNSET)
        errors: list[BookingRateWriteRestrictionHalfErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BookingRateWriteRestrictionHalfErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        _rejection = d.pop("rejection", UNSET)
        rejection: BookingUpstreamFailure | Unset
        if isinstance(_rejection,  Unset):
            rejection = UNSET
        else:
            rejection = BookingUpstreamFailure.from_dict(_rejection)




        booking_rate_write_restriction_half = cls(
            requested=requested,
            fields=fields,
            dates=dates,
            applied=applied,
            verification=verification,
            errors=errors,
            rejection=rejection,
        )


        booking_rate_write_restriction_half.additional_properties = d
        return booking_rate_write_restriction_half

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
