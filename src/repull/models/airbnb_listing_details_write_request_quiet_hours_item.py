from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AirbnbListingDetailsWriteRequestQuietHoursItem")



@_attrs_define
class AirbnbListingDetailsWriteRequestQuietHoursItem:
    """ 
        Attributes:
            start_time (str):  Example: 22.
            end_time (str):  Example: 7.
     """

    start_time: str
    end_time: str





    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "start_time": start_time,
            "end_time": end_time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        airbnb_listing_details_write_request_quiet_hours_item = cls(
            start_time=start_time,
            end_time=end_time,
        )

        return airbnb_listing_details_write_request_quiet_hours_item

