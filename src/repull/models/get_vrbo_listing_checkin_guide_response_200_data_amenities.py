from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_checkin_guide_response_200_data_amenities_additional_property_type_0 import GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0





T = TypeVar("T", bound="GetVrboListingCheckinGuideResponse200DataAmenities")



@_attrs_define
class GetVrboListingCheckinGuideResponse200DataAmenities:
    """ Keyed by Vrbo amenity id (e.g. HOT_TUB_HOSPITALITY).

     """

    additional_properties: dict[str, GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0 | None] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_checkin_guide_response_200_data_amenities_additional_property_type_0 import GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_checkin_guide_response_200_data_amenities_additional_property_type_0 import GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0
        d = dict(src_dict)
        get_vrbo_listing_checkin_guide_response_200_data_amenities = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0 | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0.from_dict(data)



                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0 | None, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        get_vrbo_listing_checkin_guide_response_200_data_amenities.additional_properties = additional_properties
        return get_vrbo_listing_checkin_guide_response_200_data_amenities

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0 | None:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GetVrboListingCheckinGuideResponse200DataAmenitiesAdditionalPropertyType0 | None) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
