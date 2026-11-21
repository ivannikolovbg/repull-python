from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty





T = TypeVar("T", bound="UpdateVrboListingAmenitiesResponse200DataGroups")



@_attrs_define
class UpdateVrboListingAmenitiesResponse200DataGroups:
    """ Keyed by group: essentials, internet, climateControl, general, office, kitchenAndDining, parking, poolAndSpa,
    sustainability, entertainment, outdoor, onsiteService, accessibility, homeSafety, safetyDevices, enhancedCleaning,
    locationAndView, localAttractionsAndActivities, checkoutInstructions.

     """

    additional_properties: dict[str, UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty
        d = dict(src_dict)
        update_vrbo_listing_amenities_response_200_data_groups = cls(
        )


        from ..models.update_vrbo_listing_amenities_response_200_data_groups_additional_property_fields_item import UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalPropertyFieldsItem
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        update_vrbo_listing_amenities_response_200_data_groups.additional_properties = additional_properties
        return update_vrbo_listing_amenities_response_200_data_groups

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: UpdateVrboListingAmenitiesResponse200DataGroupsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
