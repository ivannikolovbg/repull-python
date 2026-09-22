from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_restriction_verification_row_field import BookingRestrictionVerificationRowField
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="BookingRestrictionVerificationRow")



@_attrs_define
class BookingRestrictionVerificationRow:
    """ One restriction on one night, read back off Booking.com after the write.

        Attributes:
            room_id (str | Unset):
            rate_id (str | Unset):
            date (datetime.date | Unset):
            field (BookingRestrictionVerificationRowField | Unset):
            expected (bool | int | Unset): The value that was sent.
            booking_value (bool | int | None | Unset): What Booking.com holds for that night now; `null` when they reported
                nothing for the field either way.
            match (bool | Unset):
     """

    room_id: str | Unset = UNSET
    rate_id: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    field: BookingRestrictionVerificationRowField | Unset = UNSET
    expected: bool | int | Unset = UNSET
    booking_value: bool | int | None | Unset = UNSET
    match: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        rate_id = self.rate_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field: str | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.value


        expected: bool | int | Unset
        if isinstance(self.expected, Unset):
            expected = UNSET
        else:
            expected = self.expected

        booking_value: bool | int | None | Unset
        if isinstance(self.booking_value, Unset):
            booking_value = UNSET
        else:
            booking_value = self.booking_value

        match = self.match


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if rate_id is not UNSET:
            field_dict["rateId"] = rate_id
        if date is not UNSET:
            field_dict["date"] = date
        if field is not UNSET:
            field_dict["field"] = field
        if expected is not UNSET:
            field_dict["expected"] = expected
        if booking_value is not UNSET:
            field_dict["bookingValue"] = booking_value
        if match is not UNSET:
            field_dict["match"] = match

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        room_id = d.pop("roomId", UNSET)

        rate_id = d.pop("rateId", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        _field = d.pop("field", UNSET)
        field: BookingRestrictionVerificationRowField | Unset
        if isinstance(_field,  Unset):
            field = UNSET
        else:
            field = BookingRestrictionVerificationRowField(_field)




        def _parse_expected(data: object) -> bool | int | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | int | Unset, data)

        expected = _parse_expected(d.pop("expected", UNSET))


        def _parse_booking_value(data: object) -> bool | int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | int | None | Unset, data)

        booking_value = _parse_booking_value(d.pop("bookingValue", UNSET))


        match = d.pop("match", UNSET)

        booking_restriction_verification_row = cls(
            room_id=room_id,
            rate_id=rate_id,
            date=date,
            field=field,
            expected=expected,
            booking_value=booking_value,
            match=match,
        )


        booking_restriction_verification_row.additional_properties = d
        return booking_restriction_verification_row

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
