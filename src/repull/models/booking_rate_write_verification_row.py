from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="BookingRateWriteVerificationRow")



@_attrs_define
class BookingRateWriteVerificationRow:
    """ One night, read back off Booking.com after the write.

        Attributes:
            room_id (str | Unset):
            rate_id (str | Unset):
            date (datetime.date | Unset):
            expected_price (float | Unset): The amount that was sent.
            booking_price (float | None | Unset): The amount Booking.com holds for that night now; `null` when Booking.com
                reported nothing for it.
            match (bool | Unset):
     """

    room_id: str | Unset = UNSET
    rate_id: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    expected_price: float | Unset = UNSET
    booking_price: float | None | Unset = UNSET
    match: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        room_id = self.room_id

        rate_id = self.rate_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        expected_price = self.expected_price

        booking_price: float | None | Unset
        if isinstance(self.booking_price, Unset):
            booking_price = UNSET
        else:
            booking_price = self.booking_price

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
        if expected_price is not UNSET:
            field_dict["expectedPrice"] = expected_price
        if booking_price is not UNSET:
            field_dict["bookingPrice"] = booking_price
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




        expected_price = d.pop("expectedPrice", UNSET)

        def _parse_booking_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        booking_price = _parse_booking_price(d.pop("bookingPrice", UNSET))


        match = d.pop("match", UNSET)

        booking_rate_write_verification_row = cls(
            room_id=room_id,
            rate_id=rate_id,
            date=date,
            expected_price=expected_price,
            booking_price=booking_price,
            match=match,
        )


        booking_rate_write_verification_row.additional_properties = d
        return booking_rate_write_verification_row

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
