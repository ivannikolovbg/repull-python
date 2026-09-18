from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyBookingWindow")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyBookingWindow:
    """ Send `days`, or `unlimited: true`. Sending both is refused.

        Attributes:
            days (int | None | Unset):
            unlimited (bool | None | Unset):
     """

    days: int | None | Unset = UNSET
    unlimited: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        days: int | None | Unset
        if isinstance(self.days, Unset):
            days = UNSET
        else:
            days = self.days

        unlimited: bool | None | Unset
        if isinstance(self.unlimited, Unset):
            unlimited = UNSET
        else:
            unlimited = self.unlimited


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if days is not UNSET:
            field_dict["days"] = days
        if unlimited is not UNSET:
            field_dict["unlimited"] = unlimited

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days = _parse_days(d.pop("days", UNSET))


        def _parse_unlimited(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        unlimited = _parse_unlimited(d.pop("unlimited", UNSET))


        update_airbnb_booking_settings_body_booking_window = cls(
            days=days,
            unlimited=unlimited,
        )

        return update_airbnb_booking_settings_body_booking_window

