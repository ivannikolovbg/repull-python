from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_amenities_body_accessibility_amenities_item import UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem
  from ..models.update_airbnb_listing_amenities_body_amenities_item import UpdateAirbnbListingAmenitiesBodyAmenitiesItem





T = TypeVar("T", bound="UpdateAirbnbListingAmenitiesBody")



@_attrs_define
class UpdateAirbnbListingAmenitiesBody:
    """ At least one amenity across `amenities` and `accessibility_amenities`. A body that changes nothing is refused rather
    than reported as a successful write.

        Attributes:
            amenities (list[UpdateAirbnbListingAmenitiesBodyAmenitiesItem] | Unset):
            accessibility_amenities (list[UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem] | Unset):
     """

    amenities: list[UpdateAirbnbListingAmenitiesBodyAmenitiesItem] | Unset = UNSET
    accessibility_amenities: list[UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_amenities_body_accessibility_amenities_item import UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem
        from ..models.update_airbnb_listing_amenities_body_amenities_item import UpdateAirbnbListingAmenitiesBodyAmenitiesItem
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

        field_dict.update({
        })
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if accessibility_amenities is not UNSET:
            field_dict["accessibility_amenities"] = accessibility_amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_listing_amenities_body_accessibility_amenities_item import UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem
        from ..models.update_airbnb_listing_amenities_body_amenities_item import UpdateAirbnbListingAmenitiesBodyAmenitiesItem
        d = dict(src_dict)
        _amenities = d.pop("amenities", UNSET)
        amenities: list[UpdateAirbnbListingAmenitiesBodyAmenitiesItem] | Unset = UNSET
        if _amenities is not UNSET:
            amenities = []
            for amenities_item_data in _amenities:
                amenities_item = UpdateAirbnbListingAmenitiesBodyAmenitiesItem.from_dict(amenities_item_data)



                amenities.append(amenities_item)


        _accessibility_amenities = d.pop("accessibility_amenities", UNSET)
        accessibility_amenities: list[UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem] | Unset = UNSET
        if _accessibility_amenities is not UNSET:
            accessibility_amenities = []
            for accessibility_amenities_item_data in _accessibility_amenities:
                accessibility_amenities_item = UpdateAirbnbListingAmenitiesBodyAccessibilityAmenitiesItem.from_dict(accessibility_amenities_item_data)



                accessibility_amenities.append(accessibility_amenities_item)


        update_airbnb_listing_amenities_body = cls(
            amenities=amenities,
            accessibility_amenities=accessibility_amenities,
        )

        return update_airbnb_listing_amenities_body

