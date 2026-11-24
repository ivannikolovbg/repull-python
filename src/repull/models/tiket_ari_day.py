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
  from ..models.tiket_child_price import TiketChildPrice
  from ..models.tiket_occupancy_price import TiketOccupancyPrice





T = TypeVar("T", bound="TiketAriDay")



@_attrs_define
class TiketAriDay:
    """ What tiket.com holds for one night of one room type and rate plan. Rooms to sell (`available`, `booked`) belong to
    the room type and repeat on each of its rate plans; prices and restrictions belong to the rate plan. A field
    tiket.com returned nothing for is `null`.

        Attributes:
            date (datetime.date):  Example: 2026-12-24.
            room_type_code (str): tiket.com room type id.
            rate_plan_code (None | str): tiket.com rate plan id. `null` on a room type with no rate plan selected.
            available (int | None | Unset): Rooms to sell.
            booked (int | None | Unset): Rooms tiket.com has sold for the night.
            price (float | None | Unset): Room Based price per night, tax included.
            occupancy_prices (list[TiketOccupancyPrice] | Unset): Occupancy Based prices. Empty on a Room Based property.
            child_prices (list[TiketChildPrice] | Unset): Children prices as tiket.com holds them (set in the extranet; see
                the note on children rates under `PUT /v1/channels/tiket/availability`).
            currency (None | str | Unset):  Example: IDR.
            min_stay (int | None | Unset): Minimum nights.
            max_stay (int | None | Unset): Maximum nights.
            stop_sell (bool | None | Unset): `true` when the rate plan is closed for the night.
            closed_to_arrival (bool | None | Unset):
            closed_to_departure (bool | None | Unset):
            min_advance_days (int | None | Unset): Minimum days between booking and arrival.
            max_advance_days (int | None | Unset): Maximum days between booking and arrival.
     """

    date: datetime.date
    room_type_code: str
    rate_plan_code: None | str
    available: int | None | Unset = UNSET
    booked: int | None | Unset = UNSET
    price: float | None | Unset = UNSET
    occupancy_prices: list[TiketOccupancyPrice] | Unset = UNSET
    child_prices: list[TiketChildPrice] | Unset = UNSET
    currency: None | str | Unset = UNSET
    min_stay: int | None | Unset = UNSET
    max_stay: int | None | Unset = UNSET
    stop_sell: bool | None | Unset = UNSET
    closed_to_arrival: bool | None | Unset = UNSET
    closed_to_departure: bool | None | Unset = UNSET
    min_advance_days: int | None | Unset = UNSET
    max_advance_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_child_price import TiketChildPrice
        from ..models.tiket_occupancy_price import TiketOccupancyPrice
        date = self.date.isoformat()

        room_type_code = self.room_type_code

        rate_plan_code: None | str
        rate_plan_code = self.rate_plan_code

        available: int | None | Unset
        if isinstance(self.available, Unset):
            available = UNSET
        else:
            available = self.available

        booked: int | None | Unset
        if isinstance(self.booked, Unset):
            booked = UNSET
        else:
            booked = self.booked

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        occupancy_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occupancy_prices, Unset):
            occupancy_prices = []
            for occupancy_prices_item_data in self.occupancy_prices:
                occupancy_prices_item = occupancy_prices_item_data.to_dict()
                occupancy_prices.append(occupancy_prices_item)



        child_prices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_prices, Unset):
            child_prices = []
            for child_prices_item_data in self.child_prices:
                child_prices_item = child_prices_item_data.to_dict()
                child_prices.append(child_prices_item)



        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

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

        stop_sell: bool | None | Unset
        if isinstance(self.stop_sell, Unset):
            stop_sell = UNSET
        else:
            stop_sell = self.stop_sell

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

        min_advance_days: int | None | Unset
        if isinstance(self.min_advance_days, Unset):
            min_advance_days = UNSET
        else:
            min_advance_days = self.min_advance_days

        max_advance_days: int | None | Unset
        if isinstance(self.max_advance_days, Unset):
            max_advance_days = UNSET
        else:
            max_advance_days = self.max_advance_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date": date,
            "roomTypeCode": room_type_code,
            "ratePlanCode": rate_plan_code,
        })
        if available is not UNSET:
            field_dict["available"] = available
        if booked is not UNSET:
            field_dict["booked"] = booked
        if price is not UNSET:
            field_dict["price"] = price
        if occupancy_prices is not UNSET:
            field_dict["occupancyPrices"] = occupancy_prices
        if child_prices is not UNSET:
            field_dict["childPrices"] = child_prices
        if currency is not UNSET:
            field_dict["currency"] = currency
        if min_stay is not UNSET:
            field_dict["minStay"] = min_stay
        if max_stay is not UNSET:
            field_dict["maxStay"] = max_stay
        if stop_sell is not UNSET:
            field_dict["stopSell"] = stop_sell
        if closed_to_arrival is not UNSET:
            field_dict["closedToArrival"] = closed_to_arrival
        if closed_to_departure is not UNSET:
            field_dict["closedToDeparture"] = closed_to_departure
        if min_advance_days is not UNSET:
            field_dict["minAdvanceDays"] = min_advance_days
        if max_advance_days is not UNSET:
            field_dict["maxAdvanceDays"] = max_advance_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_child_price import TiketChildPrice
        from ..models.tiket_occupancy_price import TiketOccupancyPrice
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()




        room_type_code = d.pop("roomTypeCode")

        def _parse_rate_plan_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rate_plan_code = _parse_rate_plan_code(d.pop("ratePlanCode"))


        def _parse_available(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        available = _parse_available(d.pop("available", UNSET))


        def _parse_booked(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        booked = _parse_booked(d.pop("booked", UNSET))


        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))


        _occupancy_prices = d.pop("occupancyPrices", UNSET)
        occupancy_prices: list[TiketOccupancyPrice] | Unset = UNSET
        if _occupancy_prices is not UNSET:
            occupancy_prices = []
            for occupancy_prices_item_data in _occupancy_prices:
                occupancy_prices_item = TiketOccupancyPrice.from_dict(occupancy_prices_item_data)



                occupancy_prices.append(occupancy_prices_item)


        _child_prices = d.pop("childPrices", UNSET)
        child_prices: list[TiketChildPrice] | Unset = UNSET
        if _child_prices is not UNSET:
            child_prices = []
            for child_prices_item_data in _child_prices:
                child_prices_item = TiketChildPrice.from_dict(child_prices_item_data)



                child_prices.append(child_prices_item)


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


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


        def _parse_stop_sell(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        stop_sell = _parse_stop_sell(d.pop("stopSell", UNSET))


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


        def _parse_min_advance_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_advance_days = _parse_min_advance_days(d.pop("minAdvanceDays", UNSET))


        def _parse_max_advance_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_advance_days = _parse_max_advance_days(d.pop("maxAdvanceDays", UNSET))


        tiket_ari_day = cls(
            date=date,
            room_type_code=room_type_code,
            rate_plan_code=rate_plan_code,
            available=available,
            booked=booked,
            price=price,
            occupancy_prices=occupancy_prices,
            child_prices=child_prices,
            currency=currency,
            min_stay=min_stay,
            max_stay=max_stay,
            stop_sell=stop_sell,
            closed_to_arrival=closed_to_arrival,
            closed_to_departure=closed_to_departure,
            min_advance_days=min_advance_days,
            max_advance_days=max_advance_days,
        )


        tiket_ari_day.additional_properties = d
        return tiket_ari_day

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
