from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_safety_disclosures_response_200_data_groups_additional_property import GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty





T = TypeVar("T", bound="GetVrboListingSafetyDisclosuresResponse200DataGroups")



@_attrs_define
class GetVrboListingSafetyDisclosuresResponse200DataGroups:
    """ Keyed by group: homeSafety, safetyDevices.

     """

    additional_properties: dict[str, GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_safety_disclosures_response_200_data_groups_additional_property import GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_safety_disclosures_response_200_data_groups_additional_property import GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty
        d = dict(src_dict)
        get_vrbo_listing_safety_disclosures_response_200_data_groups = cls(
        )


        from ..models.get_vrbo_listing_safety_disclosures_response_200_data_groups_additional_property_fields_item import GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalPropertyFieldsItem
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        get_vrbo_listing_safety_disclosures_response_200_data_groups.additional_properties = additional_properties
        return get_vrbo_listing_safety_disclosures_response_200_data_groups

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GetVrboListingSafetyDisclosuresResponse200DataGroupsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
