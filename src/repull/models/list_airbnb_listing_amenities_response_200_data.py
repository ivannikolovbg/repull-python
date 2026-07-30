from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_amenity import AirbnbAmenity





T = TypeVar("T", bound="ListAirbnbListingAmenitiesResponse200Data")



@_attrs_define
class ListAirbnbListingAmenitiesResponse200Data:
    """ 
        Attributes:
            amenities (list[AirbnbAmenity] | Unset):
            accessibility_amenities (list[AirbnbAmenity] | Unset):
     """

    amenities: list[AirbnbAmenity] | Unset = UNSET
    accessibility_amenities: list[AirbnbAmenity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_amenity import AirbnbAmenity
        amenities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = []
            for amenities_item_data in self.amenities:
                amenities_item = amenities_item_data.to_dict()
                amenities.append(amenities_item)



        accessibility_amenities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.accessibility_amenities, Unset):
            accessibility_amenities = []
            for accessibility_amenities_item_data in self.accessibility_amenities:
                accessibility_amenities_item = accessibility_amenities_item_data.to_dict()
                accessibility_amenities.append(accessibility_amenities_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if accessibility_amenities is not UNSET:
            field_dict["accessibility_amenities"] = accessibility_amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_amenity import AirbnbAmenity
        d = dict(src_dict)
        _amenities = d.pop("amenities", UNSET)
        amenities: list[AirbnbAmenity] | Unset = UNSET
        if _amenities is not UNSET:
            amenities = []
            for amenities_item_data in _amenities:
                amenities_item = AirbnbAmenity.from_dict(amenities_item_data)



                amenities.append(amenities_item)


        _accessibility_amenities = d.pop("accessibility_amenities", UNSET)
        accessibility_amenities: list[AirbnbAmenity] | Unset = UNSET
        if _accessibility_amenities is not UNSET:
            accessibility_amenities = []
            for accessibility_amenities_item_data in _accessibility_amenities:
                accessibility_amenities_item = AirbnbAmenity.from_dict(accessibility_amenities_item_data)



                accessibility_amenities.append(accessibility_amenities_item)


        list_airbnb_listing_amenities_response_200_data = cls(
            amenities=amenities,
            accessibility_amenities=accessibility_amenities,
        )


        list_airbnb_listing_amenities_response_200_data.additional_properties = d
        return list_airbnb_listing_amenities_response_200_data

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
