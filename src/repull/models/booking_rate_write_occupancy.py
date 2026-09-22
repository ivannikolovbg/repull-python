from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_rate_write_occupancy_source import BookingRateWriteOccupancySource
from ..types import UNSET, Unset






T = TypeVar("T", bound="BookingRateWriteOccupancy")



@_attrs_define
class BookingRateWriteOccupancy:
    """ The party size one update was written at, and where that number came from.

        Attributes:
            index (int | Unset): Position of the update in the request `updates[]`.
            room_id (str | Unset):
            rate_id (str | Unset):
            value (int | Unset): The party size the amount was written against.
            source (BookingRateWriteOccupancySource | Unset): `request` — you stated it. `rate_plan` — Booking.com's maximum
                occupancy for this rate plan. `room` — Booking.com's room definition, used when the rate plan did not state one.
     """

    index: int | Unset = UNSET
    room_id: str | Unset = UNSET
    rate_id: str | Unset = UNSET
    value: int | Unset = UNSET
    source: BookingRateWriteOccupancySource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        index = self.index

        room_id = self.room_id

        rate_id = self.rate_id

        value = self.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if rate_id is not UNSET:
            field_dict["rateId"] = rate_id
        if value is not UNSET:
            field_dict["value"] = value
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        room_id = d.pop("roomId", UNSET)

        rate_id = d.pop("rateId", UNSET)

        value = d.pop("value", UNSET)

        _source = d.pop("source", UNSET)
        source: BookingRateWriteOccupancySource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = BookingRateWriteOccupancySource(_source)




        booking_rate_write_occupancy = cls(
            index=index,
            room_id=room_id,
            rate_id=rate_id,
            value=value,
            source=source,
        )


        booking_rate_write_occupancy.additional_properties = d
        return booking_rate_write_occupancy

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
