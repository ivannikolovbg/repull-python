from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingOccupancyRule")



@_attrs_define
class BookingOccupancyRule:
    """ One occupancy rule: the price for a party of `persons`, relative to the leading-occupancy price. Send exactly one of
    `additional` or `percentage`.

        Attributes:
            persons (int): The party size this rule prices. Must differ from `leadingOccupancy` and be no more than the room
                holds. Example: 2.
            additional (float | None | Unset): Signed amount added to the leading-occupancy price, in the rate plan's
                currency. `-12.01` = 12.01 less. Example: -12.01.
            percentage (float | None | Unset): Signed percent change from the leading-occupancy price. `-10` = 10% less, `5`
                = 5% more. (Booking.com's own feeds show the result as a multiplier, `90.0`; Repull reads it back as `-10`.)
            round_ (bool | None | Unset): Ask Booking.com to round the derived price. Default `false`.
     """

    persons: int
    additional: float | None | Unset = UNSET
    percentage: float | None | Unset = UNSET
    round_: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        persons = self.persons

        additional: float | None | Unset
        if isinstance(self.additional, Unset):
            additional = UNSET
        else:
            additional = self.additional

        percentage: float | None | Unset
        if isinstance(self.percentage, Unset):
            percentage = UNSET
        else:
            percentage = self.percentage

        round_: bool | None | Unset
        if isinstance(self.round_, Unset):
            round_ = UNSET
        else:
            round_ = self.round_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "persons": persons,
        })
        if additional is not UNSET:
            field_dict["additional"] = additional
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if round_ is not UNSET:
            field_dict["round"] = round_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        persons = d.pop("persons")

        def _parse_additional(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        additional = _parse_additional(d.pop("additional", UNSET))


        def _parse_percentage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percentage = _parse_percentage(d.pop("percentage", UNSET))


        def _parse_round_(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        round_ = _parse_round_(d.pop("round", UNSET))


        booking_occupancy_rule = cls(
            persons=persons,
            additional=additional,
            percentage=percentage,
            round_=round_,
        )

        return booking_occupancy_rule

