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






T = TypeVar("T", bound="PromotionRulesBookingWindow")



@_attrs_define
class PromotionRulesBookingWindow:
    """ 
        Attributes:
            start (datetime.date | Unset):
            end (datetime.date | Unset):
            start_hour (int | Unset):
            end_hour (int | Unset):
     """

    start: datetime.date | Unset = UNSET
    end: datetime.date | Unset = UNSET
    start_hour: int | Unset = UNSET
    end_hour: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        start_hour = self.start_hour

        end_hour = self.end_hour


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if start_hour is not UNSET:
            field_dict["startHour"] = start_hour
        if end_hour is not UNSET:
            field_dict["endHour"] = end_hour

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




        start_hour = d.pop("startHour", UNSET)

        end_hour = d.pop("endHour", UNSET)

        promotion_rules_booking_window = cls(
            start=start,
            end=end,
            start_hour=start_hour,
            end_hour=end_hour,
        )


        promotion_rules_booking_window.additional_properties = d
        return promotion_rules_booking_window

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
