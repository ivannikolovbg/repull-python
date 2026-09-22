from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.booking_property_listings_item_mapped_via import BookingPropertyListingsItemMappedVia
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingPropertyListingsItem")



@_attrs_define
class BookingPropertyListingsItem:
    """ 
        Attributes:
            listing_id (str | Unset): Repull listing id — what `/v1/channels/booking/properties/{id}` and
                `/v1/channels/booking/listings/{id}/pricing` take.
            name (None | str | Unset):
            city (None | str | Unset):
            room_id (None | str | Unset): Repull-side room row id, as used by `POST /v1/connect/booking/map-rooms`.
            room_booking_id (None | str | Unset): Booking.com's own room id — the `roomId` an ARI write takes.
            room_name (None | str | Unset):
            mapped_via (BookingPropertyListingsItemMappedVia | Unset): Which record carries the mapping: the room mapping
                written by Connect, or the legacy property-level link.
     """

    listing_id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    room_id: None | str | Unset = UNSET
    room_booking_id: None | str | Unset = UNSET
    room_name: None | str | Unset = UNSET
    mapped_via: BookingPropertyListingsItemMappedVia | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        room_id: None | str | Unset
        if isinstance(self.room_id, Unset):
            room_id = UNSET
        else:
            room_id = self.room_id

        room_booking_id: None | str | Unset
        if isinstance(self.room_booking_id, Unset):
            room_booking_id = UNSET
        else:
            room_booking_id = self.room_booking_id

        room_name: None | str | Unset
        if isinstance(self.room_name, Unset):
            room_name = UNSET
        else:
            room_name = self.room_name

        mapped_via: str | Unset = UNSET
        if not isinstance(self.mapped_via, Unset):
            mapped_via = self.mapped_via.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room_booking_id is not UNSET:
            field_dict["roomBookingId"] = room_booking_id
        if room_name is not UNSET:
            field_dict["roomName"] = room_name
        if mapped_via is not UNSET:
            field_dict["mappedVia"] = mapped_via

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_room_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_id = _parse_room_id(d.pop("roomId", UNSET))


        def _parse_room_booking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_booking_id = _parse_room_booking_id(d.pop("roomBookingId", UNSET))


        def _parse_room_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_name = _parse_room_name(d.pop("roomName", UNSET))


        _mapped_via = d.pop("mappedVia", UNSET)
        mapped_via: BookingPropertyListingsItemMappedVia | Unset
        if isinstance(_mapped_via,  Unset):
            mapped_via = UNSET
        else:
            mapped_via = BookingPropertyListingsItemMappedVia(_mapped_via)




        booking_property_listings_item = cls(
            listing_id=listing_id,
            name=name,
            city=city,
            room_id=room_id,
            room_booking_id=room_booking_id,
            room_name=room_name,
            mapped_via=mapped_via,
        )


        booking_property_listings_item.additional_properties = d
        return booking_property_listings_item

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
