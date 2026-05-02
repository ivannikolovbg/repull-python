from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MarketTopComp")



@_attrs_define
class MarketTopComp:
    """ 
        Attributes:
            id (int | Unset):
            platform_listing_id (str | Unset):
            title (None | str | Unset):
            property_type (None | str | Unset):
            bedrooms (int | None | Unset):
            max_guests (int | None | Unset):
            rating (float | None | Unset):
            review_count (int | None | Unset):
            current_nightly_rate (float | None | Unset):
            thumbnail_url (None | str | Unset):
            lat (float | None | Unset):
            lng (float | None | Unset):
            url (str | Unset):
            distance_km (float | None | Unset):
     """

    id: int | Unset = UNSET
    platform_listing_id: str | Unset = UNSET
    title: None | str | Unset = UNSET
    property_type: None | str | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    max_guests: int | None | Unset = UNSET
    rating: float | None | Unset = UNSET
    review_count: int | None | Unset = UNSET
    current_nightly_rate: float | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    lat: float | None | Unset = UNSET
    lng: float | None | Unset = UNSET
    url: str | Unset = UNSET
    distance_km: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform_listing_id = self.platform_listing_id

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        property_type: None | str | Unset
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

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

        rating: float | None | Unset
        if isinstance(self.rating, Unset):
            rating = UNSET
        else:
            rating = self.rating

        review_count: int | None | Unset
        if isinstance(self.review_count, Unset):
            review_count = UNSET
        else:
            review_count = self.review_count

        current_nightly_rate: float | None | Unset
        if isinstance(self.current_nightly_rate, Unset):
            current_nightly_rate = UNSET
        else:
            current_nightly_rate = self.current_nightly_rate

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

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

        url = self.url

        distance_km: float | None | Unset
        if isinstance(self.distance_km, Unset):
            distance_km = UNSET
        else:
            distance_km = self.distance_km


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if platform_listing_id is not UNSET:
            field_dict["platform_listing_id"] = platform_listing_id
        if title is not UNSET:
            field_dict["title"] = title
        if property_type is not UNSET:
            field_dict["property_type"] = property_type
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if max_guests is not UNSET:
            field_dict["max_guests"] = max_guests
        if rating is not UNSET:
            field_dict["rating"] = rating
        if review_count is not UNSET:
            field_dict["review_count"] = review_count
        if current_nightly_rate is not UNSET:
            field_dict["current_nightly_rate"] = current_nightly_rate
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if url is not UNSET:
            field_dict["url"] = url
        if distance_km is not UNSET:
            field_dict["distance_km"] = distance_km

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        platform_listing_id = d.pop("platform_listing_id", UNSET)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_property_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type = _parse_property_type(d.pop("property_type", UNSET))


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


        def _parse_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rating = _parse_rating(d.pop("rating", UNSET))


        def _parse_review_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        review_count = _parse_review_count(d.pop("review_count", UNSET))


        def _parse_current_nightly_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        current_nightly_rate = _parse_current_nightly_rate(d.pop("current_nightly_rate", UNSET))


        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnail_url", UNSET))


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


        url = d.pop("url", UNSET)

        def _parse_distance_km(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_km = _parse_distance_km(d.pop("distance_km", UNSET))


        market_top_comp = cls(
            id=id,
            platform_listing_id=platform_listing_id,
            title=title,
            property_type=property_type,
            bedrooms=bedrooms,
            max_guests=max_guests,
            rating=rating,
            review_count=review_count,
            current_nightly_rate=current_nightly_rate,
            thumbnail_url=thumbnail_url,
            lat=lat,
            lng=lng,
            url=url,
            distance_km=distance_km,
        )


        market_top_comp.additional_properties = d
        return market_top_comp

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
