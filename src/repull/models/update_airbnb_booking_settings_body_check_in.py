from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_booking_settings_body_check_in_end_type_1 import UpdateAirbnbBookingSettingsBodyCheckInEndType1
from ..models.update_airbnb_booking_settings_body_check_in_start_type_1 import UpdateAirbnbBookingSettingsBodyCheckInStartType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyCheckIn")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyCheckIn:
    """ `start` must be earlier than `end` unless either is `FLEXIBLE`.

        Attributes:
            start (int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInStartType1):
            end (int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInEndType1):
     """

    start: int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInStartType1 = UNSET
    end: int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInEndType1 = UNSET





    def to_dict(self) -> dict[str, Any]:
        start: int | None | str | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        elif isinstance(self.start, UpdateAirbnbBookingSettingsBodyCheckInStartType1):
            start = self.start.value
        else:
            start = self.start

        end: int | None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, UpdateAirbnbBookingSettingsBodyCheckInEndType1):
            end = self.end.value
        else:
            end = self.end


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_start(data: object) -> int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInStartType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_1 = UpdateAirbnbBookingSettingsBodyCheckInStartType1(data)



                return start_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInStartType1, data)

        start = _parse_start(d.pop("start", UNSET))


        def _parse_end(data: object) -> int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInEndType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_1 = UpdateAirbnbBookingSettingsBodyCheckInEndType1(data)



                return end_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(int | None | Unset | UpdateAirbnbBookingSettingsBodyCheckInEndType1, data)

        end = _parse_end(d.pop("end", UNSET))


        update_airbnb_booking_settings_body_check_in = cls(
            start=start,
            end=end,
        )

        return update_airbnb_booking_settings_body_check_in

