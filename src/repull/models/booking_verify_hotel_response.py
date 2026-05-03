from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingVerifyHotelResponse")



@_attrs_define
class BookingVerifyHotelResponse:
    """ Successful verify response. The session is transitioned to `awaiting_room_mapping` and a `pms_connections` row is
    upserted.

        Attributes:
            valid (bool):  Example: True.
            session_id (str):
            connection_id (str): Repull-side `pms_connections.id` for the linked Booking account.
            hotel_id (str):
            hotel_name (None | str | Unset):
            hotel_type (None | str | Unset): Booking.com hotel/property type code (e.g. `apartment`, `hotel`).
            country (None | str | Unset):
            city (None | str | Unset):
     """

    valid: bool
    session_id: str
    connection_id: str
    hotel_id: str
    hotel_name: None | str | Unset = UNSET
    hotel_type: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        session_id = self.session_id

        connection_id = self.connection_id

        hotel_id = self.hotel_id

        hotel_name: None | str | Unset
        if isinstance(self.hotel_name, Unset):
            hotel_name = UNSET
        else:
            hotel_name = self.hotel_name

        hotel_type: None | str | Unset
        if isinstance(self.hotel_type, Unset):
            hotel_type = UNSET
        else:
            hotel_type = self.hotel_type

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "valid": valid,
            "sessionId": session_id,
            "connectionId": connection_id,
            "hotelId": hotel_id,
        })
        if hotel_name is not UNSET:
            field_dict["hotelName"] = hotel_name
        if hotel_type is not UNSET:
            field_dict["hotelType"] = hotel_type
        if country is not UNSET:
            field_dict["country"] = country
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid")

        session_id = d.pop("sessionId")

        connection_id = d.pop("connectionId")

        hotel_id = d.pop("hotelId")

        def _parse_hotel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hotel_name = _parse_hotel_name(d.pop("hotelName", UNSET))


        def _parse_hotel_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hotel_type = _parse_hotel_type(d.pop("hotelType", UNSET))


        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        booking_verify_hotel_response = cls(
            valid=valid,
            session_id=session_id,
            connection_id=connection_id,
            hotel_id=hotel_id,
            hotel_name=hotel_name,
            hotel_type=hotel_type,
            country=country,
            city=city,
        )


        booking_verify_hotel_response.additional_properties = d
        return booking_verify_hotel_response

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
