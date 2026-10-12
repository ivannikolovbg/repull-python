from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_hotel_response_200_source import GetHotelResponse200Source
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_hotel_response_200_room_types_item import GetHotelResponse200RoomTypesItem





T = TypeVar("T", bound="GetHotelResponse200")



@_attrs_define
class GetHotelResponse200:
    """ 
        Attributes:
            id (str | Unset): A Repull hotel id, or `booking:<hotelId>` for a Booking.com property. Example: 30910.
            name (None | str | Unset):
            source (GetHotelResponse200Source | Unset): `pms`: a hotel PMS (Cloudbeds, Mews) owns rooms and room counts.
                `booking`: a Booking.com property; room counts are the room count on Booking.com.
            provider (None | str | Unset):  Example: cloudbeds.
            city (None | str | Unset):
            room_type_count (int | Unset):
            unit_count (int | Unset): Rooms across all room types.
            room_types (list[GetHotelResponse200RoomTypesItem] | Unset):
     """

    id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    source: GetHotelResponse200Source | Unset = UNSET
    provider: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    room_type_count: int | Unset = UNSET
    unit_count: int | Unset = UNSET
    room_types: list[GetHotelResponse200RoomTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_hotel_response_200_room_types_item import GetHotelResponse200RoomTypesItem
        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        room_type_count = self.room_type_count

        unit_count = self.unit_count

        room_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.room_types, Unset):
            room_types = []
            for room_types_item_data in self.room_types:
                room_types_item = room_types_item_data.to_dict()
                room_types.append(room_types_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source is not UNSET:
            field_dict["source"] = source
        if provider is not UNSET:
            field_dict["provider"] = provider
        if city is not UNSET:
            field_dict["city"] = city
        if room_type_count is not UNSET:
            field_dict["roomTypeCount"] = room_type_count
        if unit_count is not UNSET:
            field_dict["unitCount"] = unit_count
        if room_types is not UNSET:
            field_dict["roomTypes"] = room_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_hotel_response_200_room_types_item import GetHotelResponse200RoomTypesItem
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _source = d.pop("source", UNSET)
        source: GetHotelResponse200Source | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GetHotelResponse200Source(_source)




        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        room_type_count = d.pop("roomTypeCount", UNSET)

        unit_count = d.pop("unitCount", UNSET)

        _room_types = d.pop("roomTypes", UNSET)
        room_types: list[GetHotelResponse200RoomTypesItem] | Unset = UNSET
        if _room_types is not UNSET:
            room_types = []
            for room_types_item_data in _room_types:
                room_types_item = GetHotelResponse200RoomTypesItem.from_dict(room_types_item_data)



                room_types.append(room_types_item)


        get_hotel_response_200 = cls(
            id=id,
            name=name,
            source=source,
            provider=provider,
            city=city,
            room_type_count=room_type_count,
            unit_count=unit_count,
            room_types=room_types,
        )


        get_hotel_response_200.additional_properties = d
        return get_hotel_response_200

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
