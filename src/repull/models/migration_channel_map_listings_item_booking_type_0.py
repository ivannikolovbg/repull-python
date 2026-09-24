from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MigrationChannelMapListingsItemBookingType0")



@_attrs_define
class MigrationChannelMapListingsItemBookingType0:
    """ 
        Attributes:
            hotel_id (str | Unset):
            room_id (str | Unset):
     """

    hotel_id: str | Unset = UNSET
    room_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hotel_id = self.hotel_id

        room_id = self.room_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if room_id is not UNSET:
            field_dict["roomId"] = room_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hotel_id = d.pop("hotelId", UNSET)

        room_id = d.pop("roomId", UNSET)

        migration_channel_map_listings_item_booking_type_0 = cls(
            hotel_id=hotel_id,
            room_id=room_id,
        )


        migration_channel_map_listings_item_booking_type_0.additional_properties = d
        return migration_channel_map_listings_item_booking_type_0

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
