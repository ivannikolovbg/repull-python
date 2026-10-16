from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_rules_stay_window_weekdays_item import PromotionRulesStayWindowWeekdaysItem
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PromotionRulesStayWindow")



@_attrs_define
class PromotionRulesStayWindow:
    """ 
        Attributes:
            start (datetime.date | Unset):
            end (datetime.date | Unset):
            weekdays (list[PromotionRulesStayWindowWeekdaysItem] | Unset):
            excluded_dates (list[datetime.date] | Unset):
            additional_dates (list[datetime.date] | Unset):
     """

    start: datetime.date | Unset = UNSET
    end: datetime.date | Unset = UNSET
    weekdays: list[PromotionRulesStayWindowWeekdaysItem] | Unset = UNSET
    excluded_dates: list[datetime.date] | Unset = UNSET
    additional_dates: list[datetime.date] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        weekdays: list[str] | Unset = UNSET
        if not isinstance(self.weekdays, Unset):
            weekdays = []
            for weekdays_item_data in self.weekdays:
                weekdays_item = weekdays_item_data.value
                weekdays.append(weekdays_item)



        excluded_dates: list[str] | Unset = UNSET
        if not isinstance(self.excluded_dates, Unset):
            excluded_dates = []
            for excluded_dates_item_data in self.excluded_dates:
                excluded_dates_item = excluded_dates_item_data.isoformat()
                excluded_dates.append(excluded_dates_item)



        additional_dates: list[str] | Unset = UNSET
        if not isinstance(self.additional_dates, Unset):
            additional_dates = []
            for additional_dates_item_data in self.additional_dates:
                additional_dates_item = additional_dates_item_data.isoformat()
                additional_dates.append(additional_dates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays
        if excluded_dates is not UNSET:
            field_dict["excludedDates"] = excluded_dates
        if additional_dates is not UNSET:
            field_dict["additionalDates"] = additional_dates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _start = d.pop("start", UNSET)
        start: datetime.date | Unset
        if isinstance(_start,  Unset):
            start = UNSET
        else:
            start = isoparse(_start).date()




        _end = d.pop("end", UNSET)
        end: datetime.date | Unset
        if isinstance(_end,  Unset):
            end = UNSET
        else:
            end = isoparse(_end).date()




        _weekdays = d.pop("weekdays", UNSET)
        weekdays: list[PromotionRulesStayWindowWeekdaysItem] | Unset = UNSET
        if _weekdays is not UNSET:
            weekdays = []
            for weekdays_item_data in _weekdays:
                weekdays_item = PromotionRulesStayWindowWeekdaysItem(weekdays_item_data)



                weekdays.append(weekdays_item)


        _excluded_dates = d.pop("excludedDates", UNSET)
        excluded_dates: list[datetime.date] | Unset = UNSET
        if _excluded_dates is not UNSET:
            excluded_dates = []
            for excluded_dates_item_data in _excluded_dates:
                excluded_dates_item = isoparse(excluded_dates_item_data).date()



                excluded_dates.append(excluded_dates_item)


        _additional_dates = d.pop("additionalDates", UNSET)
        additional_dates: list[datetime.date] | Unset = UNSET
        if _additional_dates is not UNSET:
            additional_dates = []
            for additional_dates_item_data in _additional_dates:
                additional_dates_item = isoparse(additional_dates_item_data).date()



                additional_dates.append(additional_dates_item)


        promotion_rules_stay_window = cls(
            start=start,
            end=end,
            weekdays=weekdays,
            excluded_dates=excluded_dates,
            additional_dates=additional_dates,
        )


        promotion_rules_stay_window.additional_properties = d
        return promotion_rules_stay_window

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
