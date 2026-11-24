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





T = TypeVar("T", bound="TiketAriUpdate")



@_attrs_define
class TiketAriUpdate:
    """ One date range for one room type (and, for `rates` and `restrictions`, one rate plan). Which fields apply depends on
    the request's `type`.

        Attributes:
            start (datetime.date): First night. tiket.com accepts today up to 500 days ahead.
            end (datetime.date): Last night, inclusive.
            room_type_code (str | Unset): tiket.com room type id. Required on `PUT /v1/channels/tiket/availability`; on the
                listing route it is always the listing's room.
            rate_plan_code (str | Unset): tiket.com rate plan id. Required for `rates` and `restrictions` on `PUT
                /v1/channels/tiket/availability`; on the listing route it defaults to every rate plan of the room selected for
                pushes.
            available_rooms (int | Unset): `availability`: rooms to sell.
            price (float | Unset): `rates` on a Room Based property: price per night, tax included. Greater than 0.
            occupancy_prices (list[TiketOccupancyPrice] | Unset): `rates` on an Occupancy Based property. Send `price` or
                `occupancyPrices`, not both.
            child_prices (list[TiketChildPrice] | Unset): Children prices. **Children rates are paused.** tiket.com has
                asked every channel manager not to send children rates until it fixes an issue on its side, so a write that
                includes `childPrices` is refused with `422 invalid_params` and nothing is sent. Children rates set in the
                tiket.com extranet still apply. Send `price` or `occupancyPrices` without `childPrices`.
            currency (str | Unset): ISO 4217. Defaults to the property currency. Example: IDR.
            min_stay (int | Unset): `restrictions`: minimum nights.
            max_stay (int | Unset): `restrictions`: maximum nights.
            stop_sell (bool | Unset): `restrictions`: close (`true`) or open (`false`) the rate plan. With `availability`
                and a `ratePlanCode`, also closes that rate plan.
            closed_to_arrival (bool | Unset): `restrictions`.
            closed_to_departure (bool | Unset): `restrictions`.
            min_advance_days (int | Unset): `restrictions`: minimum days between booking and arrival.
            max_advance_days (int | Unset): `restrictions`: maximum days between booking and arrival.
     """

    start: datetime.date
    end: datetime.date
    room_type_code: str | Unset = UNSET
    rate_plan_code: str | Unset = UNSET
    available_rooms: int | Unset = UNSET
    price: float | Unset = UNSET
    occupancy_prices: list[TiketOccupancyPrice] | Unset = UNSET
    child_prices: list[TiketChildPrice] | Unset = UNSET
    currency: str | Unset = UNSET
    min_stay: int | Unset = UNSET
    max_stay: int | Unset = UNSET
    stop_sell: bool | Unset = UNSET
    closed_to_arrival: bool | Unset = UNSET
    closed_to_departure: bool | Unset = UNSET
    min_advance_days: int | Unset = UNSET
    max_advance_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_child_price import TiketChildPrice
        from ..models.tiket_occupancy_price import TiketOccupancyPrice
        start = self.start.isoformat()

        end = self.end.isoformat()

        room_type_code = self.room_type_code

        rate_plan_code = self.rate_plan_code

        available_rooms = self.available_rooms

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



        currency = self.currency

        min_stay = self.min_stay

        max_stay = self.max_stay

        stop_sell = self.stop_sell

        closed_to_arrival = self.closed_to_arrival

        closed_to_departure = self.closed_to_departure

        min_advance_days = self.min_advance_days

        max_advance_days = self.max_advance_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "start": start,
            "end": end,
        })
        if room_type_code is not UNSET:
            field_dict["roomTypeCode"] = room_type_code
        if rate_plan_code is not UNSET:
            field_dict["ratePlanCode"] = rate_plan_code
        if available_rooms is not UNSET:
            field_dict["availableRooms"] = available_rooms
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
        start = isoparse(d.pop("start")).date()




        end = isoparse(d.pop("end")).date()




        room_type_code = d.pop("roomTypeCode", UNSET)

        rate_plan_code = d.pop("ratePlanCode", UNSET)

        available_rooms = d.pop("availableRooms", UNSET)

        price = d.pop("price", UNSET)

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


        currency = d.pop("currency", UNSET)

        min_stay = d.pop("minStay", UNSET)

        max_stay = d.pop("maxStay", UNSET)

        stop_sell = d.pop("stopSell", UNSET)

        closed_to_arrival = d.pop("closedToArrival", UNSET)

        closed_to_departure = d.pop("closedToDeparture", UNSET)

        min_advance_days = d.pop("minAdvanceDays", UNSET)

        max_advance_days = d.pop("maxAdvanceDays", UNSET)

        tiket_ari_update = cls(
            start=start,
            end=end,
            room_type_code=room_type_code,
            rate_plan_code=rate_plan_code,
            available_rooms=available_rooms,
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


        tiket_ari_update.additional_properties = d
        return tiket_ari_update

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
