from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_hotel_type_0_source import ListingHotelType0Source
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingHotelType0")



@_attrs_define
class ListingHotelType0:
    """ The hotel the listing belongs to: a hotel PMS hotel (Cloudbeds, Mews) or a Booking.com property with several room
    types or rooms. `null` for a standalone home. `GET /v1/hotels/{id}` lists its room types.

        Attributes:
            id (str | Unset): A Repull hotel id, or `booking:<hotelId>` for a Booking.com property. Example: booking:255832.
            name (None | str | Unset):
            source (ListingHotelType0Source | Unset):
     """

    id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    source: ListingHotelType0Source | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value



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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        source: ListingHotelType0Source | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = ListingHotelType0Source(_source)




        listing_hotel_type_0 = cls(
            id=id,
            name=name,
            source=source,
        )


        listing_hotel_type_0.additional_properties = d
        return listing_hotel_type_0

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
