from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_booking_settings_body_advance_notice_hours import UpdateAirbnbBookingSettingsBodyAdvanceNoticeHours
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyAdvanceNotice")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyAdvanceNotice:
    """ Send `hours` (or `sameDayCutoff`), `allowRequestToBook`, or both. The half you omit keeps the value Airbnb currently
    holds. `hours` and `sameDayCutoff` are the same setting: send one.

        Attributes:
            hours (UpdateAirbnbBookingSettingsBodyAdvanceNoticeHours | Unset): Counted back from 11:59 PM on the check-in
                day (listing time): `0` = same-day bookings until midnight, `1` = until 11 PM, `24` = no same-day bookings.
            same_day_cutoff (None | str | Unset): The last time a same-day booking is accepted, whole hours in the listing's
                time (`23:00` = 11 PM, `00:00` = midnight). Converted to `hours` (`23:00` = 1). Example: 23:00.
            allow_request_to_book (bool | None | Unset):
     """

    hours: UpdateAirbnbBookingSettingsBodyAdvanceNoticeHours | Unset = UNSET
    same_day_cutoff: None | str | Unset = UNSET
    allow_request_to_book: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        hours: int | Unset = UNSET
        if not isinstance(self.hours, Unset):
            hours = self.hours.value


        same_day_cutoff: None | str | Unset
        if isinstance(self.same_day_cutoff, Unset):
            same_day_cutoff = UNSET
        else:
            same_day_cutoff = self.same_day_cutoff

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
        if same_day_cutoff is not UNSET:
            field_dict["sameDayCutoff"] = same_day_cutoff
        if allow_request_to_book is not UNSET:
            field_dict["allowRequestToBook"] = allow_request_to_book

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _hours = d.pop("hours", UNSET)
        hours: UpdateAirbnbBookingSettingsBodyAdvanceNoticeHours | Unset
        if isinstance(_hours,  Unset):
            hours = UNSET
        else:
            hours = UpdateAirbnbBookingSettingsBodyAdvanceNoticeHours(_hours)




        def _parse_same_day_cutoff(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        same_day_cutoff = _parse_same_day_cutoff(d.pop("sameDayCutoff", UNSET))


        def _parse_allow_request_to_book(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_request_to_book = _parse_allow_request_to_book(d.pop("allowRequestToBook", UNSET))


        update_airbnb_booking_settings_body_advance_notice = cls(
            hours=hours,
            same_day_cutoff=same_day_cutoff,
            allow_request_to_book=allow_request_to_book,
        )

        return update_airbnb_booking_settings_body_advance_notice

