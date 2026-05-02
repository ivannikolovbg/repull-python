from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_pricing_rate_update_date_range import BookingPricingRateUpdateDateRange
  from ..models.booking_pricing_rate_update_restrictions import BookingPricingRateUpdateRestrictions





T = TypeVar("T", bound="BookingPricingRateUpdate")



@_attrs_define
class BookingPricingRateUpdate:
    """ A single (room, rate-plan, date-range) update pushed to Booking.com via the rates API.

        Attributes:
            room_id (str): Booking.com room ID for the rate plan. Comes from `listings_booking_rooms` mapping.
            rate_id (str): Booking.com rate-plan ID.
            date_range (BookingPricingRateUpdateDateRange):
            price (float):
            currency (str):  Example: USD.
            single_price (float | None | Unset):
            occupancy (int | None | Unset):
            rooms_to_sell (int | None | Unset):
            restrictions (BookingPricingRateUpdateRestrictions | Unset): Optional length-of-stay / availability restrictions
                for one rate update.
     """

    room_id: str
    rate_id: str
    date_range: BookingPricingRateUpdateDateRange
    price: float
    currency: str
    single_price: float | None | Unset = UNSET
    occupancy: int | None | Unset = UNSET
    rooms_to_sell: int | None | Unset = UNSET
    restrictions: BookingPricingRateUpdateRestrictions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_pricing_rate_update_date_range import BookingPricingRateUpdateDateRange
        from ..models.booking_pricing_rate_update_restrictions import BookingPricingRateUpdateRestrictions
        room_id = self.room_id

        rate_id = self.rate_id

        date_range = self.date_range.to_dict()

        price = self.price

        currency = self.currency

        single_price: float | None | Unset
        if isinstance(self.single_price, Unset):
            single_price = UNSET
        else:
            single_price = self.single_price

        occupancy: int | None | Unset
        if isinstance(self.occupancy, Unset):
            occupancy = UNSET
        else:
            occupancy = self.occupancy

        rooms_to_sell: int | None | Unset
        if isinstance(self.rooms_to_sell, Unset):
            rooms_to_sell = UNSET
        else:
            rooms_to_sell = self.rooms_to_sell

        restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "roomId": room_id,
            "rateId": rate_id,
            "dateRange": date_range,
            "price": price,
            "currency": currency,
        })
        if single_price is not UNSET:
            field_dict["singlePrice"] = single_price
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if rooms_to_sell is not UNSET:
            field_dict["roomsToSell"] = rooms_to_sell
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_pricing_rate_update_date_range import BookingPricingRateUpdateDateRange
        from ..models.booking_pricing_rate_update_restrictions import BookingPricingRateUpdateRestrictions
        d = dict(src_dict)
        room_id = d.pop("roomId")

        rate_id = d.pop("rateId")

        date_range = BookingPricingRateUpdateDateRange.from_dict(d.pop("dateRange"))




        price = d.pop("price")

        currency = d.pop("currency")

        def _parse_single_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        single_price = _parse_single_price(d.pop("singlePrice", UNSET))


        def _parse_occupancy(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        occupancy = _parse_occupancy(d.pop("occupancy", UNSET))


        def _parse_rooms_to_sell(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rooms_to_sell = _parse_rooms_to_sell(d.pop("roomsToSell", UNSET))


        _restrictions = d.pop("restrictions", UNSET)
        restrictions: BookingPricingRateUpdateRestrictions | Unset
        if isinstance(_restrictions,  Unset):
            restrictions = UNSET
        else:
            restrictions = BookingPricingRateUpdateRestrictions.from_dict(_restrictions)




        booking_pricing_rate_update = cls(
            room_id=room_id,
            rate_id=rate_id,
            date_range=date_range,
            price=price,
            currency=currency,
            single_price=single_price,
            occupancy=occupancy,
            rooms_to_sell=rooms_to_sell,
            restrictions=restrictions,
        )


        booking_pricing_rate_update.additional_properties = d
        return booking_pricing_rate_update

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
