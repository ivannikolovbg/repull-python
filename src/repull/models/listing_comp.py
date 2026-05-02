from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_comp_nightly import ListingCompNightly
  from ..models.listing_comp_ratings import ListingCompRatings





T = TypeVar("T", bound="ListingComp")



@_attrs_define
class ListingComp:
    """ A single competitor listing in a comp set, sorted closest-first. Includes per-day rate/availability for the
    requested calendar window.

        Attributes:
            comp_id (int | Unset):
            listing_name (None | str | Unset):
            distance_km (float | None | Unset): Haversine distance from the source listing in km, rounded to 3 decimals.
            bedrooms (int | None | Unset):
            max_guests (int | None | Unset):
            ratings (ListingCompRatings | Unset):
            currency (None | str | Unset):
            current_nightly_rate (float | None | Unset): Latest snapshot ADR — fallback to render when the calendar window
                is empty.
            nightly (list[ListingCompNightly] | Unset): Per-day rate + availability for the requested window. May be empty
                if Atlas hasn't snapshotted the comp recently.
            lat (float | None | Unset):
            lng (float | None | Unset):
            platform (None | str | Unset):  Example: airbnb.
            external_url (None | str | Unset): Link to the listing on its source platform when one is available.
     """

    comp_id: int | Unset = UNSET
    listing_name: None | str | Unset = UNSET
    distance_km: float | None | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    max_guests: int | None | Unset = UNSET
    ratings: ListingCompRatings | Unset = UNSET
    currency: None | str | Unset = UNSET
    current_nightly_rate: float | None | Unset = UNSET
    nightly: list[ListingCompNightly] | Unset = UNSET
    lat: float | None | Unset = UNSET
    lng: float | None | Unset = UNSET
    platform: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_comp_nightly import ListingCompNightly
        from ..models.listing_comp_ratings import ListingCompRatings
        comp_id = self.comp_id

        listing_name: None | str | Unset
        if isinstance(self.listing_name, Unset):
            listing_name = UNSET
        else:
            listing_name = self.listing_name

        distance_km: float | None | Unset
        if isinstance(self.distance_km, Unset):
            distance_km = UNSET
        else:
            distance_km = self.distance_km

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        ratings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = self.ratings.to_dict()

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        current_nightly_rate: float | None | Unset
        if isinstance(self.current_nightly_rate, Unset):
            current_nightly_rate = UNSET
        else:
            current_nightly_rate = self.current_nightly_rate

        nightly: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nightly, Unset):
            nightly = []
            for nightly_item_data in self.nightly:
                nightly_item = nightly_item_data.to_dict()
                nightly.append(nightly_item)



        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lng: float | None | Unset
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comp_id is not UNSET:
            field_dict["comp_id"] = comp_id
        if listing_name is not UNSET:
            field_dict["listing_name"] = listing_name
        if distance_km is not UNSET:
            field_dict["distance_km"] = distance_km
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if max_guests is not UNSET:
            field_dict["max_guests"] = max_guests
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if currency is not UNSET:
            field_dict["currency"] = currency
        if current_nightly_rate is not UNSET:
            field_dict["current_nightly_rate"] = current_nightly_rate
        if nightly is not UNSET:
            field_dict["nightly"] = nightly
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if platform is not UNSET:
            field_dict["platform"] = platform
        if external_url is not UNSET:
            field_dict["external_url"] = external_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_comp_nightly import ListingCompNightly
        from ..models.listing_comp_ratings import ListingCompRatings
        d = dict(src_dict)
        comp_id = d.pop("comp_id", UNSET)

        def _parse_listing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_name = _parse_listing_name(d.pop("listing_name", UNSET))


        def _parse_distance_km(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_km = _parse_distance_km(d.pop("distance_km", UNSET))


        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("max_guests", UNSET))


        _ratings = d.pop("ratings", UNSET)
        ratings: ListingCompRatings | Unset
        if isinstance(_ratings,  Unset):
            ratings = UNSET
        else:
            ratings = ListingCompRatings.from_dict(_ratings)




        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_current_nightly_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_nightly_rate = _parse_current_nightly_rate(d.pop("current_nightly_rate", UNSET))


        _nightly = d.pop("nightly", UNSET)
        nightly: list[ListingCompNightly] | Unset = UNSET
        if _nightly is not UNSET:
            nightly = []
            for nightly_item_data in _nightly:
                nightly_item = ListingCompNightly.from_dict(nightly_item_data)



                nightly.append(nightly_item)


        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))


        def _parse_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lng = _parse_lng(d.pop("lng", UNSET))


        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))


        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))


        listing_comp = cls(
            comp_id=comp_id,
            listing_name=listing_name,
            distance_km=distance_km,
            bedrooms=bedrooms,
            max_guests=max_guests,
            ratings=ratings,
            currency=currency,
            current_nightly_rate=current_nightly_rate,
            nightly=nightly,
            lat=lat,
            lng=lng,
            platform=platform,
            external_url=external_url,
        )


        listing_comp.additional_properties = d
        return listing_comp

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
