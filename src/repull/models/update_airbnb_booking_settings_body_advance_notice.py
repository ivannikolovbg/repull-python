from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyAdvanceNotice")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyAdvanceNotice:
    """ Send `hours`, `allowRequestToBook`, or both. The half you omit keeps the value Airbnb currently holds.

        Attributes:
            hours (int | None | Unset):
            allow_request_to_book (bool | None | Unset):
     """

    hours: int | None | Unset = UNSET
    allow_request_to_book: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hours: int | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        else:
            hours = self.hours

        allow_request_to_book: bool | None | Unset
        if isinstance(self.allow_request_to_book, Unset):
            allow_request_to_book = UNSET
        else:
            allow_request_to_book = self.allow_request_to_book


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if hours is not UNSET:
            field_dict["hours"] = hours
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


        def _parse_allow_request_to_book(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_request_to_book = _parse_allow_request_to_book(d.pop("allowRequestToBook", UNSET))


        update_airbnb_booking_settings_body_advance_notice = cls(
            hours=hours,
            allow_request_to_book=allow_request_to_book,
        )

        return update_airbnb_booking_settings_body_advance_notice

