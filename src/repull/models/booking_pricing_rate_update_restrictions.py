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
    """ Length-of-stay and arrival restrictions for the nights in this update. Omit a field to leave that restriction
    untouched — nothing you do not state is changed.

    These are written on Booking.com's availability notification, which is the wire that carries a restriction when no
    inventory changes hands. Sending them alongside a price is supported: the prices and the restrictions are two
    writes, and the response reports each one separately (`price` and `restrictions`), so a half that lands is never
    reported as a failure and a half that is refused is never reported as applied.

    Three restrictions are refused with `422 restriction_not_supported` naming the field: Booking.com's notification has
    no element for them, and dropping a restriction you stated would be worse than refusing it. Set those on the rate
    plan in the Booking.com Extranet.

        Attributes:
            min_stay (int | None | Unset): Minimum length of stay. Booking.com stores a 1-night minimum as no minimum at
                all, so `minStay: 1` reads back as `0` and is reported as applied.
            max_stay (int | None | Unset): Maximum length of stay.
            closed_to_arrival (bool | None | Unset): Closed-to-arrival — guests may not check in on these nights. `false`
                clears the flag; omit the field to leave it as it is.
            closed_to_departure (bool | None | Unset): Closed-to-departure — guests may not check out on these nights.
                `false` clears the flag; omit the field to leave it as it is.
            min_stay_arrival (int | None | Unset): Arrival-based minimum length of stay — applies to stays that START on
                these nights, rather than any stay covering them.
            max_stay_arrival (int | None | Unset): Arrival-based maximum length of stay.
            exact_stay_arrival (int | None | Unset): Refused. Booking.com's restriction notification has no element for an
                exact arrival-based stay length, so it cannot be written through the API; sending it returns `422
                restriction_not_supported` naming `updates[N].restrictions.exactStayArrival`. Set it on the rate plan in the
                Booking.com Extranet.
            min_advance_res (None | str | Unset): Refused, for the same reason as `exactStayArrival` — returns `422
                restriction_not_supported`. Set the minimum advance-reservation window on the rate plan in the Booking.com
                Extranet.
            max_advance_res (None | str | Unset): Refused, for the same reason as `exactStayArrival` — returns `422
                restriction_not_supported`. Set the maximum advance-reservation window on the rate plan in the Booking.com
                Extranet.
     """

    min_stay: int | None | Unset = UNSET
    max_stay: int | None | Unset = UNSET
    closed_to_arrival: bool | None | Unset = UNSET
    closed_to_departure: bool | None | Unset = UNSET
    min_stay_arrival: int | None | Unset = UNSET
    max_stay_arrival: int | None | Unset = UNSET
    exact_stay_arrival: int | None | Unset = UNSET
    min_advance_res: None | str | Unset = UNSET
    max_advance_res: None | str | Unset = UNSET
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

        min_stay_arrival: int | None | Unset
        if isinstance(self.min_stay_arrival, Unset):
            min_stay_arrival = UNSET
        else:
            min_stay_arrival = self.min_stay_arrival

        max_stay_arrival: int | None | Unset
        if isinstance(self.max_stay_arrival, Unset):
            max_stay_arrival = UNSET
        else:
            max_stay_arrival = self.max_stay_arrival

        exact_stay_arrival: int | None | Unset
        if isinstance(self.exact_stay_arrival, Unset):
            exact_stay_arrival = UNSET
        else:
            exact_stay_arrival = self.exact_stay_arrival

        min_advance_res: None | str | Unset
        if isinstance(self.min_advance_res, Unset):
            min_advance_res = UNSET
        else:
            min_advance_res = self.min_advance_res

        max_advance_res: None | str | Unset
        if isinstance(self.max_advance_res, Unset):
            max_advance_res = UNSET
        else:
            max_advance_res = self.max_advance_res


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
        if min_stay_arrival is not UNSET:
            field_dict["minStayArrival"] = min_stay_arrival
        if max_stay_arrival is not UNSET:
            field_dict["maxStayArrival"] = max_stay_arrival
        if exact_stay_arrival is not UNSET:
            field_dict["exactStayArrival"] = exact_stay_arrival
        if min_advance_res is not UNSET:
            field_dict["minAdvanceRes"] = min_advance_res
        if max_advance_res is not UNSET:
            field_dict["maxAdvanceRes"] = max_advance_res

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


        def _parse_min_stay_arrival(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_stay_arrival = _parse_min_stay_arrival(d.pop("minStayArrival", UNSET))


        def _parse_max_stay_arrival(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_stay_arrival = _parse_max_stay_arrival(d.pop("maxStayArrival", UNSET))


        def _parse_exact_stay_arrival(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exact_stay_arrival = _parse_exact_stay_arrival(d.pop("exactStayArrival", UNSET))


        def _parse_min_advance_res(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_advance_res = _parse_min_advance_res(d.pop("minAdvanceRes", UNSET))


        def _parse_max_advance_res(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_advance_res = _parse_max_advance_res(d.pop("maxAdvanceRes", UNSET))


        booking_pricing_rate_update_restrictions = cls(
            min_stay=min_stay,
            max_stay=max_stay,
            closed_to_arrival=closed_to_arrival,
            closed_to_departure=closed_to_departure,
            min_stay_arrival=min_stay_arrival,
            max_stay_arrival=max_stay_arrival,
            exact_stay_arrival=exact_stay_arrival,
            min_advance_res=min_advance_res,
            max_advance_res=max_advance_res,
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
