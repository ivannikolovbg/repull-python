from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Property")



@_attrs_define
class Property:
    """ A vacation rental property from a connected PMS

        Attributes:
            id (int | Unset): Internal Repull property ID
            external_id (str | Unset): ID in the source PMS
            name (str | Unset): Property name Example: Oceanview Suite #3.
            address (str | Unset): Full address
            city (str | Unset):  Example: Miami Beach.
            state (str | Unset):  Example: FL.
            country (str | Unset):  Example: US.
            latitude (float | Unset):  Example: 25.7617.
            longitude (float | Unset):  Example: -80.1918.
            bedrooms (int | Unset):  Example: 2.
            bathrooms (float | Unset):  Example: 1.5.
            max_guests (int | Unset):  Example: 6.
            thumbnail (str | Unset): Primary photo URL
            provider (str | Unset): Source PMS Example: hostaway.
     """

    id: int | Unset = UNSET
    external_id: str | Unset = UNSET
    name: str | Unset = UNSET
    address: str | Unset = UNSET
    city: str | Unset = UNSET
    state: str | Unset = UNSET
    country: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    bedrooms: int | Unset = UNSET
    bathrooms: float | Unset = UNSET
    max_guests: int | Unset = UNSET
    thumbnail: str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        name = self.name

        address = self.address

        city = self.city

        state = self.state

        country = self.country

        latitude = self.latitude

        longitude = self.longitude

        bedrooms = self.bedrooms

        bathrooms = self.bathrooms

        max_guests = self.max_guests

        thumbnail = self.thumbnail

        provider = self.provider


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        external_id = d.pop("externalId", UNSET)

        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        bedrooms = d.pop("bedrooms", UNSET)

        bathrooms = d.pop("bathrooms", UNSET)

        max_guests = d.pop("maxGuests", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        provider = d.pop("provider", UNSET)

        property_ = cls(
            id=id,
            external_id=external_id,
            name=name,
            address=address,
            city=city,
            state=state,
            country=country,
            latitude=latitude,
            longitude=longitude,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            max_guests=max_guests,
            thumbnail=thumbnail,
            provider=provider,
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
