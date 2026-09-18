from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateAirbnbBookingSettingsBodyCheckOut")



@_attrs_define
class UpdateAirbnbBookingSettingsBodyCheckOut:
    """ 
        Attributes:
            time (int):
     """

    time: int





    def to_dict(self) -> dict[str, Any]:
        time = self.time


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "time": time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time")

        update_airbnb_booking_settings_body_check_out = cls(
            time=time,
        )

        return update_airbnb_booking_settings_body_check_out

