from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_rate_write_verification_row import BookingRateWriteVerificationRow





T = TypeVar("T", bound="BookingRateWriteVerification")



@_attrs_define
class BookingRateWriteVerification:
    """ The read-back. Booking.com's answer to a rate write is an acknowledgement of the request with no per-date status, so
    the dates are read back to find out what is actually live.

        Attributes:
            ran (bool | Unset): Whether the read-back happened.
            skipped_reason (None | str | Unset): Why it did not: `not_requested` (you sent `verify: false`),
                `all_dates_beyond_booking_horizon`, `read_back_failed`, `nothing_to_verify`. Every night of a write is read
                back, however long the range (a year is read in 31-day chunks, in parallel).
            matched (int | Unset):
            mismatched (int | Unset):
            rows (list[BookingRateWriteVerificationRow] | Unset): One row per night. When a write covers more than 62 rows,
                only the nights that did NOT match are listed and `rowsOmitted` counts the rest — `matched` and `mismatched`
                always cover every night.
            rows_omitted (int | None | Unset): Matching nights left out of `rows` on a long write. Absent when every row is
                listed.
            error (None | str | Unset): Present when the read itself failed.
     """

    ran: bool | Unset = UNSET
    skipped_reason: None | str | Unset = UNSET
    matched: int | Unset = UNSET
    mismatched: int | Unset = UNSET
    rows: list[BookingRateWriteVerificationRow] | Unset = UNSET
    rows_omitted: int | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_rate_write_verification_row import BookingRateWriteVerificationRow
        ran = self.ran

        skipped_reason: None | str | Unset
        if isinstance(self.skipped_reason, Unset):
            skipped_reason = UNSET
        else:
            skipped_reason = self.skipped_reason

        matched = self.matched

        mismatched = self.mismatched

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        rows_omitted: int | None | Unset
        if isinstance(self.rows_omitted, Unset):
            rows_omitted = UNSET
        else:
            rows_omitted = self.rows_omitted

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
        if rows is not UNSET:
            field_dict["rows"] = rows
        if rows_omitted is not UNSET:
            field_dict["rowsOmitted"] = rows_omitted
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_rate_write_verification_row import BookingRateWriteVerificationRow
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

        _rows = d.pop("rows", UNSET)
        rows: list[BookingRateWriteVerificationRow] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = BookingRateWriteVerificationRow.from_dict(rows_item_data)



                rows.append(rows_item)


        def _parse_rows_omitted(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rows_omitted = _parse_rows_omitted(d.pop("rowsOmitted", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        booking_rate_write_verification = cls(
            ran=ran,
            skipped_reason=skipped_reason,
            matched=matched,
            mismatched=mismatched,
            rows=rows,
            rows_omitted=rows_omitted,
            error=error,
        )


        booking_rate_write_verification.additional_properties = d
        return booking_rate_write_verification

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
