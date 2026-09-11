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






T = TypeVar("T", bound="AvailabilityBatchWriteRequest")



@_attrs_define
class AvailabilityBatchWriteRequest:
    """ 
        Attributes:
            dates (list[datetime.date]): ISO dates. Capped at 731 — Airbnb refuses calendar writes spanning more.
            property_ids (list[int]):
            available (bool | Unset): Block or unblock the dates.
            price (float | Unset): Nightly base price.
            min_nights (int | Unset):
            max_nights (int | Unset):
     """

    dates: list[datetime.date]
    property_ids: list[int]
    available: bool | Unset = UNSET
    price: float | Unset = UNSET
    min_nights: int | Unset = UNSET
    max_nights: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.isoformat()
            dates.append(dates_item)



        property_ids = self.property_ids



        available = self.available

        price = self.price

        min_nights = self.min_nights

        max_nights = self.max_nights


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dates": dates,
            "propertyIds": property_ids,
        })
        if available is not UNSET:
            field_dict["available"] = available
        if price is not UNSET:
            field_dict["price"] = price
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights
        if max_nights is not UNSET:
            field_dict["maxNights"] = max_nights

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dates = []
        _dates = d.pop("dates")
        for dates_item_data in (_dates):
            dates_item = isoparse(dates_item_data).date()



            dates.append(dates_item)


        property_ids = cast(list[int], d.pop("propertyIds"))


        available = d.pop("available", UNSET)

        price = d.pop("price", UNSET)

        min_nights = d.pop("minNights", UNSET)

        max_nights = d.pop("maxNights", UNSET)

        availability_batch_write_request = cls(
            dates=dates,
            property_ids=property_ids,
            available=available,
            price=price,
            min_nights=min_nights,
            max_nights=max_nights,
        )


        availability_batch_write_request.additional_properties = d
        return availability_batch_write_request

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
