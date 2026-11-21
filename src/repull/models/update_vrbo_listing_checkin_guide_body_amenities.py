from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_checkin_guide_body_amenities_additional_property import UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty





T = TypeVar("T", bound="UpdateVrboListingCheckinGuideBodyAmenities")



@_attrs_define
class UpdateVrboListingCheckinGuideBodyAmenities:
    """ `{AMENITY_ID: {instructions}}` — notes are one-way (not removable).

     """

    additional_properties: dict[str, UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_checkin_guide_body_amenities_additional_property import UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_checkin_guide_body_amenities_additional_property import UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty
        d = dict(src_dict)
        update_vrbo_listing_checkin_guide_body_amenities = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        update_vrbo_listing_checkin_guide_body_amenities.additional_properties = additional_properties
        return update_vrbo_listing_checkin_guide_body_amenities

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: UpdateVrboListingCheckinGuideBodyAmenitiesAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
