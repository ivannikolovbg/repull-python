from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.market_my_listing_type import MarketMyListingType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MarketMyListing")



@_attrs_define
class MarketMyListing:
    """ Lightweight customer listing entry for map rendering.

        Attributes:
            id (str | Unset):
            name (str | Unset):
            city (None | str | Unset):
            lat (float | Unset):
            lng (float | Unset):
            thumbnail (None | str | Unset):
            today_price (int | None | Unset): Pre-computed ADR rounded to integer.
            blocked (bool | Unset):
            booked_nights (int | Unset):
            available_nights (int | Unset):
            type_ (MarketMyListingType | Unset):  Example: mine.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    city: None | str | Unset = UNSET
    lat: float | Unset = UNSET
    lng: float | Unset = UNSET
    thumbnail: None | str | Unset = UNSET
    today_price: int | None | Unset = UNSET
    blocked: bool | Unset = UNSET
    booked_nights: int | Unset = UNSET
    available_nights: int | Unset = UNSET
    type_: MarketMyListingType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        lat = self.lat

        lng = self.lng

        thumbnail: None | str | Unset
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = self.thumbnail

        today_price: int | None | Unset
        if isinstance(self.today_price, Unset):
            today_price = UNSET
        else:
            today_price = self.today_price

        blocked = self.blocked

        booked_nights = self.booked_nights

        available_nights = self.available_nights

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if today_price is not UNSET:
            field_dict["todayPrice"] = today_price
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if booked_nights is not UNSET:
            field_dict["bookedNights"] = booked_nights
        if available_nights is not UNSET:
            field_dict["availableNights"] = available_nights
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        def _parse_thumbnail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))


        def _parse_today_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        today_price = _parse_today_price(d.pop("todayPrice", UNSET))


        blocked = d.pop("blocked", UNSET)

        booked_nights = d.pop("bookedNights", UNSET)

        available_nights = d.pop("availableNights", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: MarketMyListingType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = MarketMyListingType(_type_)




        market_my_listing = cls(
            id=id,
            name=name,
            city=city,
            lat=lat,
            lng=lng,
            thumbnail=thumbnail,
            today_price=today_price,
            blocked=blocked,
            booked_nights=booked_nights,
            available_nights=available_nights,
            type_=type_,
        )


        market_my_listing.additional_properties = d
        return market_my_listing

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
