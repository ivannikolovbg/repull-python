from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PropertyAvailabilityDay")



@_attrs_define
class PropertyAvailabilityDay:
    """ One calendar day in the availability window.

        Attributes:
            date (datetime.date): The calendar date, ISO `YYYY-MM-DD`. Example: 2026-09-01.
            available (bool): Whether the property is bookable on this date. `false` when the channel calendar marks the
                date unavailable (stop-sell / blocked).
            price (float): Nightly price for this date in the property currency. Falls back to the property's default
                nightly price for dates with no explicit calendar override. Example: 245.
            min_nights (int): Minimum-stay requirement for a stay starting on this date. Example: 2.
     """

    date: datetime.date
    available: bool
    price: float
    min_nights: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        available = self.available

        price = self.price

        min_nights = self.min_nights


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date": date,
            "available": available,
            "price": price,
            "minNights": min_nights,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()




        available = d.pop("available")

        price = d.pop("price")

        min_nights = d.pop("minNights")

        property_availability_day = cls(
            date=date,
            available=available,
            price=price,
            min_nights=min_nights,
        )


        property_availability_day.additional_properties = d
        return property_availability_day

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
