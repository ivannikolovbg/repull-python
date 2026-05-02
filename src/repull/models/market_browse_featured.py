from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MarketBrowseFeatured")



@_attrs_define
class MarketBrowseFeatured:
    """ Curated featured market entry on the discovery summary. Enriched with `subscribed` so the dashboard can render
    "Already unlocked" pills without an extra round-trip.

        Attributes:
            city (str | Unset):
            country (str | Unset): ISO 3166-1 alpha-2.
            listings (int | Unset): Atlas-tracked active comps in this city.
            avg_adr (float | None | Unset): Atlas-aggregated avg nightly rate (mixed currency, dominated by the country
                base).
            subscribed (bool | Unset):
     """

    city: str | Unset = UNSET
    country: str | Unset = UNSET
    listings: int | Unset = UNSET
    avg_adr: float | None | Unset = UNSET
    subscribed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        listings = self.listings

        avg_adr: float | None | Unset
        if isinstance(self.avg_adr, Unset):
            avg_adr = UNSET
        else:
            avg_adr = self.avg_adr

        subscribed = self.subscribed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if listings is not UNSET:
            field_dict["listings"] = listings
        if avg_adr is not UNSET:
            field_dict["avg_adr"] = avg_adr
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        listings = d.pop("listings", UNSET)

        def _parse_avg_adr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_adr = _parse_avg_adr(d.pop("avg_adr", UNSET))


        subscribed = d.pop("subscribed", UNSET)

        market_browse_featured = cls(
            city=city,
            country=country,
            listings=listings,
            avg_adr=avg_adr,
            subscribed=subscribed,
        )


        market_browse_featured.additional_properties = d
        return market_browse_featured

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
