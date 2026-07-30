from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.property_status import PropertyStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_amenity import ListingAmenity





T = TypeVar("T", bound="Property")



@_attrs_define
class Property:
    """ A vacation rental property in your Repull workspace. Backed by the core `listings` row — enriched per-PMS fields
    (bedrooms, property type, provider id, etc.) live in provider-specific detail tables and are NOT returned here.

    Field availability differs by endpoint:
    - `channels` is returned by the list endpoint (`GET /v1/properties`) only.
    - `latitude`, `longitude`, `createdAt`, and `amenities` are returned by the detail endpoint (`GET
    /v1/properties/{id}`) only. `amenities` requires `?include=amenities`.

        Attributes:
            id (str | Unset): Internal Repull property ID. Equal to the listing id (`listings.id`); the same integer is used
                as `listingId` on reservations and `propertyId` on availability.
            name (str | Unset): Property name Example: Oceanview Suite #3.
            address (None | str | Unset): Street address (from the listing's `street` field).
            city (None | str | Unset):  Example: Miami Beach.
            latitude (float | None | Unset): Detail endpoint only. Example: 25.7617.
            longitude (float | None | Unset): Detail endpoint only. Example: -80.1918.
            currency (None | str | Unset): ISO 4217 currency code for this property's pricing. Example: USD.
            status (PropertyStatus | Unset): Derived from `listings.active`.
            lifecycle_status (None | str | Unset): The listing's lifecycle state (e.g. `live`, `draft`, `archived`).
            created_at (datetime.datetime | Unset): When the property was created. Detail endpoint only.
            channels (list[str] | Unset): OTAs/channels this property is actively published on, as channel-name strings
                (e.g. `airbnb`, `booking`, `vrbo`). Empty array when the property has no active channel links. List endpoint
                (`GET /v1/properties`) only. Example: ['airbnb', 'booking'].
            amenities (list[ListingAmenity] | Unset): Amenity rows for the property. Detail endpoint only, and **only
                present when the caller passes `?include=amenities`.** Empty array (`[]`) when the property has no amenity rows.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    address: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    status: PropertyStatus | Unset = UNSET
    lifecycle_status: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    channels: list[str] | Unset = UNSET
    amenities: list[ListingAmenity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_amenity import ListingAmenity
        id = self.id

        name = self.name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        lifecycle_status: None | str | Unset
        if isinstance(self.lifecycle_status, Unset):
            lifecycle_status = UNSET
        else:
            lifecycle_status = self.lifecycle_status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels



        amenities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = []
            for amenities_item_data in self.amenities:
                amenities_item = amenities_item_data.to_dict()
                amenities.append(amenities_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if currency is not UNSET:
            field_dict["currency"] = currency
        if status is not UNSET:
            field_dict["status"] = status
        if lifecycle_status is not UNSET:
            field_dict["lifecycleStatus"] = lifecycle_status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if channels is not UNSET:
            field_dict["channels"] = channels
        if amenities is not UNSET:
            field_dict["amenities"] = amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_amenity import ListingAmenity
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))


        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        _status = d.pop("status", UNSET)
        status: PropertyStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PropertyStatus(_status)




        def _parse_lifecycle_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_status = _parse_lifecycle_status(d.pop("lifecycleStatus", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        channels = cast(list[str], d.pop("channels", UNSET))


        _amenities = d.pop("amenities", UNSET)
        amenities: list[ListingAmenity] | Unset = UNSET
        if _amenities is not UNSET:
            amenities = []
            for amenities_item_data in _amenities:
                amenities_item = ListingAmenity.from_dict(amenities_item_data)



                amenities.append(amenities_item)


        property_ = cls(
            id=id,
            name=name,
            address=address,
            city=city,
            latitude=latitude,
            longitude=longitude,
            currency=currency,
            status=status,
            lifecycle_status=lifecycle_status,
            created_at=created_at,
            channels=channels,
            amenities=amenities,
        )


        property_.additional_properties = d
        return property_

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
