from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbListing")



@_attrs_define
class AirbnbListing:
    """ An Airbnb listing in the host account. Mirrors the Airbnb partner API shape with light normalization.

        Attributes:
            id (str | Unset): Airbnb listing ID Example: 12345678.
            name (str | Unset): Listing title
            status (str | Unset): Listing status (active, unlisted, etc.)
            property_type (None | str | Unset):
            room_type (None | str | Unset):
            bedrooms (int | None | Unset):
            bathrooms (float | None | Unset):
            max_guests (int | None | Unset):
            thumbnail_url (None | str | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    property_type: None | str | Unset = UNSET
    room_type: None | str | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    bathrooms: float | None | Unset = UNSET
    max_guests: int | None | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        property_type: None | str | Unset
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        room_type: None | str | Unset
        if isinstance(self.room_type, Unset):
            room_type = UNSET
        else:
            room_type = self.room_type

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: float | None | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if room_type is not UNSET:
            field_dict["roomType"] = room_type
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        def _parse_property_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))


        def _parse_room_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_type = _parse_room_type(d.pop("roomType", UNSET))


        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_bathrooms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))


        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("maxGuests", UNSET))


        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))


        airbnb_listing = cls(
            id=id,
            name=name,
            status=status,
            property_type=property_type,
            room_type=room_type,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            max_guests=max_guests,
            thumbnail_url=thumbnail_url,
        )


        airbnb_listing.additional_properties = d
        return airbnb_listing

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
