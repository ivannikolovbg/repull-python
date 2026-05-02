from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MarketSummary")



@_attrs_define
class MarketSummary:
    """ Per-city KPIs combining the customer's own listings with Atlas comp aggregates.

        Attributes:
            city (str | Unset):  Example: Radium Hot Springs.
            my_listings (int | Unset):
            total_listings (int | Unset): Atlas-tracked active comps in this city.
            market_share_pct (int | None | Unset):
            my_avg_adr (float | None | Unset):
            market_avg_adr (float | None | Unset):
            price_diff_pct (int | None | Unset): (myAvgAdr - marketAvgAdr) / marketAvgAdr * 100, rounded.
            my_avg_rating (float | None | Unset):
            market_avg_rating (float | None | Unset):
            my_occupancy_pct (float | None | Unset): Customer's 30-day forward occupancy %.
            market_occupancy_pct (float | None | Unset):
            property_types (int | Unset): Distinct property types Atlas has seen in this city.
     """

    city: str | Unset = UNSET
    my_listings: int | Unset = UNSET
    total_listings: int | Unset = UNSET
    market_share_pct: int | None | Unset = UNSET
    my_avg_adr: float | None | Unset = UNSET
    market_avg_adr: float | None | Unset = UNSET
    price_diff_pct: int | None | Unset = UNSET
    my_avg_rating: float | None | Unset = UNSET
    market_avg_rating: float | None | Unset = UNSET
    my_occupancy_pct: float | None | Unset = UNSET
    market_occupancy_pct: float | None | Unset = UNSET
    property_types: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        city = self.city

        my_listings = self.my_listings

        total_listings = self.total_listings

        market_share_pct: int | None | Unset
        if isinstance(self.market_share_pct, Unset):
            market_share_pct = UNSET
        else:
            market_share_pct = self.market_share_pct

        my_avg_adr: float | None | Unset
        if isinstance(self.my_avg_adr, Unset):
            my_avg_adr = UNSET
        else:
            my_avg_adr = self.my_avg_adr

        market_avg_adr: float | None | Unset
        if isinstance(self.market_avg_adr, Unset):
            market_avg_adr = UNSET
        else:
            market_avg_adr = self.market_avg_adr

        price_diff_pct: int | None | Unset
        if isinstance(self.price_diff_pct, Unset):
            price_diff_pct = UNSET
        else:
            price_diff_pct = self.price_diff_pct

        my_avg_rating: float | None | Unset
        if isinstance(self.my_avg_rating, Unset):
            my_avg_rating = UNSET
        else:
            my_avg_rating = self.my_avg_rating

        market_avg_rating: float | None | Unset
        if isinstance(self.market_avg_rating, Unset):
            market_avg_rating = UNSET
        else:
            market_avg_rating = self.market_avg_rating

        my_occupancy_pct: float | None | Unset
        if isinstance(self.my_occupancy_pct, Unset):
            my_occupancy_pct = UNSET
        else:
            my_occupancy_pct = self.my_occupancy_pct

        market_occupancy_pct: float | None | Unset
        if isinstance(self.market_occupancy_pct, Unset):
            market_occupancy_pct = UNSET
        else:
            market_occupancy_pct = self.market_occupancy_pct

        property_types = self.property_types


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if city is not UNSET:
            field_dict["city"] = city
        if my_listings is not UNSET:
            field_dict["myListings"] = my_listings
        if total_listings is not UNSET:
            field_dict["totalListings"] = total_listings
        if market_share_pct is not UNSET:
            field_dict["marketSharePct"] = market_share_pct
        if my_avg_adr is not UNSET:
            field_dict["myAvgAdr"] = my_avg_adr
        if market_avg_adr is not UNSET:
            field_dict["marketAvgAdr"] = market_avg_adr
        if price_diff_pct is not UNSET:
            field_dict["priceDiffPct"] = price_diff_pct
        if my_avg_rating is not UNSET:
            field_dict["myAvgRating"] = my_avg_rating
        if market_avg_rating is not UNSET:
            field_dict["marketAvgRating"] = market_avg_rating
        if my_occupancy_pct is not UNSET:
            field_dict["myOccupancyPct"] = my_occupancy_pct
        if market_occupancy_pct is not UNSET:
            field_dict["marketOccupancyPct"] = market_occupancy_pct
        if property_types is not UNSET:
            field_dict["propertyTypes"] = property_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        my_listings = d.pop("myListings", UNSET)

        total_listings = d.pop("totalListings", UNSET)

        def _parse_market_share_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        market_share_pct = _parse_market_share_pct(d.pop("marketSharePct", UNSET))


        def _parse_my_avg_adr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        my_avg_adr = _parse_my_avg_adr(d.pop("myAvgAdr", UNSET))


        def _parse_market_avg_adr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_avg_adr = _parse_market_avg_adr(d.pop("marketAvgAdr", UNSET))


        def _parse_price_diff_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price_diff_pct = _parse_price_diff_pct(d.pop("priceDiffPct", UNSET))


        def _parse_my_avg_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        my_avg_rating = _parse_my_avg_rating(d.pop("myAvgRating", UNSET))


        def _parse_market_avg_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_avg_rating = _parse_market_avg_rating(d.pop("marketAvgRating", UNSET))


        def _parse_my_occupancy_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        my_occupancy_pct = _parse_my_occupancy_pct(d.pop("myOccupancyPct", UNSET))


        def _parse_market_occupancy_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_occupancy_pct = _parse_market_occupancy_pct(d.pop("marketOccupancyPct", UNSET))


        property_types = d.pop("propertyTypes", UNSET)

        market_summary = cls(
            city=city,
            my_listings=my_listings,
            total_listings=total_listings,
            market_share_pct=market_share_pct,
            my_avg_adr=my_avg_adr,
            market_avg_adr=market_avg_adr,
            price_diff_pct=price_diff_pct,
            my_avg_rating=my_avg_rating,
            market_avg_rating=market_avg_rating,
            my_occupancy_pct=my_occupancy_pct,
            market_occupancy_pct=market_occupancy_pct,
            property_types=property_types,
        )


        market_summary.additional_properties = d
        return market_summary

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
