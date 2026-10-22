from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PostalAddress")



@_attrs_define
class PostalAddress:
    """ The full postal address, unit included. Returned on every active row of `GET /v1/properties`, `GET
    /v1/properties/{id}`, `GET /v1/listings` and `GET /v1/listings/{id}` (on listings, these fields sit inside
    `address`). Each part is read from the listing first, then from the connected channels (Airbnb, Vrbo, Booking.com),
    so `line2` carries the apartment or unit number that tells units in the same building apart. A part nobody has
    stored is `null`.

        Attributes:
            line1 (None | str): Street address: number and street. Example: 2700 Northwest 2nd Avenue.
            line2 (None | str): Apartment, unit, suite or building. Example: Unit 241.
            city (None | str):  Example: Miami.
            state (None | str): State, province or region. Example: FL.
            postal_code (None | str): Postal or ZIP code. Example: 33127.
            country_code (None | str): ISO 3166-1 alpha-2 country code. Example: US.
     """

    line1: None | str
    line2: None | str
    city: None | str
    state: None | str
    postal_code: None | str
    country_code: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        line1: None | str
        line1 = self.line1

        line2: None | str
        line2 = self.line2

        city: None | str
        city = self.city

        state: None | str
        state = self.state

        postal_code: None | str
        postal_code = self.postal_code

        country_code: None | str
        country_code = self.country_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "line1": line1,
            "line2": line2,
            "city": city,
            "state": state,
            "postalCode": postal_code,
            "countryCode": country_code,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_line1(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line1 = _parse_line1(d.pop("line1"))


        def _parse_line2(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        line2 = _parse_line2(d.pop("line2"))


        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))


        def _parse_state(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state = _parse_state(d.pop("state"))


        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postalCode"))


        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("countryCode"))


        postal_address = cls(
            line1=line1,
            line2=line2,
            city=city,
            state=state,
            postal_code=postal_code,
            country_code=country_code,
        )


        postal_address.additional_properties = d
        return postal_address

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
