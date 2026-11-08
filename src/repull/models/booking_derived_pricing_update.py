from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.booking_occupancy_rule import BookingOccupancyRule





T = TypeVar("T", bound="BookingDerivedPricingUpdate")



@_attrs_define
class BookingDerivedPricingUpdate:
    """ Occupancy-based pricing for one rate plan (Booking.com "derived prices"). The nightly price you write with `type:
    "rates"` is the price for `leadingOccupancy` guests; each rule prices a smaller (or other) party relative to it, on
    every night — date-specific prices included.

    **A write replaces the rate plan's whole rule set.** Rules you leave out are removed. Send `"occupancies": []` to
    remove every rule (all party sizes then pay the leading price).

    Read the rules back with `GET /v1/channels/booking/properties/{id}/rooms` (`rates[].occupancyPricing`); this write
    also reads them back itself unless you send `verify: false`.

        Attributes:
            room_id (str): Booking.com room id. Example: 1761085301.
            rate_id (str): Booking.com rate-plan id. Its `pricingType` must be `RLO` or `OBP`. Example: 70596570.
            leading_occupancy (int): The party size the nightly price is for. Must equal the rate plan's `maxPersons` (`GET
                /v1/channels/booking/properties/{id}/rooms`): Booking.com accepts a different value and then drops every nightly
                price on the rate plan, so any other value is refused with `422`. Example: 3.
            occupancies (list[BookingOccupancyRule]): The rules, one per party size. `rules` is accepted as an alias. Empty
                removes every rule. Example: [{'persons': 2, 'additional': -12.01}, {'persons': 1, 'additional': -12.01}].
     """

    room_id: str
    rate_id: str
    leading_occupancy: int
    occupancies: list[BookingOccupancyRule]





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_occupancy_rule import BookingOccupancyRule
        room_id = self.room_id

        rate_id = self.rate_id

        leading_occupancy = self.leading_occupancy

        occupancies = []
        for occupancies_item_data in self.occupancies:
            occupancies_item = occupancies_item_data.to_dict()
            occupancies.append(occupancies_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "roomId": room_id,
            "rateId": rate_id,
            "leadingOccupancy": leading_occupancy,
            "occupancies": occupancies,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_occupancy_rule import BookingOccupancyRule
        d = dict(src_dict)
        room_id = d.pop("roomId")

        rate_id = d.pop("rateId")

        leading_occupancy = d.pop("leadingOccupancy")

        occupancies = []
        _occupancies = d.pop("occupancies")
        for occupancies_item_data in (_occupancies):
            occupancies_item = BookingOccupancyRule.from_dict(occupancies_item_data)



            occupancies.append(occupancies_item)


        booking_derived_pricing_update = cls(
            room_id=room_id,
            rate_id=rate_id,
            leading_occupancy=leading_occupancy,
            occupancies=occupancies,
        )

        return booking_derived_pricing_update

