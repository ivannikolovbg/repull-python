from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingPricingRateUpdateRestrictions")



@_attrs_define
class BookingPricingRateUpdateRestrictions:
    """ Optional length-of-stay / availability restrictions for one rate update.

        Attributes:
            min_stay (int | None | Unset):
            max_stay (int | None | Unset):
            closed_to_arrival (bool | None | Unset):
            closed_to_departure (bool | None | Unset):
     """

    min_stay: int | None | Unset = UNSET
    max_stay: int | None | Unset = UNSET
    closed_to_arrival: bool | None | Unset = UNSET
    closed_to_departure: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_stay: int | None | Unset
        if isinstance(self.min_stay, Unset):
            min_stay = UNSET
        else:
            min_stay = self.min_stay

        max_stay: int | None | Unset
        if isinstance(self.max_stay, Unset):
            max_stay = UNSET
        else:
            max_stay = self.max_stay

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_stay is not UNSET:
            field_dict["minStay"] = min_stay
        if max_stay is not UNSET:
            field_dict["maxStay"] = max_stay
        if closed_to_arrival is not UNSET:
            field_dict["closedToArrival"] = closed_to_arrival
        if closed_to_departure is not UNSET:
            field_dict["closedToDeparture"] = closed_to_departure

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_min_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_stay = _parse_min_stay(d.pop("minStay", UNSET))


        def _parse_max_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_stay = _parse_max_stay(d.pop("maxStay", UNSET))


        def _parse_closed_to_arrival(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed_to_arrival = _parse_closed_to_arrival(d.pop("closedToArrival", UNSET))


        def _parse_closed_to_departure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        closed_to_departure = _parse_closed_to_departure(d.pop("closedToDeparture", UNSET))


        booking_pricing_rate_update_restrictions = cls(
            min_stay=min_stay,
            max_stay=max_stay,
            closed_to_arrival=closed_to_arrival,
            closed_to_departure=closed_to_departure,
        )


        booking_pricing_rate_update_restrictions.additional_properties = d
        return booking_pricing_rate_update_restrictions

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
