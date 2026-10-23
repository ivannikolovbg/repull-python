from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingRules")



@_attrs_define
class ListingRules:
    """ 
        Attributes:
            min_nights (int | None | Unset):
            max_nights (int | None | Unset):
            booking_window_days (int | None | Unset): How far ahead a guest can book. `null` when unlimited or not set.
            advance_notice_hours (int | None | Unset): Hours of notice required before check-in.
            preparation_days (int | None | Unset): Nights blocked between stays.
            allows_booking_requests (bool | None | Unset): Whether guests may send a booking request inside the notice
                window.
            instant_book (None | str | Unset):
     """

    min_nights: int | None | Unset = UNSET
    max_nights: int | None | Unset = UNSET
    booking_window_days: int | None | Unset = UNSET
    advance_notice_hours: int | None | Unset = UNSET
    preparation_days: int | None | Unset = UNSET
    allows_booking_requests: bool | None | Unset = UNSET
    instant_book: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_nights: int | None | Unset
        if isinstance(self.min_nights, Unset):
            min_nights = UNSET
        else:
            min_nights = self.min_nights

        max_nights: int | None | Unset
        if isinstance(self.max_nights, Unset):
            max_nights = UNSET
        else:
            max_nights = self.max_nights

        booking_window_days: int | None | Unset
        if isinstance(self.booking_window_days, Unset):
            booking_window_days = UNSET
        else:
            booking_window_days = self.booking_window_days

        advance_notice_hours: int | None | Unset
        if isinstance(self.advance_notice_hours, Unset):
            advance_notice_hours = UNSET
        else:
            advance_notice_hours = self.advance_notice_hours

        preparation_days: int | None | Unset
        if isinstance(self.preparation_days, Unset):
            preparation_days = UNSET
        else:
            preparation_days = self.preparation_days

        allows_booking_requests: bool | None | Unset
        if isinstance(self.allows_booking_requests, Unset):
            allows_booking_requests = UNSET
        else:
            allows_booking_requests = self.allows_booking_requests

        instant_book: None | str | Unset
        if isinstance(self.instant_book, Unset):
            instant_book = UNSET
        else:
            instant_book = self.instant_book


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights
        if max_nights is not UNSET:
            field_dict["maxNights"] = max_nights
        if booking_window_days is not UNSET:
            field_dict["bookingWindowDays"] = booking_window_days
        if advance_notice_hours is not UNSET:
            field_dict["advanceNoticeHours"] = advance_notice_hours
        if preparation_days is not UNSET:
            field_dict["preparationDays"] = preparation_days
        if allows_booking_requests is not UNSET:
            field_dict["allowsBookingRequests"] = allows_booking_requests
        if instant_book is not UNSET:
            field_dict["instantBook"] = instant_book

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_min_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_nights = _parse_min_nights(d.pop("minNights", UNSET))


        def _parse_max_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_nights = _parse_max_nights(d.pop("maxNights", UNSET))


        def _parse_booking_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        booking_window_days = _parse_booking_window_days(d.pop("bookingWindowDays", UNSET))


        def _parse_advance_notice_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        advance_notice_hours = _parse_advance_notice_hours(d.pop("advanceNoticeHours", UNSET))


        def _parse_preparation_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        preparation_days = _parse_preparation_days(d.pop("preparationDays", UNSET))


        def _parse_allows_booking_requests(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allows_booking_requests = _parse_allows_booking_requests(d.pop("allowsBookingRequests", UNSET))


        def _parse_instant_book(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instant_book = _parse_instant_book(d.pop("instantBook", UNSET))


        listing_rules = cls(
            min_nights=min_nights,
            max_nights=max_nights,
            booking_window_days=booking_window_days,
            advance_notice_hours=advance_notice_hours,
            preparation_days=preparation_days,
            allows_booking_requests=allows_booking_requests,
            instant_book=instant_book,
        )


        listing_rules.additional_properties = d
        return listing_rules

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
