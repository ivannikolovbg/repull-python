from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_amenities_response_200_data_groups import UpdateVrboListingAmenitiesResponse200DataGroups





T = TypeVar("T", bound="UpdateVrboListingAmenitiesResponse200Data")



@_attrs_define
class UpdateVrboListingAmenitiesResponse200Data:
    """ What Vrbo has after the write, read back from Vrbo.

        Attributes:
            groups (UpdateVrboListingAmenitiesResponse200DataGroups | Unset): Keyed by group: essentials, internet,
                climateControl, general, office, kitchenAndDining, parking, poolAndSpa, sustainability, entertainment, outdoor,
                onsiteService, accessibility, homeSafety, safetyDevices, enhancedCleaning, locationAndView,
                localAttractionsAndActivities, checkoutInstructions.
     """

    groups: UpdateVrboListingAmenitiesResponse200DataGroups | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_amenities_response_200_data_groups import UpdateVrboListingAmenitiesResponse200DataGroups
        groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_amenities_response_200_data_groups import UpdateVrboListingAmenitiesResponse200DataGroups
        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: UpdateVrboListingAmenitiesResponse200DataGroups | Unset
        if isinstance(_groups,  Unset):
            groups = UNSET
        else:
            groups = UpdateVrboListingAmenitiesResponse200DataGroups.from_dict(_groups)




        update_vrbo_listing_amenities_response_200_data = cls(
            groups=groups,
        )


        update_vrbo_listing_amenities_response_200_data.additional_properties = d
        return update_vrbo_listing_amenities_response_200_data

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
