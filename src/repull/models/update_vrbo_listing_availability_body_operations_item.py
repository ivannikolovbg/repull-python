from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_availability_body_operations_item_availability import UpdateVrboListingAvailabilityBodyOperationsItemAvailability
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="UpdateVrboListingAvailabilityBodyOperationsItem")



@_attrs_define
class UpdateVrboListingAvailabilityBodyOperationsItem:
    """ One write, applied to every night it names: `start_date` + `end_date` (inclusive) or `dates`. The fields are those
    of the Airbnb per-channel calendar operation.

        Attributes:
            start_date (datetime.date | Unset):
            end_date (datetime.date | Unset):
            dates (list[str] | Unset): `YYYY-MM-DD`, or ranges as `YYYY-MM-DD:YYYY-MM-DD`.
            daily_price (float | Unset): The nightly price on Vrbo, in the listing's Vrbo currency (sent as is — no markup).
            availability (UpdateVrboListingAvailabilityBodyOperationsItemAvailability | Unset): `unavailable` blocks the
                nights on Vrbo; `available` opens them (never a night a booking holds).
            min_nights (int | Unset):
            closed_to_arrival (bool | Unset): No check-in on these nights.
            closed_to_departure (bool | Unset): No check-out on these nights.
     """

    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    dates: list[str] | Unset = UNSET
    daily_price: float | Unset = UNSET
    availability: UpdateVrboListingAvailabilityBodyOperationsItemAvailability | Unset = UNSET
    min_nights: int | Unset = UNSET
    closed_to_arrival: bool | Unset = UNSET
    closed_to_departure: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        dates: list[str] | Unset = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates



        daily_price = self.daily_price

        availability: str | Unset = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value


        min_nights = self.min_nights

        closed_to_arrival = self.closed_to_arrival

        closed_to_departure = self.closed_to_departure


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if dates is not UNSET:
            field_dict["dates"] = dates
        if daily_price is not UNSET:
            field_dict["daily_price"] = daily_price
        if availability is not UNSET:
            field_dict["availability"] = availability
        if min_nights is not UNSET:
            field_dict["min_nights"] = min_nights
        if closed_to_arrival is not UNSET:
            field_dict["closed_to_arrival"] = closed_to_arrival
        if closed_to_departure is not UNSET:
            field_dict["closed_to_departure"] = closed_to_departure

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()




        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()




        dates = cast(list[str], d.pop("dates", UNSET))


        daily_price = d.pop("daily_price", UNSET)

        _availability = d.pop("availability", UNSET)
        availability: UpdateVrboListingAvailabilityBodyOperationsItemAvailability | Unset
        if isinstance(_availability,  Unset):
            availability = UNSET
        else:
            availability = UpdateVrboListingAvailabilityBodyOperationsItemAvailability(_availability)




        min_nights = d.pop("min_nights", UNSET)

        closed_to_arrival = d.pop("closed_to_arrival", UNSET)

        closed_to_departure = d.pop("closed_to_departure", UNSET)

        update_vrbo_listing_availability_body_operations_item = cls(
            start_date=start_date,
            end_date=end_date,
            dates=dates,
            daily_price=daily_price,
            availability=availability,
            min_nights=min_nights,
            closed_to_arrival=closed_to_arrival,
            closed_to_departure=closed_to_departure,
        )

        return update_vrbo_listing_availability_body_operations_item

