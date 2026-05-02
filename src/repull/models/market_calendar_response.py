from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.market_calendar_day import MarketCalendarDay
  from ..models.market_calendar_response_date_range import MarketCalendarResponseDateRange
  from ..models.market_event import MarketEvent





T = TypeVar("T", bound="MarketCalendarResponse")



@_attrs_define
class MarketCalendarResponse:
    """ 
        Attributes:
            city (str | Unset):
            date_range (MarketCalendarResponseDateRange | Unset):
            days (list[MarketCalendarDay] | Unset):
            events (list[MarketEvent] | Unset):
     """

    city: str | Unset = UNSET
    date_range: MarketCalendarResponseDateRange | Unset = UNSET
    days: list[MarketCalendarDay] | Unset = UNSET
    events: list[MarketEvent] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_calendar_day import MarketCalendarDay
        from ..models.market_calendar_response_date_range import MarketCalendarResponseDateRange
        from ..models.market_event import MarketEvent
        city = self.city

        date_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_range, Unset):
            date_range = self.date_range.to_dict()

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)



        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if city is not UNSET:
            field_dict["city"] = city
        if date_range is not UNSET:
            field_dict["dateRange"] = date_range
        if days is not UNSET:
            field_dict["days"] = days
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_calendar_day import MarketCalendarDay
        from ..models.market_calendar_response_date_range import MarketCalendarResponseDateRange
        from ..models.market_event import MarketEvent
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        _date_range = d.pop("dateRange", UNSET)
        date_range: MarketCalendarResponseDateRange | Unset
        if isinstance(_date_range,  Unset):
            date_range = UNSET
        else:
            date_range = MarketCalendarResponseDateRange.from_dict(_date_range)




        _days = d.pop("days", UNSET)
        days: list[MarketCalendarDay] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = MarketCalendarDay.from_dict(days_item_data)



                days.append(days_item)


        _events = d.pop("events", UNSET)
        events: list[MarketEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = MarketEvent.from_dict(events_item_data)



                events.append(events_item)


        market_calendar_response = cls(
            city=city,
            date_range=date_range,
            days=days,
            events=events,
        )


        market_calendar_response.additional_properties = d
        return market_calendar_response

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
