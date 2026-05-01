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






T = TypeVar("T", bound="CalendarDay")



@_attrs_define
class CalendarDay:
    """ 
        Attributes:
            date (datetime.date | Unset):  Example: 2026-04-15.
            available (bool | Unset):
            price (float | Unset):  Example: 250.
            min_nights (int | Unset):  Example: 2.
     """

    date: datetime.date | Unset = UNSET
    available: bool | Unset = UNSET
    price: float | Unset = UNSET
    min_nights: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        available = self.available

        price = self.price

        min_nights = self.min_nights


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date is not UNSET:
            field_dict["date"] = date
        if available is not UNSET:
            field_dict["available"] = available
        if price is not UNSET:
            field_dict["price"] = price
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()




        available = d.pop("available", UNSET)

        price = d.pop("price", UNSET)

        min_nights = d.pop("minNights", UNSET)

        calendar_day = cls(
            date=date,
            available=available,
            price=price,
            min_nights=min_nights,
        )


        calendar_day.additional_properties = d
        return calendar_day

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
