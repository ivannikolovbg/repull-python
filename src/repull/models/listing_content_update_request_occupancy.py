from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateRequestOccupancy")



@_attrs_define
class ListingContentUpdateRequestOccupancy:
    """ 
        Attributes:
            max_guests (int | None | Unset):
            bedrooms (int | None | Unset):
            beds (int | None | Unset):
            bathrooms (float | None | Unset): Decimal, e.g. 1.5.
     """

    max_guests: int | None | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    beds: int | None | Unset = UNSET
    bathrooms: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        beds: int | None | Unset
        if isinstance(self.beds, Unset):
            beds = UNSET
        else:
            beds = self.beds

        bathrooms: float | None | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if beds is not UNSET:
            field_dict["beds"] = beds
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("maxGuests", UNSET))


        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_beds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        beds = _parse_beds(d.pop("beds", UNSET))


        def _parse_bathrooms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))


        listing_content_update_request_occupancy = cls(
            max_guests=max_guests,
            bedrooms=bedrooms,
            beds=beds,
            bathrooms=bathrooms,
        )


        listing_content_update_request_occupancy.additional_properties = d
        return listing_content_update_request_occupancy

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
