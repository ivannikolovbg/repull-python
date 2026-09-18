from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateAirbnbListingAmenitiesResponse200Data")



@_attrs_define
class UpdateAirbnbListingAmenitiesResponse200Data:
    """ 
        Attributes:
            amenities (int | Unset): How many regular amenities were written.
            accessibility_amenities (int | Unset): How many accessibility amenities were written.
     """

    amenities: int | Unset = UNSET
    accessibility_amenities: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amenities = self.amenities

        accessibility_amenities = self.accessibility_amenities


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if accessibility_amenities is not UNSET:
            field_dict["accessibilityAmenities"] = accessibility_amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amenities = d.pop("amenities", UNSET)

        accessibility_amenities = d.pop("accessibilityAmenities", UNSET)

        update_airbnb_listing_amenities_response_200_data = cls(
            amenities=amenities,
            accessibility_amenities=accessibility_amenities,
        )


        update_airbnb_listing_amenities_response_200_data.additional_properties = d
        return update_airbnb_listing_amenities_response_200_data

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
