from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_rooms_rates_response_rooms_item_rates_item import BookingRoomsRatesResponseRoomsItemRatesItem





T = TypeVar("T", bound="BookingRoomsRatesResponseRoomsItem")



@_attrs_define
class BookingRoomsRatesResponseRoomsItem:
    """ 
        Attributes:
            room_id (None | str | Unset): Booking.com room id — use as `roomId` in an ARI update.
            room_name (None | str | Unset):
            max_adults (int | None | Unset): Booking.com's capacity for this room, as imported. The occupancy a rate write
                falls back to when the rate plan states no `maxPersons`. Null when Booking.com never stated one.
            rates (list[BookingRoomsRatesResponseRoomsItemRatesItem] | Unset):
     """

    room_id: None | str | Unset = UNSET
    room_name: None | str | Unset = UNSET
    max_adults: int | None | Unset = UNSET
    rates: list[BookingRoomsRatesResponseRoomsItemRatesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_rooms_rates_response_rooms_item_rates_item import BookingRoomsRatesResponseRoomsItemRatesItem
        room_id: None | str | Unset
        if isinstance(self.room_id, Unset):
            room_id = UNSET
        else:
            room_id = self.room_id

        room_name: None | str | Unset
        if isinstance(self.room_name, Unset):
            room_name = UNSET
        else:
            room_name = self.room_name

        max_adults: int | None | Unset
        if isinstance(self.max_adults, Unset):
            max_adults = UNSET
        else:
            max_adults = self.max_adults

        rates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room_name is not UNSET:
            field_dict["roomName"] = room_name
        if max_adults is not UNSET:
            field_dict["maxAdults"] = max_adults
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_rooms_rates_response_rooms_item_rates_item import BookingRoomsRatesResponseRoomsItemRatesItem
        d = dict(src_dict)
        def _parse_room_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_id = _parse_room_id(d.pop("roomId", UNSET))


        def _parse_room_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_name = _parse_room_name(d.pop("roomName", UNSET))


        def _parse_max_adults(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_adults = _parse_max_adults(d.pop("maxAdults", UNSET))


        _rates = d.pop("rates", UNSET)
        rates: list[BookingRoomsRatesResponseRoomsItemRatesItem] | Unset = UNSET
        if _rates is not UNSET:
            rates = []
            for rates_item_data in _rates:
                rates_item = BookingRoomsRatesResponseRoomsItemRatesItem.from_dict(rates_item_data)



                rates.append(rates_item)


        booking_rooms_rates_response_rooms_item = cls(
            room_id=room_id,
            room_name=room_name,
            max_adults=max_adults,
            rates=rates,
        )


        booking_rooms_rates_response_rooms_item.additional_properties = d
        return booking_rooms_rates_response_rooms_item

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
