from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateRequestAddress")



@_attrs_define
class ListingContentUpdateRequestAddress:
    """ Partial address. Only provided sub-fields are written; the ones you omit keep their current value, and an explicit
    `null` clears one.

    This is also the repair path for a listing that cannot be published: Airbnb requires `street` and `city` for every
    country and additionally `state` and `postalCode` for a **US** property — and a listing with no `countryCode`
    behaves as US. Send just the missing part, e.g. `{ "address": { "state": "FL" } }`. `GET /v1/listings/{id}/publish-
    status` names what is missing.

        Attributes:
            street (None | str | Unset): Street address including the number. Required by Airbnb for every country.
            city (None | str | Unset): City / town. Required by Airbnb for every country.
            state (None | str | Unset): State, province or region. **Required for a US property**, and a listing with no
                `countryCode` counts as US. Example: FL.
            postal_code (None | str | Unset): Postal code — ZIP in the US, postcode in the UK, and so on. **Required for a
                US property**, and a listing with no `countryCode` counts as US. Send the complete code; a partial postcode is
                rejected downstream. Alias: `zipcode`. Example: 33139.
            zipcode (None | str | Unset): Alias for `postalCode`, accepted because it is the field name on the Airbnb
                mirror. `postalCode` wins if you send both. Example: 33139.
            country_code (None | str | Unset): ISO-3166 alpha-2 country code. **Send this for any non-US property.** Leaving
                it unset does not mean "unknown" — the publish path treats a listing with no country as US and then demands
                `state` and `postalCode`. Example: US.
            lat (float | None | Unset): Latitude. Never a substitute for the postal address — Airbnb rejects coordinates it
                cannot reconcile with a full address.
            lng (float | None | Unset): Longitude. See `lat`.
     """

    street: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    zipcode: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    lat: float | None | Unset = UNSET
    lng: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        zipcode: None | str | Unset
        if isinstance(self.zipcode, Unset):
            zipcode = UNSET
        else:
            zipcode = self.zipcode

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if zipcode is not UNSET:
            field_dict["zipcode"] = zipcode
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("street", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postalCode", UNSET))


        def _parse_zipcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zipcode = _parse_zipcode(d.pop("zipcode", UNSET))


        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))


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


        listing_content_update_request_address = cls(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            zipcode=zipcode,
            country_code=country_code,
            lat=lat,
            lng=lng,
        )


        listing_content_update_request_address.additional_properties = d
        return listing_content_update_request_address

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
