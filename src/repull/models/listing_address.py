from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingAddress")



@_attrs_define
class ListingAddress:
    """ The listing's postal address, unit included. Each part is read from the listing first, then from the connected
    channels (Airbnb, Vrbo, Booking.com). On an inactive row only `city` is present.

        Attributes:
            street (None | str | Unset): Street line as stored on the listing. Kept for existing integrations; same value as
                `line1` unless the listing has no street of its own. Example: 2700 Northwest 2nd Avenue.
            line1 (None | str | Unset): Street address: number and street. Example: 2700 Northwest 2nd Avenue.
            line2 (None | str | Unset): Apartment, unit, suite or building. Example: Unit 241.
            city (None | str | Unset):  Example: Miami.
            state (None | str | Unset): State, province or region. Example: FL.
            postal_code (None | str | Unset): Postal or ZIP code. Example: 33127.
            country_code (None | str | Unset): ISO 3166-1 alpha-2 country code. Example: US.
     """

    street: None | str | Unset = UNSET
    line1: None | str | Unset = UNSET
    line2: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        line1: None | str | Unset
        if isinstance(self.line1, Unset):
            line1 = UNSET
        else:
            line1 = self.line1

        line2: None | str | Unset
        if isinstance(self.line2, Unset):
            line2 = UNSET
        else:
            line2 = self.line2

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

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if street is not UNSET:
            field_dict["street"] = street
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

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


        def _parse_line1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line1 = _parse_line1(d.pop("line1", UNSET))


        def _parse_line2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        line2 = _parse_line2(d.pop("line2", UNSET))


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


        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))


        listing_address = cls(
            street=street,
            line1=line1,
            line2=line2,
            city=city,
            state=state,
            postal_code=postal_code,
            country_code=country_code,
        )


        listing_address.additional_properties = d
        return listing_address

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
