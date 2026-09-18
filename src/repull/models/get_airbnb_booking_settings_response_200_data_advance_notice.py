from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAirbnbBookingSettingsResponse200DataAdvanceNotice")



@_attrs_define
class GetAirbnbBookingSettingsResponse200DataAdvanceNotice:
    """ How much notice a booking needs.

        Attributes:
            hours (int | None | Unset): Whole hours of notice. `0` allows same-day bookings.
            same_day_bookings_allowed (bool | None | Unset): Derived: `hours === 0`.
            allow_request_to_book (bool | None | Unset): Whether a guest may still REQUEST to book inside the notice window.
     """

    hours: int | None | Unset = UNSET
    same_day_bookings_allowed: bool | None | Unset = UNSET
    allow_request_to_book: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hours: int | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        else:
            hours = self.hours

        same_day_bookings_allowed: bool | None | Unset
        if isinstance(self.same_day_bookings_allowed, Unset):
            same_day_bookings_allowed = UNSET
        else:
            same_day_bookings_allowed = self.same_day_bookings_allowed

        allow_request_to_book: bool | None | Unset
        if isinstance(self.allow_request_to_book, Unset):
            allow_request_to_book = UNSET
        else:
            allow_request_to_book = self.allow_request_to_book


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hours is not UNSET:
            field_dict["hours"] = hours
        if same_day_bookings_allowed is not UNSET:
            field_dict["sameDayBookingsAllowed"] = same_day_bookings_allowed
        if allow_request_to_book is not UNSET:
            field_dict["allowRequestToBook"] = allow_request_to_book

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))


        def _parse_same_day_bookings_allowed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        same_day_bookings_allowed = _parse_same_day_bookings_allowed(d.pop("sameDayBookingsAllowed", UNSET))


        def _parse_allow_request_to_book(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_request_to_book = _parse_allow_request_to_book(d.pop("allowRequestToBook", UNSET))


        get_airbnb_booking_settings_response_200_data_advance_notice = cls(
            hours=hours,
            same_day_bookings_allowed=same_day_bookings_allowed,
            allow_request_to_book=allow_request_to_book,
        )


        get_airbnb_booking_settings_response_200_data_advance_notice.additional_properties = d
        return get_airbnb_booking_settings_response_200_data_advance_notice

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
