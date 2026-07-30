from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_calendar_operation_availability import AirbnbCalendarOperationAvailability
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbCalendarOperation")



@_attrs_define
class AirbnbCalendarOperation:
    """ One calendar operation. Supply either `start_date` + `end_date` OR a `dates` array. Every restriction here is
    forwarded verbatim to Airbnb's batch calendar API.

        Attributes:
            start_date (datetime.date | None | Unset): Inclusive range start (pair with `end_date`).
            end_date (datetime.date | None | Unset): Inclusive range end (pair with `start_date`).
            dates (list[str] | None | Unset): Explicit date or `start:end` range strings, as an alternative to
                `start_date`/`end_date`.
            daily_price (float | None | Unset): Nightly price override.
            availability (AirbnbCalendarOperationAvailability | Unset): Stop-sell is expressed here: `unavailable` blocks
                the date(s); `available` re-opens; `default` reverts to rule-based availability.
            min_nights (int | None | Unset): Minimum length of stay for the date(s).
            max_nights (int | None | Unset): Maximum length of stay for the date(s).
            closed_to_arrival (bool | None | Unset): Closed-to-arrival — no check-ins on the affected date(s).
            closed_to_departure (bool | None | Unset): Closed-to-departure — no check-outs on the affected date(s).
            notes (None | str | Unset):
     """

    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    dates: list[str] | None | Unset = UNSET
    daily_price: float | None | Unset = UNSET
    availability: AirbnbCalendarOperationAvailability | Unset = UNSET
    min_nights: int | None | Unset = UNSET
    max_nights: int | None | Unset = UNSET
    closed_to_arrival: bool | None | Unset = UNSET
    closed_to_departure: bool | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        dates: list[str] | None | Unset
        if isinstance(self.dates, Unset):
            dates = UNSET
        elif isinstance(self.dates, list):
            dates = self.dates


        else:
            dates = self.dates

        daily_price: float | None | Unset
        if isinstance(self.daily_price, Unset):
            daily_price = UNSET
        else:
            daily_price = self.daily_price

        availability: str | Unset = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value


        min_nights: int | None | Unset
        if isinstance(self.min_nights, Unset):
            min_nights = UNSET
        else:
            min_nights = self.min_nights

        max_nights: int | None | Unset
        if isinstance(self.max_nights, Unset):
            max_nights = UNSET
        else:
            max_nights = self.max_nights

        closed_to_arrival: bool | None | Unset
        if isinstance(self.closed_to_arrival, Unset):
            closed_to_arrival = UNSET
        else:
            closed_to_arrival = self.closed_to_arrival

        closed_to_departure: bool | None | Unset
        if isinstance(self.closed_to_departure, Unset):
            closed_to_departure = UNSET
        else:
            closed_to_departure = self.closed_to_departure

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if max_nights is not UNSET:
            field_dict["max_nights"] = max_nights
        if closed_to_arrival is not UNSET:
            field_dict["closed_to_arrival"] = closed_to_arrival
        if closed_to_departure is not UNSET:
            field_dict["closed_to_departure"] = closed_to_departure
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()



                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))


        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        def _parse_dates(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dates_type_0 = cast(list[str], data)

                return dates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dates = _parse_dates(d.pop("dates", UNSET))


        def _parse_daily_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        daily_price = _parse_daily_price(d.pop("daily_price", UNSET))


        _availability = d.pop("availability", UNSET)
        availability: AirbnbCalendarOperationAvailability | Unset
        if isinstance(_availability,  Unset):
            availability = UNSET
        else:
            availability = AirbnbCalendarOperationAvailability(_availability)




        def _parse_min_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_nights = _parse_min_nights(d.pop("min_nights", UNSET))


        def _parse_max_nights(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_nights = _parse_max_nights(d.pop("max_nights", UNSET))


        def _parse_closed_to_arrival(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed_to_arrival = _parse_closed_to_arrival(d.pop("closed_to_arrival", UNSET))


        def _parse_closed_to_departure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed_to_departure = _parse_closed_to_departure(d.pop("closed_to_departure", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        airbnb_calendar_operation = cls(
            start_date=start_date,
            end_date=end_date,
            dates=dates,
            daily_price=daily_price,
            availability=availability,
            min_nights=min_nights,
            max_nights=max_nights,
            closed_to_arrival=closed_to_arrival,
            closed_to_departure=closed_to_departure,
            notes=notes,
        )


        airbnb_calendar_operation.additional_properties = d
        return airbnb_calendar_operation

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
