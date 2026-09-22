from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_restriction_verification_row import BookingRestrictionVerificationRow





T = TypeVar("T", bound="BookingRestrictionVerification")



@_attrs_define
class BookingRestrictionVerification:
    """ The restriction read-back. It runs out of the SAME call that reads the prices back, so proving a restriction costs
    no extra request.

        Attributes:
            ran (bool | Unset):
            skipped_reason (None | str | Unset): `not_requested` (no restrictions were sent, `verify: false`, or Booking.com
                refused them), `span_too_long`, `all_dates_beyond_booking_horizon`, `read_back_failed`, `nothing_to_verify`.
            matched (int | Unset):
            mismatched (int | Unset):
            unreported (int | Unset): Restrictions Booking.com's read-back did not mention either way. Counted apart from
                `mismatched`: an unknown is not a failure.
            rows (list[BookingRestrictionVerificationRow] | Unset):
            error (None | str | Unset):
     """

    ran: bool | Unset = UNSET
    skipped_reason: None | str | Unset = UNSET
    matched: int | Unset = UNSET
    mismatched: int | Unset = UNSET
    unreported: int | Unset = UNSET
    rows: list[BookingRestrictionVerificationRow] | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_restriction_verification_row import BookingRestrictionVerificationRow
        ran = self.ran

        skipped_reason: None | str | Unset
        if isinstance(self.skipped_reason, Unset):
            skipped_reason = UNSET
        else:
            skipped_reason = self.skipped_reason

        matched = self.matched

        mismatched = self.mismatched

        unreported = self.unreported

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ran is not UNSET:
            field_dict["ran"] = ran
        if skipped_reason is not UNSET:
            field_dict["skippedReason"] = skipped_reason
        if matched is not UNSET:
            field_dict["matched"] = matched
        if mismatched is not UNSET:
            field_dict["mismatched"] = mismatched
        if unreported is not UNSET:
            field_dict["unreported"] = unreported
        if rows is not UNSET:
            field_dict["rows"] = rows
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_restriction_verification_row import BookingRestrictionVerificationRow
        d = dict(src_dict)
        ran = d.pop("ran", UNSET)

        def _parse_skipped_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skipped_reason = _parse_skipped_reason(d.pop("skippedReason", UNSET))


        matched = d.pop("matched", UNSET)

        mismatched = d.pop("mismatched", UNSET)

        unreported = d.pop("unreported", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[BookingRestrictionVerificationRow] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = BookingRestrictionVerificationRow.from_dict(rows_item_data)



                rows.append(rows_item)


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        booking_restriction_verification = cls(
            ran=ran,
            skipped_reason=skipped_reason,
            matched=matched,
            mismatched=mismatched,
            unreported=unreported,
            rows=rows,
            error=error,
        )


        booking_restriction_verification.additional_properties = d
        return booking_restriction_verification

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
