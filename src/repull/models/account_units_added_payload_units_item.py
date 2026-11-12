from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AccountUnitsAddedPayloadUnitsItem")



@_attrs_define
class AccountUnitsAddedPayloadUnitsItem:
    """ 
        Attributes:
            unit_id (str): The `unit_id` to pass to `POST /v1/connections/{id}/mappings`.
            name (str):
            hotel_id (str): Booking.com property ID.
            room_id (None | str): Booking.com room ID.
            mapped (bool): Whether the unit is already mapped to a listing. New units are almost always unmapped: their
                bookings, messages and reviews import once you map them.
            listing_id (int | None): The listing the unit is mapped to, when `mapped`.
     """

    unit_id: str
    name: str
    hotel_id: str
    room_id: None | str
    mapped: bool
    listing_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        unit_id = self.unit_id

        name = self.name

        hotel_id = self.hotel_id

        room_id: None | str
        room_id = self.room_id

        mapped = self.mapped

        listing_id: int | None
        listing_id = self.listing_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "unitId": unit_id,
            "name": name,
            "hotelId": hotel_id,
            "roomId": room_id,
            "mapped": mapped,
            "listingId": listing_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_id = d.pop("unitId")

        name = d.pop("name")

        hotel_id = d.pop("hotelId")

        def _parse_room_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        room_id = _parse_room_id(d.pop("roomId"))


        mapped = d.pop("mapped")

        def _parse_listing_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        listing_id = _parse_listing_id(d.pop("listingId"))


        account_units_added_payload_units_item = cls(
            unit_id=unit_id,
            name=name,
            hotel_id=hotel_id,
            room_id=room_id,
            mapped=mapped,
            listing_id=listing_id,
        )


        account_units_added_payload_units_item.additional_properties = d
        return account_units_added_payload_units_item

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
