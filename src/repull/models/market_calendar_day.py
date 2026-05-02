from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.market_calendar_day_events_item import MarketCalendarDayEventsItem





T = TypeVar("T", bound="MarketCalendarDay")



@_attrs_define
class MarketCalendarDay:
    """ 
        Attributes:
            date (datetime.date | Unset):
            market_avg_rate (float | None | Unset):
            market_min_rate (float | None | Unset):
            market_max_rate (float | None | Unset):
            priced_listings (int | Unset):
            occupancy_pct (float | None | Unset):
            total_listings (int | Unset):
            wheelhouse_occupancy (float | None | Unset):
            wheelhouse_adr (float | None | Unset):
            events (list[MarketCalendarDayEventsItem] | Unset):
            my_price (float | None | Unset): Only present when `listingId` is supplied.
            my_available (bool | Unset): Only meaningful when `listingId` is supplied.
     """

    date: datetime.date | Unset = UNSET
    market_avg_rate: float | None | Unset = UNSET
    market_min_rate: float | None | Unset = UNSET
    market_max_rate: float | None | Unset = UNSET
    priced_listings: int | Unset = UNSET
    occupancy_pct: float | None | Unset = UNSET
    total_listings: int | Unset = UNSET
    wheelhouse_occupancy: float | None | Unset = UNSET
    wheelhouse_adr: float | None | Unset = UNSET
    events: list[MarketCalendarDayEventsItem] | Unset = UNSET
    my_price: float | None | Unset = UNSET
    my_available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_calendar_day_events_item import MarketCalendarDayEventsItem
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        market_avg_rate: float | None | Unset
        if isinstance(self.market_avg_rate, Unset):
            market_avg_rate = UNSET
        else:
            market_avg_rate = self.market_avg_rate

        market_min_rate: float | None | Unset
        if isinstance(self.market_min_rate, Unset):
            market_min_rate = UNSET
        else:
            market_min_rate = self.market_min_rate

        market_max_rate: float | None | Unset
        if isinstance(self.market_max_rate, Unset):
            market_max_rate = UNSET
        else:
            market_max_rate = self.market_max_rate

        priced_listings = self.priced_listings

        occupancy_pct: float | None | Unset
        if isinstance(self.occupancy_pct, Unset):
            occupancy_pct = UNSET
        else:
            occupancy_pct = self.occupancy_pct

        total_listings = self.total_listings

        wheelhouse_occupancy: float | None | Unset
        if isinstance(self.wheelhouse_occupancy, Unset):
            wheelhouse_occupancy = UNSET
        else:
            wheelhouse_occupancy = self.wheelhouse_occupancy

        wheelhouse_adr: float | None | Unset
        if isinstance(self.wheelhouse_adr, Unset):
            wheelhouse_adr = UNSET
        else:
            wheelhouse_adr = self.wheelhouse_adr

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)



        my_price: float | None | Unset
        if isinstance(self.my_price, Unset):
            my_price = UNSET
        else:
            my_price = self.my_price

        my_available = self.my_available


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if market_avg_rate is not UNSET:
            field_dict["marketAvgRate"] = market_avg_rate
        if market_min_rate is not UNSET:
            field_dict["marketMinRate"] = market_min_rate
        if market_max_rate is not UNSET:
            field_dict["marketMaxRate"] = market_max_rate
        if priced_listings is not UNSET:
            field_dict["pricedListings"] = priced_listings
        if occupancy_pct is not UNSET:
            field_dict["occupancyPct"] = occupancy_pct
        if total_listings is not UNSET:
            field_dict["totalListings"] = total_listings
        if wheelhouse_occupancy is not UNSET:
            field_dict["wheelhouseOccupancy"] = wheelhouse_occupancy
        if wheelhouse_adr is not UNSET:
            field_dict["wheelhouseAdr"] = wheelhouse_adr
        if events is not UNSET:
            field_dict["events"] = events
        if my_price is not UNSET:
            field_dict["myPrice"] = my_price
        if my_available is not UNSET:
            field_dict["myAvailable"] = my_available

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_calendar_day_events_item import MarketCalendarDayEventsItem
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        def _parse_market_avg_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_avg_rate = _parse_market_avg_rate(d.pop("marketAvgRate", UNSET))


        def _parse_market_min_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_min_rate = _parse_market_min_rate(d.pop("marketMinRate", UNSET))


        def _parse_market_max_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_max_rate = _parse_market_max_rate(d.pop("marketMaxRate", UNSET))


        priced_listings = d.pop("pricedListings", UNSET)

        def _parse_occupancy_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        occupancy_pct = _parse_occupancy_pct(d.pop("occupancyPct", UNSET))


        total_listings = d.pop("totalListings", UNSET)

        def _parse_wheelhouse_occupancy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wheelhouse_occupancy = _parse_wheelhouse_occupancy(d.pop("wheelhouseOccupancy", UNSET))


        def _parse_wheelhouse_adr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wheelhouse_adr = _parse_wheelhouse_adr(d.pop("wheelhouseAdr", UNSET))


        _events = d.pop("events", UNSET)
        events: list[MarketCalendarDayEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = MarketCalendarDayEventsItem.from_dict(events_item_data)



                events.append(events_item)


        def _parse_my_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        my_price = _parse_my_price(d.pop("myPrice", UNSET))


        my_available = d.pop("myAvailable", UNSET)

        market_calendar_day = cls(
            date=date,
            market_avg_rate=market_avg_rate,
            market_min_rate=market_min_rate,
            market_max_rate=market_max_rate,
            priced_listings=priced_listings,
            occupancy_pct=occupancy_pct,
            total_listings=total_listings,
            wheelhouse_occupancy=wheelhouse_occupancy,
            wheelhouse_adr=wheelhouse_adr,
            events=events,
            my_price=my_price,
            my_available=my_available,
        )


        market_calendar_day.additional_properties = d
        return market_calendar_day

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
